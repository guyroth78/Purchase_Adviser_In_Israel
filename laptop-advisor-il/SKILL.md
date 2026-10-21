---
name: laptop-advisor-il
description: "Use whenever someone asks for help choosing, buying or comparing a laptop or notebook computer, even casually and without technical detail: 'recommend me a laptop', 'which laptop should I buy', a laptop for work, teaching, university, school, gaming (for example FIFA, GTA), programming, video editing or travel, 'something durable but not too expensive', or a link to a laptop with 'is this good for me'. Also in Hebrew (מחשב נייד, לפטופ, נייד חדש, איזה מחשב לקנות, תמליץ לי על מחשב). Asks a few short questions about the person's needs, finds current models and prices (Israel-focused catalog plus web), scores them against those needs and builds an interactive page where the person can change weights, filters and price range."
---

# Laptop advisor (Israel)

Help a person choose a computer, then deliver one interactive decision page (a published Artifact) that shows which models fit their preferences and why. Reply in the person's language.

## Core idea: the preference envelope

Separate the criteria into two kinds and never mix them:
- **Hard constraints** are filters. A model that fails one is out. It is shown struck through with the reason, never as a low score. Examples: minimum RAM, OS included, warranty length, screen size, price range.
- **Soft criteria** get a target (`need`: what is enough for this person), a weight (0-5: how much it matters) and a score per model (1-5: how well the model meets the target, never rewarding more than the target). Examples: performance, keyboard and durability, prestige and build, upgradability, ports, portability, service and warranty, storage.
- **Price is not a soft criterion.** It gets its own axis, because it answers a different question: how much to pay for more fit. The price range (a lower and an upper end the person can move) is a hard constraint and appears as lines on the chart.

Fit score = sum(weight x score) / (sum(weight) x 5) x 100, rounded.

## Tone and technical level

- **Warm, not salesy.** Write like a friend who knows computers: address the person directly, acknowledge what they told you ("since you work in Excel all day..."), and keep it light. One friendly sentence at the start and a short encouraging close are enough; no exclamation marks in every line, no emoji, no flattery. The facts stay exact.
- **Match their technical level.** Judge it from how they wrote and what they need the laptop for: someone who mentions Docker, RAM bottlenecks or Thunderbolt can take terms as they are; someone who describes tasks ("emails, Zoom with the grandchildren, photos") cannot. If unsure, lean simple.
- **For a less technical person,** explain each term the first time in a few plain words and say what it means for them, not how it works. For example "16GB memory (lets you keep many programs and tabs open without slowing down)", "SSD (fast storage, so it starts in seconds)", "USB-C with video (one cable to the screen and charger)". Prefer everyday comparisons over numbers when the number does not help them decide. Skip specs that do not matter to their choice.
- **For a technical person,** be concise and precise: model numbers, specs and trade-offs without explanations they do not need.
- Apply the same level to the text on the page (the needs summary, the `need` lines, notes and `misc`), not only to the chat reply.

## Procedure

The work has three stages. The page shows them top to bottom: the needs summary (stage 1), the criteria and weights (stage 2), then the results (stage 3).

### Stage 1: Understand the person's needs (intake)

1. **Ask for a free-text description first.** One open question: who are you, and what do you need the new laptop for? Let the person write as much or as little as they like. Do not offer options yet.
2. **Then ask at most 5 short diagnostic questions**, only about what the text did not already answer (use AskUserQuestion when available, several questions in one call). Pick from: how portable it must be (carried daily, occasionally, desk only), how strong and fast it must be (apps, number of browser tabs, dev tools, media work), how many hours a day it will be used, country/currency, hard must-haves, and whether a dock or external monitors are used (that decides the USB-C requirement: video + power delivery). Do not ask for a budget: the price range is derived later from the candidates. Do not ask the person for technical targets (how much RAM, which CPU); you infer those in stage 2. Spend a question on a target only if two reasonable readings would change the result and nothing in the text decides between them.
3. **Optional: look at the current machine.** Ask for screenshots of Settings > About and Task Manager > Performance, or read them from the computer if a linked-computer tool is available. Find the real bottleneck: memory usage near 90% with low CPU means RAM is the limit, not the processor. Check uptime; on Windows a long uptime after nightly shutdowns means Fast Startup is on, so suggest a real Restart before measuring. Get the exact model (msinfo32 > System Model) to learn the current screen size.
4. **Write the needs summary.** 3-5 short plain-language lines in the person's own terms (who they are, portability, performance, hours of use, what matters). It goes into `DATA.needs` and appears in its own box at the top of the page.

### Stage 2: Diagnose, from needs to criteria

5. **Translate the needs into criteria, targets and weights.** Read `references/needs-guide.md` first and start from the closest profile.
   - **Target (`need`)**: for each soft criterion, write one short line saying what meets the need, in the person's language (for example "16GB is enough today; 32GB only if Docker is added"). This is what a score of 5 means for this person. Infer it from the needs summary and the guide; aim for the right-sized laptop, not the strongest. The page shows it under the criterion so the person can see and question it.
   - **Weight (0-5)**: how important the criterion is to this person, nothing else. At most two criteria get 5. Every weight must trace back to something in the needs summary.
   - **Split mixed criteria** when the parts have different targets (for example memory and processor), so each criterion has one clear target.
   - **Hard constraints (3-5 checkbox filters)**: the must-haves, any clear minimum (for example "at least 16GB"), and every known risk to a stated need from the guide's risk list, set `on: true`. A risk goes in as a default-on filter, not only as a note.
   The page shows all of these as controls the person can change.

### Stage 3: Find candidates and show the results

6. **Get 5-8 candidates available in the person's country.** The person is waiting: the whole run should take about as long as a plain answer without this skill would. Choose the models closest to the needs, without any price limit. A candidate does not have to satisfy everything, unless a hard constraint requires it.
   - **Start from the catalog**, in this order (details in `references/catalog-format.md`): a catalog URL the person gives, if any; the maintained remote catalog at the address in `references/sources.json`; the copy bundled in `references/catalog/` (if this installation has one) for any remote file that fails or does not match. The catalog covers laptops sold in Israel, priced in shekels: if the person is not in Israel, skip it and research from the web in their country and currency. A candidate taken from the catalog needs no further spec research.
   - **Then a short web pass** for what the catalog lacks: missing candidates, current prices, and any unknown spec that decides a hard constraint. Prefer search results and their snippets over opening pages. Open at most about 8 pages in total, mostly for the current price and availability of the likely top 3. Recommended sites in Israel: zap.co.il, baypo.co.il, https://www.ivory.co.il/%D7%9E%D7%97%D7%A9%D7%91%D7%99%D7%9D_%D7%A0%D7%99%D7%99%D7%93%D7%99%D7%9D.html. For Lenovo specs, psref.lenovo.com pages often appear in search results; use what the result shows.
   - **Never use a browser tool.** If a page cannot be fetched or comes back empty (some maker spec sites need JavaScript), skip it and move on.
   - **Fill the rest from your own knowledge** (CPU class, typical weight, ports of a known model), marked as unverified, or leave the field missing. Do not spend fetches on fields that do not change the ranking.
   - **Right-size**: for each model, take the cheapest configuration that meets the targets (not a Core Ultra 7 or 1TB version when the Ultra 5 or 512GB one meets the need). If a stronger configuration costs almost the same, mention it in the notes.
   - **Spread the prices**: include the cheapest model you can find that passes all hard constraints, several mid-priced ones, and at most two premium models. The price slider can only filter the set; it cannot add a cheaper model you did not pick.
   - A price far above the others (more than about 1.7 times the median) gets one more check before it goes in.
7. **Score against the target.** Score each model 1-5 per soft criterion against that criterion's `need`, using the scale in `references/needs-guide.md`: 5 = meets the target, 3 = meets the minimum but not the target, 1 = does not meet the need. Above the target earns nothing extra: two models that both meet it both get 5, and the cheaper one ranks first. Write a one-line reason for each score. Label the scores as your estimates from the spec, not measurements.
8. **Build the page from the template.** Do not design a new page and do not retype the template. Write only the DATA block (`const DATA = { ... };`) to a file and, if you can run code, run `python scripts/fill_template.py --data data.js --title "<short name for this search>" --out <page>.html` (the script is next to this file); it copies `assets/template.html` and replaces only the DATA block and `<title>`. If you cannot run code, copy `assets/template.html` verbatim and change only the `<title>` line and everything between `// === DATA START ===` and `// === DATA END ===`.
   Keep every field name. The template sets the page language and direction (`lang`, `dir`) from DATA and writes every visible string from `DATA.ui`, so translate `ui` for non-Hebrew users (`dir: "ltr"`, locale and currency to match). The price range slider needs no min/max in DATA: it starts at the price of the cheapest and of the most expensive candidate, so no candidate is filtered out by price, and it reaches 1,000-2,000 beyond both ends (set `budget.pad` only to override that margin). Do not set `budget.value` unless the person volunteered a ceiling. The person can then move both ends on the page and watch the results change. The panels "best fit", "fit vs price" and "envelope" are the results and re-render when criteria, weights or the price range change. Hard constraints are functions (`test`, `show`), so any rule fits (for example `m => m.ports.includes("TB4")`); add any model fields they need. Give each model a `short` label of at most 14 characters for chart labels, and a `spec` object of display strings for the comparison table under the top picks (`brand`, `cpu`, `memory`, `storage` as size and type, `gpu` only if it has a discrete or notable one, `screen`, `weight`, `misc` for anything else worth knowing). Omit what you could not find; the table shows a dash. The top list shows every passing model (it scrolls after five); the table compares the top 3 and updates with the ranking. The "fit vs price" and "envelope" charts each have a row of model chips the person can switch on and off: the scatter starts with every model, the envelope with the top 3 (it follows the ranking until the person picks). Colors are fixed per model, up to 8. `sources` lists every data source you used with its date (remote or bundled catalog with its `updated` date, web with the search date, model knowledge marked unverified); the page shows it at the bottom. Each criterion in `crit` carries its `need` line; the page shows it under the weight slider. The top list marks one model "best value": the cheapest passing model whose fit is within `valueGap` points (default 5) of the best fit; set `valueGap` in DATA only if you have a reason. Use 5-8 soft criteria and 3-5 hard ones; more crowds the radar.
9. **Publish.** Do not open a browser or take screenshots to check the page. If you can run code, one syntax check of the page script is enough (for example `node --check` on the extracted `<script>`). Then publish it as an artifact (icon: "laptop"). Do not run the Artifact quickstart or redesign; the template already follows the page rules.
10. **Reply,** in this order:
   - **What your laptop should have** (from stage 2, before any model is named): a short list of the features and components you recommend for this person and why, one line each, in plain words tied to their needs. Cover processor class, memory, storage, screen size and type, weight, battery, ports and external monitors, operating system, warranty, and any hard requirement or risk filter (for example "x86 processor, because your Python tools may not run on ARM"). These are the `need` targets and hard constraints from the page, written for the person.
   - **The recommendation:** the top pick and its fit score, the runner-up and other alternatives, and what each trades away.
   - **Before buying:** the purchase checklist below.
   - One line that the sliders, checkboxes and model chips on the page re-rank everything live.

## Follow-up: the person brings a laptop link

Later in the conversation the person may paste a link to a laptop they found and ask how it compares. Handle it with the same criteria, targets and weights as the page, so the answer is comparable:

1. **Read the page.** Fetch the URL (never a browser tool). If it cannot be read, search the model name or SKU from the link instead, and if that also fails, ask the person to paste the model name.
2. **Already on the page?** If it is the same model and configuration as a candidate, say so, give its rank and fit score, and update its price only if the link shows a different current price.
3. **Score it like the others.** Take its specs (fill gaps from your knowledge, marked unverified), check every hard constraint, and score it 1-5 on each soft criterion against the same `need` lines, with a one-line reason each. Compute its fit with the page's default weights (say that if they moved the sliders, the result on the page may differ) and its rank among the passing models.
4. **If it ranks in the top 5 and passes the hard constraints**, add it to `DATA.models` with `added: true`, add the link's store and date to `sources`, rebuild the page with `scripts/fill_template.py`, and republish it in place (same artifact). The page marks it as the person's suggestion. In the reply, give its rank and fit, and what it does better and worse than the top pick.
5. **Otherwise do not add it.** In the reply, explain why it does not fit: each hard constraint it fails, and the criteria where it scores below the top pick, with the score gap, the weight, and the spec behind it (for example "battery 2 vs 5, weight 3: 41Wh battery"). If it is close, say what change (a different configuration, a lower price) would put it in the top 5.

## Research pitfalls

- Prices and promotions change within days. Prefer prices you found in this session over stored catalog prices (see `references/catalog-format.md`), and tell the person to confirm the price before paying.
- Marketplace listings with a vague name and no maker SKU (for example "Lenovo 14 Slim") are a warning sign. Ask the seller for the full part number before considering them.
- The same model often has a no-OS SKU that looks cheaper. Compare like for like: add the cost of an OS license or say it is missing.
- Store descriptions sometimes contradict their own spec tables (generation, OS, graphics). When sources disagree, prefer the maker's official spec sheet for that SKU if you can find it; otherwise mark the spec as unconfirmed instead of choosing one silently.
- After the first two weeks, warranty service usually comes from the importer or maker, not the store, so store location matters less than it seems. Check whether a store's address is a real showroom or an online-only office with pickup elsewhere.
- Docks: a standard USB-C dock works with any laptop whose USB-C port supports DisplayPort Alt Mode and Power Delivery; Thunderbolt matters only for multi-monitor or very fast external storage. Some dock features (power button, MAC pass-through) work only with the dock maker's business line.

## Purchase checklist for the reply

- Exact SKU matches the recommended spec (RAM, storage, OS).
- Warranty length, type (on-site or carry-in), and who provides it.
- In stock, delivery or pickup location, return policy.
- Any coupon code shown on the store page.

## Template

`assets/template.html` is the full page. Its DATA block holds a worked example (a Hebrew, RTL session from Israel). Replace that block entirely; do not edit anything outside it except `<title>`.
