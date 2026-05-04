# 🚨 MUST cascade → shaper-skill (절대규칙)

> **다이어트 v2 정본**: 20개 스킬 verbatim 박제 → 1줄 포인터 치환. 효과 100% 유지·토큰 ~8KB 절감.

---

## 절대규칙

이 cascade를 발동한 스킬의 **모든 리포트·산출물 = shaper-skill 허브 MUST 경유**. 단독 md/html 출력 = FAIL.

## 진입점

모드별 분석 완료 후, 산출물 생성 직전 shaper-skill 발동.

## shaper-skill 책임

MODE_S/M/L · NYT구조 · 3패스삭제 · 4항밀도QC · design-skill cascade 강제.

## DEFAULT_RENDER = 순수 마크다운

`.md` 산출 시 `<div>`·`<span>`·`style=` 등 인라인 HTML **전면 금지**. 헤더·불릿·표·인용(`>`)·이모지만 허용.

## 예외 (HTML 발동 조건)

사용자가 `"HTML로"·"박스로"·"벤또로"·"시각화"·"카드로"` **명시 시에만** html-div-style·apple-canvas·apple-box-design cascade 경유.

## 위반 감지

md 파일에 `<div style>`·`<span style>` 삽입 = 절대규칙 위반 → 재작성.

---

## 호출 패턴 (각 SKILL.md에 1줄 포인터)

```markdown
## 🚨 MUST cascade → shaper-skill
이 스킬의 모든 산출물 = shaper-skill 허브 MUST 경유. → `shaper-skill/references/_common/cascade-must.md`
```
