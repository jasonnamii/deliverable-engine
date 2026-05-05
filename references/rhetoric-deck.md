# RHETORIC_DECK — 6수사 카드덱 (v4.1, INV 27 보조)

> **백본 1줄:** "논리 100%는 죽은 글이다." 한국 LLM 산출물의 Logos 편중을 6수사 카드덱으로 균형화한다.

> **출처:** Aristotle Rhetoric (Logos·Pathos·Ethos) · Cialdini Influence (6원리) · Heath Made to Stick (SUCCESs) · Kahneman Fast/Slow (System 1·2) · Doyle Sherlock Holmes

---

## 1. 본질 5줄

| | |
|---|---|
| **RULE** | 6수사 = Holmes·Pathos·Analogy·Numbers·Story·Image. 1+ 등장 강제 (MODE_M 1+, MODE_L 3+) |
| **출처** | Aristotle BC 350 · Cialdini 1984 · Heath 2007 · Kahneman 2011 · Doyle 1887~ |
| **SCOPE** | shaper §B-NARR N4 Analogy 슬롯의 1차 사례풀 + MODE_L 산출물 균형화 |
| **메커니즘** | BAN(부정)→슬롯 강제(긍정) 전환. UP의 BAN 일색에 균형 |
| **자가검사** | "이 산출물에 6장 중 몇 장 등장? MODE_L=3+ 미만이면 보강" |

---

## 2. 6수사 카드 정의

### 카드 1 — Holmes (통찰)

**정의:** 남이 못 보는 1단서·역방향 추론·통념 뒤집기.

**작동:**
- 표면 사실 뒤의 메커니즘 1개 발견
- "X가 보이지만, 실은 Y다"
- 모두가 A를 볼 때 B를 본다

**예:**
- "매출 +20% 성장이 보입니다. 실은 신규고객 -30%·기존고객 가격 인상 +50%였습니다."
- "고객은 가격이 아니라 시간을 산다."

**근거:** Doyle 셜록 홈즈 — 1단서 발견의 미학. UP §L1 [통찰] 태그와 정합.

### 카드 2 — Pathos (정서)

**정의:** 자기효능감·가능성·존재감·믿음 — 행동 전 감정.

**작동:**
- 1인칭 직접 화법
- 추상명사 ✗·존재감 어휘 ○
- "고객이 할 말·학부모가 칠 단어"

**예:**
- "내가 직접 결정할 수 있다."
- "이번엔 다르다는 믿음."

**근거:** Aristotle 3축 중 1·UP §발화모드 RULE 2와 정합.

### 카드 3 — Analogy (유사)

**정의:** 이미 성공한 것에 빗대기. 신뢰가 논리 전에 옴.

**작동:**
- "X는 Y와 같다·Y는 이렇게 됐다"
- 검증된 1차 사례 우선

**예:**
- "양평DNA = 일본 무인양품 (같은 신호 5축 동의 후 카테고리 확장 성공·2018)"
- "이 캠페인은 잡스 2007 키노트 구조다 (3-Beat·reinventing·아날로지)"

**근거:** Kahneman System 1 — 유사사례 1개 > 통계 100개. shaper §B-NARR N4 Analogy 슬롯의 1차 사례풀.

### 카드 4 — Numbers (수치)

**정의:** 1차 출처 + 정량 + 시간성. 검증된 수치만.

**작동:**
- 출처 박스: "수치 (출처·연도·표본수)"
- 1문장당 1수치·1고유명사
- 신뢰구간 명시

**예:**
- "정원인구 13.5만 (KOSIS 2024·전수)"
- "전환율 +12% (Nielsen 2024-Q3·n=2,400)"

**근거:** UP §L1 [정확성] 90 검증·shaper §B-PRE Lead 룰과 정합.

### 카드 5 — Story (이야기)

**정의:** Setup·Turn·Payoff 3박자. 한 인물·한 장면·한 변화.

**작동:**
- Setup: 상황 1단락
- Turn: 반전 1단락
- Payoff: 결론 1단락
- 한 사람·한 시점·한 변화

**예:**
- "(Setup) 양평 거주 김씨는 매주 주말 방문객 50명을 받았다. (Turn) 어느 날 그는 정원 사진 1장에 SNS 5만 reach를 얻었다. (Payoff) 그는 정원 카페로 업종을 바꿨다."

**근거:** Heath SUCCESs — Story가 가장 강한 부착력. NYT 인물 리드 패턴.

### 카드 6 — Image (이미지)

**정의:** 시각적 구체. 추상 ✗·구체명사 ○.

**작동:**
- 동사 정곡 1개로 장면화
- 색·소리·질감 1+ 동반
- "어슬렁거렸다·내려친다·자라난다"

**예:**
- "시장이 자란다 (추상)" → "시장이 매달 +3%씩 부풀어 오른다 (이미지)"
- "고객이 만족한다 (추상)" → "고객이 다시 문을 밀고 들어온다 (이미지)"

**근거:** 김훈 페르소나·동사 정곡 (KIWI 1-3). lexicon-ban §추상 BAN과 정합.

---

## 3. 발동 강도 (DOC_TYPE·MODE별)

| MODE | DOC_TYPE | 6수사 등장 강도 |
|---|---|---|
| MODE_S | ALL | 면제 |
| MODE_M | DELIVER·DIAGNOSE | 1+ 카드 |
| MODE_M | EVALUATE·CONVERGE | 2+ 카드 |
| MODE_L | ALL | 3+ 카드 (Numbers는 항상 포함) |
| HERO | — | Pathos·Image 우선 (김훈 페르소나) |

---

## 4. 카드 셀렉트 가이드

작성 전 1회 셀렉트:

| 의도 | 권장 카드 |
|---|---|
| 통념 뒤집기 | Holmes + Numbers |
| 행동 유도 | Pathos + Story + Image |
| 신뢰 구축 | Analogy + Numbers |
| 변화 설명 | Story + Image |
| 비교·평가 | Numbers + Analogy |
| 결정 촉구 | Holmes + Pathos |

---

## 5. 충돌 해소

| 충돌 | 해소 |
|---|---|
| Pathos vs INV 22 격식 | 격식 우선·Pathos는 합쇼체 안에서 |
| Image vs lexicon-ban 강조부사 | 강조부사 ✗·동사 정곡 ○ (KIWI 1-3) |
| Story vs B1 결론선행 | 결론 1번째 + Story는 Body에서 |
| Analogy 사례 검증 부재 | 1차 출처 신뢰 시에만 인용 |

---

## 6. Gotchas

| 함정 | 대응 |
|---|---|
| 6장 모두 다 욱여넣기 | MODE_L 3+ 권장·6장 모두 = 산만 |
| Pathos를 자갈로 채움 (매우·정말·진짜로) | 강조부사 ✗·구체 정서·존재감 어휘 |
| Analogy 검증 없이 인용 | 1차 출처 신뢰 시에만 |
| Image를 추상명사로 (혁신·차세대) | lexicon-ban hit·구체 동사로 |
| Story를 5단락+로 늘림 | 3박자·각 1단락 |
| Numbers 출처 박스 누락 | 출처·연도·표본 강제 |

---

## 7. 자기참조 면제

면제: SKILL.md, references/rhetoric-deck.md(본 문서), references/narr-gate.md
면제 ✗: 산출물(.md/.html)
