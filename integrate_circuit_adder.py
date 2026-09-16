# -*- coding: utf-8 -*-
with open(r"c:\Users\user\Desktop\DB\2026\1학년 아카데미아\[출력용]고1_집합과명제_AI퍼셉트론_워크북_4페이지.html", "r", encoding="utf-8") as f:
    full_html = f.read()

# 모달 시작 위치와 끝 위치 찾기
modal_start_idx = full_html.find('<!-- ==========================================================================\n       NAND 범용 게이트 인터랙티브 시뮬레이터 모달')
if modal_start_idx == -1:
    modal_start_idx = full_html.find('<div id="nand-modal"')

# CSS 교체: 모달 및 연산기 전용 스타일
new_modal_css = """
    /* ==========================================================================
       정밀 회로 NAND 및 0~32 연산기 모달 스타일
       ========================================================================== */
    .modal-overlay {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(5px);
      z-index: 2000;
      justify-content: center;
      align-items: center;
      padding: 12px;
    }
    .modal-overlay.active {
      display: flex;
    }
    .modal-card {
      background: #090d16;
      border: 1px solid #1e293b;
      border-radius: 16px;
      width: 100%;
      max-width: 920px;
      color: #f8fafc;
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.7);
      padding: 18px 22px;
      position: relative;
      max-height: 96vh;
      overflow-y: auto;
    }
    .modal-close-btn {
      position: absolute;
      top: 14px;
      right: 18px;
      background: #1e293b;
      color: #94a3b8;
      border: 1px solid #334155;
      width: 30px;
      height: 30px;
      border-radius: 50%;
      font-size: 14px;
      font-weight: bold;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s;
    }
    .modal-close-btn:hover {
      background: #ef4444;
      color: white;
      border-color: #ef4444;
    }
    /* 탭 헤더 */
    .tab-header {
      display: flex;
      gap: 10px;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 12px;
      margin-bottom: 14px;
    }
    .main-tab-btn {
      padding: 8px 18px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: bold;
      cursor: pointer;
      border: 1px solid #334155;
      background: #0f172a;
      color: #94a3b8;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }
    .main-tab-btn.active {
      background: #0284c7;
      color: white;
      border-color: #38bdf8;
      box-shadow: 0 0 14px rgba(56, 189, 248, 0.4);
    }
    .sim-mode-btn {
      padding: 5px 12px;
      border-radius: 6px;
      font-size: 11.5px;
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
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.35);
    }
    .sim-input-btn {
      width: 40px;
      height: 40px;
      border-radius: 8px;
      font-size: 16px;
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
      box-shadow: 0 0 12px rgba(16, 185, 129, 0.5);
    }
    /* 0~32 비트 스위치 버튼 */
    .bit-btn {
      width: 46px;
      height: 52px;
      border-radius: 8px;
      background: #1e293b;
      border: 2px solid #334155;
      color: #64748b;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-family: monospace;
      transition: all 0.2s;
    }
    .bit-btn.on {
      background: #0369a1;
      border-color: #38bdf8;
      color: white;
      box-shadow: 0 0 14px rgba(56, 189, 248, 0.5);
    }
    .bit-btn .val {
      font-size: 18px;
      font-weight: bold;
    }
    .bit-btn .label {
      font-size: 9.5px;
      margin-top: 2px;
    }
    .calc-btn {
      padding: 6px 12px;
      border-radius: 6px;
      border: 1px solid #334155;
      background: #1e293b;
      color: #cbd5e1;
      font-size: 11.5px;
      font-weight: bold;
      cursor: pointer;
      transition: all 0.2s;
    }
    .calc-btn:hover {
      background: #334155;
      color: white;
    }
    @media print {
      .modal-overlay {
        display: none !important;
      }
    }
"""

# HTML 본문 생성
new_modal_html_and_js = """
  <!-- ==========================================================================
       [인터랙티브 모달] 탭 1: 정밀 회로 NAND / 탭 2: 0~32 2진수 연산기 & 가산기
       ========================================================================== -->
  <div id="nand-modal" class="modal-overlay" onclick="handleOverlayClick(event)">
    <div class="modal-card" onclick="event.stopPropagation()">
      <button class="modal-close-btn" onclick="closeNandModal()" title="닫기">✕</button>
      
      <!-- 상단 탭 헤더 -->
      <div class="tab-header">
        <button id="tab-btn-nand" class="main-tab-btn active" onclick="switchMainTab('NAND')">
          ⚡ [탭 1] NAND 만능 게이트 정밀 회로
        </button>
        <button id="tab-btn-counter" class="main-tab-btn" onclick="switchMainTab('COUNTER')">
          🔢 [탭 2] 0~32 2진수 연산기 & 가산기 회로
        </button>
      </div>

      <!-- ==================================================================
           [탭 1 콘텐츠] NAND 만능 게이트 정밀 회로 (SVG 정밀 배선)
           ================================================================== -->
      <div id="tab-content-nand">
        <!-- 모드 선택 버튼들 -->
        <div style="display:flex; gap:8px; justify-content:center; margin-bottom:12px; flex-wrap:wrap;">
          <button id="btn-mode-not" class="sim-mode-btn active" onclick="setNandMode('NOT')">[NOT] 게이트 (NAND 1개)</button>
          <button id="btn-mode-and" class="sim-mode-btn" onclick="setNandMode('AND')">[AND] 게이트 (NAND 2개)</button>
          <button id="btn-mode-or" class="sim-mode-btn" onclick="setNandMode('OR')">[OR] 게이트 (NAND 3개)</button>
          <button id="btn-mode-xor" class="sim-mode-btn" onclick="setNandMode('XOR')">[XOR] 게이트 (NAND 4개)</button>
        </div>

        <!-- 입력/출력 컨트롤러 -->
        <div style="background:#020617; border:1px solid #1e293b; border-radius:10px; padding:10px 16px; margin-bottom:12px; display:flex; justify-content:space-between; align-items:center;">
          <div style="display:flex; align-items:center; gap:16px;">
            <div style="display:flex; align-items:center; gap:8px;">
              <span style="font-size:11.5px; font-weight:bold; color:#94a3b8;">입력 A (클릭토글):</span>
              <button id="sim-btn-a" class="sim-input-btn" onclick="toggleSimInput('A')">0</button>
            </div>
            <div id="sim-container-b" style="display:flex; align-items:center; gap:8px;">
              <span style="font-size:11.5px; font-weight:bold; color:#94a3b8;">입력 B (클릭토글):</span>
              <button id="sim-btn-b" class="sim-input-btn" onclick="toggleSimInput('B')">0</button>
            </div>
          </div>
          <div style="display:flex; align-items:center; gap:10px; border-left:1px solid #1e293b; padding-left:14px;">
            <span style="font-size:11.5px; font-weight:bold; color:#94a3b8;">최종 출력:</span>
            <div id="sim-output-badge" style="width:40px; height:40px; border-radius:8px; background:#0f172a; color:#38bdf8; font-size:18px; font-weight:bold; font-family:monospace; display:flex; align-items:center; justify-content:center; border:2px solid #38bdf8;">
              1
            </div>
          </div>
        </div>

        <!-- 정밀 SVG 회로 캔버스 -->
        <div style="background:#020617; border:1px solid #1e293b; border-radius:10px; padding:10px; min-height:160px; display:flex; justify-content:center; align-items:center; overflow-x:auto; margin-bottom:12px;">
          <svg id="nand-circuit-svg" width="680" height="150" viewBox="0 0 680 150" style="background:#020617;"></svg>
        </div>

        <!-- 하단 설명 및 진리표 -->
        <div style="display:grid; grid-template-columns: 2fr 1fr; gap:12px;">
          <div style="background:#020617; border:1px solid #1e293b; border-radius:8px; padding:10px; font-size:11px;">
            <div style="color:#38bdf8; font-weight:bold; margin-bottom:3px;">📌 수학적 동작 원리</div>
            <div id="sim-explanation" style="color:#cbd5e1; line-height:1.45;"></div>
          </div>
          <div style="background:#020617; border:1px solid #1e293b; border-radius:8px; padding:10px;">
            <div style="color:#94a3b8; font-size:10.5px; font-weight:bold; margin-bottom:4px; text-align:center;">진리표 (Truth Table)</div>
            <div id="sim-truth-table" style="font-size:10.5px; font-family:monospace;"></div>
          </div>
        </div>
      </div>

      <!-- ==================================================================
           [탭 2 콘텐츠] 0~32 2진수 연산기 & 가산기 회로 시뮬레이터
           ================================================================== -->
      <div id="tab-content-counter" style="display:none;">
        <!-- 상단 십진수 디스플레이 및 제어 버튼 -->
        <div style="background:#020617; border:1px solid #1e293b; border-radius:12px; padding:14px 18px; margin-bottom:12px; display:flex; justify-content:space-between; align-items:center;">
          <div>
            <span style="font-size:11px; color:#94a3b8; font-weight:bold;">10진수 숫자 출력</span>
            <div style="display:flex; align-items:baseline; gap:8px;">
              <span id="display-decimal" style="font-size:36px; font-weight:800; font-family:monospace; color:#38bdf8; text-shadow:0 0 15px rgba(56,189,248,0.5);">
                0
              </span>
              <span id="display-range" style="font-size:13px; color:#64748b; font-weight:bold;">/ 32 (범위: 0 ~ 32)</span>
            </div>
          </div>

          <div style="display:flex; gap:6px; align-items:center;">
            <button class="calc-btn" onclick="stepCounter(-1)">-1 감소</button>
            <button class="calc-btn" onclick="stepCounter(1)">+1 증가</button>
            <button id="auto-btn" class="calc-btn" style="background:#0284c7; color:white;" onclick="toggleAutoCount()">▶ 0~32 자동 카운트</button>
            <button class="calc-btn" onclick="resetCounter()">리셋 (0)</button>
          </div>
        </div>

        <!-- 6비트 스위치 컨트롤러 ($2^5 \sim 2^0$) -->
        <div style="background:#020617; border:1px solid #1e293b; border-radius:12px; padding:12px; margin-bottom:12px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
            <span style="font-size:11px; font-weight:bold; color:#94a3b8;">
              🎛 6비트 2진수 스위치 (각 비트를 직접 클릭해서 0과 1을 켜보세요!)
            </span>
            <span style="font-size:11px; font-mono; color:#38bdf8;" id="binary-string-view">
              2진수: 000000(2)
            </span>
          </div>

          <div style="display:flex; gap:10px; justify-content:center;">
            <!-- 비트 5 (32) -->
            <div id="bit-5" class="bit-btn" onclick="toggleBit(5)">
              <span class="val">0</span>
              <span class="label">2⁵(32)</span>
            </div>
            <!-- 비트 4 (16) -->
            <div id="bit-4" class="bit-btn" onclick="toggleBit(4)">
              <span class="val">0</span>
              <span class="label">2⁴(16)</span>
            </div>
            <!-- 비트 3 (8) -->
            <div id="bit-3" class="bit-btn" onclick="toggleBit(3)">
              <span class="val">0</span>
              <span class="label">2³(8)</span>
            </div>
            <!-- 비트 2 (4) -->
            <div id="bit-2" class="bit-btn" onclick="toggleBit(2)">
              <span class="val">0</span>
              <span class="label">2²(4)</span>
            </div>
            <!-- 비트 1 (2) -->
            <div id="bit-1" class="bit-btn" onclick="toggleBit(1)">
              <span class="val">0</span>
              <span class="label">2¹(2)</span>
            </div>
            <!-- 비트 0 (1) -->
            <div id="bit-0" class="bit-btn" onclick="toggleBit(0)">
              <span class="val">0</span>
              <span class="label">2⁰(1)</span>
            </div>
          </div>
        </div>

        <!-- 2진수 가산기 연산 원리 SVG 다이어그램 -->
        <div style="background:#020617; border:1px solid #1e293b; border-radius:10px; padding:10px; margin-bottom:10px;">
          <div style="font-size:11px; color:#38bdf8; font-weight:bold; margin-bottom:6px;">
            ⚡ 컴퓨터 연산기(ALU) 핵심: 반가산기(Half Adder) 덧셈 회로 시뮬레이션
          </div>
          <svg id="adder-circuit-svg" width="680" height="95" viewBox="0 0 680 95" style="background:#020617;"></svg>
        </div>

        <div style="background:#0f172a; border:1px solid #1e293b; border-radius:8px; padding:8px 12px; font-size:11px; color:#94a3b8; line-height:1.45;">
          💡 <strong>연산기 원리</strong> : 
          10진수 $32$는 2진수로 <strong>100000₂</strong> (스위치 6번째만 ON)입니다. 
          스위치 5개($16+8+4+2+1$)로 $0 \sim 31$을 표현하고, 여기에 $+1$을 더하면 
          <strong>가산기 회로의 올림수(Carry)</strong>가 도미노처럼 연속 전달되어 6번째 비트가 1이 되면서 $32$가 출력됩니다!
        </div>
      </div>
    </div>
  </div>

  <script>
    // -------------------------------------------------------------
    // 모달 및 탭 전환
    // -------------------------------------------------------------
    function openNandModal() {
      document.getElementById('nand-modal').classList.add('active');
      renderNandSvg();
      updateCounterUI();
    }
    function closeNandModal() {
      document.getElementById('nand-modal').classList.remove('active');
      if (autoInterval) {
        clearInterval(autoInterval);
        autoInterval = null;
        document.getElementById('auto-btn').textContent = '▶ 0~32 자동 카운트';
      }
    }
    function handleOverlayClick(e) {
      if (e.target.id === 'nand-modal') closeNandModal();
    }

    function switchMainTab(tab) {
      const btnNand = document.getElementById('tab-btn-nand');
      const btnCounter = document.getElementById('tab-btn-counter');
      const contentNand = document.getElementById('tab-content-nand');
      const contentCounter = document.getElementById('tab-content-counter');

      if (tab === 'NAND') {
        btnNand.className = 'main-tab-btn active';
        btnCounter.className = 'main-tab-btn';
        contentNand.style.display = 'block';
        contentCounter.style.display = 'none';
        renderNandSvg();
      } else {
        btnNand.className = 'main-tab-btn';
        btnCounter.className = 'main-tab-btn active';
        contentNand.style.display = 'none';
        contentCounter.style.display = 'block';
        updateCounterUI();
      }
    }

    // -------------------------------------------------------------
    // [탭 1] 정밀 회로 NAND 시뮬레이터 로직
    // -------------------------------------------------------------
    let simMode = 'NOT';
    let simA = 0;
    let simB = 0;

    function setNandMode(mode) {
      simMode = mode;
      ['not', 'and', 'or', 'xor'].forEach(m => {
        const btn = document.getElementById('btn-mode-' + m);
        btn.className = (m === mode.toLowerCase()) ? 'sim-mode-btn active' : 'sim-mode-btn';
      });
      document.getElementById('sim-container-b').style.display = (mode === 'NOT') ? 'none' : 'flex';
      renderNandSvg();
    }

    function toggleSimInput(which) {
      if (which === 'A') simA = (simA === 0) ? 1 : 0;
      if (which === 'B') simB = (simB === 0) ? 1 : 0;
      renderNandSvg();
    }

    // SVG 게이트 심볼 생성 헬퍼
    function svgNandGate(x, y, label, outVal) {
      const color = outVal ? '#38bdf8' : '#64748b';
      const fill = outVal ? '#0c4a6e' : '#1e293b';
      return `
        <g transform="translate(${x}, ${y})">
          <!-- 게이트 본체 D 형태 -->
          <path d="M 0,0 L 28,0 A 20,20 0 0,1 28,40 L 0,40 Z" fill="${fill}" stroke="${color}" stroke-width="2"/>
          <!-- 반전 버블 -->
          <circle cx="53" cy="20" r="5" fill="#090d16" stroke="${color}" stroke-width="2"/>
          <text x="18" y="24" font-size="10" font-weight="bold" fill="${color}" text-anchor="middle">${label}</text>
        </g>
      `;
    }

    function renderNandSvg() {
      document.getElementById('sim-btn-a').textContent = simA;
      document.getElementById('sim-btn-a').className = 'sim-input-btn ' + (simA ? 'on' : '');
      document.getElementById('sim-btn-b').textContent = simB;
      document.getElementById('sim-btn-b').className = 'sim-input-btn ' + (simB ? 'on' : '');

      const svg = document.getElementById('nand-circuit-svg');
      const exp = document.getElementById('sim-explanation');
      const table = document.getElementById('sim-truth-table');
      const badge = document.getElementById('sim-output-badge');

      const colA = simA ? '#38bdf8' : '#334155';
      const colB = simB ? '#38bdf8' : '#334155';

      let out = 0;

      if (simMode === 'NOT') {
        out = !(simA && simA) ? 1 : 0;
        const colOut = out ? '#38bdf8' : '#334155';

        svg.innerHTML = `
          <!-- 입력 A 라벨 및 핀 -->
          <text x="30" y="78" font-size="12" font-weight="bold" fill="${colA}">A = ${simA}</text>
          <!-- 분기선: A에서 위아래 핀으로 정확히 배선 -->
          <line x1="80" y1="75" x2="140" y2="75" stroke="${colA}" stroke-width="3"/>
          <circle cx="140" cy="75" r="4" fill="${colA}"/>
          <path d="M 140,75 L 140,65 L 200,65" fill="none" stroke="${colA}" stroke-width="3"/>
          <path d="M 140,75 L 140,85 L 200,85" fill="none" stroke="${colA}" stroke-width="3"/>
          
          <!-- NAND 1 게이트 -->
          ${svgNandGate(200, 55, "NAND", out)}

          <!-- 출력선 -->
          <line x1="258" y1="75" x2="380" y2="75" stroke="${colOut}" stroke-width="3"/>
          <circle cx="380" cy="75" r="6" fill="${colOut}"/>
          <text x="400" y="79" font-size="13" font-weight="bold" fill="${colOut}">출력 NOT(A) = ${out}</text>
        `;
        exp.innerHTML = `
          • <strong>수학적 원리</strong>: $\\text{NOT}(A) = \\text{NAND}(A, A)$<br>
          신호 A를 두 입력 단자에 묶어 넣으면, $A=0$일 때 $1$, $A=1$일 때 $0$이 출력되어 완벽한 NOT이 완성됩니다!
        `;
        renderTruthTableRows([{a:0, b:0, out:1}, {a:1, b:1, out:0}], true);

      } else if (simMode === 'AND') {
        const n1 = !(simA && simB) ? 1 : 0;
        out = !(n1 && n1) ? 1 : 0;
        const colN1 = n1 ? '#38bdf8' : '#334155';
        const colOut = out ? '#38bdf8' : '#334155';

        svg.innerHTML = `
          <text x="25" y="60" font-size="11" font-weight="bold" fill="${colA}">A = ${simA}</text>
          <text x="25" y="95" font-size="11" font-weight="bold" fill="${colB}">B = ${simB}</text>
          <line x1="75" y1="56" x2="160" y2="56" stroke="${colA}" stroke-width="3"/>
          <line x1="75" y1="92" x2="160" y2="92" stroke="${colB}" stroke-width="3"/>
          
          <!-- 1단계: NAND 1 -->
          ${svgNandGate(160, 48, "NAND1", n1)}

          <!-- 분기선: NAND1 출력이 둘로 나뉘어 NAND2로 들어감 -->
          <line x1="218" y1="68" x2="270" y2="68" stroke="${colN1}" stroke-width="3"/>
          <circle cx="270" cy="68" r="4" fill="${colN1}"/>
          <path d="M 270,68 L 270,58 L 330,58" fill="none" stroke="${colN1}" stroke-width="3"/>
          <path d="M 270,68 L 270,78 L 330,78" fill="none" stroke="${colN1}" stroke-width="3"/>

          <!-- 2단계: NAND 2 (NOT 역할) -->
          ${svgNandGate(330, 48, "NAND2", out)}

          <line x1="388" y1="68" x2="480" y2="68" stroke="${colOut}" stroke-width="3"/>
          <circle cx="480" cy="68" r="6" fill="${colOut}"/>
          <text x="495" y="72" font-size="12" font-weight="bold" fill="${colOut}">A AND B = ${out}</text>
        `;
        exp.innerHTML = `
          • <strong>수학적 원리</strong>: $\\text{AND}(A, B) = \\text{NOT}(\\text{NAND}(A, B))$<br>
          1단계 NAND 게이트의 결과를 다시 2단계 NAND(NOT)로 뒤집어 정직한 AND 출력을 만듭니다!
        `;
        renderTruthTableRows([
          {a:0, b:0, out:0}, {a:0, b:1, out:0}, {a:1, b:0, out:0}, {a:1, b:1, out:1}
        ]);

      } else if (simMode === 'OR') {
        const nA = !(simA && simA) ? 1 : 0;
        const nB = !(simB && simB) ? 1 : 0;
        out = !(nA && nB) ? 1 : 0;
        const colNA = nA ? '#38bdf8' : '#334155';
        const colNB = nB ? '#38bdf8' : '#334155';
        const colOut = out ? '#38bdf8' : '#334155';

        svg.innerHTML = `
          <!-- A 입력 및 NAND1(NOT) -->
          <text x="20" y="38" font-size="11" font-weight="bold" fill="${colA}">A = ${simA}</text>
          <path d="M 70,35 L 100,35 L 100,26 L 140,26" fill="none" stroke="${colA}" stroke-width="3"/>
          <path d="M 100,35 L 100,44 L 140,44" fill="none" stroke="${colA}" stroke-width="3"/>
          <circle cx="100" cy="35" r="4" fill="${colA}"/>
          ${svgNandGate(140, 15, "NOT A", nA)}

          <!-- B 입력 및 NAND2(NOT) -->
          <text x="20" y="118" font-size="11" font-weight="bold" fill="${colB}">B = ${simB}</text>
          <path d="M 70,115 L 100,115 L 100,106 L 140,106" fill="none" stroke="${colB}" stroke-width="3"/>
          <path d="M 100,115 L 100,124 L 140,124" fill="none" stroke="${colB}" stroke-width="3"/>
          <circle cx="100" cy="115" r="4" fill="${colB}"/>
          ${svgNandGate(140, 95, "NOT B", nB)}

          <!-- 두 출력이 NAND3로 정확히 배선 -->
          <path d="M 198,35 L 260,35 L 260,65 L 310,65" fill="none" stroke="${colNA}" stroke-width="3"/>
          <path d="M 198,115 L 260,115 L 260,85 L 310,85" fill="none" stroke="${colNB}" stroke-width="3"/>

          ${svgNandGate(310, 55, "NAND3", out)}

          <line x1="368" y1="75" x2="470" y2="75" stroke="${colOut}" stroke-width="3"/>
          <circle cx="470" cy="75" r="6" fill="${colOut}"/>
          <text x="485" y="79" font-size="12" font-weight="bold" fill="${colOut}">A OR B = ${out}</text>
        `;
        exp.innerHTML = `
          • <strong>드모르간 법칙의 응용</strong>: $A + B = \\overline{\\bar{A} \\cdot \\bar{B}} = \\text{NAND}(\\text{NOT}(A), \\text{NOT}(B))$<br>
          각 입력을 반전시켜 세 번째 NAND에 넣으면 마법처럼 합집합(OR)이 됩니다!
        `;
        renderTruthTableRows([
          {a:0, b:0, out:0}, {a:0, b:1, out:1}, {a:1, b:0, out:1}, {a:1, b:1, out:1}
        ]);

      } else if (simMode === 'XOR') {
        const n1 = !(simA && simB) ? 1 : 0;
        const n2 = !(simA && n1) ? 1 : 0;
        const n3 = !(simB && n1) ? 1 : 0;
        out = !(n2 && n3) ? 1 : 0;
        const colN1 = n1 ? '#38bdf8' : '#334155';
        const colN2 = n2 ? '#38bdf8' : '#334155';
        const colN3 = n3 ? '#38bdf8' : '#334155';
        const colOut = out ? '#38bdf8' : '#334155';

        svg.innerHTML = `
          <text x="15" y="45" font-size="11" font-weight="bold" fill="${colA}">A = ${simA}</text>
          <text x="15" y="110" font-size="11" font-weight="bold" fill="${colB}">B = ${simB}</text>

          <!-- A선과 B선의 교차 및 NAND1으로의 배선 -->
          <path d="M 65,42 L 100,42 L 100,68 L 135,68" fill="none" stroke="${colA}" stroke-width="2.5"/>
          <path d="M 65,108 L 100,108 L 100,86 L 135,86" fill="none" stroke="${colB}" stroke-width="2.5"/>
          <circle cx="100" cy="42" r="3.5" fill="${colA}"/>
          <circle cx="100" cy="108" r="3.5" fill="${colB}"/>

          <!-- A는 NAND2로 직행 -->
          <path d="M 100,42 L 250,42 L 250,30 L 280,30" fill="none" stroke="${colA}" stroke-width="2.5"/>
          <!-- B는 NAND3로 직행 -->
          <path d="M 100,108 L 250,108 L 250,120 L 280,120" fill="none" stroke="${colB}" stroke-width="2.5"/>

          <!-- NAND 1 -->
          ${svgNandGate(135, 57, "N1", n1)}

          <!-- N1 출력이 분기하여 NAND2와 NAND3으로 연결 -->
          <path d="M 193,77 L 225,77 L 225,46 L 280,46" fill="none" stroke="${colN1}" stroke-width="2.5"/>
          <path d="M 225,77 L 225,104 L 280,104" fill="none" stroke="${colN1}" stroke-width="2.5"/>
          <circle cx="225" cy="77" r="3.5" fill="${colN1}"/>

          <!-- NAND 2 & NAND 3 -->
          ${svgNandGate(280, 18, "N2", n2)}
          ${svgNandGate(280, 92, "N3", n3)}

          <!-- N2, N3 출력이 NAND 4로 집결 -->
          <path d="M 338,38 L 400,38 L 400,68 L 435,68" fill="none" stroke="${colN2}" stroke-width="2.5"/>
          <path d="M 338,112 L 400,112 L 400,86 L 435,86" fill="none" stroke="${colN3}" stroke-width="2.5"/>

          <!-- NAND 4 -->
          ${svgNandGate(435, 57, "N4", out)}

          <line x1="493" y1="77" x2="570" y2="77" stroke="${colOut}" stroke-width="3"/>
          <circle cx="570" cy="77" r="6" fill="${colOut}"/>
          <text x="585" y="81" font-size="12" font-weight="bold" fill="${colOut}">A XOR B = ${out}</text>
        `;
        exp.innerHTML = `
          • <strong>XOR의 NAND 4개 완성</strong>: 단층 퍼셉트론으로 불가능했던 XOR을 단 4개의 NAND 게이트로 배선하여 완벽히 해결합니다!<br>
          두 신호가 서로 다를 때만 $1$이 출력되는 가산기 덧셈의 핵심입니다.
        `;
        renderTruthTableRows([
          {a:0, b:0, out:0}, {a:0, b:1, out:1}, {a:1, b:0, out:1}, {a:1, b:1, out:0}
        ]);
      }

      badge.textContent = out;
      badge.style.borderColor = out ? '#38bdf8' : '#475569';
      badge.style.color = out ? '#38bdf8' : '#ef4444';
      badge.style.boxShadow = out ? '0 0 12px rgba(56, 189, 248, 0.4)' : 'none';
    }

    function renderTruthTableRows(rows, isSingle=false) {
      const table = document.getElementById('sim-truth-table');
      if (isSingle) {
        table.innerHTML = `
          <div style="display:grid; grid-template-columns:1fr 1fr; border-bottom:1px solid #334155; padding-bottom:2px; color:#64748b; text-align:center;">
            <span>A</span><span>OUT</span>
          </div>
          ${rows.map(r => `
            <div style="display:grid; grid-template-columns:1fr 1fr; text-align:center; padding:2px 0; ${r.a===simA ? 'background:#0c4a6e; color:#7dd3fc; font-weight:bold;' : 'color:#94a3b8;'}">
              <span>${r.a}</span><span>${r.out}</span>
            </div>
          `).join('')}
        `;
      } else {
        table.innerHTML = `
          <div style="display:grid; grid-template-columns:1fr 1fr 1.2fr; border-bottom:1px solid #334155; padding-bottom:2px; color:#64748b; text-align:center;">
            <span>A</span><span>B</span><span>OUT</span>
          </div>
          ${rows.map(r => {
            const act = (r.a === simA && r.b === simB);
            return `
              <div style="display:grid; grid-template-columns:1fr 1fr 1.2fr; text-align:center; padding:2px 0; border-radius:3px; ${act ? 'background:#0c4a6e; color:#7dd3fc; font-weight:bold; border:1px solid #0284c7;' : 'color:#94a3b8;'}">
                <span>${r.a}</span><span>${r.b}</span><span>${r.out}</span>
              </div>
            `;
          }).join('')}
        `;
      }
    }

    // -------------------------------------------------------------
    // [탭 2] 0~32 2진수 연산기 & 가산기 로직
    // -------------------------------------------------------------
    let currentNumber = 0; // 0 ~ 32
    let autoInterval = null;

    function updateCounterUI() {
      if (currentNumber < 0) currentNumber = 0;
      if (currentNumber > 32) currentNumber = 32;

      document.getElementById('display-decimal').textContent = currentNumber;
      const bin6 = currentNumber.toString(2).padStart(6, '0');
      document.getElementById('binary-string-view').textContent = `2진수: ${bin6}(2)`;

      for (let i = 0; i <= 5; i++) {
        // 비트 0은 1의 자리 (bin6의 끝 인덱스 5)
        const bitVal = parseInt(bin6[5 - i]);
        const btn = document.getElementById('bit-' + i);
        btn.className = 'bit-btn ' + (bitVal ? 'on' : '');
        btn.querySelector('.val').textContent = bitVal;
      }

      renderAdderSvg();
    }

    function toggleBit(bitIndex) {
      const bitWeight = Math.pow(2, bitIndex);
      const bin6 = currentNumber.toString(2).padStart(6, '0');
      const curBitVal = parseInt(bin6[5 - bitIndex]);

      if (curBitVal === 0) {
        currentNumber += bitWeight;
      } else {
        currentNumber -= bitWeight;
      }
      updateCounterUI();
    }

    function stepCounter(delta) {
      currentNumber += delta;
      updateCounterUI();
    }

    function resetCounter() {
      currentNumber = 0;
      updateCounterUI();
    }

    function toggleAutoCount() {
      const btn = document.getElementById('auto-btn');
      if (autoInterval) {
        clearInterval(autoInterval);
        autoInterval = null;
        btn.textContent = '▶ 0~32 자동 카운트';
        btn.style.background = '#0284c7';
      } else {
        btn.textContent = '⏸ 일시 정지';
        btn.style.background = '#ea580c';
        autoInterval = setInterval(() => {
          if (currentNumber >= 32) {
            currentNumber = 0;
          } else {
            currentNumber++;
          }
          updateCounterUI();
        }, 600);
      }
    }

    // 반가산기(Half Adder) SVG 회로 렌더링
    function renderAdderSvg() {
      const svg = document.getElementById('adder-circuit-svg');
      // 현재 숫자의 최하위 1비트에 1을 더하는 연산 시연
      const a = currentNumber & 1; // 입력 A
      const b = 1;                 // 1을 더함
      const sum = a ^ b;           // 합 XOR
      const carry = a & b;         // 올림수 AND

      const colA = a ? '#38bdf8' : '#334155';
      const colB = '#38bdf8'; // b=1
      const colSum = sum ? '#10b981' : '#334155';
      const colCarry = carry ? '#f59e0b' : '#334155';

      svg.innerHTML = `
        <text x="20" y="32" font-size="10" font-weight="bold" fill="${colA}">현재 최하위비트 A = ${a}</text>
        <text x="20" y="72" font-size="10" font-weight="bold" fill="${colB}">더할 수(+1) B = 1</text>

        <!-- A, B 신호선 -->
        <path d="M 140,28 L 190,28 L 190,20 L 230,20" fill="none" stroke="${colA}" stroke-width="2.5"/>
        <path d="M 140,28 L 190,28 L 190,65 L 230,65" fill="none" stroke="${colA}" stroke-width="2.5"/>
        <circle cx="190" cy="28" r="3.5" fill="${colA}"/>

        <path d="M 140,68 L 205,68 L 205,32 L 230,32" fill="none" stroke="${colB}" stroke-width="2.5"/>
        <path d="M 140,68 L 205,68 L 205,77 L 230,77" fill="none" stroke="${colB}" stroke-width="2.5"/>
        <circle cx="205" cy="68" r="3.5" fill="${colB}"/>

        <!-- XOR 게이트 (합 Sum 계산) -->
        <g transform="translate(230, 10)">
          <path d="M 0,0 C 10,8 10,24 0,32 C 15,32 30,22 36,16 C 30,10 15,0 0,0 Z" fill="#1e293b" stroke="${colSum}" stroke-width="2"/>
          <path d="M -5,0 C 5,8 5,24 -5,32" fill="none" stroke="${colSum}" stroke-width="2"/>
          <text x="16" y="20" font-size="9" fill="${colSum}" font-weight="bold">XOR</text>
        </g>
        <line x1="268" y1="26" x2="360" y2="26" stroke="${colSum}" stroke-width="2.5"/>
        <circle cx="360" cy="26" r="4" fill="${colSum}"/>
        <text x="375" y="30" font-size="11" font-weight="bold" fill="${colSum}">합(Sum) = ${sum} (결과 비트)</text>

        <!-- AND 게이트 (올림수 Carry 계산) -->
        <g transform="translate(230, 56)">
          <path d="M 0,0 L 18,0 A 15,15 0 0,1 18,30 L 0,30 Z" fill="#1e293b" stroke="${colCarry}" stroke-width="2"/>
          <text x="14" y="19" font-size="9" fill="${colCarry}" font-weight="bold">AND</text>
        </g>
        <line x1="265" y1="71" x2="360" y2="71" stroke="${colCarry}" stroke-width="2.5"/>
        <circle cx="360" cy="71" r="4" fill="${colCarry}"/>
        <text x="375" y="75" font-size="11" font-weight="bold" fill="${colCarry}">올림수(Carry) = ${carry} (다음 자릿수로 전달)</text>
      `;
    }
  </script>
"""

# 기존 모달 코드가 있으면 교체하고, 없으면 body 끝에 추가
if modal_start_idx != -1:
    before_modal = full_html[:modal_start_idx]
    final_html = before_modal + new_modal_html_and_js + "\n</body>\n</html>"
else:
    final_html = full_html.replace("</body>", new_modal_html_and_js + "\n</body>")

# CSS 업데이트
final_html = final_html.replace("/* ==========================================================================\n       NAND 시뮬레이터 모달 팝업 스타일", new_modal_css)

with open(r"c:\Users\user\Desktop\DB\2026\1학년 아카데미아\[출력용]고1_집합과명제_AI퍼셉트론_워크북_4페이지.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("정밀 회로 NAND 및 0~32 연산기 모달 완벽 통합 완료!")
