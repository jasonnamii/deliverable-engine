---
name: paper-engine
version: 3.1.0
description: |
  paper-engine — NYT 산출물 허브. v3.1: PRE_WRITE_GUARD — 사전생성형 전환. §B 작성 단계 자체에 5종 룰 강제(단문 8~20자·시그니처 자연주입·BAN 사전회피·문장당 1명제·문단 ≤80자). 사후교정형 → 사전생성형. v3.0: HUMANIZE_GATE 3중(BAN_LEXICON·STYLE_NORTH_STAR·ANTI_BLOAT). 형 코퍼스 1MB 실측 기반. v2.6: HERO 형식·어조 룰. v2.5: 작업라벨 본질보호. v2.3: DOC_TYPE 4분기·CEW·반대주장.
  P1: 산출물, 페이퍼엔진, 보고서, 기획안, 제안서, 진단서, 전략서, 리포트, 비교분석, 글쓰기, 1pager, 플레이북, PRD, HERO, 히어로, 휴머나이즈, AI문서티, 번역투, 장황, 압축, 사전가드, 작성가드.
  P2: 써줘, 적어줘, 작성해줘, 만들어줘, 정리해줘, write, draft, create.
  P3: NYT inverted pyramid, claim-evidence-warrant, document type router, hero format, humanize gate, anti-bloat, ban lexicon, pre-write guard.
  P5: md파일로, html파일로, 보고서로.
  NOT: 세션브리핑(→session-briefing), 사업계획서(→bp-guide), 제출청소(→trigger-dictionary).
vault_dependency: SOFT
---

# Paper Engine — NYT 스타일 산출물 허브

산출물 품질 중앙 허브. 산문체 금지, NYT(역피라미드·압정) 강제. 불릿·헤더·수치·인용·단문 필수.
**v3.1:** **PRE_WRITE_GUARD** — 사전생성형 전환. 정보·데이터를 받아 *처음부터* 룰 박힌 상태로 작성. 사후교정 ✗.
**v3.0:** **HUMANIZE_GATE** — AI 문서티 측정 가능한 0에 수렴. 형 코퍼스 23개 PDF·1MB·19,874줄 실측 데이터 기반.
**v2.6:** **HERO 형식 기본** + 어조 룰. **v2.5:** **작업라벨 본질보호**. **v2.3:** DOC_TYPE 분기·CEW·반대주장.

---

## ⛔ 절대 규칙 (20)

| # | 규칙 | 위반 |
|---|------|------|
| 1 | **게이트키퍼** md/html cascade 자동 | 품질 붕괴 |
| 2 | **산문체 FORBIDDEN** 긴문장·연결어 금지·불릿·단문·수치 필수 | NYT 위반 |
| 3 | **역피라미드** 결론 1st·뒤 30% 삭제 생존 | 귀납=FAIL |
| 4 | **9패스 압축 (v3.0)** §C-NEW 9패스·50%+ 감축 | 70% 쓰레기 잔존 |
| 5 | **6항 밀도QC** 주제문·모호동사·중복·구체사실·EVIDENCE·NUMBER | 밀도 미달 |
| 6 | **STEALTH** 내부 라벨 본문 노출 금지 | 사용자 혼란 |
| 7 | **MUST cascade → design-skill** | 포맷 혼재 |
| 8 | **DEFAULT_RENDER 순수MD** `.md`에 div·style 금지 | 렌더 깨짐 |
| 9 | **DOC_TYPE 분기 (v2.3)** DELIVER/DIAGNOSE/EVALUATE/CONVERGE·압정비율 차등 | 사고형 압살 |
| 10 | **CEW (v2.3)** 모든 주장=C+E+W. 1개 누락=FAIL | 등급만 적층 |
| 11 | **Pin↔Body 매핑 (v2.3)** 압정 N↔Body N 1:1 | 떠있는 결론 |
| 12 | **반대주장 박스 (v2.3)** MODE_M·L Body당 1+ | 선전문화 |
| 13 | **작업라벨 본질보호 (v2.5)** 산출물=인간언어·작업라벨 ZERO | 사용자 혼란 |
| 14 | **HERO 형식 (v2.6)** 본문 섹션 첫 줄=압축 한 문장 | 방향성 ✗ |
| 15 | **어조 룰 (v2.6)** 인물호칭·버전라벨·장사어휘·작업라벨 금지 | 내부어 누출 |
| 16 | **BAN_LEXICON (v3.0)** AI 5대 흔적·형식부사·접속비대·번역투·형식명사 60+ grep. 적발→평문변환 | AI 흔적 누출 |
| 17 | **STYLE_NORTH_STAR (v3.0)** 한국 명문+형 시그니처 10조. 단문 8~20자·구체명사 70%+·능동형. 위반 3+→재작성 | 문체 사망 |
| 18 | **ANTI_BLOAT (v3.0)** §C-NEW 9패스. 50%+ 감축. 산출 직전 70% 절단 | 70% 쓰레기 잔존 |
| 19 | **PRE_WRITE_GUARD (v3.1)** §B 진입 전 5종 강제. 사전생성형. §C는 안전망 | 사후교정 의존·1번 메커니즘 |
| 20 | **CONFIRM_GATE (v3.2)** 산출물 송출 직전 형 컨펌 1회. 자가신고 우회 차단. 면제: ≤5줄·단답·진단본문 | AI 티 사후 발견·재작업 |

> **INV 13·14·15 본질 (v2.5·v2.6)**
> 13 작업라벨 ZERO·"사전 없이 읽히나?" → `references/no-work-label.md` · 14 HERO 섹션 첫줄=압축 한문장·담담 → `references/hero-format.md` · 15 어조 금지(인물호칭·버전라벨·LTV·팔다)·허용(BEP/KPI/MECE/MVP) → `references/hero-format.md §6`

> **INV 16·17·18 — HUMANIZE_GATE (v3.0 본질)**
> 본질·사전·10조·9패스 = `references/humanize-gate.md` + `references/banwords-lexicon.md` + `scripts/humanize_check.py`. 산출 직전 3중 스캔 강제, 적발 1+ → 평문변환·재출력 (루프 max 2회).

> **INV 19 — PRE_WRITE_GUARD (v3.1 본질)**
> §B 진입 전 5종 룰 강제 — ① 단문 8~20자 ② 시그니처 자연주입 ③ BAN 사전회피 ④ 1문장 1명제 ⑤ 문단 ≤80자. 메커니즘: 사후교정 ✗·사전생성 ○. 자가검사: "형 코퍼스 1MB 등장 만한가?" NO → 재생성. 상세 = `references/pre-write-guard.md`

---

## §A. ROUTER (길이 + DOC_TYPE)

### A-1. 길이

| 길이 | 모드 | 구조 |
|---|---|---|
| ≤500자 | **MODE_S** | UP §6 3블록 직행 |
| 500~2000자 | **MODE_M** | NYT 리드 + 압정 |
| >2000자 | **MODE_L** | NYT 풀 |

### A-2. DOC_TYPE → `references/doc-types.md`

| 종류 | 트리거 | 압정 | 핵심 의무 |
|------|--------|------|----------|
| **DELIVER** | "보고·요약·1pager" (디폴트) | 1:7:2 | NYT 표준 |
| **DIAGNOSE** | "진단·원인·처방" | 1:6:3 | 5Whys·처방·리스크 |
| **EVALUATE** | "비교·우열·등급" | 1:5:4 | 등급 옆 근거 1줄 의무 |
| **CONVERGE** | "통합·종합·수렴" | 1:4:5 | 다소스 교차비교 매트릭스 의무 |

복합 우선: CONVERGE > EVALUATE > DIAGNOSE > DELIVER. EVALUATE/DIAGNOSE는 MODE_S 금지·CONVERGE는 MODE_L 강제.

### A-3. RENDER

| 확장자 | 명시 | design-skill |
|---|---|---|
| `.md` | (없음) | MUST 순수MD |
| `.md` | "HTML로·박스·벤토" | MUST html-div-style |
| `.html` | (전부) | MUST C9 |

---

## §B. NYT 구조

### §B-PRE. 사전 작성 가드 (v3.1, INV 19)

5종 룰 + 메타 1: ① 단문 8~20자 ② 시그니처 자연주입 ③ BAN 사전회피 ④ 1문장 1명제 ⑤ 문단 ≤80자 ⑥ "형 코퍼스 1MB 등장 만한가?". 본질·예시·검사절차 = `references/pre-write-guard.md`
**📚 형 코퍼스 실측 예시·BAN/GOOD 사전:**
- `→ references/jason-corpus-examples.md` (형 코퍼스 1.05MB · PT 17개·IR 2개·BP 추출 verbatim 헤드·구문)
- `→ VAULT/Agent-Ops/_refs/jason_lexicon_BAN.md` (AI식 28개 어휘·형 코퍼스 0회 등장 = 확정 BAN)
- `→ VAULT/Agent-Ops/_refs/jason_lexicon_GOOD.md` (형 시그니처 50+ 어휘·구문 패턴)


### §B-구조

- **Headline** = 결론 주장 1줄. 형식: "X는 Y다·X가 Y한다·X는 Y가 아니라 Z다". 설명형("X에 대한 분석") 금지
- **의사결정 1줄** Headline 직후 "이 문서가 바꾸는 의사결정"
- **Lead** 5W1H 또는 결론+근거+사례 (≤5문장). 1문장당 1수치·1고유명사 의무
- **Nut graf** "왜 중요한가" (MODE_L)
- **Body** 소제목 + **HERO 한 줄 (INV 14)** + 본문. 단락 ≤80자. 중요도 내림차순
- **Pin↔Body 매핑** (INV 11) 1:1. 매핑표: `| 압정 주장 | Body §X | 증거 위치 |`
- **HERO 서사** 분석→핵심→아이템. 마지막 묶음(합성·결론) 분석 면제

### §B-CONFIRM. 송출 직전 형 컨펌 게이트 (3단계, INV 20)

**목적:** 자가신고 우회 차단. PRE_WRITE 자체검증 통과 = 송출 ✗ → 형 컨펌 후 송출.

**발동:** §D 6항 QC 통과 후, *최종 송출 직전* 1회.

**형식 (verbatim):**
```
🔍 송출 전 검토 부탁드려요. AI 티·번역투·장황 있나요?
[OK / 수정 / 재작성]
```

**규칙:**
- 형 OK → 최종 송출
- 형 수정 → 형 지적 부분만 §B-PRE 재진입 → 재출력
- 형 재작성 → §B 전체 재진입

**SCOPE_OUT (컨펌 면제):**
- ≤5줄 답변
- 단답·확인성·실행보고
- 진단 본문 (산출물 ✗·대화 내 분석)
- 일반대화·핑퐁·컨펌게이트 자체

**CHECK:** 산출물 송출인데 §B-CONFIRM 미발동 = FAIL → 송출 폐기·재출력.
- **자르기** 뒤 30% 삭제 → 결론·근거 생존? YES=PASS

---

## §C-NEW. 9패스 압축 (v3.0, INV 18 ANTI_BLOAT)

본질·상세 = `references/humanize-gate.md §5`. ① 질문재술 ② 서문·종결 ③ 헤징→1개 ④ 동의어→1개 ⑤ 예시 1개 ⑥ 3항강박 ⑦ "수있다"우회 ⑧ 수식어 누적 ⑨ **산출직전 70% 절단**. 목표 50%+ 감축. 루프 max 2회.

---

## §D. 6항 QC

| # | 체크 | FAIL |
|---|------|------|
| 1 | 주제문 우선 | 첫 문장 ≠ 주제문 |
| 2 | 모호동사 빈도 | "있다·것이다" >1/문단 |
| 3 | 중복 금지 | 같은 정보 2회+ |
| 4 | 구체사실 밀도 | 인용·수치·고유명사 <1/문단 |
| 5 | EVIDENCE_INJECTION | 등급(강·중·약·★) 옆 근거 1줄 누락 |
| 6 | NUMBER_PROVENANCE | 수치 옆 (출처·가정·기준·비교) 누락 |

D-1 NUMBER 형식: `3,200명 (KOSIS 2024-12, 전년比 +45%)`

---

## §E. FORMAT + CEW + 반대주장

E-1 강제: 불릿·번호·헤더·인용박스·표·수치 + HERO 한 줄
E-2 금지: 긴문장(25단어+)·수동태·모호동사·연결어 남발 + 인물호칭·버전라벨·장사어휘(INV 15)

E-3 CEW: `[C]: [E] → [W]` 한 줄. C+E+W 셋 다 누락 = FAIL

E-4 반대주장 박스 (MODE_M·L Body당 1+):
```
> 반대주장: [반론] · 반박 근거: [E'] · 현 결론 우위: [사유]
```

---

## §F. Cascade + 다소스

F-1 3티어 (≤20행 경량 / 21~50 풀 / 51+ 풀)
F-2 MULTI_SOURCE (CONVERGE 의무) 교차비교 매트릭스: `| 편 | 결론 | 합의 | 모순 | 빈자리 |`
F-3 시각 V1~V10 → design-skill C9. 상세 = `references/cascade-protocol.md`

---

## §G. 파이프라인

```
① PREFLIGHT → ② §A 라우터+RENDER
→ ③ §B-PRE 활성화 (v3.1, INV 19) → §B 작성 [5종 룰 강제] (Headline·의사결정·Lead·Body[HERO]·Pin↔Body)
   토큰 직전 자기검열: "형 코퍼스 1MB 등장 만한가?" NO → 재생성
→ ④ §C 9패스 ANTI_BLOAT (안전망. ③ 충실 시 ≤2패스) → ⑤ §D 6항 QC → ⑥ §E FORMAT+CEW+반대주장
→ ⑦ §H 7중 자체스캔 (INV 13~19) — `humanize_check.py`+LLM 판정. 적발 → 재작성 (루프 max 2회)
→ ⑧ design-skill → ⑨ [HTML]qc-mobile/[MD]div 검사 → ⑩ Pin↔Body (INV 11) → ⑪ §B-CONFIRM 형 컨펌 게이트 (v3.2, INV 20) → ⑫ 산출

** 메커니즘: 사전생성형. ③에서 룰 박힌 상태로 작성, ④부터 안전망, ⑪에서 형 컨펌. 사후교정 ✗·자가신고 우회 ✗. **
```

---

## §H. 자체 스캔 통합 (INV 13·14·15·16·17·18·19)

| INV | 1차 검사 | 2차 검사 |
|---|---|---|
| 13 작업라벨 | LLM 판정 ("사전 없이 읽히나?") | `references/no-work-label.md` |
| 14 HERO 서사 | HERO 줄만 추출 → 흐름 점검 | `references/hero-format.md §3` |
| 15 어조 | 인물호칭·버전라벨 카탈로그 대조 | `references/hero-format.md §6` |
| 16 BAN_LEXICON | `scripts/humanize_check.py` | `references/banwords-lexicon.md` |
| 17 STYLE | 10조 체크리스트 | `references/humanize-gate.md §4` |
| 18 ANTI_BLOAT | 9패스 + "이 문장 없으면 결론 흔들?" | `references/humanize-gate.md §5` |
| 19 PRE_WRITE_GUARD | 5종 룰 사전 적용 + "형 코퍼스에 등장할 만한가?" | `references/pre-write-guard.md` |

적발 1+ → 전수재작성 → 재스캔. 2회차 적발 → STOP+보고. 부분치환 금지.

---

## §K. Self-Check

`python scripts/validate.py .` errors=[], 루프 2회. `evals/cases.json` 3+. 스캐너는 자기참조 라인(INV 마커) 제외.

---

## Gotchas

| 함정 | 대응 |
|---|---|
| 산문체 관성·결론 끝에·형부 남발·수치 0 | §E·§B·§C-NEW·§D-4 |
| DOC_TYPE 무시·DELIVER 강제 | §A-2 차등 |
| CEW 누락·압정만·반대주장 박스 0·다소스 인덱스화·수치 단독·의사결정 누락 | INV 10·11·12·F-2·D-1·B-1 |
| 작업 라벨 누출·부분치환·메타라벨 (v3.1 통과·압정 1:4:5) | INV 13 → 전수재작성·메타 삭제 |
| HERO 누락·카피톤 | INV 14 → 모든 섹션 첫줄·담담 |
| 인물호칭·장사어휘·작업약자 누출 | INV 15 → 역할명·평문·BEP/KPI/MECE/MVP만 통과 |
| **AI 흔적·번역투·장황 (v3.0)** | **INV 16·17·18 → `references/humanize-gate.md`+`humanize_check.py`** |
| **사후교정 의존 (1번 메커니즘)** | **INV 19 → `references/pre-write-guard.md`. ③ §B 진입 전 5종 활성화** |
| **시그니처 무리하게 끼우기** | **자연스럽지 않으면 빼라. 강제 ✗** |

---

## 예시

요청: `"리서치 15편 종합해줘. 보고서로"` → 라우팅(비공개): 길이=길음·수렴형·본문 비중 ↑·자기반박·산출 직전 7중 스캔(작업라벨·HERO·어조·BAN·STYLE·BLOAT·PRE_WRITE).

산출물 본문 시작 (HERO 첫 줄 + 가드 통과):
```
## 1. 다섯 영역에서 같은 결론이 다른 각도로 나타난다.
본문: 시장 규모(KOSIS 2024)·고객 행동(Nielsen 2024-Q3)·...

## 2. 진짜 차별점은 결과물의 종류가 아니라 소유 구조다.
본문: ...
```

산출물 0개 강제 (BAN_LEXICON 면제 라인 — `references/banwords-lexicon.md`): 종류·모드·결론비율·사고도구약어·인물호칭·버전라벨·장사어휘·**AI 5대 흔적** (사전 60+) 모두 금지.

상세: `references/pre-write-guard.md` · `humanize-gate.md` · `banwords-lexicon.md` · `hero-format.md` · `no-work-label.md` · `doc-types.md` · `cascade-protocol.md` · `CHANGELOG.md`
