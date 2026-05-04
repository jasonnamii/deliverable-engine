# shaper-skill/references/_common/ — 공통 보일러 정본 모듈

> **다이어트 v2 (260504)**: 60개 스킬에 verbatim 박제된 공통 블록을 1줄 포인터로 치환. 효과 100% 유지·토큰 ~14K 감축.

---

## 모듈

| 모듈 | 정본 위치 | 박힌 스킬 수 | 절감 |
|---|---|---|---|
| §CONFIRM_GATE | `_common/confirm-gate.md` | 18개 | ~22KB |
| §INV NO_WORK_LABEL | `shaper-skill/references/no-work-label.md` (포인터 → `_common/no-work-label-pointer.md`) | 43개 | ~24KB |
| 🚨 MUST cascade → shaper-skill | `_common/cascade-must.md` | 20개 | ~8KB |

## 호출 규칙

각 SKILL.md는 verbatim 블록 대신 **헤더 1줄 + 포인터 1줄**만 둔다:

```markdown
## §CONFIRM_GATE
산출물 송출 직전 형 컨펌 1회. → `shaper-skill/references/_common/confirm-gate.md`

## §INV NO_WORK_LABEL
산출물·대화 작업 라벨 ZERO. → `shaper-skill/references/no-work-label.md`

## 🚨 MUST cascade → shaper-skill
모든 산출물 shaper-skill MUST 경유. → `shaper-skill/references/_common/cascade-must.md`
```

## 본질 보존

- 헤더는 그대로 (트리거·grep 호환)
- 포인터는 절대경로 형식 (cascade·grep 모두 작동)
- 도메인 ALLOW 리스트가 다른 스킬은 본문에 ALLOW만 1줄 보존
