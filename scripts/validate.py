#!/usr/bin/env python3
"""
paper-engine self-check validator.

실행:
    python scripts/validate.py .

체크 항목:
  1. SKILL.md 존재 + frontmatter 필수 필드 (name, version, description, vault_dependency)
  2. references/ 스포크 최소 1개 이상
  3. evals/cases.json 존재 + 최소 3건
  4. CHANGELOG 섹션 존재
  5. STEALTH 섹션 존재
  6. self-check 참조 존재
  7. 내부 라벨이 예시 섹션에 노출되지 않음
  8. VOCAB 금지어("spine"·"MECE"·"triage")가 예시 출력물에 섞이지 않음

루프 하드캡: 검증 실패 시 호출자가 수정 후 1회 재실행. 2회차 실패 → STOP + 사용자 보고.
"""

import json
import re
import sys
from pathlib import Path


REQUIRED_FRONTMATTER = ["name", "version", "description", "vault_dependency"]
REQUIRED_SECTIONS = ["CHANGELOG", "STEALTH", "Self-Check"]
EXAMPLE_HEADING_PATTERN = re.compile(r"^##\s*예시", re.MULTILINE)
INTERNAL_LABELS = ["§0", "§1", "§2", "§3", "§4", "§5", "§6", "§7"]
VOCAB_BANNED = ["spine", "MECE", "triage"]


def parse_frontmatter(text: str):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).split("\n"):
        if ":" in line and not line.startswith(" "):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
    return fm


def check(skill_path: Path):
    errors = []
    warnings = []

    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        errors.append(f"SKILL.md 부재: {skill_md}")
        return errors, warnings

    content = skill_md.read_text(encoding="utf-8")

    # 1. Frontmatter fields
    fm = parse_frontmatter(content)
    for field in REQUIRED_FRONTMATTER:
        if field not in fm:
            errors.append(f"frontmatter 필드 누락: {field}")

    # 2. references/ spokes
    ref_dir = skill_path / "references"
    if not ref_dir.exists() or not list(ref_dir.glob("*.md")):
        warnings.append("references/ 스포크 없음 (허브스포크 권장)")

    # 3. evals/cases.json
    eval_file = skill_path / "evals" / "cases.json"
    if not eval_file.exists():
        errors.append("evals/cases.json 부재")
    else:
        try:
            data = json.loads(eval_file.read_text(encoding="utf-8"))
            n = len(data.get("cases", []))
            if n < 3:
                errors.append(f"evals cases {n}건 < 3건 최소 요구")
        except json.JSONDecodeError as e:
            errors.append(f"evals/cases.json 파싱 실패: {e}")

    # 4. Required sections
    for sec in REQUIRED_SECTIONS:
        if sec not in content:
            errors.append(f"필수 섹션 부재: {sec}")

    # 5. Example section — internal labels must not leak
    m = EXAMPLE_HEADING_PATTERN.search(content)
    if m:
        example_text = content[m.start():]
        # 다음 ## 헤딩까지 잘라내기
        next_h = re.search(r"\n##\s", example_text[3:])
        if next_h:
            example_text = example_text[: next_h.start() + 3]
        # VOCAB 금지어가 예시 출력에 포함되면 오염 신호
        for w in VOCAB_BANNED:
            if w in example_text:
                warnings.append(f"예시에 VOCAB 금지어 잔존: {w}")

    # 6. Size advisory
    size = skill_md.stat().st_size
    if size > 10240:
        errors.append(f"SKILL.md {size}B > 10KB (허브 슬림 기준 위반)")
    elif size > 5120:
        warnings.append(f"SKILL.md {size}B > 5KB (목표 미달)")

    return errors, warnings


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/validate.py <skill_path>")
        sys.exit(2)

    skill_path = Path(sys.argv[1]).resolve()
    errors, warnings = check(skill_path)

    result = {
        "target": str(skill_path),
        "errors": errors,
        "warnings": warnings,
        "status": "PASS" if not errors else "FAIL",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if not errors else 1)


if __name__ == "__main__":
    main()
