## Javier Elías Crespo

**I direct Claude Code to build systems that run on their own, and I prove they work.**

BFA in Industrial Design → butler at The St. Regis → licensed phone agent at Optum (UnitedHealthcare) → AI builder.
Puerto Rico · US citizen · English and Spanish.

**Portfolio → [javierxelias-svg.github.io](https://javierxelias-svg.github.io)** · [LinkedIn](https://www.linkedin.com/in/javier-elías-83343b39a) · javierxelias@gmail.com

---

### The proof: [CareerOS](https://github.com/javierxelias-svg/careeros-public)

A job-search engine I designed and operate. Every morning it reads employers' own job boards, throws out what doesn't fit, ranks the rest and sends me a short list.

| | |
|---|---|
| **Runs by itself** | Every morning on GitHub Actions. **108 of its first 109 cloud runs passed** since Sep 28, 2026. The one failure was a break I caused on purpose, to prove the alert reaches my phone. |
| **Built over** | **125 commits I directed** since July 6, 2026, plus 57 the system made itself (its daily records). |
| **Reads** | **295 employer job boards, 16,258 listings** in the live engine's Oct 17, 2026 run. |
| **Tested** | **25 test files, 886 checks in the live engine (744 in the public copy), all passing.** When a real posting fools it, that posting becomes a test so the mistake can't come back. |
| **Size** | 13,765 lines of Python in the live engine (12,517 in the public copy). I didn't hand-type them. I decided what each part does, reviewed it, and verified it by running it. |

<!-- careeros:start -->
Public copy, run by GitHub every day. Last run Oct 26, 2026: 11,327 listings from 189 job boards · 744 checks passing · [run log](https://github.com/javierxelias-svg/careeros-public/actions/runs/40368171683)
<!-- careeros:end -->

### How I build

1. **Write the rule first,** in plain words: what "done" means and what the system must never do.
2. **Claude Code writes the code.**
3. **I run it and read the real output,** not a summary of it.
4. **I break it on purpose** (bad input, missing key, no network) and make sure it fails loudly instead of quietly.
5. **Nothing counts as done without a receipt:** a passing test, a message ID, a log line. The sentence *"this should work"* is banned.

What I keep out of the AI's hands: secrets (they live in GitHub secrets and the Mac Keychain, never in code), and the last step of anything that reaches a real person.

### Times it was confidently wrong, and how I caught it

- **A $260,000 salary that didn't exist.** The parser read "$125M raised at Series B" as $125 an hour. Funding figures are now refused, and that exact sentence is a test.
- **27 days of silence and no alarm.** A power outage killed the Mac, and the alarms lived on the same dead machine. I moved it to the cloud, and now the morning message reports its own absence ("No digest for 3 days").
- **I blamed the wrong part, then corrected the record.** The bug looked like a broken salary reader. The reader was right; it was being fed bad data. I made a separate commit just to fix my own wrong explanation.
- All of it, dated, with the fix and the test for each: **[the build log →](https://github.com/javierxelias-svg/careeros-public/blob/main/BUILD-LOG.md)** · **[How I debug it →](https://javierxelias-svg.github.io/how-i-found-this/)**

### The other half

Two years as a butler and two years on the phone with health-insurance members taught me what most builders never practice: explaining technical things to non-technical people in the words they actually use, and staying calm when someone's problem is urgent.

**Also built:** [Food Pantry Weekly Digest](https://javierxelias-svg.github.io/food-pantry-weekly-digest/), a working demo that turns a pantry's weekly numbers into a plain-English brief and a community ask ([code](https://github.com/javierxelias-svg/food-pantry-weekly-digest)).

**Learning now:** SQL.
