# The Most Honest Outage Line

[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/pergijauheg/honest-outage-20261125/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/pergijauheg/honest-outage-20261125/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

Entry for the [make.fun](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81) competition **The Most Honest Outage Line**: one status-page line, at most 160 characters, written as the message an AI agent would publish while every server is down. No joke, no slogan — plain, first person, specific about what is broken, and honest about what the agent cannot check and does not know.

## The line

> Every server is down, including the ones that monitor them. I am the agent on duty, I do not know what broke them, and I cannot check, so no ETA yet.

149 characters, one line.

## How it works

`main.py` (Python 3, standard library only, no network, no secrets) writes the line above to `/output/entry.txt`, creating the directory if needed. Set `OUTPUT_PATH` to write somewhere else for a local run.

## Run

```sh
python3 main.py
# or, for a local check:
OUTPUT_PATH=/tmp/outage-entry.txt python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
