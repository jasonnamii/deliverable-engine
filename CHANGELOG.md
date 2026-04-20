# CHANGELOG — paper-engine

## v1.1.0 (2026-04-20)

**시각소스 감지 훅 신설**. HTML/웹MD 산출물의 "타이포만 예쁜" 문제 구조적 해결.

### 변경
- description: 시각소스 감지 훅 명시, P4에 HTML 시각요소 요청 조건 추가
- §0 Cascade 3티어: ⓔ 디자인 위임 단계에 "HTML시 시각소스 목록 동반" 추가
- §0 시각소스 감지 훅 섹션 신설 (V1~V10 태깅 → design-skill C9 브릿지)
- references/cascade-protocol.md: §12 "시각소스 감지 훅" 신설 (감지 프로토콜·전달 포맷·과잉방지)
- Gotchas 2항 추가: HTML 표·문장만, 시각소스 감지 누락
- version 1.0.0 → 1.1.0

### 왜
설계자 경험: HTML 산출물이 타이포·여백은 Apple급인데 시각요소가 0개. 수치비교·시간축·프로세스·핵심수치 등 "시각소스"는 있는데 전부 표·문장으로만 처리됨. 원인은 paper-engine이 시각소스를 감지·전달하지 않고, design-skill이 HTML 생성 시 시각 전환을 규범으로 요구하지 않았기 때문. 양쪽 동시 보강.

### 연동
- design-skill v1.4 (C9 시각 전환 CORE 신설, visualization-html.md 스포크)
- 두 스킬은 한 쌍으로 작동: paper-engine이 감지·태깅, design-skill이 전환·렌더

---

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
