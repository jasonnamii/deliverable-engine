# CHANGELOG — paper-engine

## v2.0.0 (2026-04-21)

**NYT 스타일 전면 재설계 (Major)**. 산문체 금지 강제, 역피라미드·압정(pin) 구조·3패스 삭제·4항 밀도QC 5층 구조화.

### 변경
- 형 요청: "NYT처럼 산문체 무조건 탈피"
- §A MODE_ROUTER 신설 (S/M/L 길이 분기)
- §B NYT_STRUCTURE 신설 (Headline·Lead·Nut graf·Body 4층, 압정 비율 1:7:2, 자르기 30% 테스트)
- §C DELETION_FIRST_EDIT 신설 (3패스: 형용사·부사 80%, 연결어, 동의반복)
- §D DENSITY_CHECK 신설 (4항: 주제문·모호동사·중복·구체사실 밀도)
- §E FORMAT 신설 (강제: 불릿·헤더·인용·수치 / 금지: 긴 문장·수동태·모호동사·설명형)
- §F Cascade 3티어 유지 (구 §0), 시각소스 감지 훅 유지
- 기존 §2~§5 (매크로·메조·제목·파일) 구조는 §B~§E에 흡수, 산문체 유도 조항 전부 삭제
- INVARIANT 5→7항 확장 (산문체 FORBIDDEN·역피라미드·3패스·4항 QC 추가)
- "모래시계" → "압정(pin)" 재명명, 별칭 유지
- version 1.1.0 → 2.0.0

### 왜
UP v39.6와 정합. UP §6 OUTPUT_COMPRESSION은 대화 출력 ≤33% 압축. paper-engine은 문서 산출물용으로 별도 구조 필요. 한국 보고서 관성(배경→현황→분석→결론 귀납구조·긴 문장·산문체)이 AI 산출물 품질 주 병목. NYT 100년 편집 경험치(역피라미드·리드·단문·수치)를 DSL화하여 관성 무력화. Strunk & White "Omit needless words" + McKinsey Top-Down + Hemingway 단문 원칙 통합.

### 연동
- UP v39.6 §6: MODE_S(≤500자)는 UP §6 3블록(CONCLUSION·CASE·GROUND) 공유
- design-skill v1.4: HTML 시각소스 감지 훅(§F) 유지, C9 cascade 호환
- 스킬 충돌: UP §5 "§6 > skill_defaults" 규칙상 대화 출력은 UP §6 우선, 문서 산출은 paper-engine §A~§E 우선

---

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
