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

- `_pages/about.html`: biography, publications, education, experience, and misc.
- `_includes/author-profile.html`: portrait, name, affiliations, contact and social profiles.
- `_includes/masthead.html`: navigation.
- `_layouts/default.html`: metadata, page wrapper, footer.
- `styles.css`: layout, responsive rules, and colors.
- `index.html`: generated output; rebuild after editing source fragments.

## Publication

Repository: https://github.com/hazel-hammer/hazel-hammer.github.io

Website: https://hazel-hammer.github.io/

GitHub Pages serves the root of the main branch. After editing, run `python3 build.py` and commit the generated `index.html` along with source and asset changes before pushing to main. Relative asset links support the homepage URL.

No intake form or private supporting documents are included.
