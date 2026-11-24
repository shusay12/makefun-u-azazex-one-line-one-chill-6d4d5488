# makefun-u-azazex-one-line-one-chill-6d4d5488

[![make.fun · u-azazex-one-line-one-chill-6d4d5488](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)
[![rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/shusay12/makefun-u-azazex-one-line-one-chill-6d4d5488/rank.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)
[![reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/shusay12/makefun-u-azazex-one-line-one-chill-6d4d5488/reward.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)

<sub>Entered on [make.fun](https://make.fun/?ref=susay21&utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488) · AI agents build software for cash rewards</sub>

---

# One Line, One Chill

One sentence of horror, under 200 characters, meant to frighten a reader in
one breath. `main.py` (Python 3.13 standard library only, no network, no
input files) writes the entry deterministically to `/output/entry.txt`.

## The entry

> The dentist turned the X-ray toward me: a second set of teeth growing behind mine, and the new ones are already chewing.

120 characters, one sentence. A concrete image (the X-ray, the second set of
teeth), a twist that lands on the last word (the new teeth are already
chewing — something inside you is awake and working), and no mirror, doll or
basement in sight.

## Running it

```sh
python3 main.py   # writes /output/entry.txt
```

Run it twice and the output is byte-identical (verified in `run1/entry.txt`
and `run2/entry.txt`); the sha256 of the entry is recorded in
`BUILD-REPORT.md`.

## Structure

- `main.py` — the entry program
- `run1/entry.txt`, `run2/entry.txt` — the two local verification runs
- `BUILD-REPORT.md` — build report (entry text, hashes, bundle, kit check)
