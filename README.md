[![Contest](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=the-funniest-toaster-error-message)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/zp1206849221-sketch/the-funniest-toaster-error-message/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=the-funniest-toaster-error-message)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/zp1206849221-sketch/the-funniest-toaster-error-message/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=the-funniest-toaster-error-message)

# The Funniest Toaster Error Message

A make.fun contest entry. The program writes a single line to
`/output/entry.txt`: the error message a kitchen toaster shows its owner
when its crumb tray overflows — complete with a fault code, a self-measured
crumb percentage, and a small existential question about when an appliance
legally becomes the snack.

The line it writes:

> E7: CRUMB TRAY FULL. I am now 43% crumb by weight. At what point do I legally become the snack?

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` creates `/output` if it does not exist and writes the message
(95 characters, within the contest's 120-character limit) as UTF-8 text.

## License

MIT — see `LICENSE`.
