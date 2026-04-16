# CHANGELOG — paper-engine

## v1.0.0 (2026-04-17)

**개명 + 리팩터**. deliverable-engine → paper-engine.

### 변경
- skill-doctor 67.7 → 100점 대응 완료 (🔴 0, 🟠 0)
- 허브 슬림화: 13.7KB → <5KB (references/ 분할 확대)
- P1 일반 키워드 제거: "정리·분석·작성" → P2 동사로 이관 (문서화 의도 아닌 요청 오발동 차단)
- STEALTH 섹션 신설 (내부 라벨 노출 금지)
- Self-Check 섹션 신설 (validate.py + evals/cases.json 3건+)
- 절대 규칙 섹션 신설 (게이트키퍼·PREFLIGHT·재검증 명시)
- version 1.0.0 명시
- evals/cases.json 추가 (회귀 검증 3 케이스)
- scripts/validate.py 추가 (frontmatter·섹션·VOCAB 자동 검사)
- references/cascade-protocol.md 확장 (§1~§11)
- Gotchas 확장: 엣지케이스·장기대화·이름 변경 이력 혼선

### 구간
- v0.x — deliverable-engine 시절 (changelog 미기록 구간)
