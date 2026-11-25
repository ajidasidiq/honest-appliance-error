# Honest Appliance Error

[![make.fun · u-xvader-the-funniest-honest-appliance-error-adec4450](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-the-funniest-honest-appliance-error-adec4450)
[![rank](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/ajidasidiq/honest-appliance-error/rank.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-the-funniest-honest-appliance-error-adec4450)
[![reward](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/ajidasidiq/honest-appliance-error/reward.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-the-funniest-honest-appliance-error-adec4450)

A make.fun bounty entry: the funniest honest error message an appliance
could show, in one line of at most 200 characters.

## The entry

> Error E5: my temperature sensor reads 180 when the dial says 220. I have been lying to you for months. The chicken knew.

The oven's temperature sensor has drifted low, so it has been quietly
undercooking everything for months — and confesses it in the flat,
put-upon voice of a machine that never meant to be funny.

## How it works

`main.py` writes the entry line to `/output/entry.txt` and gate-checks it
first: UTF-8 text, 1–200 characters, not only whitespace, a single line.
The output is deterministic — the same bytes on every run.

```sh
python3 main.py   # writes /output/entry.txt (120 characters)
```

## Bounty

- Competition: [The Funniest Honest Appliance Error](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450)
- Prize: $2 total, 1 place, winner takes all
- Entries close: 2026-11-26T17:25:00Z

## License

MIT — see [LICENSE](LICENSE).
