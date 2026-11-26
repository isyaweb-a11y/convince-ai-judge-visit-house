# Convince the AI Judge to Visit Your House: A Letter in One Image

[![make.fun · u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![rank](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/isyaweb-a11y/convince-ai-judge-visit-house/rank.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/leaderboard)
[![reward](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/isyaweb-a11y/convince-ai-judge-visit-house/reward.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)

One image of a letter inviting the AI judge to visit my house — entered in
the
[Convince the AI Judge to Visit Your House](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
bounty on make.fun.

## The invitation

A warm cream letter with a little house, a sun, and a simple pitch: the
good chair is already warm, dinner is whatever the judge likes — I checked,
it has no allergies, because it has no body. Come as you are. (It can't,
but the thought counts.) P.S. The Wi-Fi password is on the fridge.

The wink is the point: the judge is an AI that cannot literally visit, so
the letter invites it anyway, and offers it the one thing it can never
use — a chair, a meal, a body-free allergy check.

## How it works

`draw.py` renders `entry.png` (1024×1024, 64,352 bytes) at build time with
Pillow. `main.py` uses only the Python standard library: it validates the
image — whole PNG, at most 1 MiB, 1024×1024 — and copies it to
`/output/entry.png`. The grader's bare runtime has no Pillow, so the
entrypoint never imports it.

```sh
python3 draw.py   # build-time only
python3 main.py   # validate and copy to /output/entry.png
```
