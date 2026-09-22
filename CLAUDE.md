# Peggy Vivas — Landing Page CLAUDE.md

Rules for this repo. The brand itself is defined one level up, in
`../Peggy_Brand_OS_v4_master.md` and `../CLAUDE.md` — read those before writing copy.
**Target 200 lines for every file here, 250 when cutting would lose something.**

## What This Is

A single bilingual landing page for **Peggy Vivas**, holistic facilitator in Miami. It says who
she is and what a visitor can do next. Traffic comes from her Instagram bio and from people she
meets through her professional work, so it is read on a phone far more often than on a desktop.

English is the default. Spanish is one tap away and equal in weight.

## Stack

Static HTML, CSS and one small script. **There is no build step, no framework, no package
manager, and none should be added for a page this size.**

| File | What it holds |
|---|---|
| `index.html` | All content, in both languages |
| `styles.css` | The whole design system: tokens, layout, responsive rules |
| `app.js` | Language toggle, top-bar scroll state, reveal-on-scroll |
| `tools/optimize-images.py` | Turns source photos into web-sized WebP + JPEG |
| `assets/img/` | Generated images. Never hand-edit; re-run the script |
| `vercel.json` | Clean URLs and a one-year cache on `/assets/img/` |

Run it: `python3 -m http.server 4321`, then open `http://localhost:4321`.

## How the Two Languages Work

Both languages live in the DOM. `<html>` carries `data-lang`, and CSS hides the other one:

```css
html[data-lang="en"] [lang="es"] { display: none; }
html[data-lang="es"] [lang="en"] { display: none; }
```

- **Every visible string needs both a `lang="en"` and a `lang="es"` version.** A string with only
  one is a bug: it stays on screen in the wrong language, or vanishes entirely.
- Block content duplicates the element (`<p lang="en">` and `<p lang="es">`). Inline content
  wraps in `<span lang="…">`.
- `app.js` remembers the choice in `localStorage` and falls back to the browser language on a
  first visit. With JavaScript off, the page stays in English and still reads correctly.
- **English is written first and Spanish is a rewrite, not a translation.** The Spanish for the
  mechanism section is Peggy's own wording from Brand OS §9 and should stay verbatim.

## Copy Rules

**Invoke the `authentic-content-writer` skill before writing or changing any text on this page**,
in either language. Then apply Brand OS §6 in full. The ones this page gets wrong most easily:

- No negation-into-affirmation. The two exceptions already on the page are Peggy's own
  established lines (the philosophy quote, and "no solo lo escucha") and stay verbatim.
- No CTA phrased as a question.
- Never exactly three items in a list.
- One next step. Every button on this page opens the same WhatsApp thread; the prefilled text
  differs by section, the action does not.
- No invented facts. See below.

## Facts on This Page

Everything below traces to the Brand OS, to LinkedIn, or to something Mafer confirmed directly.

- Casa Magia 33, Design District · up to 30 people · no previous experience
- Reiki Sistémico with **Francisco**, Reiki Kahuna master, 18 years teaching, **October 17–18**
- Advanced PSYCH-K Facilitator · EMF Balancing Technique practitioner · Reiki Master, Kahuna
  lineage · Family Constellations facilitator
- *Mastering Connections*, continuing education approved by the Florida DBPR for property managers
- WhatsApp +1 786 290 1127 · peggyvivas@gmail.com · Instagram @peggyc.viv · LinkedIn

**Not on the page, deliberately:**

- **Venue, time and price for October 17–18** — unconfirmed. The card says to message for them.
  If the date passes without new dates confirmed, remove the card rather than leave it stale.
- **A tagline** — three candidates exist, none chosen. Do not put one in the hero.
- **Her employer.** LinkedIn lists Director of Business Development at Ball Janik LLP. Peggy has
  not said she wants it on a page about her practice. Ask before adding it.
- **Prices, session length, testimonials, review counts.** None are confirmed for this page.

## Photographs

- **Only photographs in which Peggy is the only identifiable person may be used here.** The
  Casa Magia 33 session photos show attendees' faces, and a public page needs each of their
  consent. This is Brand OS §6 rule 7 and it is the strictest rule in this repo.
- Sources live outside the repo in `../media/`. Only the generated files are committed.
- **Always re-generate through `tools/optimize-images.py`.** It bakes EXIF rotation into the
  pixels, which matters because WebP does not carry orientation and several of the originals are
  stored sideways. Exporting them any other way puts Peggy on her side on the live site.
- Originals are 3 to 8 MB each. Nothing that size ever goes in `assets/img/`.

## Deploy

- **GitHub:** `mariafffernanda/life-with-peggy`, private.
- **Vercel:** new project, no build command, output is the repo root. **Push to `main` deploys.**
- Work on a branch for anything larger than a typo, and check `git branch --show-current` before
  committing.
- After a deploy, open the live URL at phone and desktop width before calling it done.

## Working With Claude

1. **Never invent a fact about Peggy or her practice.** Missing means ask, not fill.
2. **Change text in both languages in the same edit.** Never leave one side stale.
3. **Check the mechanism, not just the wording** — the page's spine is Reiki first, then the
   systemic work can reach something. Copy that drifts off it turns generic.
4. **Verify in a browser at 390px and 1440px** after any layout change. State what you checked.
5. **Peggy approves what ships.** Drafts stay drafts, however good they read.
6. **Scope precisely.** This is a one-page site; do not add routes, frameworks or a CMS because a
   change would be marginally tidier that way.

## Definition of Done

- [ ] `authentic-content-writer` invoked before any copy change
- [ ] Both languages present for every new string, and the toggle switches cleanly
- [ ] Checked at 390px and 1440px in a real browser, not assumed
- [ ] No console errors
- [ ] Images generated by the script, not hand-exported, and under 150 KB each
- [ ] Every new fact traceable to the Brand OS, LinkedIn or Peggy herself
- [ ] One action on the page: the WhatsApp thread

## Do Not Touch

- `assets/img/` by hand — regenerate it instead.
- The source photos in `../media/` — never edit, move or delete them.
- The `lang="en"` / `lang="es"` attribute pattern — the whole language system rests on it.
