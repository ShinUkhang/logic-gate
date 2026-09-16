# -*- coding: utf-8 -*-
"""
===================================================================
[고1 아카데미아] 집합과 명제 - 파이썬 기초 실습 (3단계)
주제: 인공지능 퍼셉트론(Perceptron)과 슬라이더로 조절하는 1차 부등식 직선
실행 방법: IDLE 메뉴에서 Run -> Run Module (또는 키보드 F5)
특징: 표준 파이썬 Tkinter GUI 탑재 (슬라이더를 움직여 직선을 맞춰보세요!)
===================================================================
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import tkinter as tk
from tkinter import ttk

# ===================================================================
# 1. 가장 기초적인 퍼셉트론 함수 (단 5줄!)
# ===================================================================
def perceptron(x1, x2, w1, w2, b):
    """
    입력 x1, x2에 가중치 w1, w2를 곱하고 편향 b를 더한 값이
    0 이상이면 1(참), 0 미만이면 0(거짓)을 반환합니다.
    """
    z = w1 * x1 + w2 * x2 + b  # 직선의 방정식: w1*x1 + w2*x2 + b = 0
    if z >= 0:
        return 1
    else:
        return 0

print("=" * 65)
print("  [3단계 실습] 인공지능의 기초: 퍼셉트론과 직선의 방정식")
print("=" * 65)
print("\n1. AND 게이트 예시 계산 (w1=2, w2=2, b=-3):")

inputs = [(0, 0), (1, 0), (0, 1), (1, 1)]
for x1, x2 in inputs:
    out = perceptron(x1, x2, w1=2, w2=2, b=-3)
    print(f"  입력 ({x1}, {x2}) -> 퍼셉트론 출력: {out}")

print("\n2. 화면에 나타난 [인터랙티브 슬라이더 창]에서")
print("   w1, w2, b 슬라이더를 마우스로 움직여서 점들을 분류해보세요!")
print("=" * 65)


# ===================================================================
# 2. 인터랙티브 GUI 시각화 (슬라이더로 실시간 직선 조절)
# ===================================================================
def launch_interactive_gui():
    root = tk.Tk()
    root.title("[고1 아카데미아] 퍼셉트론 슬라이더 시각화 시뮬레이터")
    root.geometry("640x780")
    root.configure(bg="#f8fafc")

    # 상단 제목
    title_lbl = tk.Label(
        root, 
        text="🎮 퍼셉트론 슬라이더로 직선 맞춰보기", 
        font=("맑은 고딕", 15, "bold"),
        bg="#f8fafc", fg="#0f172a"
    )
    title_lbl.pack(pady=8)

    desc_lbl = tk.Label(
        root, 
        text="슬라이더(w1, w2, b)를 움직여 목표 게이트를 맞춰보세요!", 
        font=("맑은 고딕", 10),
        bg="#f8fafc", fg="#475569"
    )
    desc_lbl.pack(pady=2)

    # 캔버스 (좌표평면)
    canvas_size = 380
    canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="white", highlightthickness=1, highlightbackground="#cbd5e1")
    canvas.pack(pady=6)

    # 상태 표시 라벨
    status_frame = tk.Frame(root, bg="#f1f5f9", padx=10, pady=6)
    status_frame.pack(fill="x", padx=30, pady=4)

    eq_lbl = tk.Label(status_frame, text="", font=("Consolas", 11, "bold"), bg="#f1f5f9", fg="#1e3a8a")
    eq_lbl.pack()

    score_lbl = tk.Label(status_frame, text="", font=("맑은 고딕", 10, "bold"), bg="#f1f5f9", fg="#059669")
    score_lbl.pack(pady=2)

    # 목표 게이트 및 모드 변수
    target_mode = tk.StringVar(value="AND") # AND, OR, NAND, XOR, MLP

    # 목표값 정의
    targets = {
        "AND":  {(0, 0): 0, (1, 0): 0, (0, 1): 0, (1, 1): 1},
        "OR":   {(0, 0): 0, (1, 0): 1, (0, 1): 1, (1, 1): 1},
        "NAND": {(0, 0): 1, (1, 0): 1, (0, 1): 1, (1, 1): 0},
        "XOR":  {(0, 0): 0, (1, 0): 1, (0, 1): 1, (1, 1): 0}
    }

    # 좌표 변환 함수
    margin = 60
    scale = canvas_size - 2 * margin

    def to_canvas(x, y):
        cx = margin + x * scale
        cy = (canvas_size - margin) - y * scale
        return cx, cy

    def update_plot(*args):
        canvas.delete("all")
        mode = target_mode.get()
        current_target = targets[mode if mode != "MLP" else "XOR"]

        # 1. 축 및 모눈 그리기
        canvas.create_line(margin, canvas_size - margin, canvas_size - 25, canvas_size - margin, fill="#94a3b8", width=2, arrow=tk.LAST)
        canvas.create_line(margin, canvas_size - margin, margin, 25, fill="#94a3b8", width=2, arrow=tk.LAST)
        canvas.create_text(canvas_size - 15, canvas_size - margin + 15, text="x1", font=("맑은 고딕", 10, "bold"), fill="#475569")
        canvas.create_text(margin - 15, 15, text="x2", font=("맑은 고딕", 10, "bold"), fill="#475569")

        # 눈금 숫자
        for val in [0, 1]:
            cx, cy = to_canvas(val, 0)
            canvas.create_text(cx, canvas_size - margin + 15, text=str(val), font=("맑은 고딕", 9), fill="#64748b")
            cx, cy = to_canvas(0, val)
            canvas.create_text(margin - 15, cy, text=str(val), font=("맑은 고딕", 9), fill="#64748b")

        # 2. 다층 퍼셉트론 모드 특별 처리
        if mode == "MLP":
            # 2개의 점선 그리기 (OR 직선, NAND 직선)
            def draw_dashed_line(w1, w2, b, color):
                x_s, x_e = -0.3, 1.3
                y_s = (-w1 * x_s - b) / w2
                y_e = (-w1 * x_e - b) / w2
                c1 = to_canvas(x_s, y_s)
                c2 = to_canvas(x_e, y_e)
                canvas.create_line(c1[0], c1[1], c2[0], c2[1], fill=color, width=2, dash=(4, 4))

            draw_dashed_line(2.0, 2.0, -1.0, "#f59e0b") # OR선
            draw_dashed_line(-2.0, -2.0, 3.0, "#8b5cf6") # NAND선

            # 점 그리기
            for (px, py), target_val in current_target.items():
                cx, cy = to_canvas(px, py)
                # 다층 퍼셉트론 실제 계산
                s1 = perceptron(px, py, -2, -2, 3) # NAND
                s2 = perceptron(px, py, 2, 2, -1)  # OR
                pred = perceptron(s1, s2, 2, 2, -3) # AND
                
                color = "#ef4444" if pred == 1 else "#3b82f6"
                r = 13
                canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill=color, outline="#0f172a", width=2)
                canvas.create_text(cx, cy, text=str(pred), fill="white", font=("맑은 고딕", 10, "bold"))
                canvas.create_text(cx, cy - 20, text=f"({px},{py})", font=("맑은 고딕", 8, "bold"), fill="#334155")

            eq_lbl.config(text="[다층 퍼셉트론] 2개의 직선 사이(OR ∩ NAND) 영역으로 분리")
            score_lbl.config(text="★ XOR 완벽 해결! (정확도: 4/4 = 100%) ★", fg="#059669")
            return

        # 3. 단층 퍼셉트론 슬라이더 값 읽기
        w1 = round(scale_w1.get(), 1)
        w2 = round(scale_w2.get(), 1)
        b = round(scale_b.get(), 1)

        eq_lbl.config(text=f"현재 직선의 식: ({w1})·x1 + ({w2})·x2 + ({b}) = 0")

        # 직선 그리기
        if abs(w2) > 0.01:
            x_s, x_e = -0.3, 1.3
            y_s = (-w1 * x_s - b) / w2
            y_e = (-w1 * x_e - b) / w2
            c1 = to_canvas(x_s, y_s)
            c2 = to_canvas(x_e, y_e)
            canvas.create_line(c1[0], c1[1], c2[0], c2[1], fill="#10b981", width=3)
        elif abs(w1) > 0.01: # 수직선
            x_val = -b / w1
            c1 = to_canvas(x_val, -0.3)
            c2 = to_canvas(x_val, 1.3)
            canvas.create_line(c1[0], c1[1], c2[0], c2[1], fill="#10b981", width=3)

        # 점 그리기 & 정확도 계산
        correct_count = 0
        for (px, py), target_val in current_target.items():
            cx, cy = to_canvas(px, py)
            pred = perceptron(px, py, w1, w2, b)
            is_match = (pred == target_val)
            if is_match:
                correct_count += 1

            # 예측값에 따라 색상 결정 (1: 빨강, 0: 파랑)
            color = "#ef4444" if pred == 1 else "#3b82f6"
            r = 13
            # 정답 맞추면 굵은 테두리, 틀리면 점선 테두리
            outline_col = "#0f172a" if is_match else "#f97316"
            canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill=color, outline=outline_col, width=2)
            canvas.create_text(cx, cy, text=str(pred), fill="white", font=("맑은 고딕", 10, "bold"))
            canvas.create_text(cx, cy - 20, text=f"({px},{py}) 목표:{target_val}", font=("맑은 고딕", 8, "bold"), fill="#334155")

        # 점수 표시
        if correct_count == 4:
            score_lbl.config(text=f"🎉 [{mode} 게이트] 분류 성공! (정확도: 4/4 100%)", fg="#059669")
        else:
            if mode == "XOR":
                score_lbl.config(text=f"※ XOR은 1개의 직선으로 절대 4개를 다 맞출 수 없습니다! (현재 {correct_count}/4)", fg="#dc2626")
            else:
                score_lbl.config(text=f"🎯 목표 [{mode}]: {correct_count}/4 일치 (슬라이더를 더 조절해보세요)", fg="#d97706")

    # 슬라이더 컨트롤 프레임
    slider_frame = tk.LabelFrame(root, text=" 🎛 가중치와 편향 슬라이더 ", font=("맑은 고딕", 10, "bold"), bg="#f8fafc", fg="#334155", padx=15, pady=6)
    slider_frame.pack(fill="x", padx=25, pady=4)

    # w1 슬라이더
    row1 = tk.Frame(slider_frame, bg="#f8fafc")
    row1.pack(fill="x", pady=2)
    tk.Label(row1, text="가중치 w1 :", width=10, font=("맑은 고딕", 9, "bold"), bg="#f8fafc").pack(side="left")
    scale_w1 = tk.Scale(row1, from_=-3.0, to=3.0, resolution=0.1, orient="horizontal", command=update_plot, bg="#f8fafc", highlightthickness=0)
    scale_w1.set(2.0)
    scale_w1.pack(side="left", fill="x", expand=True)

    # w2 슬라이더
    row2 = tk.Frame(slider_frame, bg="#f8fafc")
    row2.pack(fill="x", pady=2)
    tk.Label(row2, text="가중치 w2 :", width=10, font=("맑은 고딕", 9, "bold"), bg="#f8fafc").pack(side="left")
    scale_w2 = tk.Scale(row2, from_=-3.0, to=3.0, resolution=0.1, orient="horizontal", command=update_plot, bg="#f8fafc", highlightthickness=0)
    scale_w2.set(2.0)
    scale_w2.pack(side="left", fill="x", expand=True)

    # b 슬라이더
    row3 = tk.Frame(slider_frame, bg="#f8fafc")
    row3.pack(fill="x", pady=2)
    tk.Label(row3, text="편향 b   :", width=10, font=("맑은 고딕", 9, "bold"), bg="#f8fafc").pack(side="left")
    scale_b = tk.Scale(row3, from_=-4.0, to=4.0, resolution=0.1, orient="horizontal", command=update_plot, bg="#f8fafc", highlightthickness=0)
    scale_b.set(-3.0)
    scale_b.pack(side="left", fill="x", expand=True)

    # 게이트 선택 버튼들
    btn_frame = tk.Frame(root, bg="#f8fafc")
    btn_frame.pack(pady=6)

    def set_mode(m, w1_v, w2_v, b_v):
        target_mode.set(m)
        if m != "MLP":
            scale_w1.set(w1_v)
            scale_w2.set(w2_v)
            scale_b.set(b_v)
        update_plot()

    btn_opt = {"font": ("맑은 고딕", 9, "bold"), "padx": 6, "pady": 3}
    tk.Button(btn_frame, text="AND 맞추기", bg="#e2e8f0", command=lambda: set_mode("AND", 2.0, 2.0, -3.0), **btn_opt).grid(row=0, column=0, padx=3)
    tk.Button(btn_frame, text="OR 맞추기", bg="#e2e8f0", command=lambda: set_mode("OR", 2.0, 2.0, -1.0), **btn_opt).grid(row=0, column=1, padx=3)
    tk.Button(btn_frame, text="NAND 맞추기", bg="#e2e8f0", command=lambda: set_mode("NAND", -2.0, -2.0, 3.0), **btn_opt).grid(row=0, column=2, padx=3)
    tk.Button(btn_frame, text="XOR 도전(불가체험)", bg="#fee2e2", fg="#b91c1c", command=lambda: set_mode("XOR", 1.0, 1.0, -1.0), **btn_opt).grid(row=0, column=3, padx=3)
    tk.Button(btn_frame, text="XOR 해결(다층)", bg="#fef08a", fg="#854d0e", command=lambda: set_mode("MLP", 0, 0, 0), **btn_opt).grid(row=0, column=4, padx=3)

    # 초기 화면 렌더링
    update_plot()
    root.mainloop()

if __name__ == "__main__":
    launch_interactive_gui()
