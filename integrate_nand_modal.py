# -*- coding: utf-8 -*-
with open(r"c:\Users\user\Desktop\DB\2026\1학년 아카데미아\[출력용]고1_집합과명제_AI퍼셉트론_워크북_4페이지.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. 툴바 버튼 추가
old_toolbar = """    <h2>📚 [고1 아카데미아] 집합과 명제 & AI 퍼셉트론 4차시 워크북 (총 4페이지 완결)</h2>
    <button class="print-btn" onclick="window.print()">
      🖨️ 인쇄하기 / PDF로 저장
    </button>"""

new_toolbar = """    <h2>📚 [고1 아카데미아] 집합과 명제 & AI 퍼셉트론 4차시 워크북 (총 4페이지 완결)</h2>
    <div class="toolbar-actions">
      <button class="sim-btn" onclick="openNandModal()">
        ⚡ NAND 실습 시뮬레이터 열기
      </button>
      <button class="print-btn" onclick="window.print()">
        🖨️ 인쇄하기 / PDF로 저장
      </button>
    </div>"""

html = html.replace(old_toolbar, new_toolbar)

# 2. 2페이지 활동 2 제목에 시뮬레이터 열기 버튼 추가
old_act2 = """<div class="section-title">⚡ [활동 2] 반도체의 기적: NAND 게이트 하나로 모든 연산 처리하기</div>"""
new_act2 = """<div class="section-title" style="justify-content: space-between;">
          <span>⚡ [활동 2] 반도체의 기적: NAND 게이트 하나로 모든 연산 처리하기</span>
          <button class="sim-btn" onclick="openNandModal()" style="font-size: 10px; padding: 2px 8px; height: 22px;">
            🎮 화면에서 시뮬레이터 직접 조작하기 (클릭)
          </button>
        </div>"""

html = html.replace(old_act2, new_act2)

# 3. CSS에 모달 및 시뮬레이터 스타일 추가
modal_css = """
    /* ==========================================================================
       NAND 시뮬레이터 모달 팝업 스타일
       ========================================================================== */
    .modal-overlay {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(4px);
      z-index: 2000;
      justify-content: center;
      align-items: center;
      padding: 15px;
    }
    .modal-overlay.active {
      display: flex;
    }
    .modal-card {
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 16px;
      width: 100%;
      max-width: 820px;
      color: #f8fafc;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
      padding: 20px;
      position: relative;
      max-height: 94vh;
      overflow-y: auto;
    }
    .modal-close-btn {
      position: absolute;
      top: 14px;
      right: 18px;
      background: #334155;
      color: #cbd5e1;
      border: none;
      width: 28px;
      height: 28px;
      border-radius: 50%;
      font-size: 14px;
      font-weight: bold;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.2s;
    }
    .modal-close-btn:hover {
      background: #ef4444;
      color: white;
    }
    .sim-mode-btn {
      padding: 6px 14px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: bold;
      cursor: pointer;
      border: 1px solid #334155;
      background: #1e293b;
      color: #94a3b8;
      transition: all 0.2s;
    }
    .sim-mode-btn.active {
      background: #0284c7;
      color: white;
      border-color: #38bdf8;
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.4);
    }
    .sim-input-btn {
      width: 44px;
      height: 44px;
      border-radius: 10px;
      font-size: 18px;
      font-weight: bold;
      font-family: monospace;
      cursor: pointer;
      border: 2px solid #475569;
      background: #1e293b;
      color: #94a3b8;
      transition: all 0.2s;
    }
    .sim-input-btn.on {
      background: #10b981;
      color: white;
      border-color: #34d399;
      box-shadow: 0 0 14px rgba(16, 185, 129, 0.5);
    }
    .wire-active {
      background-color: #38bdf8 !important;
      box-shadow: 0 0 10px #38bdf8, 0 0 3px #0284c7;
    }
    .wire-inactive {
      background-color: #334155 !important;
      box-shadow: none;
    }
    .gate-box {
      background: #1e293b;
      border: 1.5px solid #475569;
      border-radius: 10px;
      padding: 8px 12px;
      text-align: center;
      min-width: 90px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.3);
      transition: all 0.2s;
    }
    .gate-active {
      border-color: #38bdf8 !important;
      box-shadow: 0 0 14px rgba(56, 189, 248, 0.4);
    }
    @media print {
      .modal-overlay {
        display: none !important;
      }
    }
"""

html = html.replace("/* 인쇄 시 스타일 */", modal_css + "\n    /* 인쇄 시 스타일 */")

# 4. 모달 HTML 구조 및 스크립트 추가 (body 닫히기 직전)
modal_html_and_js = """
  <!-- ==========================================================================
       NAND 범용 게이트 인터랙티브 시뮬레이터 모달
       ========================================================================== -->
  <div id="nand-modal" class="modal-overlay" onclick="handleOverlayClick(event)">
    <div class="modal-card" onclick="event.stopPropagation()">
      <button class="modal-close-btn" onclick="closeNandModal()" title="닫기">✕</button>
      
      <div style="display:flex; align-items:center; gap:8px; margin-bottom:14px; border-bottom:1px solid #334155; padding-bottom:10px;">
        <span style="font-size:20px;">⚡</span>
        <h3 style="margin:0; font-size:16px; font-weight:bold; color:#38bdf8;">
          NAND 범용 게이트 대화형 시뮬레이터
        </h3>
        <span style="font-size:11px; background:#1e293b; color:#94a3b8; padding:2px 8px; border-radius:4px; border:1px solid #334155;">
          교재 연계 인터랙티브 실습
        </span>
      </div>

      <!-- 모드 선택 버튼들 -->
      <div style="display:flex; gap:8px; justify-content:center; margin-bottom:16px; flex-wrap:wrap;">
        <button id="btn-mode-not" class="sim-mode-btn active" onclick="setNandMode('NOT')">[NOT] 게이트 (NAND 1개)</button>
        <button id="btn-mode-and" class="sim-mode-btn" onclick="setNandMode('AND')">[AND] 게이트 (NAND 2개)</button>
        <button id="btn-mode-or" class="sim-mode-btn" onclick="setNandMode('OR')">[OR] 게이트 (NAND 3개)</button>
        <button id="btn-mode-xor" class="sim-mode-btn" onclick="setNandMode('XOR')">[XOR] 게이트 (NAND 4개)</button>
      </div>

      <!-- 입력 버튼 및 출력 표시 컨트롤러 -->
      <div style="background:#020617; border:1px solid #1e293b; border-radius:12px; padding:12px 18px; margin-bottom:16px; display:flex; justify-content:space-between; align-items:center;">
        <div style="display:flex; align-items:center; gap:16px;">
          <div style="display:flex; align-items:center; gap:8px;">
            <span style="font-size:12px; font-weight:bold; color:#94a3b8;">입력 A :</span>
            <button id="sim-btn-a" class="sim-input-btn" onclick="toggleSimInput('A')">0</button>
          </div>
          <div id="sim-container-b" style="display:flex; align-items:center; gap:8px;">
            <span style="font-size:12px; font-weight:bold; color:#94a3b8;">입력 B :</span>
            <button id="sim-btn-b" class="sim-input-btn" onclick="toggleSimInput('B')">0</button>
          </div>
        </div>

        <div style="display:flex; align-items:center; gap:10px; border-left:1px solid #1e293b; padding-left:16px;">
          <span style="font-size:12px; font-weight:bold; color:#94a3b8;">최종 출력 (Output) :</span>
          <div id="sim-output-badge" style="width:44px; height:44px; border-radius:10px; background:#1e293b; color:#38bdf8; font-size:20px; font-weight:bold; font-family:monospace; display:flex; align-items:center; justify-content:center; border:2px solid #38bdf8; box-shadow:0 0 12px rgba(56, 189, 248, 0.4);">
            1
          </div>
        </div>
      </div>

      <!-- 회로 애니메이션 다이어그램 뷰 -->
      <div style="background:#020617; border:1px solid #1e293b; border-radius:12px; padding:18px; min-height:160px; display:flex; justify-content:center; align-items:center; overflow-x:auto; margin-bottom:14px;">
        <div id="sim-circuit-diagram" style="width:100%; display:flex; justify-content:center; align-items:center;"></div>
      </div>

      <!-- 하단 설명 및 진리표 -->
      <div style="display:grid; grid-template-columns: 2fr 1fr; gap:14px;">
        <div style="background:#020617; border:1px solid #1e293b; border-radius:10px; padding:12px; font-size:12px;">
          <div style="color:#38bdf8; font-weight:bold; margin-bottom:4px;">📌 수학적 동작 원리</div>
          <div id="sim-explanation" style="color:#cbd5e1; line-height:1.5;"></div>
        </div>
        <div style="background:#020617; border:1px solid #1e293b; border-radius:10px; padding:12px;">
          <div style="color:#94a3b8; font-size:11px; font-weight:bold; margin-bottom:6px; text-align:center;">진리표 (Truth Table)</div>
          <div id="sim-truth-table" style="font-size:11px; font-family:monospace;"></div>
        </div>
      </div>
    </div>
  </div>

  <script>
    // 모달 제어 함수
    function openNandModal() {
      document.getElementById('nand-modal').classList.add('active');
      renderSim();
    }
    function closeNandModal() {
      document.getElementById('nand-modal').classList.remove('active');
    }
    function handleOverlayClick(e) {
      if (e.target.id === 'nand-modal') {
        closeNandModal();
      }
    }

    // 시뮬레이터 상태 변수
    let simMode = 'NOT';
    let simA = 0;
    let simB = 0;

    function setNandMode(mode) {
      simMode = mode;
      ['not', 'and', 'or', 'xor'].forEach(m => {
        const btn = document.getElementById('btn-mode-' + m);
        if (m === mode.toLowerCase()) {
          btn.className = 'sim-mode-btn active';
        } else {
          btn.className = 'sim-mode-btn';
        }
      });
      document.getElementById('sim-container-b').style.display = (mode === 'NOT') ? 'none' : 'flex';
      renderSim();
    }

    function toggleSimInput(which) {
      if (which === 'A') simA = (simA === 0) ? 1 : 0;
      if (which === 'B') simB = (simB === 0) ? 1 : 0;
      renderSim();
    }

    function renderSim() {
      const btnA = document.getElementById('sim-btn-a');
      const btnB = document.getElementById('sim-btn-b');
      btnA.textContent = simA;
      btnA.className = 'sim-input-btn ' + (simA ? 'on' : '');
      btnB.textContent = simB;
      btnB.className = 'sim-input-btn ' + (simB ? 'on' : '');

      const diagram = document.getElementById('sim-circuit-diagram');
      const exp = document.getElementById('sim-explanation');
      const table = document.getElementById('sim-truth-table');
      const badge = document.getElementById('sim-output-badge');

      let out = 0;

      if (simMode === 'NOT') {
        const n1 = !(simA && simA) ? 1 : 0;
        out = n1;

        diagram.innerHTML = `
          <div style="display:flex; align-items:center; gap:10px;">
            <div style="text-align:center;">
              <span style="font-size:10px; color:#94a3b8;">입력 A</span>
              <div class="sim-input-btn ${simA ? 'on' : ''}" style="width:34px; height:34px; font-size:14px; margin-top:2px;">${simA}</div>
            </div>
            <div style="display:flex; flex-direction:column; gap:8px;">
              <div class="${simA ? 'wire-active' : 'wire-inactive'}" style="width:30px; height:3px; border-radius:2px;"></div>
              <div class="${simA ? 'wire-active' : 'wire-inactive'}" style="width:30px; height:3px; border-radius:2px;"></div>
            </div>
            <div class="gate-box ${n1 ? 'gate-active' : ''}">
              <div style="font-size:11px; color:#38bdf8; font-weight:bold;">NAND 1</div>
              <div style="font-size:10px; color:#94a3b8;">입력 (${simA}, ${simA})</div>
              <div style="font-size:12px; font-weight:bold; color:${n1 ? '#38bdf8' : '#64748b'};">출력: ${n1}</div>
            </div>
            <div class="${n1 ? 'wire-active' : 'wire-inactive'}" style="width:30px; height:3px; border-radius:2px;"></div>
            <div style="text-align:center;">
              <span style="font-size:10px; color:#94a3b8;">NOT(A)</span>
              <div style="width:34px; height:34px; border-radius:8px; background:#1e293b; border:1.5px solid ${out ? '#38bdf8' : '#475569'}; color:${out ? '#38bdf8' : '#ef4444'}; font-weight:bold; font-size:14px; display:flex; align-items:center; justify-content:center; margin-top:2px; ${out ? 'box-shadow:0 0 10px rgba(56,189,248,0.4)' : ''}">
                ${out}
              </div>
            </div>
          </div>
        `;
        exp.innerHTML = `
          <strong>NOT 동작 원리:</strong> NAND 게이트의 두 입력에 같은 신호 A를 묶어 넣습니다.<br>
          • A=0 ➔ NAND(0,0) = <span style="color:#10b981; font-weight:bold;">1</span><br>
          • A=1 ➔ NAND(1,1) = <span style="color:#ef4444; font-weight:bold;">0</span><br>
          단 1개의 NAND 게이트로 반전(NOT)이 완벽히 구현됩니다!
        `;
        table.innerHTML = `
          <div style="display:grid; grid-template-columns:1fr 1fr; border-bottom:1px solid #334155; padding-bottom:3px; color:#64748b; text-align:center;">
            <span>A</span><span>OUT</span>
          </div>
          <div style="display:grid; grid-template-columns:1fr 1fr; text-align:center; padding:3px 0; border-radius:4px; ${simA===0 ? 'background:#0c4a6e; color:#7dd3fc; font-weight:bold;' : 'color:#94a3b8;'}">
            <span>0</span><span>1</span>
          </div>
          <div style="display:grid; grid-template-columns:1fr 1fr; text-align:center; padding:3px 0; border-radius:4px; ${simA===1 ? 'background:#0c4a6e; color:#7dd3fc; font-weight:bold;' : 'color:#94a3b8;'}">
            <span>1</span><span>0</span>
          </div>
        `;

      } else if (simMode === 'AND') {
        const n1 = !(simA && simB) ? 1 : 0;
        const n2 = !(n1 && n1) ? 1 : 0;
        out = n2;

        diagram.innerHTML = `
          <div style="display:flex; align-items:center; gap:8px;">
            <div style="display:flex; flex-direction:column; gap:6px;">
              <div style="display:flex; align-items:center; gap:4px;">
                <span style="font-size:9px; color:#94a3b8;">A(${simA})</span>
                <div class="${simA ? 'wire-active' : 'wire-inactive'}" style="width:20px; height:3px; border-radius:2px;"></div>
              </div>
              <div style="display:flex; align-items:center; gap:4px;">
                <span style="font-size:9px; color:#94a3b8;">B(${simB})</span>
                <div class="${simB ? 'wire-active' : 'wire-inactive'}" style="width:20px; height:3px; border-radius:2px;"></div>
              </div>
            </div>
            <div class="gate-box ${n1 ? 'gate-active' : ''}">
              <div style="font-size:10.5px; color:#38bdf8; font-weight:bold;">NAND 1</div>
              <div style="font-size:11px; font-weight:bold; color:${n1 ? '#38bdf8' : '#64748b'};">${n1}</div>
            </div>
            <div class="${n1 ? 'wire-active' : 'wire-inactive'}" style="width:20px; height:3px; border-radius:2px;"></div>
            <div class="gate-box ${n2 ? 'gate-active' : ''}">
              <div style="font-size:10.5px; color:#38bdf8; font-weight:bold;">NAND 2 (NOT)</div>
              <div style="font-size:11px; font-weight:bold; color:${n2 ? '#38bdf8' : '#64748b'};">${n2}</div>
            </div>
            <div class="${n2 ? 'wire-active' : 'wire-inactive'}" style="width:20px; height:3px; border-radius:2px;"></div>
            <div style="text-align:center;">
              <span style="font-size:9.5px; color:#94a3b8;">A AND B</span>
              <div style="width:34px; height:34px; border-radius:8px; background:#1e293b; border:1.5px solid ${out ? '#38bdf8' : '#475569'}; color:${out ? '#38bdf8' : '#ef4444'}; font-weight:bold; font-size:14px; display:flex; align-items:center; justify-content:center; margin-top:2px;">
                ${out}
              </div>
            </div>
          </div>
        `;
        exp.innerHTML = `
          <strong>AND 동작 원리:</strong> AND는 NAND의 결과를 다시 반전(NOT)시킨 것입니다.<br>
          • 1단계: NAND(A, B)를 계산합니다.<br>
          • 2단계: 그 결과를 다시 NAND 2에 넣어 NOT을 취하면 완벽한 AND 출력이 나옵니다!
        `;
        renderTruthTable([
          {a:0, b:0, out:0}, {a:0, b:1, out:0}, {a:1, b:0, out:0}, {a:1, b:1, out:1}
        ]);

      } else if (simMode === 'OR') {
        const nA = !(simA && simA) ? 1 : 0;
        const nB = !(simB && simB) ? 1 : 0;
        const n3 = !(nA && nB) ? 1 : 0;
        out = n3;

        diagram.innerHTML = `
          <div style="display:flex; align-items:center; gap:8px;">
            <div style="display:flex; flex-direction:column; gap:12px;">
              <div style="display:flex; align-items:center; gap:4px;">
                <span style="font-size:9px; color:#94a3b8;">A(${simA})</span>
                <div class="${simA ? 'wire-active' : 'wire-inactive'}" style="width:15px; height:3px;"></div>
                <div class="gate-box ${nA ? 'gate-active' : ''}" style="min-width:65px; padding:4px 6px;">
                  <div style="font-size:9.5px; color:#38bdf8;">NAND 1 (NOT)</div>
                  <div style="font-size:10px; font-weight:bold;">${nA}</div>
                </div>
                <div class="${nA ? 'wire-active' : 'wire-inactive'}" style="width:15px; height:3px;"></div>
              </div>
              <div style="display:flex; align-items:center; gap:4px;">
                <span style="font-size:9px; color:#94a3b8;">B(${simB})</span>
                <div class="${simB ? 'wire-active' : 'wire-inactive'}" style="width:15px; height:3px;"></div>
                <div class="gate-box ${nB ? 'gate-active' : ''}" style="min-width:65px; padding:4px 6px;">
                  <div style="font-size:9.5px; color:#38bdf8;">NAND 2 (NOT)</div>
                  <div style="font-size:10px; font-weight:bold;">${nB}</div>
                </div>
                <div class="${nB ? 'wire-active' : 'wire-inactive'}" style="width:15px; height:3px;"></div>
              </div>
            </div>
            <div class="gate-box ${n3 ? 'gate-active' : ''}" style="min-width:85px;">
              <div style="font-size:10.5px; color:#38bdf8; font-weight:bold;">NAND 3</div>
              <div style="font-size:11px; font-weight:bold;">${n3}</div>
            </div>
            <div class="${n3 ? 'wire-active' : 'wire-inactive'}" style="width:20px; height:3px;"></div>
            <div style="text-align:center;">
              <span style="font-size:9.5px; color:#94a3b8;">A OR B</span>
              <div style="width:34px; height:34px; border-radius:8px; background:#1e293b; border:1.5px solid ${out ? '#38bdf8' : '#475569'}; color:${out ? '#38bdf8' : '#ef4444'}; font-weight:bold; font-size:14px; display:flex; align-items:center; justify-content:center; margin-top:2px;">
                ${out}
              </div>
            </div>
          </div>
        `;
        exp.innerHTML = `
          <strong>OR 동작 원리 (드모르간 법칙의 마법):</strong><br>
          • $A + B = \\overline{\\bar{A} \\cdot \\bar{B}} = \\text{NAND}(\\text{NOT}(A), \\text{NOT}(B))$<br>
          입력 A와 B를 각각 NOT(NAND)시킨 후 마지막 NAND 3에 넣으면 합집합(OR)이 완성됩니다!
        `;
        renderTruthTable([
          {a:0, b:0, out:0}, {a:0, b:1, out:1}, {a:1, b:0, out:1}, {a:1, b:1, out:1}
        ]);

      } else if (simMode === 'XOR') {
        const n1 = !(simA && simB) ? 1 : 0;
        const n2 = !(simA && n1) ? 1 : 0;
        const n3 = !(simB && n1) ? 1 : 0;
        const n4 = !(n2 && n3) ? 1 : 0;
        out = n4;

        diagram.innerHTML = `
          <div style="display:flex; align-items:center; gap:8px;">
            <div style="text-align:center; font-size:10px; color:#94a3b8;">A(${simA}), B(${simB})</div>
            <div class="gate-box ${n1 ? 'gate-active' : ''}" style="min-width:70px; padding:4px 6px;">
              <div style="font-size:9.5px; color:#38bdf8;">NAND 1</div>
              <div style="font-size:10px; font-weight:bold;">${n1}</div>
            </div>
            <div style="display:flex; flex-direction:column; gap:8px;">
              <div class="gate-box ${n2 ? 'gate-active' : ''}" style="min-width:70px; padding:4px 6px;">
                <div style="font-size:9.5px; color:#38bdf8;">NAND 2</div>
                <div style="font-size:10px; font-weight:bold;">${n2}</div>
              </div>
              <div class="gate-box ${n3 ? 'gate-active' : ''}" style="min-width:70px; padding:4px 6px;">
                <div style="font-size:9.5px; color:#38bdf8;">NAND 3</div>
                <div style="font-size:10px; font-weight:bold;">${n3}</div>
              </div>
            </div>
            <div class="gate-box ${n4 ? 'gate-active' : ''}" style="min-width:70px; padding:4px 6px;">
              <div style="font-size:9.5px; color:#38bdf8;">NAND 4</div>
              <div style="font-size:10px; font-weight:bold;">${n4}</div>
            </div>
            <div style="text-align:center;">
              <span style="font-size:9.5px; color:#94a3b8;">A XOR B</span>
              <div style="width:34px; height:34px; border-radius:8px; background:#1e293b; border:1.5px solid ${out ? '#38bdf8' : '#475569'}; color:${out ? '#38bdf8' : '#ef4444'}; font-weight:bold; font-size:14px; display:flex; align-items:center; justify-content:center; margin-top:2px;">
                ${out}
              </div>
            </div>
          </div>
        `;
        exp.innerHTML = `
          <strong>XOR 동작 원리 (NAND 4개 합성):</strong><br>
          • 단층 퍼셉트론으로 불가능했던 XOR을 단 4개의 NAND 게이트로 조립하여 해결합니다!<br>
          • 서로 다를 때만 1이 출력되는 컴퓨터 가산기의 핵심 연산입니다.
        `;
        renderTruthTable([
          {a:0, b:0, out:0}, {a:0, b:1, out:1}, {a:1, b:0, out:1}, {a:1, b:1, out:0}
        ]);
      }

      badge.textContent = out;
      badge.style.borderColor = out ? '#38bdf8' : '#475569';
      badge.style.color = out ? '#38bdf8' : '#ef4444';
      badge.style.boxShadow = out ? '0 0 12px rgba(56, 189, 248, 0.4)' : 'none';
    }

    function renderTruthTable(rows) {
      const table = document.getElementById('sim-truth-table');
      table.innerHTML = `
        <div style="display:grid; grid-template-columns:1fr 1fr 1.2fr; border-bottom:1px solid #334155; padding-bottom:3px; color:#64748b; text-align:center;">
          <span>A</span><span>B</span><span>OUT</span>
        </div>
        ${rows.map(r => {
          const isActive = (r.a === simA && r.b === simB);
          return `
            <div style="display:grid; grid-template-columns:1fr 1fr 1.2fr; text-align:center; padding:3px 0; border-radius:4px; ${isActive ? 'background:#0c4a6e; color:#7dd3fc; font-weight:bold; border:1px solid #0284c7;' : 'color:#94a3b8;'}">
              <span>${r.a}</span><span>${r.b}</span><span>${r.out}</span>
            </div>
          `;
        }).join('')}
      `;
    }
  </script>
"""

html = html.replace("</body>", modal_html_and_js + "\n</body>")

with open(r"c:\Users\user\Desktop\DB\2026\1학년 아카데미아\[출력용]고1_집합과명제_AI퍼셉트론_워크북_4페이지.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML 교재에 대화형 NAND 시뮬레이터 모달 탑재 완료!")
