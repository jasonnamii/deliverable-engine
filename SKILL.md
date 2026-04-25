---
name: paper-engine
version: 2.5.0
description: |
  paper-engine(페이퍼엔진) — NYT스타일 산출물 허브. 역피라미드·압정·3패스·4항QC. v2.5: NO_WORK_LABEL 본질보호 게이트(산출물·대화 = 인간 언어, 작업 라벨 ZERO, 1만 페이지 1단어=FAIL, 판정질문 "사전 없이 읽히나?"). v2.3: DOC_TYPE 4분기(전달/진단/평가/수렴) + Claim-Evidence-Warrant + 반대주장 박스 + 수치맥락 + Pin↔Body 매핑 + 의사결정 매핑.
  P1: 산출물, 페이퍼엔진, 보고서, 기획안, 제안서, 진단서, 전략서, 리포트, 컨설팅보고서, 처방서, 평가보고서, 수렴리포트, 종합분석, 비교분석, 문서, 문서작성, 글쓰기, 작성, 글, 정리, 요약서, 요약문, 결과물, 아웃풋, 1pager, 문서화, 플레이북, 스크립트, 진단리포트, 처방전, 설계안, 분석결과, 협상전략서, 협상분석, 캠페인브리프, 미디어플랜, 복기리포트, 리뷰메모, 레드라인, 설득안, 검증보고서, 분석메모, RCA보고서, 리스크보고서, 대시보드, 리뷰보고서, 아젠다, 회의록, 액션아이템, 진단결과, 상담노트, 평가서, 비교표, PRD, 계획서, 내용정리, 글작성.
  P2: 써줘, 써, 적어줘, 편집해줘, 드래프트해줘, 뽑아줘, 통합해줘, 비교해줘, 평가해줘, 작성해줘, 만들어줘, 정리해줘, 생성해줘, 문서화해줘, 글써줘, write, draft, evaluate, converge, create, generate, produce.
  P5: md파일로, html파일로, 보고서로, 진단서로, 리포트로, 평가서로.
  NOT: 세션브리핑(→session-briefing), 사업계획서(→bp-guide), 제출청소(→trigger-dictionary).
vault_dependency: SOFT
---

# Paper Engine — NYT 스타일 산출물 허브

산출물 품질 중앙 허브. 산문체 금지, NYT(역피라미드·압정) 강제. 불릿·헤더·수치·인용·단문 필수.
**v2.5:** **NO_WORK_LABEL 본질보호 게이트** — 산출물·대화 = 인간 언어. 작업 라벨 ZERO. 1만 페이지 1단어 = FAIL.
**v2.3:** DOC_TYPE 분기·CEW·반대주장·Pin↔Body 의무 추가.

---

## ⛔ 절대 규칙 (13)

| # | 규칙 | 위반 |
|---|------|------|
| 1 | **게이트키퍼** md/html cascade 자동 | 품질 붕괴 |
| 2 | **산문체 FORBIDDEN** 긴문장·연결어 ✗·불릿·단문·수치 필수 | NYT 위반 |
| 3 | **역피라미드** 결론 1st·뒤 30% 삭제 생존 | 귀납 = FAIL |
| 4 | **3패스 삭제** 형부·연결어·중복 | 지방 잔존 |
| 5 | **4항 밀도QC** 주제문·모호동사·중복·구체사실≥1 | 밀도 미달 |
| 6 | **STEALTH** 내부 라벨 본문 노출 ✗ | 사용자 혼란 |
| 7 | **MUST cascade → design-skill** | 포맷 혼재 |
| 8 | **DEFAULT_RENDER 순수MD** `.md`에 div·style ✗ (예외: 명시) | 렌더 깨짐 |
| 9 | **DOC_TYPE 분기 (v2.3)** 4종(DELIVER/DIAGNOSE/EVALUATE/CONVERGE)·압정비율 차등 | 사고형 본문 압살 |
| 10 | **Claim-Evidence-Warrant (v2.3)** 모든 주장=C+E+W. 1개라도 ✗=FAIL | 등급만 적층 |
| 11 | **Pin↔Body 매핑 (v2.3)** 압정 N개 ↔ Body N개 1:1. 압정만=FAIL | 떠있는 결론 |
| 12 | **반대주장 박스 (v2.3)** MODE_M·L Body당 1+ 의무 | 선전문화 |
| 13 | **NO_WORK_LABEL (v2.5)** 산출물·대화 = 인간 언어. 작업 라벨 ZERO. (1만 페이지 1단어 = FAIL) 적발 → 전수 재작성. 부분치환 ✗ | 사용자 혼란·내부어 누출 |

> **INV 13 — NO_WORK_LABEL 5줄 (본질)**
>
> - **RULE**: 산출물·대화 = 인간 언어. 작업 라벨 ZERO. (1만 페이지 1단어 = FAIL)
> - **판정**: "이 단어, 이 대화 밖 사람이 사전 없이 읽을 수 있나?" NO → 작업 라벨 → 금지
> - **ALLOW**: 업계 전문용어 (BEP·KPI·MECE·MVP 등) · 고유명사 · 법조문
> - **CONVERT**: 라벨 발견 → 실명·평문 풀어쓰기 (예: Y2 → "2년차" / 4축 → 실제 4개 이름 / C:E:W: → 평문)
> - **SELF_CHECK**: 산출 직전 자체 스캔. 1개라도 발견 = 차단·재작성
>
> 사전·예시·자주새는 단어·변환사례 = `references/no-work-label.md` (보조)

---

## §A. ROUTER (길이 + DOC_TYPE)

### A-1. 길이

| 길이 | 모드 | 구조 |
|---|---|---|
| ≤500자 | **MODE_S** | UP §6 3블록 직행 |
| 500~2000자 | **MODE_M** | NYT 리드 + 압정 |
| >2000자 | **MODE_L** | NYT 풀 |

### A-2. DOC_TYPE (v2.3 신규) → `references/doc-types.md` 필독

| 종류 | 트리거 | 압정 | 핵심 의무 |
|------|--------|------|----------|
| **DELIVER** | "보고·요약·1pager" (디폴트) | 1:7:2 | NYT 표준 |
| **DIAGNOSE** | "진단·원인·처방" | 1:6:3 | 5Whys·처방·리스크 본문 |
| **EVALUATE** | "비교·우열·등급" | 1:5:4 | **등급 옆 근거 1줄 의무** |
| **CONVERGE** | "통합·종합·수렴" | 1:4:5 | **다소스 교차비교 매트릭스 의무** |

복합 우선: CONVERGE > EVALUATE > DIAGNOSE > DELIVER. EVALUATE/DIAGNOSE는 MODE_S 금지·CONVERGE는 MODE_L 강제.

### A-3. RENDER

| 확장자 | 명시 | design-skill |
|---|---|---|
| `.md` | (없음) | MUST 순수MD |
| `.md` | "HTML로·박스·벤토" | MUST html-div-style |
| `.html` | (전부) | MUST C9 |

---

## §B. NYT 구조

### B-1. 4층 + 의사결정 1줄

- **Headline** = 결론 주장 1줄
- **의사결정 1줄 (v2.3 신규)** Headline 직후 "이 문서가 바꾸는 의사결정 1줄" 의무. 미작성=FAIL
- **Lead** 5W1H 또는 결론+근거+사례 (≤5문장)
- **Nut graf** "왜 중요한가" (MODE_L)
- **Body** 소제목·중요도 내림차순

### B-2. 압정 비율 (DOC_TYPE 차등)

DELIVER 1:7:2 / DIAGNOSE 1:6:3 / EVALUATE 1:5:4 / CONVERGE 1:4:5

### B-3. Pin↔Body 매핑 (v2.3, INV 11)

압정 주장 N개 → Body 섹션 N개 1:1. 매핑표 형식:

| 압정 주장 | Body §X | 증거 위치 |

압정에만 있고 Body에 증거 ✗ = FAIL.

### B-4. 자르기

뒤 30% 삭제 → 결론·근거 생존? YES=PASS

---

## §C. 3패스 삭제

| 패스 | 대상 | 효과 |
|---|---|---|
| 1 | 형용사·부사 80% | -20% |
| 2 | 연결어구 전부 | -10% |
| 3 | 동의반복 | -10% |

목표 33~50% 감축.

---

## §D. 6항 QC (v2.3 +2항)

| # | 체크 | FAIL |
|---|------|------|
| 1 | 주제문 우선 | 첫 문장 ≠ 주제문 |
| 2 | 모호동사 빈도 | "있다·것이다" >1/문단 |
| 3 | 중복 금지 | 같은 정보 2회+ |
| 4 | 구체사실 밀도 | 인용·수치·고유명사 <1/문단 |
| 5 | **EVIDENCE_INJECTION (v2.3)** | 등급(강·중·약·★) 옆 근거 1줄 ✗ |
| 6 | **NUMBER_PROVENANCE (v2.3)** | 수치 옆 (출처·가정·기준·비교) ✗ |

1항 FAIL → §C 재실행. 루프 2회.

### D-1. NUMBER_PROVENANCE 형식

| 잘못 | 옳음 |
|------|------|
| `3,200명` | `3,200명 (KOSIS 2024-12, 전년比 +45%, 군평균 800명)` |
| `+42억` | `+42억 (가정: 단가 12만·캐파 5K·점유율 30%, 기준시나리오)` |

수치 = 값 + 기준점 + 비교/증감 + (출처/가정).

---

## §E. FORMAT + CEW + 반대주장

### E-1. 강제: 불릿·번호·헤더·인용박스·표·수치(D-1)
### E-2. 금지: 긴문장(25단어+)·수동태·모호동사·연결어 남발·설명형 서술

### E-3. Claim-Evidence-Warrant (v2.3, INV 10)

| 부 | 정의 | 예 |
|----|------|-----|
| **C 주장** | 결론·평가·등급 | "양평DNA 활용도 = 강" |
| **E 증거** | 1차 출처·수치·고유명사 | "두물머리·세미원·황순원 + KOSIS 2024 정원인구 13.5만" |
| **W 정당화** | E가 C 지지 사유 | "3대축이 단일 정체성 → Glyndebourne·Wonderfruit 정합" |

C+E+W 셋 다 ✗ = FAIL. **불릿 압축형 OK:** `[C]: [E] → [W]` 한 줄.

### E-4. 반대주장 박스 (v2.3, INV 12)

MODE_M·L Body당 1+ 의무:
```
> **반대주장:** [C에 대한 반론]
> **반박 근거:** [E']
> **현 결론 우위 사유:** [왜 C 우위인가]
```
미작성=FAIL.

---

## §F. Cascade 3티어 + 다소스 프로토콜

### F-1. 3티어

| | ≤20행 | 21~50 | 51+ |
|---|:-:|:-:|:-:|
| 외부 | 경량 | 풀 | 풀 |
| 내부 | 패스스루 | 경량 | 풀 |

### F-2. MULTI_SOURCE (v2.3, CONVERGE 의무)

3편+ 통합 시 교차비교 매트릭스 의무:

| 편 | 핵심 결론 | 합의 | 모순 | 빈자리 |

단순 인덱스화(편→결론 1줄 나열) = FAIL.

### F-3. 시각 V1~V10 → design-skill C9 (HTML)

상세: `references/cascade-protocol.md`

---

## §G. 파이프라인

```
① PREFLIGHT(수신자·목적·DOC_TYPE) → ② §A 길이+DOC_TYPE → ②-b §A-3 RENDER
→ ③ §B 작성(Headline+의사결정1줄+Lead+Body+Pin↔Body)
→ ④ §C 3패스 → ⑤ §D 6항 QC(v2.3 EVIDENCE+NUMBER 포함)
→ ⑥ §E FORMAT+CEW+반대주장 → ⑦ design-skill cascade MUST
→ ⑧ [HTML] qc-mobile.sh → ⑨ [MD] div 위반 검사
→ ⑩ Pin↔Body 매핑 검증(INV 11)
→ ⑩-b §I NO_WORK_LABEL 자체 스캔 (INV 13) — LLM 판정질문 + 사전 보조. 적발 1+ → 전수재작성 → ⑩-b 재실행. 2회차 적발 → STOP+보고
→ ⑪ 산출
```

---

## §I. NO_WORK_LABEL 스캔 (INV 13)

본질 5줄 = INV 13 행 직접 참조. 본문 중복 ✗.

1차 = LLM 자체 판정질문. 2차 = `python scripts/validate.py --check-output FILE` (보조). 적발 1+ → 전수재작성 → 재스캔. 2회차 적발 → STOP. 부분치환 ✗. 상세·치환표·예시: `references/no-work-label.md`.

---

## §H. Self-Check

`python scripts/validate.py .` errors=[], 루프 2회. `evals/cases.json` 3+. 스캐너는 자기참조 라인(INV 13·v2.5·no-work-label.md 마커) 제외.

---

## Gotchas

| 함정 | 대응 |
|---|---|
| 산문체 관성 | §E 강제 |
| 결론 끝에 | §B 역피라미드 |
| 형부 남발 | §C pass1 80% |
| 수치 0개 | §D-4 FAIL |
| **DOC_TYPE 무시·DELIVER 강제** | §A-2 차등 |
| **C·E·W 중 누락** | INV 10·등급만=FAIL |
| **압정 주장 Body 부재** | INV 11·매핑표 |
| **반대주장 박스 0** | INV 12·MODE_M·L Body당 1+ |
| **수치 단독** | D-1 (출처·가정) 의무 |
| **다소스 인덱스화** | F-2 매트릭스 의무 |
| **의사결정 1줄 누락** | B-1 의무 |
| HTML 시각 누락 | §F-3 V1~V10 |
| HTML 모바일 QC | §G-⑧ |
| `.md` div | INV 8 |
| design-skill 미호출 | INV 7 |
| spoke cascade | research-frame 등 §4.5 강제 |
| **작업 라벨 산출물 누출 (대화 밖 사람이 사전 없이 못 읽는 단어)** | **INV 13 NO_WORK_LABEL → 실명·평문 풀어쓰기로 전수재작성** |
| **부분치환으로 라벨만 바꾸기** | **사고 자체가 라벨식. 전수재작성만 통과** |
| **메타라벨 누출 (예: "v3.1 페이퍼엔진 통과 · 압정 1:4:5")** | **메타블록 자체 삭제. 사용자에게 의미 없음** |
| **MECE·KPI·BEP·MVP를 라벨로 오판해 차단** | **§I ALLOW 화이트리스트 — 업계 전문용어는 통과** |

---

## 예시 (라벨 단어 0개 강제)

요청: `"리서치 15편 종합해줘. 보고서로"`

내부 라우팅(사용자 비공개): 길이 = 길음 → 종류 = 수렴형 · 결론 비율 낮음 · 본문 비중 높음 · 비교표 의무 · 결론↔본문 대응표 · 자기반박 박스 · 산출 직전 작업 라벨 스캔.

산출물에 등장 가능한 단어: "한 줄 결론", "도입", "본문", "리서치 비교표", "합의·모순·빈자리", "반대 주장", "결론과 근거 연결", "마무리".

산출물에 0개 강제: 종류 코드(전달형/수렴형 등 영문·한글 라벨 단어), 모드 코드, 결론 비율 표기, 사고도구 약어 — 모두 ✗.

상세: `references/no-work-label.md` · `references/doc-types.md` · `references/cascade-protocol.md` · `CHANGELOG.md`
