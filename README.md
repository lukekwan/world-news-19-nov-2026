[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/lukekwan/world-news-19-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/lukekwan/world-news-19-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# World News — 19 November 2026

One image that sums up 19 November's world news, built as a breaking-news
front page. The date is printed right up top so the picture stands on its
own: red BREAKING banner, "THE WORLD." masthead, one lead story, six more
stories down the side, and a ticker along the bottom.

## The 12 stories

**Lead:** Trump, Xi and Putin meet in Shenzhen — first-ever trilateral
summit, held today (Nov 19). Xi greeted Trump at the airport; Xi called
Russia ties a "source of stability"; Putin called Western powers "former
hegemons".

1. Anthropic IPO raises $81.3B, the largest IPO ever, topping SpaceX's
   $75B; $107.3B with a $26B private placement; shares start trading on
   Nasdaq today under ANT; valued at about $1.5 trillion.
2. Ethiopia-Eritrea border clashes near Badme; troops massing along the
   1,000 km border; fears of full-scale war.
3. Israel launches first Gaza ground push since the truce, tanks past the
   Yellow Line near Nuseirat camp; dozens flee.
4. U.S. and Venezuela sign deal to re-establish military ties, Defence
   Secretary Hegseth says.
5. Bangladesh deploys paramilitary as unrest grows over Hasina's return;
   arson attacks reported.
6. Magnitude 5.7 earthquake hits Kumamoto, Japan; no tsunami warning.

**Ticker:** COP31 climate talks in Antalya near a deal, closing Nov 20. ·
U.S.-Saudi nuclear deal "satisfactory", IAEA chief Grossi says. · Record
one in four children now live in conflict zones, Save the Children says
(23.4% in 2025). · Russian military aircraft alarm Taiwan and Japan after
flying south from Russia's Far East. · NASA's Voyager 1 reaches a
light-day from Earth.

## How it's made

`poster.html` is plain HTML/CSS with one inline SVG diagram (the three
leaders converging on Shenzhen) — no external assets, system fonts only.
`shoot.mjs` screenshots it to `entry.png` at exactly 1024x1024 with
headless Chromium. `main.py` (standard library only) copies the rendered
image to the output directory and checks the PNG signature, the 1 MiB size
limit, the 1024x1024 dimensions, and that the bytes are identical across
runs.
