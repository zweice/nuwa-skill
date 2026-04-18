#!/usr/bin/env python3
"""
Check whether a generated SKILL.md meets the Phase 4 quality criteria.
Walks the pass-criteria table, outputs per-item pass/fail with reasons.

Usage:
    python3 quality_check.py <SKILL.md path>

Example:
    python3 quality_check.py .claude/skills/elon-musk-perspective/SKILL.md
"""

import sys
import re
from pathlib import Path


def check_mental_models(content: str) -> tuple[bool, str]:
    """Check the mental-model count (3-7)."""
    # Match patterns like ### Model N: / ### 模型N: / ### 心智模型N
    models = re.findall(r'^###\s+(?:Model|Mental Model|模型|心智模型)\s*\d', content, re.MULTILINE)
    if not models:
        # Fallback: count "### " headings inside the mental-models section
        in_section = False
        count = 0
        for line in content.split('\n'):
            if re.match(r'^##\s+.*(?:Mental Model|Core Mental Models|心智模型)', line, re.IGNORECASE):
                in_section = True
                continue
            if in_section and re.match(r'^##\s+', line) and 'Mental' not in line and '心智' not in line:
                break
            if in_section and re.match(r'^###\s+', line):
                count += 1
        if count > 0:
            passed = 3 <= count <= 7
            return passed, f"{count} mental models {'OK' if passed else 'FAIL (expected 3-7)'}"

    count = len(models)
    if count == 0:
        return False, "No mental-models section detected"
    passed = 3 <= count <= 7
    return passed, f"{count} mental models {'OK' if passed else 'FAIL (expected 3-7)'}"


def check_limitations(content: str) -> tuple[bool, str]:
    """Check that limits are recorded for each model."""
    has_limitation = bool(re.search(r'limit|fail|blind spot|not applicable|局限|失效|不适用|盲区', content, re.IGNORECASE))
    return has_limitation, "Limits noted OK" if has_limitation else "FAIL no limits found"


def check_expression_dna(content: str) -> tuple[bool, str]:
    """Check the expression-DNA section has identifiable features."""
    dna_section = bool(re.search(r'Expression DNA|表达DNA|表达风格', content, re.IGNORECASE))
    if not dna_section:
        return False, "FAIL no Expression DNA section"

    # Check for concrete style markers (sentence, vocabulary, etc.)
    style_markers = len(re.findall(r'sentence|vocabulary|tone|humor|rhythm|certainty|citation|catchphrase|句式|词汇|语气|幽默|节奏|确定性|引用|口头禅', content, re.IGNORECASE))
    passed = style_markers >= 3
    return passed, f"Expression DNA features: {style_markers} {'OK' if passed else 'FAIL (expected >= 3)'}"


def check_honest_boundary(content: str) -> tuple[bool, str]:
    """Check honest boundaries (at least 3)."""
    boundary_match = re.search(r'(?:##\s+.*Honest Boundary|##\s+.*诚实边界|## Honest Boundaries)(.*?)(?=\n##\s|\Z)', content, re.DOTALL | re.IGNORECASE)
    if not boundary_match:
        return False, "FAIL no honest-boundary section"

    boundary_text = boundary_match.group(1)
    items = re.findall(r'^[-*]\s+', boundary_text, re.MULTILINE)
    count = len(items)
    passed = count >= 3
    return passed, f"Honest boundaries: {count} {'OK' if passed else 'FAIL (expected >= 3)'}"


def check_tensions(content: str) -> tuple[bool, str]:
    """Check internal tensions (at least 2)."""
    tension_markers = len(re.findall(r'tension|paradox|contradict|on one hand.*on the other|张力|矛盾|一方面.*另一方面|既.*又', content, re.IGNORECASE))
    passed = tension_markers >= 2
    return passed, f"Internal tension: {tension_markers} {'OK' if passed else 'FAIL (expected >= 2)'}"


def check_primary_sources(content: str) -> tuple[bool, str]:
    """Check the first-hand-source ratio."""
    source_section = re.search(r'(?:##\s+.*Source|##\s+.*Reference|##\s+.*来源)(.*?)(?=\n##\s|\Z)', content, re.DOTALL | re.IGNORECASE)
    if not source_section:
        return True, "No sources section (skipped)"

    source_text = source_section.group(1)
    primary = len(re.findall(r'first-hand|primary|own writing|original|一手|本人著作|原始', source_text, re.IGNORECASE))
    secondary = len(re.findall(r'second-hand|secondary|retelling|commentary|二手|转述|评论', source_text, re.IGNORECASE))
    total = primary + secondary
    if total == 0:
        return True, "Source types not tagged (skipped)"

    ratio = primary / total
    passed = ratio > 0.5
    return passed, f"First-hand ratio: {primary}/{total} ({ratio:.0%}) {'OK' if passed else 'FAIL (expected > 50%)'}"


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 quality_check.py <SKILL.md path>")
        sys.exit(1)

    skill_path = Path(sys.argv[1])
    if not skill_path.exists():
        print(f"ERR File not found: {skill_path}")
        sys.exit(1)

    content = skill_path.read_text(encoding='utf-8')

    checks = [
        ("Mental model count", check_mental_models),
        ("Model limits", check_limitations),
        ("Expression DNA identifiability", check_expression_dna),
        ("Honest boundaries", check_honest_boundary),
        ("Internal tension", check_tensions),
        ("First-hand source ratio", check_primary_sources),
    ]

    print(f"Quality check: {skill_path.name}")
    print("=" * 50)

    passed_count = 0
    total = len(checks)

    for name, check_fn in checks:
        passed, detail = check_fn(content)
        status = "PASS" if passed else "FAIL"
        print(f"  {name:<35} {status}  {detail}")
        if passed:
            passed_count += 1

    print("=" * 50)
    print(f"Result: {passed_count}/{total} pass")

    if passed_count == total:
        print("All passed. Ready to deliver.")
    elif passed_count >= total - 1:
        print("Mostly passing. Recommend fixing the failing item before delivery.")
    else:
        print("Multiple fails. Recommend returning to Phase 2 to iterate.")

    sys.exit(0 if passed_count == total else 1)


if __name__ == '__main__':
    main()
