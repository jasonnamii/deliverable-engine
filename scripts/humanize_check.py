#!/usr/bin/env python3
"""
paper-engine HUMANIZE_GATE 보조 스캐너 (v3.0, INV 16·17·18).

실행:
    python scripts/humanize_check.py FILE       # 산출물 grep
    python scripts/humanize_check.py --report   # 본 사전 카탈로그 출력

본질 게이트는 LLM 자체 판정 — "이 문장, 형 코퍼스 1MB 안에 한 번이라도 등장할 만한가?"
본 스캐너는 자주 새는 어휘를 사전·패턴으로 잡는 '보조 게이트'.

루프 하드캡: 산출물 적발 시 호출자가 평문변환 후 1회 재실행. 2회차 적발 → STOP+보고.

단일 권위: references/banwords-lexicon.md
"""

import json
import re
import sys
from pathlib import Path


# ============================================================
# BAN_LEXICON — 형 코퍼스 1MB·19874줄 실측 0회 검증된 어휘 위주
# 단일 권위: references/banwords-lexicon.md
# ============================================================

# 1. AI 메타담화 어구
BAN_META = [
    "결론적으로", "요약하면", "정리하면", "요컨대", "한마디로",
    "라고 할 수 있다", "라고 볼 수 있다", "할 수 있다고 본다",
    "주목할 만한", "강조할 필요가 있다", "다시 한번 강조하면",
    "언급할 가치가 있는", "주목할",
]

# 2. AI 형식주의 부사
BAN_FORMAL = [
    "본질적으로", "근본적으로", "구체적으로", "전반적으로",
    "점진적으로", "효과적으로", "효율적으로", "전략적으로",
    "혁신적으로", "지속적으로",
]

# 3. AI 접속 비대
BAN_CONJ = [
    "한편", "더욱이", "게다가", "나아가",
    "이에 따라", "이를 통해", "이러한 점에서",
    "이와 관련하여", "위와 같은 맥락에서",
]
# 따라서·그러므로는 일반어 충돌 → grep 시 가중치만 카운트

# 4. 영한 번역투
BAN_TRANS_PATTERNS = [
    (r"에\s*있어서", "~에 있어서"),
    (r"함에\s*있어", "~함에 있어"),
    (r"되어진다|되어졌다", "이중 피동"),
    (r"\b될\s*수\s*있다\b", "수동형 가능"),
    (r"어져야\s*한다", "이중 피동 의무"),
    (r"에\s*다름\s*아니다", "~에 다름 아니다"),
]

# 5. 형식명사 비대
BAN_FORM_NOUN_PATTERNS = [
    (r"것으로\s*보인다", "~것으로 보인다"),
    (r"수\s*있는\s*것이\s*있다", "~수 있는 것이 있다"),
    (r"수\s*있다고\s*본다", "~수 있다고 본다"),
    (r"할\s*필요가\s*있다", "~할 필요가 있다"),
    (r"하는\s*것이\s*중요하다", "~하는 것이 중요하다"),
    (r"라는\s*점에서", "~라는 점에서"),
]

# 6. 작업라벨 구조어
BAN_LABEL_PATTERNS = [
    (r"\b\d+축\b", "N축 라벨"),
    (r"\b\d+레이어\b", "N레이어 라벨"),
    (r"\b\d+트랙\b", "N트랙 라벨"),
    (r"\bPhase\s*\d+\b", "Phase N (영문)"),
    (r"\bLayer\s*\d+\b", "Layer N (영문)"),
    (r"\b페이즈\b", "페이즈"),
    (r"\b레이어\b", "레이어"),
]

# 형 시그니처 (참조용 — 차단 ✗, 카운트만)
SIG_FORMER = [
    "직접", "그냥", "왜", "어떻게", "정말",
    "확실히", "진짜", "사실", "딱", "근데", "솔직히",
]

# ============================================================
# ALLOW — 형 코퍼스에 빈도 있는 예외 (마케팅 업계어 등)
# ============================================================
ALLOW = {
    "패러다임",  # 형 코퍼스 5회
    "최적화",    # 형 코퍼스 52회
    "지속적으로",  # 형 코퍼스 21회 (위 BAN과 충돌 — 빈도 가중치로 후처리)
}

# 자기참조 면제 마커
SELF_REF_MARKERS = [
    "BAN_LEXICON", "humanize-gate.md", "banwords-lexicon.md",
    "humanize_check.py", "INV 16", "INV 17", "INV 18",
    "AI 5대 흔적", "형 코퍼스",
]


def scan_humanize(text: str, allow_self_ref: bool = False):
    """휴머나이즈 게이트 스캔. (line_no, line, matches, severity) 리스트 반환."""
    hits = []
    lines = text.split("\n")
    for i, line in enumerate(lines, 1):
        if allow_self_ref and any(m in line for m in SELF_REF_MARKERS):
            continue
        matches = []
        # 1. 메타담화 (HIGH)
        for w in BAN_META:
            if w in line and w not in ALLOW:
                matches.append(("META", w))
        # 2. 형식주의 부사 (HIGH)
        for w in BAN_FORMAL:
            if w in line and w not in ALLOW:
                matches.append(("FORMAL", w))
        # 3. 접속 비대 (MID)
        for w in BAN_CONJ:
            if w in line:
                matches.append(("CONJ", w))
        # 4. 번역투 패턴
        for pat, label in BAN_TRANS_PATTERNS:
            if re.search(pat, line):
                matches.append(("TRANS", label))
        # 5. 형식명사
        for pat, label in BAN_FORM_NOUN_PATTERNS:
            if re.search(pat, line):
                matches.append(("FNOUN", label))
        # 6. 작업라벨
        for pat, label in BAN_LABEL_PATTERNS:
            if re.search(pat, line):
                matches.append(("LABEL", label))
        if matches:
            severity = "HIGH" if any(c in ("META", "FORMAL", "LABEL") for c, _ in matches) else "MID"
            hits.append((i, line.rstrip(), matches, severity))
    return hits


def count_signature(text: str):
    """형 시그니처 어휘 빈도 카운트 (장려용)."""
    counts = {}
    for w in SIG_FORMER:
        cnt = len(re.findall(r"\b" + re.escape(w) + r"\b", text))
        if cnt:
            counts[w] = cnt
    return counts


def check_output(file_path: Path):
    """산출물 휴머나이즈 스캔. exit 0 통과, 1 적발."""
    if not file_path.exists():
        print(json.dumps({"status": "FAIL", "error": f"파일 없음: {file_path}"},
                         ensure_ascii=False, indent=2))
        sys.exit(2)
    text = file_path.read_text(encoding="utf-8")
    hits = scan_humanize(text, allow_self_ref=False)
    sig = count_signature(text)
    high = [h for h in hits if h[3] == "HIGH"]
    result = {
        "target": str(file_path),
        "ban_hits_count": len(hits),
        "ban_high_count": len(high),
        "signature_counts": sig,
        "status": "PASS" if not high else "FAIL",
        "guidance": (
            "1차 게이트는 LLM 자체 판정 — '이 문장, 형 코퍼스 1MB 안에 "
            "한 번이라도 등장할 만한가?'. 본 스캐너는 보조."
        ),
        "hits": [
            {"line": ln, "severity": sv, "matches": list(set(ms)), "text": txt[:200]}
            for ln, txt, ms, sv in hits[:30]
        ],
        "verdict": (
            f"통과 — HIGH 적발 0개. 시그니처 {sum(sig.values())}회"
            if not high
            else f"적발 HIGH {len(high)}개 / TOTAL {len(hits)}개 — 평문변환·재작성 필요. 부분치환 ✗"
        ),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if not high else 1)


def report():
    """본 사전 카탈로그 출력."""
    cat = {
        "META": BAN_META,
        "FORMAL": BAN_FORMAL,
        "CONJ": BAN_CONJ,
        "TRANS_PATTERNS": [p[1] for p in BAN_TRANS_PATTERNS],
        "FNOUN_PATTERNS": [p[1] for p in BAN_FORM_NOUN_PATTERNS],
        "LABEL_PATTERNS": [p[1] for p in BAN_LABEL_PATTERNS],
        "SIGNATURE_FORMER": SIG_FORMER,
        "ALLOW": list(ALLOW),
    }
    print(json.dumps(cat, ensure_ascii=False, indent=2))


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python scripts/humanize_check.py FILE")
        print("  python scripts/humanize_check.py --report")
        sys.exit(2)

    if sys.argv[1] == "--report":
        report()
        return

    check_output(Path(sys.argv[1]).resolve())


if __name__ == "__main__":
    main()
