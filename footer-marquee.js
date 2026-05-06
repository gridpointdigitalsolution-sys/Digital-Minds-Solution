/* DMS Footer Marquee — "Let's Talk" infinite scroll strip
   Injects a full-width ticker ABOVE the footer grid on every page.
   Pure CSS animation, no dependencies.
   Also applies nurui-style hover effects to all footer links.
*/
(function () {
  'use strict';

  /* ---- Inject CSS ---- */
  var style = document.createElement('style');
  style.textContent = [

    /* ========================================================
       MARQUEE STRIP — positioned at very top of #footer
    ======================================================== */
    '.dms-marquee-strip {',
    '  width: 100%;',
    '  overflow: hidden;',
    '  border-bottom: 1px solid rgba(30,48,85,.6);',
    '  padding: 28px 0;',
    '  margin-bottom: 72px;',   /* pushes footer grid down */
    '  background: transparent;',
    '  cursor: default;',
    '  user-select: none;',
    '}',

    '.dms-marquee-inner {',
    '  display: flex;',
    '  width: max-content;',
    '  animation: dmsMarqueeScroll 18s linear infinite;',
    '}',
    '.dms-marquee-inner:hover { animation-play-state: paused; }',

    '.dms-marquee-group {',
    '  display: flex;',
    '  align-items: center;',
    '  gap: 0;',
    '  flex-shrink: 0;',
    '}',

    '.dms-marquee-text {',
    '  font-family: "Plus Jakarta Sans", sans-serif;',
    '  font-size: clamp(48px, 6vw, 96px);',
    '  font-weight: 800;',
    '  letter-spacing: -.03em;',
    '  line-height: 1;',
    '  white-space: nowrap;',
    '  color: var(--white, #fff);',
    '  padding: 0 40px;',
    '  transition: color .25s ease;',
    '}',
    '.dms-marquee-inner:hover .dms-marquee-text {',
    '  color: var(--amber-gold, #E5A820);',
    '}',

    /* Diamond separator (DMS brand touch) */
    '.dms-marquee-sep {',
    '  display: flex;',
    '  align-items: center;',
    '  flex-shrink: 0;',
    '  padding: 0 16px;',
    '}',
    '.dms-marquee-sep svg {',
    '  width: 36px;',
    '  height: 36px;',
    '  flex-shrink: 0;',
    '}',

    /* Keyframe — scroll left by exactly 50% (one group width) for seamless loop */
    '@keyframes dmsMarqueeScroll {',
    '  0%   { transform: translateX(0); }',
    '  100% { transform: translateX(-50%); }',
    '}',

    '@media (prefers-reduced-motion: reduce) {',
    '  .dms-marquee-inner { animation: none; }',
    '}',

    /* ========================================================
       NURUI FOOTER HOVER — link reveal + column accents
    ======================================================== */

    /* Footer column title: amber underline draws on hover */
    '.footer-col-title {',
    '  position: relative;',
    '  padding-bottom: 10px;',
    '}',
    '.footer-col-title::after {',
    '  content: "";',
    '  position: absolute;',
    '  bottom: 0; left: 0;',
    '  width: 0; height: 1.5px;',
    '  background: var(--amber-gold, #E5A820);',
    '  border-radius: 2px;',
    '  transition: width .45s cubic-bezier(.16,1,.3,1);',
    '}',
    '.footer-col:hover .footer-col-title::after { width: 40px; }',

    /* Footer links: slide-in background + arrow reveal */
    '.footer-col ul li {',
    '  position: relative;',
    '  border-radius: 6px;',
    '  margin: 0 -8px;',
    '  padding: 0 8px;',
    '}',
    '.footer-col ul li::before {',
    '  content: "";',
    '  position: absolute;',
    '  inset: 0;',
    '  border-radius: inherit;',
    '  background: rgba(0,47,167,.14);',
    '  transform: scaleX(0);',
    '  transform-origin: left;',
    '  transition: transform .32s cubic-bezier(.16,1,.3,1);',
    '}',
    '.footer-col ul li:hover::before { transform: scaleX(1); }',

    '.footer-col ul a {',
    '  position: relative;',
    '  z-index: 1;',
    '  display: flex;',
    '  align-items: center;',
    '  gap: 0;',
    '  transition: color .2s ease, gap .3s cubic-bezier(.16,1,.3,1), padding-left .3s cubic-bezier(.16,1,.3,1);',
    '}',
    '.footer-col ul a::before {',
    '  content: "→";',
    '  font-size: 12px;',
    '  color: var(--amber-gold, #E5A820);',
    '  opacity: 0;',
    '  max-width: 0;',
    '  overflow: hidden;',
    '  transition: opacity .25s ease, max-width .3s cubic-bezier(.16,1,.3,1);',
    '  white-space: nowrap;',
    '  margin-right: 0;',
    '}',
    '.footer-col ul li:hover a::before {',
    '  opacity: 1;',
    '  max-width: 20px;',
    '  margin-right: 6px;',
    '}',
    '.footer-col ul a:hover { color: var(--white, #fff); }',

    /* Social links: bounce + tint */
    '.social-link {',
    '  transition: transform .3s cubic-bezier(.34,1.56,.64,1), background .25s ease, color .25s ease !important;',
    '}',
    '.social-link:hover {',
    '  transform: translateY(-4px) scale(1.12) !important;',
    '  background: var(--klein-blue, #002FA7) !important;',
    '  color: var(--white, #fff) !important;',
    '  border-color: var(--klein-blue, #002FA7) !important;',
    '}',

    /* Light mode adjustments */
    '[data-theme="light"] .dms-marquee-text { color: var(--deep-space, #08101E); }',
    '[data-theme="light"] .dms-marquee-inner:hover .dms-marquee-text { color: var(--klein-blue, #002FA7); }',
    '[data-theme="light"] .footer-col ul li::before { background: rgba(0,47,167,.08); }',

  ].join('\n');
  document.head.appendChild(style);

  /* ---- Build + inject the marquee strip ---- */
  function buildMarquee() {
    var footer = document.getElementById('footer');
    if (!footer) return;

    /* Separator SVG — diamond/star in brand blue */
    var sepSVG = [
      '<svg viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">',
      '  <polygon points="18,2 34,18 18,34 2,18" fill="rgba(0,47,167,0.7)" stroke="rgba(229,168,32,0.5)" stroke-width="1"/>',
      '  <polygon points="18,8 28,18 18,28 8,18" fill="rgba(229,168,32,0.5)"/>',
      '</svg>'
    ].join('');

    /* One group: 3× "Let's Talk" with separators */
    function group() {
      return [
        '<div class="dms-marquee-group">',
        '  <span class="dms-marquee-text">Let\'s Talk</span>',
        '  <span class="dms-marquee-sep">' + sepSVG + '</span>',
        '  <span class="dms-marquee-text">Let\'s Talk</span>',
        '  <span class="dms-marquee-sep">' + sepSVG + '</span>',
        '  <span class="dms-marquee-text">Let\'s Talk</span>',
        '  <span class="dms-marquee-sep">' + sepSVG + '</span>',
        '</div>'
      ].join('');
    }

    /* Two identical groups for seamless loop (translateX -50%) */
    var strip = document.createElement('div');
    strip.className = 'dms-marquee-strip';
    strip.innerHTML = '<div class="dms-marquee-inner">' + group() + group() + '</div>';

    /* Insert as FIRST child of #footer (above .container) */
    footer.insertBefore(strip, footer.firstChild);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', buildMarquee);
  } else {
    buildMarquee();
  }
}());
