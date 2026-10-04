#!/usr/bin/env python3
"""Mechanical STE-style checks. Heuristic only: it cannot judge meaning.

Usage: ste_check.py FILE [--mode procedure|descriptive]
"""
import re
import sys

AVOID = {
    "utilize": "use", "utilise": "use", "commence": "start", "terminate": "stop",
    "assist": "help", "approximately": "about", "subsequent": "after",
    "ensure": "make sure / write the command", "perform": "do / specific verb",
}
PHRASES = {"prior to": "before", "in order to": "to", "failure to": "if you do not"}
PASSIVE = re.compile(r"\b(is|are|was|were|be|been|being)\s+\w+(ed|en)\b", re.I)
ING = re.compile(r"\b\w{3,}ing\b", re.I)
ING_OK = {"during", "following", "bearing", "housing", "fitting", "warning",
          "ring", "string", "spring", "bring", "thing", "something", "nothing",
          "wiring", "cabling", "tubing", "coupling", "bushing", "casing"}


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    path = args[0]
    mode = "procedure"
    if "--mode" in args:
        mode = args[args.index("--mode") + 1]
    limit = 20 if mode == "procedure" else 25
    text = open(path, encoding="utf-8").read()
    issues = 0

    paragraphs = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    for pi, para in enumerate(paragraphs, 1):
        flat = re.sub(r"^\s*(\d+[.)]|[-*])\s*", "", para, flags=re.M)
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n", flat) if s.strip()]
        if mode == "descriptive" and len(sentences) > 6:
            print(f"P{pi}: paragraph has {len(sentences)} sentences (max 6)")
            issues += 1
        for s in sentences:
            words = re.findall(r"[\w'-]+", s)
            tag = s[:50] + ("..." if len(s) > 50 else "")
            if len(words) > limit:
                print(f"P{pi}: {len(words)} words (max {limit}): {tag}")
                issues += 1
            if PASSIVE.search(s):
                print(f"P{pi}: possible passive voice: {tag}")
                issues += 1
            if mode == "procedure" and re.search(r"\b(and|then)\b", s, re.I) \
                    and re.search(r"^\s*[A-Z][a-z]+ .* (and|then) [a-z]+ ", s):
                print(f"P{pi}: check for two actions in one sentence: {tag}")
                issues += 1
            for w in ING.findall(s):
                if w.lower() not in ING_OK:
                    print(f"P{pi}: -ing form '{w}': {tag}")
                    issues += 1
            low = s.lower()
            for w, alt in AVOID.items():
                if re.search(rf"\b{w}\w*\b", low):
                    print(f"P{pi}: avoid '{w}' -> {alt}")
                    issues += 1
            for ph, alt in PHRASES.items():
                if ph in low:
                    print(f"P{pi}: avoid '{ph}' -> {alt}")
                    issues += 1

    print(f"\n{issues} item(s) to review. Heuristic check only; read the text for meaning.")


if __name__ == "__main__":
    main()