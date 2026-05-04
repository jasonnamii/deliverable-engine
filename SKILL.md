---
name: shaper-skill
version: 4.0.0
description: |
  shaper-skill — NYT 산출물 허브. v4.0 메이저 통폐합: INV 25→18·refs 15→11·스캐너 카테고리 16→8. 어휘 BAN 1정본(lexicon-ban)·격식 1정본(formality-gate)·KIWI 문법 1정본(kiwi-grammar). 본질 5종·§B-PRE 8종. 헤리티지 → CHANGELOG. skill-doctor 진단 점수 74→90+ 목표.
  P1: 산출물, 페이퍼엔진, 보고서, 기획안, 제안서, 진단서, 전략서, 리포트, 비교분석, 글쓰기, 1pager, 플레이북, PRD, HERO, 히어로, 휴머나이즈, AI문서티, 번역투, 장황, 압축, 사전가드, 작성가드, PT산출물, PT패턴, PT모드, PT_DOC, 형스타일, 입니다체, 합쇼체, 비즈니스격식, 관계격식, 수신자격식, 외부발신, 정중체, 격식체, UPBAN, 자가합리화차단, KIWI, 글쓰기법칙, 한국글쓰기, 단문쓰기, 한자투, 자신없는표현, 것남용, 부사자제, 동사정곡, Syntax어순.
  P2: 써줘, 적어줘, 작성해줘, 만들어줘, 정리해줘, write, draft, create.
  P3: NYT inverted pyramid, claim-evidence-warrant, document type router, hero format, humanize gate, anti-bloat, ban lexicon, pre-write guard, formality gate, KIWI rules.
  P5: md파일로, html파일로, 보고서로.
  NOT: 세션브리핑(→session-briefing), 사업계획서(→bp-guide), 제출청소(→trigger-dictionary).
vault_dependency: SOFT
---

# Shaper Skill — 쉐이퍼 스킬

산출물 품질 중앙 허브. 산문체 금지, NYT(역피라미드·압정) 강제. 불릿·헤더·수치·인용·단문 필수.

**v4.0 메이저:** 통폐합 — INV 25→18·refs 15→11·스캐너 카테고리 16→8·§B-PRE 11종→8종. 어휘/격식/KIWI 문법 3 정본화. 진단 점수 74→90+ 목표. **추가 0·통폐합만**.

상세 헤리티지 (v2.3~v3.4) = `CHANGELOG.md`

**v4.1 외부송출 cascade (2026-05-04):** §G 파이프라인 ⑨→⑩(외부송출 cascade)→⑪(산출) 신설. 외부 송출 의도 감지 시 `submission-cleanup` 스킬 자동 호출 (14축·7서브슬롯 결정주의 박멸). 작성 단계(§B·§C·§D·§H)와 직교 — shaper=작성 중·submission-cleanup=송출 직전. INV 26 신설. **변이 동기:** 형 피드백 — "다음 액션 실행" → 분리한 submission-cleanup이 외부 송출 시점에 자동 발동되도록 cascade 박제.

---

## 🎯 본질 핵심 5종 (v4.0 — 18개 INV 인지부담 압축)

매 산출물 작성 시 *반드시* 인지할 5종. 나머지 13개 INV는 안전망·세부 룰.

| # | 본질 | 1줄 |
|---|------|-----|
| **B1** | NYT 역피라미드 + HERO | 결론 1번째·뒤 30% 삭제 생존·섹션 첫줄=압축 한 문장 |
| **B2** | 사전생성 8종 (§B-PRE) | 단문·시그니처·BAN회피·1문장1명제·≤80자·격식·작업라벨회피·KIWI문법. 작성 *전* 박제 |
| **B3** | 격식 통합 (INV 22) | §A-4 LV 결정 → LV2~4 합쇼체 100%·LV1 해라체. 면제: Headline·압정·표·인용박스 |
| **B4** | 어휘 BAN 1정본 (INV 16) | `lexicon-ban.md` 8 카테고리 (AI_LEX·ADV·LABEL·TRANS·FNOUN·IDA·HEDGE·MISC). 송출 직전 grep |
| **B5** | KIWI 문법 (INV 25) | Syntax 어순·동사 정곡·1주어·단문·접속사 균형. `kiwi-grammar.md` |

**메타 자기검열 4문 (§B-PRE 진입 직전):** "형 코퍼스 등장? 격식 LV·종결? 어휘 BAN hit? KIWI 문법?" 4문 모두 YES → 작성. 1개라도 NO → 재생성.

---

## ⛔ 절대 규칙 (18)

| # | 규칙 |
|---|------|
| 1~8 | 게이트키퍼·산문체FORBIDDEN·역피라미드·9패스·6항QC·STEALTH·MUST cascade·DEFAULT_RENDER 순수MD |
| 9 | DOC_TYPE 분기 (DELIVER/DIAGNOSE/EVALUATE/CONVERGE) |
| 10 | CEW (모든 주장=C+E+W) |
| 11 | Pin↔Body 1:1 |
| 12 | 반대주장 박스 (MODE_M·L Body당 1+) |
| 13 | **작업라벨 통합 (v4.0)** 작업라벨ZERO + UP §1 작업프레임 BAN. `lexicon-ban.md §2-3 LABEL_BAN` |
| 14·15 | HERO 첫줄·어조 룰 (인물호칭·버전라벨·장사어휘 금지) |
| 16 | **어휘 BAN 통합 (v4.0)** AI 흔적·번역투·형식명사·KIWI 어휘 BAN 1정본 = `lexicon-ban.md` 8 카테고리 |
| 17 | STYLE 10조 (단문·구체명사 70%+·능동형) |
| 18 | ANTI_BLOAT 9패스·50%+ 감축 |
| 19 | PRE_WRITE_GUARD 사전생성형 (§B 진입 전 8종 강제) |
| 20 | CONFIRM_GATE 송출 직전 형 컨펌 1회 |
| 21 | PT_FORMAT_GUARD (placeholder ✗·불릿위주 ✗·도구함 9종 자연주입) |
| 22 | **격식 통합 (v4.0)** 입니다체 + 관계격식 4LV → 1정본 = `formality-gate.md` |
| 24 | UP_BAN_DICTIONARY (§3 자가합리화차단·§4 self-check 잔존. §1·§2는 INV 13·16에 흡수) |
| 25 | **KIWI 문법 (v4.0)** Syntax 어순·동사 정곡·이중주어·단문 허리·접속사 균형 = `kiwi-grammar.md` |

> **본질 박스 (INV 13·16·22·25 통합)** = `references/lexicon-ban.md` (어휘 1정본) + `formality-gate.md` (격식 1정본) + `kiwi-grammar.md` (문법 1정본). v4.0 통폐합으로 충돌 해소. 우선순위: INV 22 격식 > INV 16 어휘 > INV 13 작업라벨 > INV 25 KIWI 문법 > INV 17·18 STYLE/BLOAT.

> **INV 19·20·21 본질** = `pre-write-guard.md` + `humanize-gate.md` + `jason-pt-toolkit.md`

---

## §A. ROUTER (길이 + DOC_TYPE + RENDER + RELATION)

### A-1·A-2·A-3 라우팅
- **길이:** ≤500자 MODE_S / 500~2000자 MODE_M / >2000자 MODE_L

- **DOC_TYPE:** DELIVER(보고·디폴트) / DIAGNOSE(진단) / EVALUATE(비교) / CONVERGE(통합). 우선: CONVERGE>EVALUATE>DIAGNOSE>DELIVER. = `doc-types.md`
- **PERSONA (v4.2):** DOC_TYPE → 명저자 페르소나 자동 라우팅 (DELIVER=강원국·DIAGNOSE/EVALUATE=이오덕·CONVERGE=유시민·HERO=김훈). = `_common/persona-corpus.md §2`. 격식 LV (INV 22) 우선·페르소나는 어휘·동사·자갈제거에만 한정
- **RENDER:** `.md`→순수MD · `.md`+HTML/박스/벤토→html-div-style · `.html`→C9

### A-4. RELATION (INV 22) — 관계격식 자동추론

§B 진입 전 강제. 수신자 LV(1~4) 결정 없이 §B 진입 = FAIL.

| LV | 수신자 | 종결·어조 |
|---|---|---|
| LV4 | 투자자·이사회·VC·정부 | 입니다체 100% + 격식 최상 |
| LV3 | 거래처·외부 파트너·신규 고객 | 입니다체 100% + 정중 |
| LV2 | 사내 임원·타팀 | 입니다체 디폴트 |
| LV1 | 동료·내부 메모 | 해라체 허용 |

자동추론: 신호 grep → 디폴트 LV. 모호 시 1회 핑 ("[A]투자자 [B]거래처 [C]사내 [D]내부").
신호 grep·결정트리·핑 문구·LV별 어조·호칭 = `→ formality-gate.md`

---

## §B. NYT 구조

### §B-PRE. 사전 작성 가드 (v4.0, 8종)

8종 룰 + 메타 자기검열 4문: ①단문 8~20자 ②시그니처 자연주입(형+장르 페르소나·`_common/persona-corpus.md §4`) ③BAN 사전회피(`lexicon-ban.md`) ④1문장 1명제 ⑤문단 ≤80자 ⑥격식 LV·종결 사전결정(`formality-gate.md`) ⑦작업라벨/프레임 사전회피(`lexicon-ban.md §2-3`) ⑧KIWI 문법(`kiwi-grammar.md`).

메타 4문: "형 코퍼스 등장? 격식 LV·종결 맞나? 어휘 BAN hit? KIWI 문법 위반?" 1개라도 NO → 재생성.

상세 = `references/pre-write-guard.md`

**📚 References (v4.0 11개):**
- 정본 3종 (v4.0): `lexicon-ban.md`(어휘) · `formality-gate.md`(격식) · `kiwi-grammar.md`(KIWI 문법)
- 페르소나 1종 (v4.2 신설): `_common/persona-corpus.md` (장르×명저자 매핑·4명저자 시그니처·충돌해소·사람어휘풀)
- 휴머나이즈: `humanize-gate.md` · `pre-write-guard.md` · `hero-format.md` · `no-work-label.md`
- 분기·도구: `doc-types.md` · `cascade-protocol.md` · `jason-pt-toolkit.md`
- 형 코퍼스: `jason-corpus-examples.md`
- 1차 출처: `VAULT/_skills research/shaper-skill/2026-05-03_R1~R7.md` + `2026-05-03_v4-CONSOLIDATION-DESIGN.md`
- 헤리티지 보존: `references/_archive/` (banwords·up-ban·kiwi-writing·imnida·relation 5종)

**📐 PT (v3.2, INV 21):** placeholder ✗ + 불릿위주 ✗ + 도구함 9종 자연주입 = `references/jason-pt-toolkit.md`

### §B-구조

Headline(주장 1줄, 설명형 ✗) → 의사결정 1줄 → Lead(5W1H, 1문장당 1수치·1고유명사) → Nut graf(MODE_L) → Body(소제목 + HERO 1줄 + 단락 ≤80자) → Pin↔Body 1:1 매핑표.

### §B-CONFIRM. 송출 직전 형 컨펌 (INV 20)

산출물 송출 직전 1회: `🔍 송출 전 검토 부탁드려요. AI 티·번역투·장황 있나요? [OK / 수정 / 재작성]`
규칙: OK→송출 · 수정→§B-PRE 재진입 · 재작성→§B 전체 재진입.
SCOPE_OUT: ≤5줄·단답·확인성·실행보고·진단 본문·일반대화·핑퐁·컨펌게이트 자체.
CHECK: 산출물인데 미발동 = FAIL → 폐기·재출력.

---

## §C·§D·§E·§F (안전망)

§C 9패스(질문재술·서문·헤징·동의어·예시·3항·수있다·수식어·70%절단) §D 6항QC §E FORMAT(CEW·반대주장) §F Cascade(3티어·MULTI_SOURCE). 상세 = `humanize-gate.md` + `cascade-protocol.md`

---

## §G. 파이프라인

```
① PREFLIGHT → ② §A 라우터+RENDER+RELATION (§A-4 LV 결정, INV 22)
→ ③ §B-PRE 활성화 (v4.0, 8종) → §B 작성 [8종 룰 강제] (Headline·의사결정·Lead·Body[HERO]·Pin↔Body)
   토큰 직전 자기검열 4문: "형 코퍼스 등장? 격식? 어휘 BAN hit? KIWI 위반?" 4 모두 YES → 작성
→ ④ 통합 사후스캔 1회 (안전망) — `humanize_check.py` 8 카테고리 + LLM 판정
   ④-a 9패스 ANTI_BLOAT (③ 충실 시 ≤1패스) ④-b 6항 QC ④-c §H 8중 자체스캔 (INV 13~25)
   적발 → 재작성 (루프 max 2회)
→ ⑤ §E FORMAT+CEW+반대주장 → ⑥ design-skill → ⑦ [HTML]qc-mobile/[MD]div 검사 → ⑧ Pin↔Body (INV 11)
→ ⑨ §B-CONFIRM 형 컨펌 게이트 (v3.2, INV 20) → ⑩ **외부송출 cascade** (v4.1) → ⑪ 산출

> **⑩ 외부송출 cascade (v4.1, INV 26):** 산출 직전 외부 송출 의도 감지 — P5에 .md/.docx/.pdf/.pptx + (`외부 제출`·`송출`·`IR`·`제안서`·`정책문서`·`납품`·`출고`) hit OR 형 명시 호출 → **submission-cleanup 스킬 자동 호출** (14축·7서브슬롯 결정주의 박멸). 작성 단계 게이트(§B·§C·§D·§H)와 직교 — shaper는 작성 중·submission-cleanup은 송출 직전. 미해당 = 스킵, ⑪ 직행.

** v4.0 메커니즘: 사전생성 8종 충실 시 사후 1회 안전망. 통합 정본 3종으로 false positive 차단. **
```

---

## §H. 자체 스캔 통합 (8중, INV 13~25)

`scripts/humanize_check.py` v4.0 8 카테고리(AI_LEX·ADV_BAN·LABEL_BAN·TRANS_BAN·FNOUN_BAN·IDA·HEDGE_BAN·MISC_BAN) + LLM 판정. 적발 1+ → 전수재작성 (루프 max 2회). 부분치환 ✗.

상세 INV별 검사 매핑 = `humanize-gate.md §6` + `pre-write-guard.md` + `lexicon-ban.md §4 CHECK`

---

## §K. Self-Check

`python scripts/validate.py .` errors=[] (루프 max 2회) + `evals/cases.json` 9+. 자기참조 라인(INV 마커) 제외.

---

## Gotchas

- 산문체·결론끝에·수치0 → §E·§B·§C
- DOC_TYPE 무시 → §A-2
- CEW·반대주장 누락 → INV 10·11·12
- 작업라벨·인물호칭 누출 → INV 13·15 (`lexicon-ban.md §2-3`)
- AI 흔적·번역투·장황 → INV 16~18 (`lexicon-ban.md` 8 카테고리)
- 사후교정 의존 → INV 19 (§B 진입 전 사전강제)
- 시그니처 무리하게 끼우기 → 자연스럽지 않으면 빼라
- 본문 이다체·LV 결정 없이 §B 진입 → INV 22 (`formality-gate.md`, §A-4 강제)
- KIWI 문법 위반 (어순·동사·이중주어·단문·접속사) → INV 25 (`kiwi-grammar.md`)
- 형 시그니처(정말·확실히·진짜)는 ALLOW. 강조부사(매우·너무나)만 BAN
- **(v4.0) 통폐합 후 헤리티지 검색** → `_archive/` 또는 `CHANGELOG.md`
- **(v4.0) v3.x INV 23(관계격식)·24(UP §1·§2) 참조** → INV 22·INV 13·INV 16에 흡수됨

## ❌ WRONG vs ✅ CORRECT (v4.0 통폐합)

```
❌ WRONG: "INV 23 관계격식 발동" (v3.x 참조 — v4.0에서 INV 22로 통합)
✅ CORRECT: "INV 22 격식 게이트 발동 (formality-gate.md 4LV 매트릭스)"
```

```
❌ WRONG: humanize_check.py에서 한 단어가 FORMAL+KIWI_ADV 2회 적발 (false positive)
✅ CORRECT: v4.0 ADV_BAN 1 카테고리로 통합 — 1회 적발
```

---

## 예시

요청 = "리서치 15편 종합해줘. 보고서로" → 길이 길음·수렴형·관계격식 자동 정중·합쇼체 100%.

산출물 본문 (합쇼체 + HERO 첫 줄):
```
## 1. 다섯 곳에서 같은 결론이 다른 각도로 나타납니다.
본문 단락은 합쇼체. 시장 규모(KOSIS 2024)·고객 행동(Nielsen 2024-Q3)이 같은 방향을 가리킵니다.

## 2. 진짜 차별점은 결과물의 종류가 아니라 소유 구조입니다.
본문이 이어집니다.
```

상세: `references/lexicon-ban.md` · `formality-gate.md` · `kiwi-grammar.md` · `pre-write-guard.md` · `humanize-gate.md` · `hero-format.md` · `no-work-label.md` · `doc-types.md` · `cascade-protocol.md` · `jason-pt-toolkit.md` · `jason-corpus-examples.md` · `CHANGELOG.md` (v2.3~v4.0 헤리티지)

**외부 cascade:** `submission-cleanup` 스킬 (외부 송출 14축 정제·축14 정본 `ai-not-canon.md` 단일 권위 — UP §L2·shaper·submission-cleanup 모두 본 정본 참조)
