# Shuning (Suzanna) Li — academic homepage

Structure adapted from RayeRen's Academic Homepage, with publication styling based on Sikai Li's repository and colors from Brandon Stewart's website. See SOURCES.md and LICENSE.

This is a static adaptation, not the full Jekyll theme. Layouts, includes, and page content remain separate; Python assembles them without Ruby or package installation.

## Local preview

```sh
python3 build.py
python3 -m http.server 4173 --bind 127.0.0.1 --directory dist
```

Open http://127.0.0.1:4173/. The build validates local assets and navigation targets and copies public files to dist/.

## Editing

- `_pages/about.html`: biography, news, publications, education, experience, hobbies.
- `_includes/author-profile.html`: portrait, name, affiliations, contact and social profiles.
- `_includes/masthead.html`: navigation.
- `_layouts/default.html`: metadata, page wrapper, footer.
- `styles.css`: layout, responsive rules, and colors.
- `index.html`: generated output; rebuild after editing source fragments.

Missing photos, profile links, publication details, dates, news, and hobbies are labeled placeholders. Pending resources are plain text, not broken links. No downloadable CV is included, per the form. The RA date follows the January 2026–present range supplied.

## Publication

Local draft only. No publishing workflows, trackers, analytics, or citation crawlers. Do not publish before owner approval. No intake form or private supporting documents are included.

After approval, root-level static output can be served with GitHub Pages. Under hazel-hammer/suzanna-li.github.io the usual project URL would be https://hazel-hammer.github.io/suzanna-li.github.io/. Confirm the desired public address before enabling Pages. Relative asset links work at a project path.
