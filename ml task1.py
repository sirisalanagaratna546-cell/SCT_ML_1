#!/usr/bin/env python3
"""
Write the embedded HTML to a file and open it in the default browser.

This replaces the previous non-Python HTML file so it can be executed
without syntax errors. Running this script will create
`ml_task1_output.html` next to this script and open it in your browser.
"""
import webbrowser
from pathlib import Path

HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Estimator — House Value Blueprint</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root{
    --navy-deep: #0a1f33;
    --navy: #123354;
    --line: #3a6285;
    --line-faint: #1e3f5c;
    --paper: #e9eff5;
    --brass: #c9a227;
    --brass-dim: #8a7222;
    --ok: #7fb88a;
  }

  * { box-sizing: border-box; }

  html, body {
    margin: 0;
    padding: 0;
    background: var(--navy-deep);
    color: var(--paper);
    font-family: 'Space Grotesk', sans-serif;
    min-height: 100vh;
  }

  body {
    background-image:
      linear-gradient(var(--line-faint) 1px, transparent 1px),
      linear-gradient(90deg, var(--line-faint) 1px, transparent 1px);
    background-size: 32px 32px;
    background-position: -1px -1px;
  }

  .wrap {
    max-width: 1100px;
    margin: 0 auto;
    padding: 56px 24px 80px;
  }

  /* Header / title block */
  header {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-bottom: 2px solid var(--line);
    padding-bottom: 20px;
    margin-bottom: 8px;
  }

  .eyebrow {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 12px;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--line);
    margin-bottom: 10px;
  }

  h1 {
    font-size: clamp(32px, 5vw, 52px);
    font-weight: 700;
    margin: 0;
    letter-spacing: -0.01em;
    line-height: 1.05;
  }

  .rev {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 12px;
    color: var(--line);
    text-align: right;
    line-height: 1.6;
  }

  .rev b { color: var(--paper); }

  /* Layout: plan (left) + specs/output (right) */
  .grid {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 40px;
    margin-top: 48px;
  }

  @media (max-width: 860px) {
    .grid { grid-template-columns: 1fr; }
  }

  /* Floor plan illustration */
  .plan-panel {
    border: 1.5px solid var(--line);
    background: rgba(18, 51, 84, 0.4);
    padding: 28px;
    position: relative;
  }

  .plan-panel svg { width: 100%; height: auto; display: block; }

  .plan-caption {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    color: var(--line);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-top: 18px;
    display: flex;
    justify-content: space-between;
  }

  /* Controls */
  .controls {
    display: flex;
    flex-direction: column;
    gap: 34px;
  }

  .field { position: relative; }

  .field-label {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 14px;
    font-family: 'IBM Plex Mono', monospace;
  }

  .field-name {
    font-size: 12px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--line);
  }

  .field-value {
    font-size: 20px;
    font-weight: 600;
    color: var(--paper);
  }

  .field-value .unit {
    font-size: 12px;
    color: var(--line);
    margin-left: 4px;
    font-weight: 400;
  }

  /* Dimension-line slider */
  .dim {
    position: relative;
    height: 40px;
  }

  .dim-line {
    position: absolute;
    top: 19px;
    left: 0;
    right: 0;
    height: 1px;
    background: var(--line);
  }

  .dim-line::before, .dim-line::after {
    content: '';
    position: absolute;
    top: -4px;
    width: 1px;
    height: 9px;
    background: var(--line);
  }
  .dim-line::before { left: 0; }
  .dim-line::after { right: 0; }

  .dim-ticks {
    position: absolute;
    top: 12px;
    left: 0;
    right: 0;
    display: flex;
    justify-content: space-between;
    pointer-events: none;
  }

  .dim-ticks span {
    width: 1px;
    height: 4px;
    background: var(--line-faint);
  }

  input[type="range"] {
    -webkit-appearance: none;
    appearance: none;
    position: relative;
    width: 100%;
    height: 40px;
    background: transparent;
    margin: 0;
    cursor: pointer;
    z-index: 2;
  }

  input[type="range"]::-webkit-slider-runnable-track {
    height: 40px;
    background: transparent;
  }

  input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 14px;
    height: 14px;
    margin-top: 12px;
    border-radius: 50%;
    background: var(--brass);
    border: 2px solid var(--navy-deep);
    box-shadow: 0 0 0 1px var(--brass);
    cursor: grab;
  }

  input[type="range"]::-moz-range-track {
    height: 1px;
    background: transparent;
  }

  input[type="range"]::-moz-range-thumb {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: var(--brass);
    border: 2px solid var(--navy-deep);
    box-shadow: 0 0 0 1px var(--brass);
    cursor: grab;
  }

  .dim-minmax {
    display: flex;
    justify-content: space-between;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    color: var(--line);
    margin-top: 2px;
  }

  /* Result title block */
  .result {
    margin-top: 10px;
    border: 2px solid var(--brass);
    padding: 26px 28px;
    position: relative;
    background: rgba(201, 162, 39, 0.05);
  }

  .result::before {
    content: 'EST.';
    position: absolute;
    top: -11px;
    left: 20px;
    background: var(--navy-deep);
    padding: 0 8px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.15em;
    color: var(--brass);
  }

  .result-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 12px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--brass-dim);
    margin-bottom: 6px;
  }

  .result-value {
    font-size: clamp(36px, 6vw, 54px);
    font-weight: 700;
    color: var(--brass);
    font-variant-numeric: tabular-nums;
    letter-spacing: -0.01em;
  }

  .result-range {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 12px;
    color: var(--line);
    margin-top: 10px;
  }

  /* Breakdown */
  .breakdown {
    margin-top: 28px;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .bd-row {
    display: grid;
    grid-template-columns: 90px 1fr 100px;
    align-items: center;
    gap: 12px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 12px;
    color: var(--line);
  }

  .bd-bar-track {
    height: 6px;
    background: var(--line-faint);
    position: relative;
  }

  .bd-bar-fill {
    height: 100%;
    background: var(--brass);
    transition: width 0.25s ease;
  }

  .bd-val {
    text-align: right;
    color: var(--paper);
  }

  footer {
    margin-top: 56px;
    padding-top: 20px;
    border-top: 1px solid var(--line-faint);
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    color: var(--line);
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 10px;
  }

  @media (prefers-reduced-motion: reduce) {
    .bd-bar-fill { transition: none; }
  }

  input[type="range"]:focus-visible::-webkit-slider-thumb {
    outline: 2px solid var(--paper);
    outline-offset: 2px;
  }
  input[type="range"]:focus-visible {
    outline: none;
  }
</style>
</head>
<body>
<div class="wrap">

  <header>
    <div>
      <div class="eyebrow">Drawing No. HV-01 &nbsp;·&nbsp; Scale N.T.S.</div>
      <h1>House Value<br>Estimator</h1>
    </div>
    <div class="rev">
      MODEL <b>Linear Regression</b><br>
      TRAINED ON <b>300 records</b><br>
      R² <b>0.80</b>
    </div>
  </header>

  <div class="grid">

    <div class="plan-panel">
      <svg viewBox="0 0 400 300" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Outer walls -->
        <rect x="30" y="30" width="340" height="240" stroke="#5c86a8" stroke-width="2"/>
        <!-- Interior walls: living / bed / bed / bath -->
        <line x1="30" y1="150" x2="230" y2="150" stroke="#3a6285" stroke-width="1.5"/>
        <line x1="230" y1="30" x2="230" y2="270" stroke="#3a6285" stroke-width="1.5"/>
        <line x1="230" y1="180" x2="370" y2="180" stroke="#3a6285" stroke-width="1.5"/>
        <line x1="300" y1="180" x2="300" y2="270" stroke="#3a6285" stroke-width="1.5"/>

        <!-- Door swings -->
        <path d="M230 150 A 40 40 0 0 1 190 190" stroke="#2a4a66" stroke-width="1" fill="none"/>
        <path d="M300 180 A 30 30 0 0 1 270 210" stroke="#2a4a66" stroke-width="1" fill="none"/>

        <!-- Room labels -->
        <text x="115" y="95" fill="#8fb3d1" font-family="IBM Plex Mono, monospace" font-size="11" letter-spacing="1">LIVING</text>
        <text x="115" y="215" fill="#8fb3d1" font-family="IBM Plex Mono, monospace" font-size="11" letter-spacing="1">BEDROOM A</text>
        <text x="255" y="70" fill="#8fb3d1" font-family="IBM Plex Mono, monospace" font-size="11" letter-spacing="1">KITCHEN</text>
        <text x="245" y="215" fill="#8fb3d1" font-family="IBM Plex Mono, monospace" font-size="11" letter-spacing="1" id="plan-bed2">BEDROOM B</text>
        <text x="315" y="240" fill="#8fb3d1" font-family="IBM Plex Mono, monospace" font-size="10" letter-spacing="1" id="plan-bath">BATH</text>

        <!-- Dimension line along the top -->
        <line x1="30" y1="15" x2="370" y2="15" stroke="#3a6285" stroke-width="1"/>
        <line x1="30" y1="10" x2="30" y2="20" stroke="#3a6285" stroke-width="1"/>
        <line x1="370" y1="10" x2="370" y2="20" stroke="#3a6285" stroke-width="1"/>
        <text x="175" y="10" fill="#5c86a8" font-family="IBM Plex Mono, monospace" font-size="10" id="plan-width">— SQ FT —</text>

        <!-- fixtures that toggle with bathroom count -->
        <g id="bath-fixtures"></g>
        <g id="bed-fixtures"></g>
      </svg>
      <div class="plan-caption">
        <span>FLOOR PLAN — SCHEMATIC</span>
        <span id="plan-tag">2200 SF · 3 BR · 2.5 BA</span>
      </div>
    </div>

    <div class="controls">

      <div class="field">
        <div class="field-label">
          <span class="field-name">Square Footage</span>
          <span class="field-value"><span id="sqftVal">2200</span><span class="unit">sq ft</span></span>
        </div>
        <div class="dim">
          <div class="dim-line"></div>
          <div class="dim-ticks">
            <span></span><span></span><span></span><span></span><span></span>
            <span></span><span></span><span></span><span></span>
          </div>
          <input type="range" id="sqft" min="400" max="3700" step="10" value="2200">
        </div>
        <div class="dim-minmax"><span>400</span><span>3,700</span></div>
      </div>

      <div class="field">
        <div class="field-label">
          <span class="field-name">Bedrooms</span>
          <span class="field-value"><span id="bedVal">3</span></span>
        </div>
        <div class="dim">
          <div class="dim-line"></div>
          <div class="dim-ticks">
            <span></span><span></span><span></span><span></span><span></span>
          </div>
          <input type="range" id="bedrooms" min="1" max="5" step="1" value="3">
        </div>
        <div class="dim-minmax"><span>1</span><span>5</span></div>
      </div>

      <div class="field">
        <div class="field-label">
          <span class="field-name">Bathrooms</span>
          <span class="field-value"><span id="bathVal">2.5</span></span>
        </div>
        <div class="dim">
          <div class="dim-line"></div>
          <div class="dim-ticks">
            <span></span><span></span><span></span><span></span><span></span><span></span><span></span>
          </div>
          <input type="range" id="bathrooms" min="1" max="4" step="0.5" value="2.5">
        </div>
        <div class="dim-minmax"><span>1</span><span>4</span></div>
      </div>

      <div class="result">
        <div class="result-label">Estimated Value</div>
        <div class="result-value" id="priceOut">$288,880</div>
        <div class="result-range" id="rangeOut">± $26,700 typical error (RMSE)</div>
      </div>

      <div class="breakdown" id="breakdown"></div>

    </div>
  </div>

  <footer>
    <span>MODEL: price ≈ 80.47·sqft + 13,169·bed + 19,963·bath + 19,992</span>
    <span>NOT AN APPRAISAL — DEMONSTRATION ONLY</span>
  </footer>
</div>

<script>
  // Coefficients from the trained scikit-learn LinearRegression model
  const COEF = { sqft: 80.46514573, bedrooms: 13168.85684523, bathrooms: 19963.03735888 };
  const INTERCEPT = 19992.454386122263;
  const RMSE = 26703;

  const sqftEl = document.getElementById('sqft');
  const bedEl = document.getElementById('bedrooms');
  const bathEl = document.getElementById('bathrooms');

  const sqftVal = document.getElementById('sqftVal');
  const bedVal = document.getElementById('bedVal');
  const bathVal = document.getElementById('bathVal');
  const priceOut = document.getElementById('priceOut');
  const rangeOut = document.getElementById('rangeOut');
  const breakdown = document.getElementById('breakdown');
  const planTag = document.getElementById('plan-tag');
  const planWidth = document.getElementById('plan-width');

  function fmt(n) {
    return '$' + Math.round(n).toLocaleString('en-US');
  }

  function render() {
    const sqft = parseFloat(sqftEl.value);
    const bed = parseInt(bedEl.value, 10);
    const bath = parseFloat(bathEl.value);

    sqftVal.textContent = sqft.toLocaleString('en-US');
    bedVal.textContent = bed;
    bathVal.textContent = bath.toFixed(1).replace('.0', bath % 1 === 0 ? '' : '.5');

    const contribSqft = COEF.sqft * sqft;
    const contribBed = COEF.bedrooms * bed;
    const contribBath = COEF.bathrooms * bath;
    const total = contribSqft + contribBed + contribBath + INTERCEPT;

    priceOut.textContent = fmt(total);
    rangeOut.textContent = `${fmt(total - RMSE)} – ${fmt(total + RMSE)} typical range`;

    const parts = [
      { label: 'BASE', value: INTERCEPT },
      { label: 'SQ FT', value: contribSqft },
      { label: 'BEDS', value: contribBed },
      { label: 'BATHS', value: contribBath },
    ];
    const max = Math.max(...parts.map(p => p.value));

    breakdown.innerHTML = parts.map(p => `
      <div class="bd-row">
        <span>${p.label}</span>
        <div class="bd-bar-track"><div class="bd-bar-fill" style="width:${Math.max(2, (p.value / max) * 100)}%"></div></div>
        <span class="bd-val">${fmt(p.value)}</span>
      </div>
    `).join('');

    planTag.textContent = `${sqft.toLocaleString('en-US')} SF · ${bed} BR · ${bath} BA`;
    planWidth.textContent = `— ${sqft.toLocaleString('en-US')} SF —`;
  }

  [sqftEl, bedEl, bathEl].forEach(el => el.addEventListener('input', render));
  render();
</script>
</body>
</html>
'''


def main():
    out = Path(__file__).with_name('ml_task1_output.html')
    out.write_text(HTML, encoding='utf-8')
    print(f'Wrote HTML to {out}')
    webbrowser.open(out.resolve().as_uri())


if __name__ == '__main__':
    main()
