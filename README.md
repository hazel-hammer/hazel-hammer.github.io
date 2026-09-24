# Shuning (Suzanna) Li — academic website

A responsive, dependency-free academic website for Shuning Li. Built from the completed intake form, with warm colors and serif typography inspired by [Brandon Stewart's website](https://brandonstewart.org/). [Sikai Li's website](https://skevinci.github.io/) informed the academic structure and CoorDex capitalization; its biography and achievements have not been copied.

## Preview locally

Requires Python 3. No package installation is needed.

```sh
python3 build.py
python3 -m http.server 4173 --bind 127.0.0.1 --directory dist
```

Open http://127.0.0.1:4173 in a browser. The build checks local assets, duplicate section IDs, and in-page navigation links. It copies only public files into `dist/`.

## Edit

- `index.html`: biography, research, experience, education, and contact details.
- `styles.css`: typography, colors, responsive layout, and print styles.
- `build.py`: local validation and static output creation.

No external fonts, trackers, JavaScript, or third-party asset requests are used.

## Content awaiting confirmation

- AnyBody and CoorDex intentionally contain placeholders. Replace their summaries and resources with confirmed titles, author lists, statuses, links, and images when ready.
- GitHub, Google Scholar, and LinkedIn are plain-text placeholders, not clickable links. Replace them with supplied profile URLs.
- No portrait was supplied, so the design uses a typographic introduction.
- No downloadable CV is included, per the form.
- No graduation date or PhD entry year was supplied; neither is invented.
- The form describes the Sharpa role as an internship; the page uses that role without claiming particular contributions.
- Research assistant work with Mingyu Ding is dated January 2026–present, following the explicit date range in the form.

## Publication

This draft is prepared locally for review. There is no deployment workflow and nothing is published by the build command.

After the owner approves publication, these root-level static files can be served using GitHub Pages. The repository is named `suzanna-li.github.io` under `hazel-hammer`, so GitHub Pages normally treats it as a project site at `https://hazel-hammer.github.io/suzanna-li.github.io/`, not as the account's root website. The relative stylesheet link works at either a root or project path. Confirm the desired public URL before enabling Pages or pushing a deployment branch.

Do not include the intake form or private supporting material in the repository.
