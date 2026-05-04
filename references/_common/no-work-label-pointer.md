# §INV NO_WORK_LABEL — 1줄 포인터 정본

> **다이어트 v2**: 43개 스킬 verbatim 표 박제 → 1줄 포인터 치환. 효과 100% 유지·토큰 ~24KB 절감.
> **본질 정본**: `shaper-skill/references/no-work-label.md` (이미 존재)

---

## 5줄 핵심 (각 스킬 SKILL.md에 인라인 박제용)

| | |
|---|---|
| RULE | 산출물·대화 = 인간 언어. 작업 라벨 ZERO. (1만 페이지 1단어 = FAIL) |
| 판정 | "이 단어, 이 대화 밖 사람이 사전 없이 읽을 수 있나?" — NO → 작업 라벨 → 금지 |
| ALLOW | 업계 전문용어·고유명사·법조문 |
| CONVERT | 라벨 발견 → 실명·평문 풀어쓰기 |
| SELF_CHECK | 산출 직전 자체 스캔. 1개라도 발견 = 차단·재작성 |

상세·예외·도메인별 ALLOW 리스트는 → `shaper-skill/references/no-work-label.md`

---

## 호출 패턴 (각 SKILL.md에 1줄 포인터)

```markdown
## §INV NO_WORK_LABEL
산출물·대화 모두 작업 라벨 ZERO. → `shaper-skill/references/no-work-label.md`
```

도메인별 ALLOW 리스트가 필요한 스킬(예: ads-playbook의 ROAS·CPA·CAPI 등)은 본문에 ALLOW만 1줄 추가:

```markdown
## §INV NO_WORK_LABEL
산출물·대화 작업 라벨 ZERO. ALLOW: ROAS·CPA·CAPI·tROAS·SKAN·PMax·ASA·ASC·UAC·CTR·CVR·CPC·CPM·LTV·CAC·MMP·MMM. → `shaper-skill/references/no-work-label.md`
```
