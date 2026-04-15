# deliverable-engine

> 🇺🇸 [English README](./README.md)

**모든 도메인스킬의 .md 산출물을 자동으로 구조화·포맷·QC하는 중앙 허브. 단독 작성도 관장.**

## 사전 요구

- **Claude Cowork 또는 Claude Code** 환경
- 권장: [design-skill](https://github.com/jasonnamii/design-skill) (시각문법 cascade)

## 목표

일반 LLM 문서의 고질적 문제 — 결론이 끝에 묻히고, 밀도가 처음부터 끝까지 균질하고, 축별 나열이 사전식으로 이어지는 구조. 이 엔진은 모든 .md 출력을 가로채서 모래시계 구조(결론 먼저→spine→세부 확장)로 재배치하고, 블록 간 밀도를 의도적으로 교대 배치한다. 읽는 사람이 발굴하는 게 아니라, 메시지가 설치되는 문서를 만든다.

## 사용 시점 & 방법

어떤 스킬이든 .md 파일을 생성하면 자동 발동 — 명시적 호출 불필요. 대화 중 문서화 의도가 감지되면("1% 게이트") 선제적으로 문서 전환을 제안한다. 직접 사용시 "보고서로", "진단서로", "리포트로" 같은 포맷 키워드를 포함하면 즉시 진입.

## 사용 사례

| 상황 | 프롬프트 | 동작 |
|---|---|---|
| biz-skill 전략 보고서 | `"전략 진단해줘, 보고서로"` | biz-skill 18축 분석 → 산출물 엔진이 서사 엮기 + 밀도 교대로 변환 |
| 간단한 내부 메모 | `"회의 내용 정리해줘"` | 내부/짧음 → 패스스루 티어 (최소 오버헤드) |
| 팀 공유용 분석 리포트 | `"팀한테 공유할 분석 리포트 만들어줘"` | 외부 + 긴 문서 → 풀 파이프라인 (모래시계 + 블록설계 + QC 4축 + 디자인) |

## 주요 기능

- **3티어 게이트** — 용도(외부/내부) × 길이(20/50행) 매트릭스로 풀/경량/패스스루 자동 분기
- **모래시계 구조 (§2)** — 역피라미드(결론 먼저) → spine(최고 밀도) → 피라미드(세부 확장). spine에 종속되지 않는 내용은 삭제
- **블록설계 7규칙 (§3)** — 밀도 교대(고/중/저), 블록 간 전환장치 강제, 1블록1목적
- **spine 추출 폴백** — 추출 실패(순수 데이터, 리스트, 다중 동등 결론) 시 참조형 문서로 자동 분류
- **티어별 QC** — 풀: 4축 전수(숫자·논리·문체·블록정합). 경량: 숫자+VOCAB만. 패스스루: 스킵
- **Cascade 아키텍처** — Interceptor 패턴. 분석 로직 불간섭, 출력 형태만 변환

## 연동 스킬

- **[design-skill](https://github.com/jasonnamii/design-skill)** — 시각문법·포맷팅 (디자인 단일 권위)
- **[biz-skill](https://github.com/jasonnamii/biz-skill)** — 18축 전략 출력 → 서사 재구성
- **[risk-radar](https://github.com/jasonnamii/risk-radar)** — 리스크 매트릭스 → 밀도 교대 블록
- **[research-frame](https://github.com/jasonnamii/research-frame)** — 축별 리서치 → 통합 산출물
- **[trigger-dictionary](https://github.com/jasonnamii/trigger-dictionary)** — 제출청소 (외부 제출 전 정제)

## 설치

```bash
git clone https://github.com/jasonnamii/deliverable-engine.git ~/.claude/skills/deliverable-engine
```

## 업데이트

```bash
cd ~/.claude/skills/deliverable-engine && git pull
```

`~/.claude/skills/`에 배치된 스킬은 Claude Code 및 Cowork 세션에서 자동으로 사용 가능합니다.

## Cowork Skills

25개 이상의 커스텀 스킬 중 하나입니다. 전체 카탈로그: [github.com/jasonnamii/cowork-skills](https://github.com/jasonnamii/cowork-skills)

## 라이선스

MIT License — 자유롭게 사용, 수정, 공유 가능합니다.
