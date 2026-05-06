(function () {
  'use strict';

  /* ── CSS ── */
  var style = document.createElement('style');
  style.textContent = [
    '#dms-scroll-top {',
    '  position: fixed;',
    '  bottom: 32px;',
    '  right: 90px;',
    '  width: 52px;',
    '  height: 52px;',
    '  border-radius: 50%;',
    '  background: var(--card-dark, #0D1826);',
    '  border: 1px solid var(--card-border, #1E3055);',
    '  cursor: pointer;',
    '  z-index: 9990;',
    '  display: flex;',
    '  align-items: center;',
    '  justify-content: center;',
    '  padding: 0;',
    '  opacity: 0;',
    '  transform: translateY(16px);',
    '  pointer-events: none;',
    '  transition: opacity 0.35s ease, transform 0.35s ease,',
    '              background 0.25s ease, border-color 0.25s ease,',
    '              box-shadow 0.25s ease;',
    '}',
    '#dms-scroll-top.dms-visible {',
    '  opacity: 1;',
    '  transform: translateY(0);',
    '  pointer-events: auto;',
    '}',
    '#dms-scroll-top:hover {',
    '  background: var(--klein-blue, #002FA7);',
    '  border-color: var(--klein-blue, #002FA7);',
    '  box-shadow: 0 8px 32px rgba(0, 47, 167, 0.45);',
    '}',
    '#dms-scroll-top:hover .dms-arrow-icon {',
    '  transform: translateY(-2px);',
    '}',
    '.dms-arrow-icon {',
    '  position: absolute;',
    '  transition: transform 0.2s ease;',
    '  display: flex;',
    '  align-items: center;',
    '  justify-content: center;',
    '}',
    '#dms-scroll-top svg.dms-ring {',
    '  position: absolute;',
    '  top: 0;',
    '  left: 0;',
    '  width: 52px;',
    '  height: 52px;',
    '  transform: rotate(-90deg);',
    '}',
    /* Light mode overrides */
    '@media (prefers-color-scheme: light) {',
    '  #dms-scroll-top {',
    '    background: #ffffff;',
    '    border-color: #d1dae8;',
    '  }',
    '  #dms-scroll-top:hover {',
    '    background: var(--klein-blue, #002FA7);',
    '    border-color: var(--klein-blue, #002FA7);',
    '    box-shadow: 0 8px 32px rgba(0, 47, 167, 0.45);',
    '  }',
    '}',
    /* Class-based light mode (for sites that use data-theme or .light class) */
    '[data-theme="light"] #dms-scroll-top,',
    '.light #dms-scroll-top {',
    '  background: #ffffff;',
    '  border-color: #d1dae8;',
    '}',
    /* Mobile */
    '@media (max-width: 768px) {',
    '  #dms-scroll-top {',
    '    bottom: 80px;',
    '    right: 16px;',
    '  }',
    '}'
  ].join('\n');
  document.head.appendChild(style);

  /* ── Constants ── */
  var RADIUS = 22;
  var CIRCUMFERENCE = 2 * Math.PI * RADIUS; // ~138.23

  /* ── Build button ── */
  var btn = document.createElement('button');
  btn.id = 'dms-scroll-top';
  btn.setAttribute('aria-label', 'Scroll to top');
  btn.setAttribute('title', 'Back to top');

  /* Progress ring SVG */
  var ringNS = 'http://www.w3.org/2000/svg';
  var ringSVG = document.createElementNS(ringNS, 'svg');
  ringSVG.setAttribute('class', 'dms-ring');
  ringSVG.setAttribute('viewBox', '0 0 52 52');
  ringSVG.setAttribute('aria-hidden', 'true');

  /* Background track circle (faint) */
  var trackCircle = document.createElementNS(ringNS, 'circle');
  trackCircle.setAttribute('cx', '26');
  trackCircle.setAttribute('cy', '26');
  trackCircle.setAttribute('r', String(RADIUS));
  trackCircle.setAttribute('fill', 'none');
  trackCircle.setAttribute('stroke', 'rgba(229,168,32,0.15)');
  trackCircle.setAttribute('stroke-width', '2');
  ringSVG.appendChild(trackCircle);

  /* Progress arc */
  var progressCircle = document.createElementNS(ringNS, 'circle');
  progressCircle.setAttribute('cx', '26');
  progressCircle.setAttribute('cy', '26');
  progressCircle.setAttribute('r', String(RADIUS));
  progressCircle.setAttribute('fill', 'none');
  progressCircle.setAttribute('stroke', '#E5A820');
  progressCircle.setAttribute('stroke-width', '2');
  progressCircle.setAttribute('stroke-linecap', 'round');
  progressCircle.setAttribute('stroke-dasharray', String(CIRCUMFERENCE));
  progressCircle.setAttribute('stroke-dashoffset', String(CIRCUMFERENCE));
  ringSVG.appendChild(progressCircle);

  btn.appendChild(ringSVG);

  /* Upward arrow icon */
  var arrowWrap = document.createElement('span');
  arrowWrap.className = 'dms-arrow-icon';

  var arrowSVG = document.createElementNS(ringNS, 'svg');
  arrowSVG.setAttribute('viewBox', '0 0 16 16');
  arrowSVG.setAttribute('width', '16');
  arrowSVG.setAttribute('height', '16');
  arrowSVG.setAttribute('fill', 'none');
  arrowSVG.setAttribute('aria-hidden', 'true');

  var arrowPath = document.createElementNS(ringNS, 'path');
  arrowPath.setAttribute('d', 'M8 13V3M3 8l5-5 5 5');
  arrowPath.setAttribute('stroke', '#E5A820');
  arrowPath.setAttribute('stroke-width', '1.75');
  arrowPath.setAttribute('stroke-linecap', 'round');
  arrowPath.setAttribute('stroke-linejoin', 'round');

  arrowSVG.appendChild(arrowPath);
  arrowWrap.appendChild(arrowSVG);
  btn.appendChild(arrowWrap);

  document.body.appendChild(btn);

  /* ── Scroll logic ── */
  function getScrollPercent() {
    var scrollTop = window.scrollY || document.documentElement.scrollTop;
    var docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    if (docHeight <= 0) return 0;
    return scrollTop / docHeight;
  }

  function onScroll() {
    var scrollY = window.scrollY || document.documentElement.scrollTop;

    /* Show / hide */
    if (scrollY > 300) {
      btn.classList.add('dms-visible');
    } else {
      btn.classList.remove('dms-visible');
    }

    /* Update ring */
    var pct = getScrollPercent();
    var offset = CIRCUMFERENCE * (1 - pct);
    progressCircle.setAttribute('stroke-dashoffset', String(offset));
  }

  window.addEventListener('scroll', onScroll, { passive: true });

  /* ── Click → smooth scroll to top ── */
  btn.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}());
