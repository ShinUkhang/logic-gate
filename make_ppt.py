# -*- coding: utf-8 -*-
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 와이드스크린 비율 설정
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # 색상 팔레트
    NAVY = RGBColor(15, 23, 42)        # #0f172a
    DARK_BLUE = RGBColor(30, 58, 138)   # #1e3a8a
    ACCENT_BLUE = RGBColor(37, 99, 235) # #2563eb
    LIGHT_BG = RGBColor(248, 250, 252)  # #f8fafc
    CARD_BG = RGBColor(255, 255, 255)
    TEXT_DARK = RGBColor(30, 41, 59)    # #1e293b
    TEXT_MUTED = RGBColor(100, 116, 139)# #64748b
    WHITE = RGBColor(255, 255, 255)
    BORDER_COLOR = RGBColor(226, 232, 240)
    HIGHLIGHT_GOLD = RGBColor(217, 119, 6) # #d97706

    blank_slide_layout = prs.slide_layouts[6]

    def add_header(slide, title_text, category_text="고1 아카데미아 | 집합과 명제 & AI"):
        # 상단 카테고리 태그
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_BLUE
        p_cat.font.name = "맑은 고딕"

        # 메인 제목
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.8))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = NAVY
        p_title.font.name = "맑은 고딕"

    def add_card(slide, left, top, width, height, title="", bg_color=CARD_BG, border_color=BORDER_COLOR):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.5)
        
        if title:
            tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), width - Inches(0.4), Inches(0.4))
            tf = tb.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = title
            p.font.size = Pt(14)
            p.font.bold = True
            p.font.color.rgb = DARK_BLUE
            p.font.name = "맑은 고딕"
        return shape

    # ==========================================================
    # Slide 1: 표지
    # ==========================================================
    s1 = prs.slides.add_slide(blank_slide_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = NAVY
    bg1.line.fill.background()

    tb1 = s1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(11), Inches(3.8))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    
    p = tf1.paragraphs[0]
    p.text = "고등학교 1학년 수학 융합 아카데미아"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = RGBColor(147, 197, 253)
    p.font.name = "맑은 고딕"

    p2 = tf1.add_paragraph()
    p2.text = "수학적 논리에서 인공지능까지"
    p2.font.size = Pt(36)
    p2.font.bold = True
    p2.font.color.rgb = WHITE
    p2.font.name = "맑은 고딕"
    p2.space_before = Pt(12)

    p3 = tf1.add_paragraph()
    p3.text = ": 집합과 명제로 이해하는 컴퓨터 연산과 퍼셉트론(Perceptron)"
    p3.font.size = Pt(22)
    p3.font.color.rgb = RGBColor(226, 232, 240)
    p3.font.name = "맑은 고딕"
    p3.space_before = Pt(8)

    p4 = tf1.add_paragraph()
    p4.text = "■ 1~2차시 강의  |  ■ 3차시 파이썬 IDLE 실습  |  ■ 4차시 세특 연계 보고서 작성"
    p4.font.size = Pt(14)
    p4.font.color.rgb = RGBColor(253, 224, 71)
    p4.font.name = "맑은 고딕"
    p4.space_before = Pt(28)

    # ==========================================================
    # Slide 2: 컴퓨터는 어떻게 생각할까?
    # ==========================================================
    s2 = prs.slides.add_slide(blank_slide_layout)
    add_header(s2, "1. 생각 열기 : 컴퓨터는 어떻게 생각할까?")

    add_card(s2, Inches(0.8), Inches(1.6), Inches(3.6), Inches(5.0), "기계의 물리적 신호")
    tb = s2.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(3.2), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• 전압이 높음 (High, 5V) → 1\n• 전압이 낮음 (Low, 0V) → 0\n\n컴퓨터의 본체는 전기가 통하느냐 안 통하느냐만을 구분하는 수억 개의 스위치(트랜지스터)입니다."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_DARK
    p.font.name = "맑은 고딕"

    add_card(s2, Inches(4.8), Inches(1.6), Inches(3.6), Inches(5.0), "인간의 논리적 사고")
    tb = s2.shapes.add_textbox(Inches(5.0), Inches(2.2), Inches(3.2), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• 참 (True) : 명제가 사실임\n• 거짓 (False) : 명제가 사실 아님\n\n인간은 명제와 조건을 조합하여 논리적 추론과 의사결정을 내립니다."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_DARK
    p.font.name = "맑은 고딕"

    add_card(s2, Inches(8.8), Inches(1.6), Inches(3.7), Inches(5.0), "조지 불의 혁신 (1854)", bg_color=RGBColor(239, 246, 255))
    tb = s2.shapes.add_textbox(Inches(9.0), Inches(2.2), Inches(3.3), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "★ 불리언 대수 (Boolean Algebra)\n\n'참/거짓'을 '1과 0'에 대응시켜 인간의 사고 과정을 수학적 방정식으로 완벽히 표현함!\n\n→ 현대 컴퓨터 공학과 인공지능의 시발점"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    p.font.name = "맑은 고딕"

    # ==========================================================
    # Slide 3: 명제와 불리언 대수
    # ==========================================================
    s3 = prs.slides.add_slide(blank_slide_layout)
    add_header(s3, "2. 명제(Proposition)와 Boolean 자료형")

    add_card(s3, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.0), "수학에서의 명제 (공통수학2)")
    tb = s3.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(5.2), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "■ 정의: 참(True) 또는 거짓(False)을 명확하게 판별할 수 있는 문장이나 식\n\n[예시 분석]\n• '4는 짝수이다.' → 참인 명제 (True, 1)\n• '3은 5보다 크다.' → 거짓인 명제 (False, 0)\n• 'x는 큰 수이다.' → 명제가 아님 (기준 모호)\n• 'x + 1 = 3' → 조건 (x 값에 따라 참/거짓 결정)"
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_DARK
    p.font.name = "맑은 고딕"

    add_card(s3, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.0), "컴퓨터 과학 & 파이썬에서의 불(bool)")
    tb = s3.shapes.add_textbox(Inches(7.0), Inches(2.2), Inches(5.3), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "■ Python의 bool 타입\n• True (정수 1로 취급)\n• False (정수 0으로 취급)\n\n[코드 매핑]\n>>> is_even = (4 % 2 == 0) # True\n>>> is_greater = (3 > 5)   # False\n>>> print(int(True))       # 1 출력\n>>> print(int(False))      # 0 출력"
    p.font.size = Pt(13)
    p.font.color.rgb = DARK_BLUE
    p.font.name = "맑은 고딕"

    # ==========================================================
    # Slide 4: 조건과 진리집합
    # ==========================================================
    s4 = prs.slides.add_slide(blank_slide_layout)
    add_header(s4, "3. 조건(Condition)과 진리집합(Truth Set)")

    add_card(s4, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.0), "조건을 집합으로 번역하는 핵심 개념")
    tb = s4.shapes.add_textbox(Inches(1.1), Inches(2.2), Inches(11.1), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "■ 진리집합의 정의\n   전체집합 U의 원소 중에서 조건 p(x)를 참(True)이 되게 하는 모든 원소의 집합 P\n   P = { x ∈ U | p(x) 는 참 }\n\n■ 실습 예시\n   전체집합 U = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }\n   • 조건 p(x) : 'x는 12의 약수이다'  →  진리집합 P = { 1, 2, 3, 4, 6 }\n   • 조건 q(x) : 'x는 짝수이다'       →  진리집합 Q = { 2, 4, 6, 8, 10 }\n\n★ 파이썬 컴프리헨션(Set Comprehension)과의 일치:\n   P = {x for x in U if 12 % x == 0}"
    p.font.size = Pt(13.5)
    p.font.color.rgb = TEXT_DARK
    p.font.name = "맑은 고딕"

    # ==========================================================
    # Slide 5: 명제 결합과 집합 연산
    # ==========================================================
    s5 = prs.slides.add_slide(blank_slide_layout)
    add_header(s5, "4. 명제의 결합과 집합 연산의 1:1 대응")

    add_card(s5, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.0), "수학과 정보 교과의 기호 대응표")
    
    rows, cols = 5, 4
    table_shape = s5.shapes.add_table(rows, cols, Inches(1.1), Inches(2.3), Inches(11.1), Inches(3.8))
    table = table_shape.table
    
    headers = ["명제 논리 연산", "수학 기호", "집합 연산 (진리집합)", "파이썬 연산자"]
    data = [
        ["논리곱 (그리고, AND)", "p ∧ q", "P ∩ Q (교집합)", "p and q  또는  P & Q"],
        ["논리합 (또는, OR)", "p ∨ q", "P ∪ Q (합집합)", "p or q   또는  P | Q"],
        ["부정 (Not)", "~p", "P^c (여집합: U - P)", "not p    또는  U - P"],
        ["배타적 논리합 (XOR)", "p ⊕ q", "(P - Q) ∪ (Q - P) (대칭차집합)", "p ^ q    또는  P ^ Q"]
    ]
    for c, h in enumerate(headers):
        cell = table.cell(0, c)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = DARK_BLUE
        for p in cell.text_frame.paragraphs:
            p.font.size = Pt(12)
            p.font.bold = True
            p.font.color.rgb = WHITE
            p.font.name = "맑은 고딕"

    for r, row in enumerate(data):
        for c, val in enumerate(row):
            cell = table.cell(r + 1, c)
            cell.text = val
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(241, 245, 249) if r % 2 == 0 else WHITE
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(11.5)
                p.font.color.rgb = TEXT_DARK
                p.font.name = "맑은 고딕"

    # ==========================================================
    # Slide 6: 드모르간 법칙
    # ==========================================================
    s6 = prs.slides.add_slide(blank_slide_layout)
    add_header(s6, "5. 수학의 정리: 드모르간 법칙 (De Morgan's Laws)")

    add_card(s6, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.0), "수학 공식 (집합 & 명제)")
    tb = s6.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(5.2), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "■ 집합에서의 드모르간 법칙\n1) (A ∪ B)^c = A^c ∩ B^c\n2) (A ∩ B)^c = A^c ∪ B^c\n\n■ 명제 논리에서의 드모르간 법칙\n1) ~(p ∨ q) ≡ ~p ∧ ~q\n2) ~(p ∧ q) ≡ ~p ∨ ~q\n\n'합집합의 여집합은 여집합의 교집합과 같다!'"
    p.font.size = Pt(13.5)
    p.font.color.rgb = TEXT_DARK
    p.font.name = "맑은 고딕"

    add_card(s6, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.0), "컴퓨터 회로에서의 의미 (비용 절감)")
    tb = s6.shapes.add_textbox(Inches(7.0), Inches(2.2), Inches(5.3), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "■ 디지털 하드웨어 최적화\n• AND 회로와 OR 회로를 각각 따로 만들 필요 없이, 단 하나의 만능 게이트(NAND)로 모두 변환 가능!\n\n■ 드모르간 법칙의 하드웨어 표현:\n   NAND 게이트 ≡ 입력이 반전된 OR 회로\n   NOR 게이트  ≡ 입력이 반전된 AND 회로\n\n→ 반도체 칩 면적과 제조 비용을 획기적으로 감축!"
    p.font.size = Pt(13)
    p.font.color.rgb = DARK_BLUE
    p.font.name = "맑은 고딕"

    # ==========================================================
    # Slide 7: 명제 p -> q와 진리집합 포함관계
    # ==========================================================
    s7 = prs.slides.add_slide(blank_slide_layout)
    add_header(s7, "6. 명제 p → q의 참·거짓과 진리집합의 포함관계")

    add_card(s7, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.0), "참인 명제 : P ⊆ Q", bg_color=RGBColor(240, 253, 244))
    tb = s7.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(5.2), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "■ 명제 p → q가 참(True)일 조건:\n   조건 p의 진리집합 P가 조건 q의 진리집합 Q에 완전히 포함될 때 (P ⊆ Q)\n\n[예시]\n• p: x는 4의 배수 (P = {4, 8, 12, ...})\n• q: x는 2의 배수 (Q = {2, 4, 6, 8, 10, 12, ...})\n→ P ⊆ Q 이므로 'x가 4의 배수이면 x는 2의 배수이다'는 참!"
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_DARK
    p.font.name = "맑은 고딕"

    add_card(s7, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.0), "거짓인 명제 : P ⊄ Q (반례의 존재)", bg_color=RGBColor(254, 242, 242))
    tb = s7.shapes.add_textbox(Inches(7.0), Inches(2.2), Inches(5.3), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "■ 명제 p → q가 거짓(False)일 조건:\n   P의 원소 중 Q에 속하지 않는 원소가 단 하나라도 존재할 때 (P - Q ≠ ∅)\n\n★ 반례 (Counterexample):\n   x ∈ P 이지만 x ∉ Q 인 원소 x\n\n[예시]\n• 'x가 2의 배수이면 x는 4의 배수이다'의 반례: x = 2, 6, 10..."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_DARK
    p.font.name = "맑은 고딕"

    # ==========================================================
    # Slide 8: 역, 이, 대우와 대우증명법
    # ==========================================================
    s8 = prs.slides.add_slide(blank_slide_layout)
    add_header(s8, "7. 명제의 역·이·대우와 대우증명법의 원리")

    add_card(s8, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.0), "명제 간의 관계와 논리적 동치성")
    tb = s8.shapes.add_textbox(Inches(1.1), Inches(2.2), Inches(11.1), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "■ 명제의 변형\n   • 원명제: p → q\n   • 역 (Converse): q → p\n   • 대우 (Contrapositive): ~q → ~p\n\n■ 대우의 핵심 성질: '원명제와 대우는 참·거짓이 항상 일치한다!'\n   [수학적 증명 via 집합론]\n   P ⊆ Q  ⟺  Q^c ⊆ P^c\n\n★ 대우증명법의 활용:\n   직접 증명하기 까다로운 명제(예: 'n^2이 짝수이면 n도 짝수이다')를\n   대우('n이 홀수이면 n^2도 홀수이다')로 바꾸어 아주 쉽게 증명!"
    p.font.size = Pt(13.5)
    p.font.color.rgb = TEXT_DARK
    p.font.name = "맑은 고딕"

    # ==========================================================
    # Slide 9: 필요조건과 충분조건
    # ==========================================================
    s9 = prs.slides.add_slide(blank_slide_layout)
    add_header(s9, "8. 필요조건과 충분조건의 직관적/수학적 판별")

    add_card(s9, Inches(0.8), Inches(1.6), Inches(3.6), Inches(5.0), "충분조건 (Sufficient)")
    tb = s9.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(3.2), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• 기호: p ⟹ q (P ⊆ Q)\n• 의미: p이기만 하면 q가 되기에 '충분'함\n• 주어 p는 더 작은(구체적인) 집합\n\n예: '정삼각형'은 '이등변삼각형'이기 위한 충분조건"
    p.font.size = Pt(12.5)
    p.font.color.rgb = TEXT_DARK
    p.font.name = "맑은 고딕"

    add_card(s9, Inches(4.8), Inches(1.6), Inches(3.6), Inches(5.0), "필요조건 (Necessary)")
    tb = s9.shapes.add_textbox(Inches(5.0), Inches(2.2), Inches(3.2), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• 기호: q ⟹ p (Q ⊆ P)\n• 의미: p가 되기 위해 q는 '반드시 필요'한 바탕\n• 주어 p는 더 큰(포괄적인) 집합\n\n예: '이등변삼각형'은 '정삼각형'이기 위한 필요조건"
    p.font.size = Pt(12.5)
    p.font.color.rgb = TEXT_DARK
    p.font.name = "맑은 고딕"

    add_card(s9, Inches(8.8), Inches(1.6), Inches(3.7), Inches(5.0), "필요충분조건 (Equivalent)", bg_color=RGBColor(239, 246, 255))
    tb = s9.shapes.add_textbox(Inches(9.0), Inches(2.2), Inches(3.3), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• 기호: p ⟺ q (P = Q)\n• 의미: 두 조건이 완전히 동치\n• 서로가 서로에게 필요하면서 충분함\n\n예: 'x = 2'와 '2x - 4 = 0'은 필요충분조건"
    p.font.size = Pt(12.5)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    p.font.name = "맑은 고딕"

    # ==========================================================
    # Slide 10: 인공지능의 시초 퍼셉트론
    # ==========================================================
    s10 = prs.slides.add_slide(blank_slide_layout)
    add_header(s10, "9. 인공지능의 시초: 퍼셉트론(Perceptron)의 수리 모델")

    add_card(s10, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.0), "퍼셉트론의 구조 (1958, 프랑크 로젠블랫)")
    tb = s10.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(5.2), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "■ 뇌의 뉴런을 모방한 인공신경망의 기본 단위\n• 입력 신호: x1, x2 (0 또는 1)\n• 가중치(Weight): w1, w2 (입력의 중요도)\n• 편향(Bias): b (뉴런의 활성화 임계값)\n\n■ 총 입력합 계산:\n   z = w1*x1 + w2*x2 + b"
    p.font.size = Pt(13.5)
    p.font.color.rgb = TEXT_DARK
    p.font.name = "맑은 고딕"

    add_card(s10, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.0), "활성화 함수 (Step Function)")
    tb = s10.shapes.add_textbox(Inches(7.0), Inches(2.2), Inches(5.3), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "■ 계단 함수 (Step Function)\n   y = 1  (z >= 0 일 때 : 참/발화)\n   y = 0  (z < 0 일 때 : 거짓/침묵)\n\n★ 고1 수학과의 연결고리:\n   w1*x1 + w2*x2 + b = 0 은\n   좌표평면 위의 '직선의 방정식'!\n   퍼셉트론은 평면을 직선으로 양분하는 결정경계(Decision Boundary) 모델입니다."
    p.font.size = Pt(13)
    p.font.color.rgb = DARK_BLUE
    p.font.name = "맑은 고딕"

    # ==========================================================
    # Slide 11: 퍼셉트론으로 AND/OR 구현
    # ==========================================================
    s11 = prs.slides.add_slide(blank_slide_layout)
    add_header(s11, "10. 단층 퍼셉트론으로 AND / OR 게이트 분리하기")

    add_card(s11, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.0), "AND 게이트의 직선의 방정식")
    tb = s11.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(5.2), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "■ 파라미터: w1 = 2, w2 = 2, b = -3\n■ 직선: 2*x1 + 2*x2 - 3 = 0\n\n[점 대입 판별]\n• (1, 1) → 2(1)+2(1)-3 = +1 >= 0 → 1 (빨강)\n• (1, 0) → 2(1)+2(0)-3 = -1 < 0  → 0 (파랑)\n• (0, 1) → 2(0)+2(1)-3 = -1 < 0  → 0 (파랑)\n• (0, 0) → 2(0)+2(0)-3 = -3 < 0  → 0 (파랑)\n\n→ (1,1)만 직선 위로 완벽 분리!"
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_DARK
    p.font.name = "맑은 고딕"

    add_card(s11, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.0), "OR 게이트의 직선의 방정식")
    tb = s11.shapes.add_textbox(Inches(7.0), Inches(2.2), Inches(5.3), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "■ 파라미터: w1 = 2, w2 = 2, b = -1\n■ 직선: 2*x1 + 2*x2 - 1 = 0\n\n[점 대입 판별]\n• (1, 1) → 2(1)+2(1)-1 = +3 >= 0 → 1 (빨강)\n• (1, 0) → 2(1)+2(0)-1 = +1 >= 0 → 1 (빨강)\n• (0, 1) → 2(0)+2(1)-1 = +1 >= 0 → 1 (빨강)\n• (0, 0) → 2(0)+2(0)-1 = -1 < 0  → 0 (파랑)\n\n→ (0,0)만 직선 아래로 완벽 분리!"
    p.font.size = Pt(13)
    p.font.color.rgb = DARK_BLUE
    p.font.name = "맑은 고딕"

    # ==========================================================
    # Slide 12: XOR 선형 분리 불가 문제
    # ==========================================================
    s12 = prs.slides.add_slide(blank_slide_layout)
    add_header(s12, "11. 인공지능의 첫 번째 암흑기: XOR 선형 분리 불가")

    add_card(s12, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.0), "XOR 문제의 수학적 모순 증명 (마빈 민스키, 1969)", bg_color=RGBColor(254, 242, 242))
    tb = s12.shapes.add_textbox(Inches(1.1), Inches(2.2), Inches(11.1), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "■ XOR 진리값: (0,0)→0, (1,1)→0   vs   (1,0)→1, (0,1)→1\n\n■ 4개의 연립부등식 형성:\n   1) (0, 0) 대입 : b < 0\n   2) (1, 0) 대입 : w1 + b >= 0  ⟹  w1 >= -b > 0\n   3) (0, 1) 대입 : w2 + b >= 0  ⟹  w2 >= -b > 0\n   4) (1, 1) 대입 : w1 + w2 + b < 0\n\n■ 모순 발생:\n   2)와 3)을 더하면 (w1 + w2) >= -2b\n   양변에 b를 더하면: w1 + w2 + b >= -b > 0  (모순! 4번 부등식과 정면 충돌!)\n\n★ 결론: 단 하나의 직선으로는 XOR 평면을 절대로 분리할 수 없다! (선형 분리 불가)"
    p.font.size = Pt(13.5)
    p.font.color.rgb = TEXT_DARK
    p.font.name = "맑은 고딕"

    # ==========================================================
    # Slide 13: 다층 퍼셉트론과 XOR 해결
    # ==========================================================
    s13 = prs.slides.add_slide(blank_slide_layout)
    add_header(s13, "12. 구원투수: 다층 퍼셉트론(MLP)과 논리 결합")

    add_card(s13, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.0), "XOR의 논리식 분해")
    tb = s13.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(5.2), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "■ 집합과 명제를 이용한 분해:\n   XOR(x1, x2) = (x1 ∨ x2) ∧ ~(x1 ∧ x2)\n               = OR(x1, x2) ∧ NAND(x1, x2)\n\n■ 2개 층의 인공신경망 구성:\n   • 은닉층 노드 1: s1 = NAND(x1, x2)\n   • 은닉층 노드 2: s2 = OR(x1, x2)\n   • 출력층 노드  : y  = AND(s1, s2)"
    p.font.size = Pt(13.5)
    p.font.color.rgb = TEXT_DARK
    p.font.name = "맑은 고딕"

    add_card(s13, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.0), "수학적 의미: 2개의 직선으로 비선형 영역 분할", bg_color=RGBColor(239, 246, 255))
    tb = s13.shapes.add_textbox(Inches(7.0), Inches(2.2), Inches(5.3), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "■ 층을 쌓으면 비선형 공간 분할이 가능!\n• 직선 1 (OR 경계선): (0,0)을 배제\n• 직선 2 (NAND 경계선): (1,1)을 배제\n• 두 직선 사이의 띠 모양 영역(교집합)에 (1,0)과 (0,1)만 남김!\n\n★ 이것이 바로 현대 '딥러닝(Deep Learning)'의 출발 원리입니다."
    p.font.size = Pt(13.5)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    p.font.name = "맑은 고딕"

    # ==========================================================
    # Slide 14: 3차시 파이썬 실습 안내
    # ==========================================================
    s14 = prs.slides.add_slide(blank_slide_layout)
    add_header(s14, "13. [3차시 예고] 파이썬 IDLE 실습 안내 (초보자 맞춤)")

    add_card(s14, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.0), "마우스 슬라이더로 조작하는 직관적인 시각화 실습 3종")
    tb = s14.shapes.add_textbox(Inches(1.1), Inches(2.2), Inches(11.1), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "■ 실습 1 : 파이썬 집합(Set) 연산과 드모르간 법칙 검증\n   → 복잡한 문법 없이 set 기호(&, |, -)만으로 직관적인 진리집합 연산 확인\n\n■ 실습 2 : 명제 진리표 생성기 & 필요·충분조건 판별\n   → 참/거짓 표를 직접 확인하고, 조건 간의 포함관계(P ⊆ Q)를 자동으로 판별\n\n■ 실습 3 : 🎮 인터랙티브 슬라이더 퍼셉트론 시뮬레이터 (핵심)\n   → 마우스로 w1, w2, b 슬라이더를 움직이며 직선이 회전/이동하는 과정을 실시간 관찰!\n   → AND, OR, NAND를 직접 맞춰보고, XOR의 선형 분리 불가와 다층 퍼셉트론의 해결을 눈으로 확인!\n\n★ 4차시에는 슬라이더 실습 결과를 바탕으로 세특 탐구보고서를 완성합니다."
    p.font.size = Pt(13.5)
    p.font.color.rgb = TEXT_DARK
    p.font.name = "맑은 고딕"

    # 파일 저장
    output_path = r"c:\Users\user\Desktop\DB\2026\1학년 아카데미아\02_강의PPT_집합과명제_컴퓨터논리와퍼셉트론.pptx"
    prs.save(output_path)
    print(f"PPT 생성 완료: {output_path}")

if __name__ == "__main__":
    create_deck()
