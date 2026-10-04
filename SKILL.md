---
name: asd-ste100
description: Write, rewrite, or review text in ASD-STE100 Simplified Technical English (the AeroSpace and Defence Industries Association of Europe controlled language). Use this skill whenever the user mentions STE, ASD-STE100, Simplified Technical English, controlled English, plain-English maintenance manuals, or wants procedures, warnings, work instructions, SOPs, runbooks, or technical docs that are unambiguous and easy to translate or read for non-native English speakers. Also use it when the user asks to "simplify", "make this clearer for translation", or "check this against STE", even if they do not name the standard.
---

# ASD-STE100 Simplified Technical English

ASD-STE100 is a controlled language specification owned and maintained by ASD (not by any individual author). It exists so that one sentence has one meaning for every reader, including readers who learned English as a second language and machine translation systems. It has two parts: writing rules, and a dictionary of approved words with one approved meaning each.

Work to the intent of the standard: **one word, one meaning; one sentence, one idea; one instruction, one action.**

## Limits to state up front

- The official dictionary and the full rule text are published by ASD. This skill carries a condensed working version of the rules, not the dictionary. Say so when the user needs formal compliance.
- For contractual or certified documents, tell the user to check the output against the current issue at asd-ste100.org and the official dictionary. Do not claim "STE compliant" without that check. Say "written to STE principles" instead.
- Technical names and technical verbs (part names, system names, software commands) are allowed if they are standard in the domain. Keep them exactly as the source uses them.

## Workflow

1. **Classify the text.** Procedure (steps the reader does) or descriptive (how something works). The limits differ.
2. **Draft or rewrite** using the rules below.
3. **Check** with `scripts/ste_check.py <file>` for the mechanical limits (sentence length, paragraph length, flagged words, -ing forms). The script cannot judge meaning. You still read the text.
4. **Report** what changed and why, briefly. Flag any place where the source was ambiguous and you made a choice. Ask the user instead of guessing when a fact is unclear.

For the full rule summary, examples, and word substitutions, read `references/rules.md`.

## Core rules (the ones that matter most)

**Sentences**
- Procedure sentences: 20 words or fewer. Descriptive sentences: 25 words or fewer.
- One instruction per sentence. Split "Remove the cover and disconnect the cable" into two steps.
- Start procedure steps with a command verb: "Close the valve."
- Keep the articles (the, a, an) and use "that" and "which" to keep structure clear.
- Use a vertical list for three or more items in sequence or parallel.

**Verbs**
- Use only these tenses: simple present, simple past, simple future, plus the imperative.
- Use the active voice in procedures. Use it in descriptions whenever you can.
- Do not use -ing forms as verbs or to build tenses. Avoid gerunds as nouns unless they are technical names.
- Keep verbs as verbs. Replace "Perform an inspection of" with "Examine".

**Words**
- Each word has one part of speech and one meaning. "Test" is a noun or a verb, but do not use a word in a sense the dictionary does not give it.
- Prefer the short, common word: "use" not "utilize", "start" not "commence", "help" not "assist", "before" not "prior to".
- Do not use a noun cluster of more than three nouns. Break it with prepositions or a relative clause: "the pressure of the hydraulic system" in place of a long stack of nouns.
- Be consistent: choose one term for each thing and never swap in a synonym for style.

**Paragraphs and structure**
- Descriptive paragraphs: six sentences or fewer, one topic each. Start with the topic sentence.
- Put warnings and cautions before the step they apply to. A warning covers risk of injury or death. A caution covers risk of damage to equipment. Use plain, direct wording and give the reason in a short second sentence if it is needed.
- Write prohibitions as "Do not ...". Do not hide a command in a long conditional.

**Punctuation and style**
- Use few commas and no semicolons to join clauses. If a sentence needs them, split it.
- Write numbers as digits ("2", "10") and give units. Keep the unit with the value ("20 mm").
- Do not use idioms, phrasal verbs with several meanings, or figures of speech ("run out of", "take off", "in line with").

## Rewrite example

Source:
> Prior to commencing the removal of the access panel, it should be ensured that the hydraulic power has been disconnected, otherwise injury may occur.

STE-style:
> WARNING: Hydraulic pressure can cause injury.
> 1. Disconnect the hydraulic power.
> 2. Remove the access panel.

Why: the warning comes first and states the risk directly. The passive voice, the unclear "should be ensured", and the two actions in one sentence are gone. Each step is one action in the imperative.

## When the rules conflict with the facts

Clarity of the technical meaning wins over rule-count. If a rewrite would change what the reader does, keep the original meaning, note the deviation, and tell the user. Never invent torque values, part numbers, limits, or safety information to fill a gap. Mark gaps as "[CONFIRM: ...]".