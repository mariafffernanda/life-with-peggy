# Peggy Vivas — Landing Page CLAUDE.md

Rules for this repo. The brand is defined one level up, in `../Peggy_Brand_OS_v4_master.md` and
`../CLAUDE.md` — read those before writing copy. **200 lines per file, 250 when cutting costs
something.**

## What This Is

A two-page bilingual site that represents **Peggy Vivas**. It is a representation page, not a
booking system: it says who she is, what she facilitates, and how to reach her. Traffic arrives
from her Instagram bio and from people who meet her professionally, mostly on a phone.

English is the default. Spanish is one tap away and equal in weight.

## Who She Is, In Her Own Framing

Her Instagram bio is the positioning the site is built on:

> Conscious Business · Human Connection · Systemic Work · Family Constellations
> Facilitator · Teacher · Speaker
> Finding My Way Home

**Three sides, one person:** the practice (systemic and energy work), the room (conscious
business taught to professionals), the road (her own travel and search). The site gives each one
space. **Do not collapse her into the holistic side.** That was the first draft's mistake.

**Magia 33 is a venue, not her identity.** It is *Magia 33*, never "Casa Magia 33", and it is
where some of her Miami group work happens, not all of her work. It belongs in the events page
and in one line of her bio, never in the hero.

## Stack

Static HTML, CSS and one small script. **No build step, no framework, no package manager.**

| File | What it holds |
|---|---|
| `index.html` | The main page, both languages |
| `events.html` | Dated group work, both languages |
| `styles.css` | Tokens, layout, responsive rules for both pages |
| `app.js` | Language toggle, top-bar scroll state, reveal-on-scroll |
| `tools/optimize-images.py` | Source photos into web-sized WebP + JPEG, plus square crops |
| `assets/img/` | Generated images. Never hand-edit; re-run the script |

Run it: `python3 -m http.server 4321`. **The browser caches aggressively on localhost** — add a
query string (`?v=2`) when a change does not appear.

## How the Two Languages Work

Both languages live in the DOM. `<html>` carries `data-lang`, and CSS hides the other:

```css
html[data-lang="en"] [lang="es"] { display: none; }
html[data-lang="es"] [lang="en"] { display: none; }
```

- **Every visible string needs both an `en` and an `es` version**, on both pages. A string with
  only one is a bug: it shows in the wrong language or vanishes.
- `app.js` remembers the choice and falls back to the browser language. With JS off the page
  stays in English and reads correctly.
- **English is written first; Spanish is a rewrite, not a translation.** Where her own Spanish
  exists (Brand OS §9, or magia33.com), keep it verbatim instead of back-translating.

## Copy Rules

**Invoke the `authentic-content-writer` skill before writing or changing any text**, either
language, then apply Brand OS §6. What this page gets wrong most easily:

- No negation-into-affirmation, no CTA phrased as a question, never exactly three items.
- One action. Every button opens the same WhatsApp thread; only the prefilled text differs.
- No invented facts. See below.

**Trademarks, written exactly this way:** PSYCH-K®, The EMF Balancing Technique®,
Bioneuroemoción®. Family Constellations and Reiki Sistémico take no symbol.

## Facts on These Pages

Everything traces to the Brand OS, to magia33.com, to her LinkedIn, or to Mafer directly.

- **More than 15 years** facilitating, across modalities and in different parts of the world
- **Family Constellations** — circles of up to 30, no previous experience
- **Reiki Sistémico** — two days with **Francisco Rubio**, Reiki Kahuna master
- **PSYCH-K® Advanced Facilitator** · **The EMF Balancing Technique®** certified practitioner ·
  **postgraduate training in Bioneuroemoción®** · Reiki Master, Reiki Kahuna lineage
- **Mastering Connections** — *"A journey with effective communication and emotional
  intelligence"*, continuing education approved by the Florida DBPR for property managers,
  presented with **Ball Janik LLP**
- English, Spanish and Italian
- Events: Sept 26, 10:00–15:00, USD 80, Magia 33, 177 NE 44th St, Miami FL 33137 ·
  Oct 17–18, 08:30–18:00, USD 333 deposit
- WhatsApp +1 786 290 1127 · peggyvivas@gmail.com · @peggyc.viv · LinkedIn

**Unresolved, so not asserted anywhere:**

- **Francisco's years.** The Brand OS says 18 years teaching; magia33.com says 17+ years in
  energetic healing. The pages say "Reiki Kahuna master" with no number until this is settled.
- **The Sept 26 event year.** Taken from magia33.com, which lists past events too. Verify before
  a deploy, and remove the card once the date passes.
- **Her title at Ball Janik LLP.** The firm is named because it appears on her own slide. Her
  role, Director of Business Development per LinkedIn, is not on the page yet.
- **A tagline.** "Finding My Way Home" is her Instagram line and appears only as her words in the
  third card. Do not promote it to the hero without her approval.

## Photographs

- **Only photographs in which Peggy is the only identifiable person.** The Magia 33 session
  photos show attendees' faces and would need each person's consent. Brand OS §6 rule 7, and the
  strictest rule here. The `speaking` photo is the one exception under review: other attendees
  are visible at the edges of the frame, so confirm before it goes public.
- Sources live outside the repo in `../media/`. Only generated files are committed.
- **Always regenerate through `tools/optimize-images.py`.** It bakes EXIF rotation into the
  pixels; WebP does not carry orientation and several originals are stored sideways.
- Each frame is composed differently, so `.side--practice`, `.side--room` and `.side--road` carry
  their own `object-position`. Changing a photo means retuning its focal point.

## The Social Section Is a Placeholder

`#social` is a grid of **her own photographs, not her live feed**, marked as such in an HTML
comment. Instagram requires login to read a profile, so there is no scraping path.
**Replace it with a Behold embed** once her account is connected, the same service Mafer's site
uses. Until then, never describe it in copy as her latest posts.

LinkedIn has no profile-feed widget. Individual posts can be embedded by URL; the section links
out instead.

## Contact, Not Booking

She announces dates through a **WhatsApp broadcast list**. The page offers to join it and links
group bookings to magia33.com. **Do not add a booking form, a calendar or a payment flow**
without her asking: it was considered and deliberately deferred.

## Deploy

- **GitHub:** `mariafffernanda/life-with-peggy`, private. **Push to `main` deploys.**
- **Vercel:** new project, no build command, output is the repo root.
- Open both pages at 390px and 1440px after any layout change before calling it done.

## Working With Claude

1. **Never invent a fact about Peggy or her practice.** Missing means ask.
2. **Change both languages in the same edit**, across both pages.
3. **Keep the three sides in balance.** A change that makes her read as only a healer, or only a
   corporate trainer, is wrong even if the sentence is good.
4. **Verify in a browser at 390px and 1440px** and say what you checked.
5. **Peggy approves what ships.**
6. **Scope precisely.** Two static pages. No routes, frameworks or CMS.

## Definition of Done

- [ ] `authentic-content-writer` invoked before any copy change
- [ ] Both languages present for every new string, on both pages, toggle verified
- [ ] Checked at 390px and 1440px in a real browser
- [ ] No console errors
- [ ] Images generated by the script, each under 150 KB
- [ ] Every new fact traceable, and nothing from the unresolved list asserted
- [ ] Trademark symbols correct
