"""Validate local page references and build a dependency-free static website."""
from html.parser import HTMLParser
from pathlib import Path
from shutil import copy2
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent
PUBLIC_FILES = ("index.html", "styles.css", ".nojekyll")

# Retain the upstream layout/include/content separation without requiring Ruby.
html = (ROOT / "_layouts/default.html").read_text()
for slot, source in {
    "masthead": "_includes/masthead.html",
    "author_profile": "_includes/author-profile.html",
    "content": "_pages/about.html",
}.items():
    html = html.replace("{{ " + slot + " }}", (ROOT / source).read_text())
if "{{" in html:
    raise ValueError("Unresolved template placeholder")
(ROOT / "index.html").write_text(html)


class PageReferences(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.references = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                raise ValueError(f"Duplicate page ID: {attrs['id']}")
            self.ids.add(attrs["id"])
        for name in ("href", "src"):
            if name in attrs:
                self.references.append(attrs[name])


page = PageReferences()
page.feed((ROOT / "index.html").read_text())
for ref in page.references:
    url = urlsplit(ref)
    if url.scheme or url.netloc:
        continue
    if url.path:
        path = unquote(url.path)
        if path not in PUBLIC_FILES:
            raise ValueError(f"Local reference is not included in the build: {ref}")
        if not (ROOT / path).is_file():
            raise ValueError(f"Missing local asset: {ref}")
    elif url.fragment and url.fragment not in page.ids:
        raise ValueError(f"Missing page section: {ref}")

output = ROOT / "dist"
output.mkdir(exist_ok=True)
for filename in PUBLIC_FILES:
    copy2(ROOT / filename, output / filename)
print(f"Built {len(PUBLIC_FILES)} files in {output}")
print("Validated all local asset references and navigation targets.")
