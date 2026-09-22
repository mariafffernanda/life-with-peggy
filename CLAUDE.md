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

Her Instagram bio is the language the site borrows:

> Conscious Business · Human Connection · Systemic Work · Family Constellations
> Facilitator · Teacher · Speaker
> Finding My Way Home

**Her corporate identity is the ground, not a side note.** Business development at executive
level, with coaching, consulting and approved continuing education alongside it. That career is
what she lives on today; the holistic practice is where her education and that career led her,
and it will take a larger share later in her working life. A draft that reads as a healer who
happens to teach a class is wrong, and that mistake has already been made once here.

**Never name her employer or her job title.** She wants the executive standing implied, not
stated: "executive roles inside Miami's professional services world" is the register. The firm
was named on the page once and removed at her request. This applies to the course section too,
even though the firm's logo appears in the photograph on her own slide.

**The balance is the hard part.** Too spiritual and her professional readers discount her. Too
corporate and the practice looks like a hobby. Every pass over the About section should be
checked against both failures.

The page holds two rooms of equal weight: **in organizations** and **with individuals**, and the
method section is what joins them. Organizational constellations and family constellations are
the same discipline addressed to different systems, which is the honest bridge between her two
worlds and the thing no competitor can copy.

**Magia 33 is a venue, not her identity.** It is *Magia 33*, never "Casa Magia 33", and it is
where some of her Miami group work happens, not all of her work. It belongs in the events page
and in one line of her bio, never in the hero.

## Palette and Feel

Her own words: nature, terracotta, tree greens, brown, black frames, beige. Elegant, aimed at a
high end audience, language that is sophisticated and still easy to understand.

Tokens live at the top of `styles.css`: `--beige` page, `--green` deep bands, `--clay` the single
accent, `--brown`, `--stone`, `--ink` for the frames. **Photographs are hung in thin black
frames** (`.frame`, and the hero panel), which is the detail that carries the whole look. Do not
introduce a second accent colour.

## Stack

Static HTML, CSS and one small script. **No build step, no framework, no package manager.**

| File | What it holds |
|---|---|
| `index.html` | The main page, both languages. Order is deliberate: hero, the two rooms, the method, Mastering Connections, the private practice, who she is, contact. **The professional work comes before the personal practice.** |
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

- No negation-into-affirmation, no comparison structures, no CTA phrased as a question.
- **Never exactly three of anything.** Not three list items, not three cards, not three clauses
  in a sentence. She notices it and dislikes it, and it is Brand OS §6 rule 3. Use two or four.
- **The register is professional and carries weight.** She sells to a high end audience in a
  legal and property context. Sophisticated, plainly understandable, never breezy.
- **No em dashes and no hyphens in prose.** Write "two day training", "one to one". Hyphens
  inside a trademark such as PSYCH-K® are the only exception.
- One action. Every button opens the same WhatsApp thread; only the prefilled text differs.
- **Every WhatsApp prefill is written in English, in both language modes.** Peggy reads English
  first, and a Spanish message arriving from an English reader confused the thread. Do not make
  the prefill follow the toggle.
- No invented facts. See below.

**Trademarks, written exactly this way:** PSYCH-K®, The EMF Balancing Technique®,
Bioneuroemoción®. Family Constellations and Reiki Sistémico take no symbol.

## Facts on These Pages

Everything traces to the Brand OS, to magia33.com, to her LinkedIn, or to Mafer directly.

- **Business development at executive level**, in Miami, with coaching and consulting alongside
- **More than fifteen years** facilitating, across modalities and in different parts of the world
- **Family Constellations** — circles of up to 30, no previous experience
- **Reiki Sistémico** — two days with **Francisco Rubio**, Reiki Kahuna master
- **PSYCH-K® Advanced Facilitator** · **The EMF Balancing Technique®** certified practitioner ·
  **postgraduate training in Bioneuroemoción®** · Reiki Master, Reiki Kahuna lineage
- **Mastering Connections**, her course, described in her own material: *"A journey with
  effective communication and emotional intelligence."* A DBPR approved continuing education
  course for **community association managers**, grounded in **Organizational Constellations**,
  bringing a systemic perspective to leadership, communication and human dynamics in the
  workplace. It helps managers recognize relational patterns, navigate complex interactions,
  strengthen professional connections, and lead with greater awareness and intention.
  **1 continuing education credit, DBPR approved.**
- English, Spanish and Italian
- Events: Sept 26, 10:00–15:00, USD 80, Magia 33, 177 NE 44th St, Miami FL 33137 ·
  Oct 17–18, 08:30–18:00, USD 333 deposit
- WhatsApp +1 786 290 1127 · peggyvivas@gmail.com · @peggyc.viv · LinkedIn

**Unresolved, so not asserted anywhere:**

- **Francisco's years.** The Brand OS says 18 years teaching; magia33.com says 17+ years in
  energetic healing. The pages say "Reiki Kahuna master" with no number until this is settled.
- **The Sept 26 event year.** Taken from magia33.com, which lists past events too. Verify before
  a deploy, and remove the card once the date passes.
- **Her real estate sales associate licence**, listed on LinkedIn, is not on the page. Ask before
  adding it; her professional identity there is business development, not brokerage.
- **A tagline.** "Finding My Way Home" is her Instagram line and appears only as her words in the
  third card. Do not promote it to the hero without her approval.

## The About Section Is a Biography

**The current copy was written and approved by the client. Do not rewrite it on your own
judgement.** It was rewritten four times before it landed, so treat it as settled: two kinds of
rooms over fifteen years, the training as language for what she had already been watching, the
two running together now, then the grouped credentials, then her own line.

If it must change, keep it profound and plain. No inner life she has not described herself, no
origin story, no spiritual register, no corporate register.

**The credentials are grouped** under Professional, Training and certifications, and Languages.
Terracotta labels, hairline rules, no markers.

## Mobile Is Tighter Than Desktop On Purpose

Under 620px the whole scale steps down: smaller type, shorter blocks, landscape crops, lighter
card padding. The default scale read as oversized boxes on a phone and hid the shape of the
page. Most visitors arrive from her Instagram bio, so **check a change on a phone first.**

## Two Details She Asked For By Name

- **Credentials are an index, not bullets.** Hairline rules, no dash markers, no symbols. She
  rejected the bulleted treatment on sight.
- **Photographs hang in thin black frames.** Keep it.

## Photographs

- **Her chosen photographs**, and where they sit: `hero` the dawn portrait in the framed hero
  panel, `window` the temple window in About, `road` and `open` her two other favourites, in the
  third side card and the closing band.
- **Only photographs in which Peggy is the only identifiable person.** The Magia 33 session
  photos show attendees' faces and would need each person's consent. Brand OS §6 rule 7, and the
  strictest rule here. The `speaking` photo is the one exception under review: other attendees
  are visible at the edges of the frame, so confirm before it goes public.
- Sources live outside the repo in `../media/`. Only generated files are committed.
- **Always regenerate through `tools/optimize-images.py`.** It bakes EXIF rotation into the
  pixels; WebP does not carry orientation and several originals are stored sideways.
- Each frame is composed differently, so `.side--practice`, `.side--room` and `.side--road` carry
  their own `object-position`. Changing a photo means retuning its focal point.

## No Social Grid

A placeholder grid of her own photographs was built and then removed: reusing the same pictures
across the page made it look repetitive. **The contact block carries plain Instagram, LinkedIn
and email buttons instead, with no images.**

When her Instagram is connected, a **Behold** embed can bring in the real feed, the same service
Mafer's site uses. Until a live feed exists, do not put pictures in a section that implies one.
LinkedIn has no profile feed widget; individual posts embed by URL.

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
