# Peggy Vivas — landing page

Static bilingual landing page. No build step: `index.html`, `styles.css`, `app.js`
and pre-optimized images in `assets/img/`.

## Run it locally

    python3 -m http.server 4321
    # http://localhost:4321

## Re-generate the images

Source photos live outside this repo, in `../media/`. After changing which photos
the page uses, edit the `PHOTOS` map in `tools/optimize-images.py` and run:

    python3 tools/optimize-images.py "../media/more content for landing page"

## Deploy

Push to `main`. Vercel builds nothing and serves the files as they are.

See `CLAUDE.md` for the rules that govern content changes.
