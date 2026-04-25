# CHANGELOG — paper-engine

## v2.6.0 (2026-04-26) — HERO 형식 기본 모드 + 어조 룰

### 배경

KISAS 방향전환 정리 작업에서 형의 명시적 룰 도출:
- "각 섹션 첫 줄에 HERO 한 문장. HERO만 쭉 읽어도 방향성을 알 수 있게."
- "선언적 멋짐 금지. 담담하게."
- "HERO 한 줄들이 분석 → 핵심 → 아이템 서사로 흐른다. 본문은 NYT·모래시계 등 내용 구조와 직교."
- "장사 어휘(팔다·전환·만석) 금지. 인물 호칭(피디님·박사) 금지. 버전 라벨(v3.2·SoT) 금지. 작업 약자(LTV·NPS) 풀어쓰기."

### 변경

- **INV 14 신설** — HERO 형식. 모든 본문 섹션 첫 줄 = 압축 한 문장. HERO만 차례로 읽으면 분석→핵심→아이템 서사. 한 섹션이라도 누락 = FAIL. 담담 톤.
- **INV 15 신설** — 어조 룰. 인물 호칭·버전 라벨·장사 어휘·작업 라벨·작업 약자 금지. 업계 표준 약자(BEP·KPI·MECE·MVP)는 한 번 정의 후 통과.
- **§B-1 갱신** — Body 정의에 HERO 한 줄 의무 추가.
- **§B-4 신설** — HERO 서사 흐름 (분석→핵심→아이템). 마지막 묶음 분석 면제.
- **§E-1·E-2 갱신** — 강제·금지 항목에 HERO·어조 룰 추가.
- **§G 파이프라인 ⑩-b 확장** — 작업라벨(INV 13) + HERO 서사(INV 14) + 어조(INV 15) 3중 자체 스캔.
- **§I 자체 스캔** — 3 INV 통합 검사 표.
- **references/hero-format.md 신설** — 본질 4줄·HERO 룰·서사 흐름·담담 톤·어조 사전·결합 예·Gotchas.
- **description 압축** — 853자 → 500자 미만. P3에 영문 키워드 추가(NYT inverted pyramid·CEW·document type router·hero format).
- **Gotchas 확장** — HERO 누락·카피 톤·서사 깨짐·인물 호칭·장사 어휘·약자 풀어쓰기 누락 6항.

### 직교 원리

HERO는 형식 층, DOC_TYPE은 내용 층. 전달형·진단형·평가형·수렴형 어느 것이든 HERO를 입을 수 있다. NYT 압정 본문 + HERO, 5Whys 진단 본문 + HERO, 다소스 매트릭스 본문 + HERO 모두 가능.

### 호환성

기존 v2.5의 INV 1~13 모두 유지. v2.5 산출물은 v2.6에서 INV 14·15 추가 검사 시 HERO 누락·어조 위반으로 FAIL 가능 → 재작성 필요.

---

## v2.5.0 (2026-04-25) — NO_WORK_LABEL 본질보호 게이트

형 진단(양평 v3 사례 `00_기획종합분석_v3.md`): **"산출물에 축·레이어·트랙 같은 작업 라벨 단어가 한 글자라도 나오면 페일이다. 1만 페이지에 1단어라도 = FAIL."**

내가 처음 잡은 방향(BANNED_VOCAB 사전 30+개)은 형이 직접 정정 — 사전식은 누락이 곧 구멍, 본질은 판정질문 1개. 본 버전은 NO_WORK_LABEL 5줄 본질을 채택하고 사전·패턴은 보조 위치로 격하.

### INV 13 — NO_WORK_LABEL 5줄 (단일 권위)

| | |
|---|---|
| RULE | 산출물·대화 = 인간 언어. 작업 라벨 ZERO. (1만 페이지 1단어 = FAIL) |
| 판정 | "이 단어, 이 대화 밖 사람이 사전 없이 읽을 수 있나?" — NO → 라벨 → 금지 |
| ALLOW | 업계 전문용어 (BEP·KPI·MECE·MVP 등) · 고유명사 · 법조문 |
| CONVERT | 라벨 → 실명·평문 풀어쓰기 (Y2 → "2년차" / 4축 → 실제 4개 이름 / C:E:W → 평문) |
| SELF_CHECK | 산출 직전 자체 스캔. 1개라도 = 차단·전수재작성. 부분치환 ✗ |

### 신규 파일

- `references/no-work-label.md` (단일 권위) — 5줄 본질 + ALLOW 화이트리스트 + CONVERT 치환표 + 양평 v3 ANTI-PATTERN

### 수정 파일

- `SKILL.md` — 절대규칙 12→13개, INV 13 신설, §I 스캔 섹션 추가, §G 파이프라인 ⑩-b 추가, Gotchas 4행 추가
- `scripts/validate.py` — `--check-output FILE` 모드 신설, 사전·패턴 보조 게이트, ALLOW 화이트리스트 반영, 자기참조 면제
- `evals/cases.json` — C9·C10·C11 신규 3건 (구조라벨 위반·메타라벨 위반·ALLOW 통과)

### 양평 v3 사례 검증 결과

`scripts/validate.py --check-output sample.md` → **10개 라인 적발 FAIL**:
- DNA 4축 / 마지막 레이어 / 3트랙 진입점·관계 설계 / Pin↔Body 매핑 / 압정 / CONVERGE MODE_L / v3.1 페이퍼엔진 통과 / DEEP 4항 QC

처리: **부분치환 ✗ → 전수 재작성**. 라벨을 라벨로 바꾸지 말고 실명·평문으로(`4축` → `정원·물·문학·휴식 네 가지`, `3트랙` → `살롱·교육·메가 세 사업`, `흑자축` → `흑자 사업`, 메타블록 자체 삭제).

### 우선순위

INV 13은 다른 모든 규칙(Pin↔Body 표 의무·CEW 한 줄 등)보다 **상위**. 다른 규칙이 라벨을 요구하면 그 다른 규칙을 자연어로 풀어쓴다.

---

## v2.3.0 (2026-04-25)

**DOC_TYPE 분기 + Claim-Evidence-Warrant + 반대주장 박스 + Pin↔Body + 의사결정 매핑 + 수치맥락**

형 진단: "압정만 적층되고 본문 휘발·등급만 박혀있음·논증 부재". 양평 _research/ 16편(특히 종합·수렴) 안티패턴 직격.

### 시스템 의무 4 (다소스·압축 단절 차단)
- **INV 9 DOC_TYPE 분기:** 길이만이 아닌 종류 분기. DELIVER(1:7:2)·DIAGNOSE(1:6:3)·EVALUATE(1:5:4)·CONVERGE(1:4:5) 압정비율 차등. EVALUATE/DIAGNOSE = MODE_S 금지·CONVERGE = MODE_L 강제. (`references/doc-types.md` 신규)
- **INV 10 EVIDENCE_INJECTION (§D-5):** 평가표 등급(강·중·약·★·점수) 옆 근거 1줄 컬럼 의무. 미명시 = FAIL. 양평 §2 비교표 안티패턴 차단.
- **NUMBER_PROVENANCE (§D-6, §D-1):** 모든 수치 옆 (출처·가정·기준·비교) 의무. `3,200명` → `3,200명 (KOSIS 2024-12, 전년比 +45%, 군평균 800명)`. `+42억` → `+42억 (가정: 단가·캐파·점유율, 시나리오)`.
- **MULTI_SOURCE_PROTOCOL (§F-2):** 3편+ 통합 시 다소스 교차비교 매트릭스 의무 (편·결론·합의·모순·빈자리). 단순 인덱스화 = FAIL. 양평 종합 §G 15편 인덱스 안티패턴 차단.

### 본질 의무 5 (진짜 페이퍼 본질)
- **INV 10 Claim-Evidence-Warrant (§E-3):** 모든 주장 = C(주장)+E(증거 1+)+W(왜 E가 C 지지) 단위. Toulmin 모델 압축형. 셋 중 하나라도 ✗ = FAIL. 양평 종합 "강·중·약·즉사" 등급만 = E·W 부재 = 이 룰 위반. 불릿 압축 OK: `[C]: [E] → [W]`.
- **INV 11 Pin↔Body 매핑 (§B-3):** 압정(상단 결론) 주장 N개 ↔ Body 섹션 N개 1:1 매핑 의무. 매핑표(압정 주장·Body §X·증거 위치) 작성. 압정에만 있고 Body에 ✗ = FAIL. 양평 종합 §A "특이사항 7개" 떠있음 차단.
- **INV 12 반대주장 박스 (§E-4):** MODE_M·L에서 Body 섹션당 반대주장 박스 1+ 의무. 형식: 반대주장·반박 근거(E')·현 결론 우위 사유(W'). 단언만 = 선전문 = NYT 위반.
- **수치 맥락 (§D-1):** 수치 = 값 + 기준점 + 비교/증감 + (출처/가정). 단독 수치 금지.
- **의사결정 1줄 (§B-1):** Headline 직후 "이 문서가 바꾸는 의사결정 1줄" 의무. research-frame §1-1과 동일 사상. 미작성 = FAIL.

### 신규 파일
- `references/doc-types.md` (130줄) — 4종 정의·트리거·골격·매트릭스·평가표 템플릿

### 수정 파일
- `SKILL.md` — 절대규칙 7→12개 확장, §A ROUTER에 DOC_TYPE 추가, §B에 의사결정1줄+Pin↔Body, §D 4항→6항 QC, §E에 CEW+반대주장박스, §F에 MULTI_SOURCE
- `references/cascade-protocol.md` §3 — 참조형 폴백을 DOC_TYPE 분기로 통합
- `evals/cases.json` — C4~C8 신규 5건 (DOC_TYPE·CEW·Pin↔Body·반대주장 검증)

### 영향
- **양평 종합·수렴 같은 산출물 차단:** 등급만 적층·압정만·논증 부재·다소스 인덱스화 모두 v2.3에서 FAIL
- **출력 의무 ↑:** EVALUATE/CONVERGE 산출물 토큰 +30~40% 예상 (CEW·Pin↔Body·반대주장·교차비교)
- **DELIVER는 v2.0 호환:** 압정 1:7:2·전달형 산출은 영향 없음

### 호환
- v2.0~v2.2 DELIVER 산출은 종류 미명시 시 디폴트로 호환
- 명시적 트리거("비교·종합·통합·진단") 시 v2.3 신규 의무 발동
- biz·hit·human·ads·person·ruby·management·sales·brand·copy·nego·contract·startup·holdings·risk·benchmark·app-and-jang·data·policy·consulting 21 spoke spoke 자동 cascade 시 DOC_TYPE 자동 판정

---

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
