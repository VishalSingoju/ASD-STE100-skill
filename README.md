# ASD-STE100-skill
A Claude skill for writing and reviewing technical text in ASD-STE100 Simplified Technical English, with a rules reference and a heuristic checker script.
# asd-ste100

A Claude skill that helps write, rewrite, and review text in
ASD-STE100 Simplified Technical English, the controlled language
maintained by the AeroSpace and Defence Industries Association of Europe (ASD).

## What it does
- Rewrites procedures, warnings, SOPs, and runbooks into clear, unambiguous English
- Applies the core STE rules: short sentences, active voice, one instruction per
  step, one meaning per word, and limited noun clusters
- Includes a script (`scripts/ste_check.py`) that flags long sentences, passive
  voice, -ing forms, and words that have simpler replacements

## What's inside
- `SKILL.md`: workflow and core rules
- `references/rules.md`: condensed rule summary and word substitutions
- `scripts/ste_check.py`: heuristic checker

## Limitations
This is a condensed, paraphrased working version, not the official specification
or the approved-word dictionary. The checker is heuristic and cannot judge
meaning. For certified or contractual documents, verify against the current
issue at asd-ste100.org.

## Disclaimer
ASD-STE100 is owned and maintained by ASD. This project is independent and is
not affiliated with or endorsed by ASD.
