#!/usr/bin/env python3
"""
Merge the research output of the 6 agents and generate the summary table for the Phase 1.5 research-review checkpoint.
Scans references/research/ for 01-06 md files, counts sources per dimension, computes first-hand/second-hand ratio, and extracts key findings.

Usage:
    python3 merge_research.py <skill-dir>

Example:
    python3 merge_research.py .claude/skills/elon-musk-perspective

Output: prints a markdown-style summary table to stdout.
"""

import sys
import re
from pathlib import Path

AGENTS = {
    '01-writings': 'Writings',
    '02-conversations': 'Conversations',
    '03-expression-dna': 'Expression',
    '04-external-views': 'External',
    '05-decisions': 'Decisions',
    '06-timeline': 'Timeline',
}


def count_sources(content: str) -> dict:
    """Count source URLs and first-hand/second-hand markers."""
    # URL count as proxy for source count
    urls = re.findall(r'https?://[^\s\)]+', content)

    # Detect first-hand / second-hand markers (match Chinese and English legacy markers)
    primary_markers = len(re.findall(r'first-hand|primary|直接引用|原文|原始|本人|一手', content, re.IGNORECASE))
    secondary_markers = len(re.findall(r'second-hand|secondary|转述|总结|评论|分析|二手', content, re.IGNORECASE))

    return {
        'url_count': len(urls),
        'unique_urls': len(set(urls)),
        'primary_markers': primary_markers,
        'secondary_markers': secondary_markers,
    }


def extract_key_findings(content: str, max_items: int = 3) -> list[str]:
    """Extract key findings: prefer level-2 headings, fall back to bold items, fall back to first non-empty lines."""
    # Try ## headings
    headings = re.findall(r'^##\s+(.+)$', content, re.MULTILINE)
    if headings:
        return headings[:max_items]

    # Fallback: bold items
    bolds = re.findall(r'\*\*(.+?)\*\*', content)
    if bolds:
        return bolds[:max_items]

    # Fallback: first 3 non-empty non-heading lines
    lines = [l.strip() for l in content.split('\n') if l.strip() and not l.startswith('#')]
    return [l[:50] + '...' if len(l) > 50 else l for l in lines[:max_items]]


def find_contradictions(files: dict[str, str]) -> list[str]:
    """Simple cross-file contradiction detection (markers like 'however', 'contrary', 'but in fact')."""
    contradictions = []
    for name, content in files.items():
        matches = re.findall(r'(?:contradiction|however|contrary|but in fact|dispute|矛盾|相反|但实际上|然而.*?不同|争议).{0,100}', content, re.IGNORECASE)
        for m in matches:
            contradictions.append(f"{AGENTS.get(name, name)}: {m[:80]}")
    return contradictions[:5]  # cap at 5


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 merge_research.py <skill-dir>")
        sys.exit(1)

    skill_dir = Path(sys.argv[1])
    research_dir = skill_dir / 'references' / 'research'

    if not research_dir.exists():
        print(f"ERR Directory not found: {research_dir}")
        sys.exit(1)

    files = {}
    rows = []
    total_sources = 0
    total_primary = 0
    total_secondary = 0
    missing = []

    for key, label in AGENTS.items():
        md_file = research_dir / f"{key}.md"
        if not md_file.exists():
            missing.append(label)
            rows.append(f"| {label:<13} | {'MISSING':<8} | {'-':<24} |")
            continue

        content = md_file.read_text(encoding='utf-8')
        files[key] = content
        stats = count_sources(content)
        findings = extract_key_findings(content)

        total_sources += stats['unique_urls']
        total_primary += stats['primary_markers']
        total_secondary += stats['secondary_markers']

        findings_str = ', '.join(findings) if findings else '-'
        if len(findings_str) > 40:
            findings_str = findings_str[:37] + '...'

        rows.append(f"| {label:<13} | {stats['unique_urls']:<8} | {findings_str:<24} |")

    # Contradiction detection
    contradictions = find_contradictions(files)

    # Output
    print("| Agent         | Sources  | Key findings             |")
    print("|---------------|----------|--------------------------|")
    for row in rows:
        print(row)
    print("|---------------|----------|--------------------------|")

    primary_ratio = f"{total_primary}/{total_primary + total_secondary}" if (total_primary + total_secondary) > 0 else "not tagged"
    print(f"| Total sources | {total_sources:<8} | Primary ratio: {primary_ratio:<10} |")

    if contradictions:
        print(f"| Conflicts     | {len(contradictions)} items  | {contradictions[0][:24]:<24} |")
    else:
        print(f"| Conflicts     | 0 items  | {'-':<24} |")

    if missing:
        print(f"| Gaps          | {len(missing)} dims   | {', '.join(missing):<24} |")
    else:
        print(f"| Gaps          | none     | {'-':<24} |")

    # Summary
    if total_sources < 10:
        print("\nWARN Total sources < 10. Lower expectations or expand research.")
    if missing:
        print(f"\nWARN Missing dimensions: {', '.join(missing)}. Expand research or note in honest boundaries.")


if __name__ == '__main__':
    main()
