---
name: shaper-skill
version: 4.4.0
description: |
  shaper-skill — NYT 산출물 허브. v4.4 BIZ_DOC(외부독자 비즈문서 본문·완결문·연결조사·풀어쓰기·§B-PRE ①②④⑤ 분기). v4.3 ABSTRACT-BAN(§B-PRE 10종·본문 추상명사 차단·UTTER 블록 면제·block-level 모드 분기). v4.2 UTTER(박웅현). 5 DOC_TYPE(DELIVER·DIAGNOSE·EVALUATE·CONVERGE·UTTER + 🆕 BIZ_DOC).
  P1: 산출물, 보고서, 기획안, 제안서, 리포트, 글쓰기, 1pager, 플레이북, PRD, HERO, 휴머나이즈, 번역투, 사전가드, 합쇼체, 격식체, KIWI, 서사층, 스파인, NARR게이트, CEWA, 아날로지, UTTER, 박웅현, 매니페스토, 헤로카피, ABSTRACT_BAN, 분석체, 블록분기, BIZ_DOC, 비즈문서, 투자제안, 전략설명서, IR본문, 기획안본문, 외부독자, 완결문, 연결조사, 풀어쓰기.
  P2: 써줘, 작성해줘, 만들어줘, 정리해줘, write, draft, create.
  P3: NYT inverted pyramid, CEWA, hero format, humanize gate, ban lexicon, pre-write guard, formality gate, KIWI, narrative gate, abstract-noun ban, UTTER mode, block-level routing.
  P5: md파일로, html파일로, 보고서로.
  NOT: 세션브리핑(→session-briefing), 사업계획서(→bp-guide), 제출청소(→submission-cleanup).
vault_dependency: SOFT
---

# Shaper Skill — 쉐이퍼 스킬

산출물 품질 중앙 허브. 산문체 금지·NYT 강제. 단어층(미시) + 서사층(거시) 이중 사전게이트.

**🆕 v4.4.0 (2026-05-07):** ⑪ BIZ_DOC 모드 신설 (DOC_TYPE 5번째). 외부 독자 비즈문서 본문 전용. §B-PRE ①②④⑤ 강제 해제·완결문·연결조사·풀어쓰기·LV3 강제·박웅현 톤(시그니처) OFF. 카피·매니페스토 블록은 UTTER로 명시 면제. 정본 = `biz-doc-mode.md`. c8 c8-launching-campaign 본문 검증 통과.
**v4.3.1 (2026-05-07):** word-boundary BAN(OS·영문약어 substring FP 차단)·ALLOW 화이트리스트(임팩트 매트릭스 표준)·HTML 주석 면제·자가합리화 5번째 마커("내 검증 끝났으니 OK"). Edit·Patch 워크플로우 명시 게이트.
**v4.3:** ⑩ ABSTRACT-BAN 신설 (§B-PRE 10종). 본문 추상명사 차단·UTTER 블록만 ALLOW. block-level 모드 분기.
**v4.2:** UTTER 모드(박웅현). **v4.1.1:** NARR_SCAN 결정주의. **v4.1:** §B-NARR 4종·INV 27.
헤리티지 = `CHANGELOG.md`

---

## 🎯 본질 핵심 (v4.3, 5종 + 추상명사층)

| # | 본질 | 1줄 |
|---|------|-----|
| **B1** | NYT 역피라미드 + HERO | 결론 1번째·뒤 30% 삭제 생존 |
| **B2** | §B-PRE 10종 (단어층, v4.3) | 단문·시그니처·BAN회피·1문장1명제·≤80자·격식·작업라벨회피·KIWI·Intent-Quote·**🆕 ABSTRACT-BAN** |
| **B3** | 격식 (INV 22) | LV2~4 합쇼체·LV1 해라체. = `formality-gate.md` |
| **B4** | 어휘 BAN (INV 16) | 8 카테고리. = `lexicon-ban.md` |
| **B5** | KIWI 문법 (INV 25) | = `kiwi-grammar.md` |

**미시 4문 (§B-PRE):** 형 코퍼스? 격식? BAN? KIWI? **거시 4문 (§B-NARR):** 스파인 응결? 헤드라인=백본? 반박자 통과? 아날로지 1+?

---

## ⛔ 절대 규칙 (19)

| # | 규칙 |
|---|------|
| 1~9 | 게이트키퍼·산문체FORBIDDEN·역피라미드·9패스·6항QC·STEALTH·MUST cascade·DEFAULT_RENDER·DOC_TYPE 분기 |
| 10 | **CEWA (v4.1)** C+E+W+**A**. = `narr-gate.md §3-4` |
| 11 | **Pin↔Body 강화 (v4.1)** "스파인 변주" 컬럼·헤드라인-only 역추론 |
| 12 | 반대주장 박스 (MODE_M·L) — N3 통과한 큰 반박만 |
| 13 | 작업라벨 ZERO. = `lexicon-ban.md §2-3` |
| 14·15 | HERO 첫줄·어조 룰 |
| 16 | 어휘 BAN 1정본 = `lexicon-ban.md` 8 카테고리 |
| 17·18 | STYLE 10조·ANTI_BLOAT 9패스 |
| 19 | PRE_WRITE_GUARD (§B 진입 전 8종) |
| 20 | CONFIRM_GATE 송출 직전 |
| 21 | PT_FORMAT_GUARD |
| 22 | 격식 1정본 = `formality-gate.md` |
| 24 | UP_BAN_DICTIONARY |
| 25 | KIWI 문법 = `kiwi-grammar.md` |
| 26 | 외부송출 cascade (submission-cleanup) |
| **27** | **🆕 §B-NARR 단일우산 (v4.1)** — 거시 사전가드 4종. MODE_M·L 강제. 정본 = `narr-gate.md` |
| **28** | **🆕 UTTER 분기 (v4.2)** — DOC_TYPE=UTTER 시 작성자=박웅현·편집자=OFF·§B-PRE(격식 LV1·문단≤80자 면제·시그니처 보존)·§B-NARR(N1만·N2~N4 OFF·N4 CEWA→CEA). UP 발화모드 cascade 채널. UTTER 미명시·다른 타입 박웅현 호출 ✗ |
| **🆕 29** | **🆕 ABSTRACT-BAN (v4.3)** — §B-PRE ⑩. 본문 추상명사 BAN / UTTER 블록 ALLOW. 정본 = `abstract-ban.md` |
| **🆕 30** | **🆕 BIZ_DOC 분기 (v4.4)** — DOC_TYPE 5번째. 외부 독자 비즈문서 본문 = §B-PRE ①②④⑤ 분기 해제·완결문·연결조사·풀어쓰기·LV3 강제·시그니처 OFF·박웅현 톤 차단. 카피 블록 UTTER 면제 유지. 정본 = `biz-doc-mode.md` |

> **v4.4 본질:** `biz-doc-mode.md`(외부독자 본문) + `narr-gate.md`(서사층) + `rhetoric-deck.md`(6수사) + `lexicon-ban.md §2-9`(추상명사층). 우선순위: 22 > 16 > 13 > 25 > **27** > **🆕 29** > **🆕 30** > 17·18.

> **직교:** §B-PRE 미시·§B-NARR 거시·둘 다 사전강제. cleanup 축15는 사후 검출만.

---

## §A. ROUTER

- **A-1 길이:** ≤500자 MODE_S / 500~2000자 MODE_M / >2000자 MODE_L
- **A-2 DOC_TYPE:** DELIVER/DIAGNOSE/EVALUATE/CONVERGE/UTTER (v4.2)/**🆕 BIZ_DOC (v4.4)**. = `doc-types.md` · UTTER = 발화·카피·매니페스토·페르소나 시나리오·브랜드 스토리·헤로카피 · 🆕 BIZ_DOC = 외부독자 비즈문서 본문(투자제안·전략설명서·기획안본문·IR본문). 정본 = `biz-doc-mode.md`
- **A-3 PERSONA:** 작성자(DELIVER=강원국·DIAGNOSE/EVALUATE=이오덕·CONVERGE=유시민·HERO=김훈·UTTER=박웅현·**🆕 BIZ_DOC=유시민**) + 편집자(이오덕·UTTER 시 OFF·BIZ_DOC=이오덕). = `_common/persona-corpus.md §2·§2-EXT`
- **A-4 RELATION:** 수신자 LV(1~4) 결정. = `formality-gate.md`
- **🆕 A-5 SPINE (v4.1):** Claude 1줄(≤30자) 제안 → 형 컴펌 1회 (`🎯 스파인: "____" [O/S/R]`). MODE_M·L 강제. = `narr-gate.md §2`

---

## §B. NYT 구조

### §B-PRE (v4.3, 10종 단어층)
①단문 8~20자 ②시그니처 ③BAN 회피 ④1문장 1명제 ⑤문단 ≤80자 ⑥격식 LV ⑦작업라벨 회피 ⑧KIWI 문법 ⑨**의도 단어 따옴표 (Intent-Quote)** ⑩**🆕 ABSTRACT-BAN (추상명사 차단)**. = `pre-write-guard.md`·`lexicon-ban.md §2-9`

**⑨ Intent-Quote (v4.3):** 일반어를 *특별 의미로 재정의*해 쓸 때 작은따옴표(' ') 강제. 의도 마킹·1초 멈춤 신호. UTTER 강제. = `pre-write-guard.md`
**🆕 ⑩ ABSTRACT-BAN (v4.3.1):** 본문 추상명사 BAN. UTTER 블록만 ALLOW. 3대 FAIL = 정의 누락·1문장 합성·영문+한자 결합. **신규 생성·Edit·Patch 모두 동일 게이트.** ALLOW = 임팩트(매트릭스 표준). word-boundary BAN = OS. = `abstract-ban.md`

**UTTER 분기:** ⑤≤80자 면제·⑥LV1·⑦라벨ZERO·시그니처 강화. ②③④⑧⑩(UTTER ALLOW) 유지.

**🆕 BIZ_DOC 분기 (v4.4):** ① 단문 강제 OFF (20~40자 권장)·② 시그니처 OFF·④ 종속절 ALLOW·⑤ 문단 ≤200자·⑥LV3 강제. ③⑦⑧⑨⑩ 유지. 정본 = `biz-doc-mode.md §3`.

### 🆕 §B-NARR (v4.1, 4종 서사층, MODE_M·L)

| 룰 | 명칭 | 자가검열 |
|---|---|---|
| **N1** | 스파인 응결 | 헤드라인 보고 §A-5 스파인 역추론? NO=재작성 |
| **N2** | 에디터 페어 | 섹션 종료 시 편집자(이오덕) 4문 |
| **N3** | 반박자 동석 | 핵심 주장 옆 *내적* 자문 — 통과만 본문 진입 |
| **N4** | CEWA | 주장당 유사 성공사례 1+ 의무 |

**N3 출력:** 자문 *내적*·본문 ZERO. 통과한 큰 반박만 INV 12 박스로 사후 표시.

**UTTER 분기:** N1 강제·N2 OFF·N3 OFF·N4 → CEA(Claim+Evidence+Analogy).

**🆕 BIZ_DOC 분기 (v4.4):** N1·N2·N3·N4 모두 강제 (외부 독자에겐 서사층이 더 중요). CEWA 풀강제.

상세 = `narr-gate.md`·`biz-doc-mode.md §4`

### 📚 References
정본: `lexicon-ban.md`·`formality-gate.md`·`kiwi-grammar.md`·`narr-gate.md`·`rhetoric-deck.md`·`abstract-ban.md`·🆕`biz-doc-mode.md`
도구: `pre-write-guard.md`·`humanize-gate.md`·`hero-format.md`·`doc-types.md`·`cascade-protocol.md`·`jason-pt-toolkit.md`·`jason-corpus-examples.md`·`no-work-label.md`·`_common/persona-corpus.md`
1차 출처: `VAULT/_skills research/shaper-skill/2026-05-05_R-NARR-LIGHT.md`

### §B-구조
Headline → 의사결정 → Lead → Nut graf(MODE_L) → Body(소제목+HERO+≤80자) → Pin↔Body 1:1 (v4.1 "스파인 변주" 컬럼).

### §B-CONFIRM
`🔍 송출 전 검토. AI 티·번역투·장황·서사층 결함? [OK/수정/재작성]`

---

## §C·§D·§E·§F (안전망)
§C 9패스 §D 6항QC §E FORMAT(CEWA·반대주장) §F Cascade. = `humanize-gate.md`·`cascade-protocol.md`

---

## §G. 파이프라인 (v4.3)

```
① PREFLIGHT → ② §A 라우터·SPINE → ③ §B-PRE (10종·미시 4문)
→ ④ §B-NARR (4종·거시 4문, MODE_M·L) → ⑤ §B 작성
→ ⑥ humanize_check.py (10 카테고리) → ⑦~⑩ FORMAT·검사·Pin↔Body
→ ⑪ CONFIRM → ⑫ submission-cleanup → ⑬ 산출
```

---

## §H. 자체 스캔 (v4.3, 10 카테고리·결정주의)

`humanize_check.py`: AI_LEX·ADV_BAN·LABEL_BAN·TRANS_BAN·FNOUN_BAN·IDA·HEDGE_BAN·MISC_BAN·NARR_SCAN·🆕`ABSTRACT_BAN`(v4.3·UTTER 블록 면제). 적발 1+ → 전수재작성 (루프 max 2).

---

## §K. Self-Check
`python scripts/validate.py .` errors=[] + `evals/cases.json` 9+.

---

## Gotchas

- 산문체·결론끝에 → §E·§B
- DOC_TYPE 무시 → §A-2
- CEW 누락 (v4.1: CEWA) → INV 10
- 작업라벨·인물호칭 → INV 13·15
- AI 흔적·번역투·장황 → INV 16~18
- 사후교정 의존 → INV 19·27 (사전강제)
- 본문 이다체·LV 미결정 → INV 22
- KIWI 위반 → INV 25
- 형 시그니처(정말·확실히·진짜·이게 다야?) ALLOW
- **Intent-Quote 누락** → "사건" vs "'스캔들'" — 일반어 의미 재정의 시 따옴표 강제
- **§A-5 SPINE 없이 §B-NARR 진입** → 거시 4문 FAIL · §B-NARR 자문 본문 출력 → N3 위반(내적만)
- **MODE_S에 §B-NARR 강제** → SCOPE_OUT
- **UTTER 모드에 분석체/CEWA 4종/LV3·4/편집자** → 박웅현 위반. UTTER = LV1·CEA·편집자 OFF
- **DELIVER·CONVERGE에 박웅현** → UTTER 전용·침범 ✗
- **🆕 (v4.3) ⑩ ABSTRACT-BAN** — 본문 추상명사 합성·블록분리 미실시·"컨셉이니 예외" 자가합리화 → 모두 FAIL. 정본 = `abstract-ban.md`
- **🆕 (v4.4) ⑪ BIZ_DOC 미적용** — 외부 독자 비즈문서 본문에 ① 단문 강제·② 시그니처(직접·그냥·왜·정말) 주입·④ 1문장 1명제 압축 = 메모형 변질·외부 독자 위화감. DOC_TYPE 판정 시 외부 독자 명시되면 BIZ_DOC 강제. 정본 = `biz-doc-mode.md`
- **🆕 (v4.4) BIZ_DOC ↔ UTTER 영토 침범** — 비즈문서 본문 전체를 박웅현 톤으로 작성 = UTTER 침범 = FAIL. 본문 = BIZ_DOC, 카피 블록만 UTTER 명시 면제. block-level 분기 그대로

## ❌ WRONG vs ✅ CORRECT (v4.1 서사층 · v4.3 추상명사층)

**서사층 (v4.1):**
```
❌ 헤드라인 = "현황 / 분석 / 시사점 / 결론" (구조어휘만·스파인 ✗)
✅ 스파인="정원이 답이다" → 헤드라인 = "양평DNA는 셋이다 / 정원이 가장 강하다 / 정원으로 +12% / 정원에 베팅한다"
```

**🆕 추상명사층 (v4.3 · ⑩ ABSTRACT-BAN):**
```
❌ DELIVER 본문: "자기 구축형 창작자 OS·디지털 페르소나 자산·알고리즘 주권 회복" (추상명사 5·정의 0)
✅ DELIVER 본문: "C8은 창작자가 일하는 곳입니다. 작업물·이력·연결을 한 곳에 모읍니다."
✅ UTTER 카피: "알고리즘 주권 회복" (블록 명시 면제 OK)
```
상세 = `abstract-ban.md`

**🆕 비즈니스 문서층 (v4.4 · ⑪ BIZ_DOC):**
```
❌ BIZ_DOC 본문에 카피 톤(메모형):
   "콘텐츠 공급 과잉 + 알고리즘 단축화. 창작자 자아 소진이 신규 시장 신호. 협업·도시 자리 부재가 구조적 공백."
   → 명사구 나열·조사 누락·외부 독자에게 메모처럼 읽힘 = FAIL

✅ BIZ_DOC 본문(완결문·연결조사·풀어쓰기):
   "콘텐츠 공급 과잉과 알고리즘 피로는 새로운 플랫폼 전환 신호입니다. 창작자 자아 소진은 단순 현상이 아니라 새로운 시장 기회의 시작입니다. 현재 시장에는 협업 구조와 오프라인 기반 창작 장면이 부재합니다."

✅ 같은 문서 안 UTTER 카피 블록 (block-level 분기):
   <div class="manifesto-block">"광고를 만들지 않았습니다. 사건을 만들었습니다."</div>
```
상세 = `biz-doc-mode.md`

---

## 예시

### 예시 1 — CONVERGE (분석체)
요청 = "리서치 15편 종합. 보고서로" (MODE_L·CONVERGE) → §A-5 SPINE → 작성자=유시민·편집자=이오덕 → §B-PRE → §B-NARR → 작성.

**§A-5:** `🎯 스파인: "다섯 곳이 한 방향을 가리킨다." [O/S/R]` → 형 OK

```
## 1. 다섯 곳에서 같은 결론이 나타납니다.
시장 규모(KOSIS 2024)·고객 행동(Nielsen 2024-Q3)이 같은 방향.
유사 사례: 일본 무인양품 2018 — 같은 신호 5축 동의 후 카테고리 확장 성공.
```

### 예시 2 — UTTER (박웅현)
요청 = "기획안 매니페스토로" (UTTER) → 작성자=박웅현·편집자 OFF → LV1·N1만·CEA → 작성.
**§A-5:** `🎯 스파인: "양평엔 정원이 있다."`
❌ "양평 DNA는 정원으로 수렴되며 시장 데이터 분석 결과 베팅할 필요가 있다." (분석체)
✅ "양평엔 정원이 있다. 그게 다야. // 베어트리파크에 7년 갔다. 매번 같은 자리에 선다. 사람들이 멈춘다. 그리고 다시 온다. // 정원이 답이다." (박웅현)

### 🆕 예시 3 — BIZ_DOC (외부 독자 비즈문서, v4.4)
요청 = "C8 런칭 캠페인 기획안 본문. 투자자·관계자용" (BIZ_DOC·MODE_L) → 작성자=유시민·편집자=이오덕 → §B-PRE BIZ 분기(①②④⑤ OFF·⑥LV3) → §B-NARR 풀강제 → 작성.
**§A-5:** `🎯 스파인: "1만 활성 사용자가 첫 분기점이다." [O/S/R]`
❌ BIZ_DOC 본문: "1만이 분기점입니다. 그다음은, 광고 없이 돕니다." (메모형·박웅현 톤 침범)
✅ BIZ_DOC 본문: "초기 목표는 1만 활성 사용자 확보입니다. 이 시점부터 연결 밀도가 의미를 갖기 시작합니다. 그다음부터는, 광고 없이도 돌아갑니다."
✅ 같은 문서 매니페스토 블록(UTTER): "1만이 분기점입니다." (block-level 면제)

상세: `biz-doc-mode.md`·`narr-gate.md`·`rhetoric-deck.md`·`lexicon-ban.md`·`formality-gate.md`·`kiwi-grammar.md`·`pre-write-guard.md`·`humanize-gate.md`·`hero-format.md`·`doc-types.md`·`cascade-protocol.md`·`jason-pt-toolkit.md`·`_common/persona-corpus.md`·`CHANGELOG.md`

**외부 cascade:** `submission-cleanup` v1.2.x (14축 + 축15 서사층 검출·경고만)
