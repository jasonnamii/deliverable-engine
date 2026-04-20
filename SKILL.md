---
name: paper-engine
version: 1.1.0
description: |
  paper-engine(페이퍼엔진) — 산출물 품질 중앙 허브. 모든 도메인스킬의 .md/.html 산출물에 구조(모래시계)·블록(7규칙)·QC(4축) + **시각소스 감지 훅** cascade 자동 주입. HTML 생성시 시각소스(수치비교·시간축·프로세스·순환·매트릭스·핵심수치) 감지→design-skill C9로 전달. 단독 문서 생산도 관장. 디자인 위임은 design-skill.
  P1: 산출물, deliverable, paper-engine, 페이퍼엔진, 보고서, 기획안, 제안서, 학습노트, 위키문서, 진단서, 전략서, 리포트, 컨설팅보고서, 프로파일, 설계안, 처방서, 액션리스트, HTML문서, 웹문서.
  P2: 써줘, 편집해줘, 드래프트해줘, 뽑아줘, ~로 만들어줘, write, edit, draft, compose.
  P3: deliverable engine, paper engine, document quality hub, block design, hourglass structure, cascade pipeline, visualization hook.
  P4: 구조화된 서술 문서 생산시, 산출물 구조 편집시, 타 스킬이 md/html 파일 생성시 자동 cascade, 사용자가 "보고서로/진단서로/html로" 등 포맷 지정시, 문서화 의도 1% 감지시 선제 제안(§0-A), HTML 산출물에 시각소스 2+ 감지시 design-skill 시각요소 요청.
  P5: md파일로, html파일로, 옵시디언으로, 보고서로, 진단서로, 전략서로, 리포트로, 웹문서로, 기획안으로.
  NOT: 데이터저장·시스템로그·raw dump(→직접수행), 세션브리핑(→session-briefing), 사업계획서(→bp-guide), 제출청소(→trigger-dictionary).
vault_dependency: SOFT
---

# Paper Engine

도메인스킬의 md 산출물에 구조·블록·QC 자동 주입 **중앙 허브**. 포맷 키워드("보고서로"·"진단서로") 또는 md 생성 시 자동 cascade. 제출청소는 trigger-dictionary.

---

## ⛔ 절대 규칙 (INVARIANT)

| # | 규칙 | 위반시 |
|---|------|--------|
| 1 | **게이트키퍼** — md 산출물 생성 시 cascade 자동 발동. 별도 호출 불필요 | 품질 통제 붕괴 |
| 2 | **PREFLIGHT** — 착수 전 수신자·목적·핵심메시지 확정. 불가 시 최선가정+명시 | 전량 재작업 |
| 3 | **재검증 (reset)** — 장기대화 CONTEXT_WATCH 발동 시 프레이밍 재확인. 가정 표류 PIVOT | 방향 이탈 |
| 4 | **STEALTH** — 내부 라벨(§0/§1/ⓐ~ⓔ/풀·경량·패스스루) 본문 노출 ✗ | 사용자 혼란 |
| 5 | **디자인 위임** — design-skill 단일 권위. 허브는 구조·블록·QC만 | 역할 중복 |

---

## §0. Cascade 3티어

용도 키워드("팀한테/보고/제출/보내") → 외부, 나머지 → 내부. 불명 → 외부.

| | ≤20행 | 21~50 | 51+ |
|---|:-:|:-:|:-:|
| 외부 | 경량 | 풀 | 풀 |
| 내부 | 패스스루 | 경량 | 풀 |

풀=ⓐ~ⓔ+QC4축 / 경량=1블록1목적+QC(숫자·VOCAB) / 패스스루=1블록1목적.

**§0-A 의도 1% 게이트:** 문서 의도 감지 → 1문장 제안, 수락 전까지 대화. P2 동사 명시 → 즉시 §1.

**5단계:** ⓐ spine → ⓑ 모래시계+블록 → ⓒ 제목 → ⓓ QC → ⓔ 디자인 위임(HTML시 **시각소스 목록 동반 전달**). 2패스 ✗. spine 폴백(데이터·리스트) → 참조형.

**시각소스 감지 훅(HTML·웹MD 전용):** ⓑ 블록 설계 중 수치비교·시간축·프로세스·순환·2축분류·핵심수치·비율·퍼널 신호를 태깅(V1~V10). ⓔ에서 design-skill에 블록별 시각소스 목록을 전달 → design-skill C9 강제 발동. 상세 → `references/cascade-protocol.md §12`.

---

## §1. 파이프라인

```
① 프레이밍 → ② 작성 → ③ QC (스킵 ✗)
```

- **① 프레이밍:** 수신자+목적+핵심메시지 3개. cascade 시 상위 결론이 핵심메시지. 질문 ✗
- **② 작성:** 매크로+메조 1회 통합. VOCAB 금지어 사전 회피
- **③ QC:** 티어별 축 적용

| 축 | 풀 | 경량 | 패스스루 |
|---|:-:|:-:|:-:|
| ①숫자정합 | ✓ | ✓ | — |
| ②논리완결 | ✓ | — | — |
| ③문체·VOCAB | ✓ | ✓ | — |
| ④블록정합 | ✓ | — | — |

VOCAB 치환표 = 스포크 참조. QC 없이 전달 = FAIL.

---

## §2. 매크로·메조·제목·파일

| 층 | 핵심 |
|---|---|
| §2 매크로 | 모래시계(역피라미드→spine→피라미드) |
| §3 메조 | 블록 7규칙 + 밀도 ENUM + 축별나열 변환 |
| §4 제목 | 설득형=주장형 / 참조형=라벨형 |
| §5 파일 | 네이밍·버전·덮어쓰기 방지·시각문법 |

50행↓ 면제: 블록전환·밀도대비·블록크기. 1블록1목적만. 파일운영 → `references/file-ops.md`.

---

## §6. Self-Check

```bash
python scripts/validate.py .    # errors=[] 통과, 루프 하드캡 2회
```

`evals/cases.json` 3건+ 필수. 실패 시 STOP + 보고(원인·영향범위). 조용한 실패 ✗. 개선 여지 → thumbs-down 피드백.

---

## Gotchas

| 함정 | 대응 |
|---|---|
| cascade 미적용 | md 생성 시 자동 |
| 축별 나열 원본 | 서사+밀도 교대 |
| 결론이 끝에 | spine 첫 3줄 |
| 프레이밍 스킵 | 전량 재작업 |
| 디자인 직접 | design-skill |
| 내부 라벨 노출 | STEALTH |
| ⓑⓒ 2패스 | 1회 통합 |
| 이름 이력 | deliverable→paper(v1.0+) |
| HTML인데 표·문장만 | ⓑ에서 V1~V10 태깅 → ⓔ에 전달 |
| 시각소스 감지 누락 → 타이포만 예쁜 HTML | cascade-protocol.md §12 체크리스트 |
| 엣지케이스 | 착수 전 점검 |

---

## 예시

`"biz-skill로 진단해줘. 보고서로 뽑아줘"` → biz-skill 실행 → md 생성 시점 cascade 자동 → ⓐ spine "3축 실패" → ⓑ 모래시계+블록 → ⓒ 주장형 제목 → ⓓ QC 4축 → ⓔ design-skill → 완성 보고서.

상세 → `references/cascade-protocol.md`. 이력 → `CHANGELOG.md`.
