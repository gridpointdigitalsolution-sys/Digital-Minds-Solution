/* ============================================================
   DMS GLOBAL PAGE LOADER — loader.js
   Injects char-by-char gold text animation on every page load
   ============================================================ */
(function () {
  'use strict';

  var LINE1 = 'Digital Minds';
  var LINE2 = 'Solutions';
  var SUB   = 'Houston · Global';

  // Delay between each character appearing (ms)
  var CHAR_DELAY = 62;
  // Extra pause before sub-label appears
  var SUB_DELAY_AFTER_LAST = 120;
  // How long to hold after everything is visible
  var HOLD = 520;
  // Fade-out duration must match CSS transition (700ms)
  var FADE = 700;

  function buildLine(text, startIndex) {
    var frag = document.createDocumentFragment();
    var idx = startIndex;
    for (var i = 0; i < text.length; i++) {
      var ch = text[i];
      var span = document.createElement('span');
      if (ch === ' ') {
        span.className = 'dms-loader-char dms-space';
      } else {
        span.className = 'dms-loader-char';
        span.style.animationDelay = (idx * CHAR_DELAY) + 'ms';
        idx++;
      }
      span.textContent = ch;
      frag.appendChild(span);
    }
    return { frag: frag, nextIndex: idx };
  }

  function create() {
    var loader = document.createElement('div');
    loader.id = 'dms-loader';
    loader.setAttribute('aria-hidden', 'true');
    loader.setAttribute('role', 'presentation');

    // Line 1: "Digital Minds"
    var line1El = document.createElement('div');
    line1El.className = 'dms-loader-line';
    var b1 = buildLine(LINE1, 0);
    line1El.appendChild(b1.frag);
    loader.appendChild(line1El);

    // Line 2: "Solutions"
    var line2El = document.createElement('div');
    line2El.className = 'dms-loader-line';
    var b2 = buildLine(LINE2, b1.nextIndex);
    line2El.appendChild(b2.frag);
    loader.appendChild(line2El);

    var totalChars = b2.nextIndex;

    // Gold rule
    var rule = document.createElement('div');
    rule.className = 'dms-loader-rule';
    var ruleDelay = totalChars * CHAR_DELAY + SUB_DELAY_AFTER_LAST;
    rule.style.animationDelay = ruleDelay + 'ms';
    loader.appendChild(rule);

    // Logo mark — appears after rule
    var logoWrap = document.createElement('div');
    logoWrap.className = 'dms-loader-logo-wrap';
    logoWrap.style.cssText = 'opacity:0;margin-top:20px;animation:dmsSubIn 0.5s ease forwards;animation-delay:' + (ruleDelay + 120) + 'ms';
    var logoImg = document.createElement('img');
    logoImg.src = 'ASSETS/logo/logo-white.svg.png';
    logoImg.alt = 'Digital Minds Solutions';
    logoImg.style.cssText = 'height:36px;width:auto;opacity:0.55;filter:brightness(0) invert(1);display:block;margin:0 auto';
    logoWrap.appendChild(logoImg);
    loader.appendChild(logoWrap);

    // Sub label
    var sub = document.createElement('p');
    sub.className = 'dms-loader-sub';
    sub.textContent = SUB;
    sub.style.animationDelay = (ruleDelay + 80) + 'ms';
    loader.appendChild(sub);

    return { el: loader, totalChars: totalChars };
  }

  function init() {
    // Skip if already exists (hot reload safety)
    if (document.getElementById('dms-loader')) return;

    var result = create();
    var loader = result.el;
    var totalChars = result.totalChars;

    // Insert as first child of body
    var body = document.body;
    body.insertBefore(loader, body.firstChild);

    // Prevent scroll while loading
    body.style.overflow = 'hidden';

    // Calculate when to dismiss
    var lastCharTime = totalChars * CHAR_DELAY + 220; // +anim duration
    var subTime = lastCharTime + SUB_DELAY_AFTER_LAST + 500;
    var dismissAt = subTime + HOLD;

    setTimeout(function () {
      loader.classList.add('dms-out');
      body.style.overflow = '';
      setTimeout(function () {
        if (loader.parentNode) loader.parentNode.removeChild(loader);
      }, FADE + 100);
    }, dismissAt);
  }

  // Run immediately if DOM ready, otherwise wait
  if (document.body) {
    init();
  } else {
    document.addEventListener('DOMContentLoaded', init);
  }
})();
