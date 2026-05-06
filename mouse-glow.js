/* ============================================================
   DMS MOUSE GLOW — gold radial spotlight following the cursor
   Skipped on touch devices, reduced-motion users, and screens
   under 900px wide.
   ============================================================ */
(function () {
  'use strict';

  // Bail on touch / reduced-motion / small screens
  if (window.matchMedia('(pointer: coarse)').matches) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (window.innerWidth < 900) return;

  function init() {
    if (document.getElementById('dms-mouse-glow')) return;

    var glow = document.createElement('div');
    glow.id = 'dms-mouse-glow';
    glow.setAttribute('aria-hidden', 'true');
    document.body.appendChild(glow);

    var x = window.innerWidth / 2;
    var y = window.innerHeight / 2;
    var tx = x, ty = y;
    var rafId = null;

    function tick() {
      // Smooth easing toward target
      x += (tx - x) * 0.18;
      y += (ty - y) * 0.18;
      glow.style.transform = 'translate(' + (x - 250) + 'px,' + (y - 250) + 'px)';
      rafId = requestAnimationFrame(tick);
    }

    document.addEventListener('mousemove', function (e) {
      tx = e.clientX;
      ty = e.clientY;
      glow.style.opacity = '1';
      if (!rafId) rafId = requestAnimationFrame(tick);
    }, { passive: true });

    document.addEventListener('mouseleave', function () {
      glow.style.opacity = '0';
    });

    // Boost the glow when hovering interactive elements
    var INTERACTIVE = 'a, button, .btn, [role="button"], .case-card, .service-card, .article-card, .pricing-card, .nav-cta, .btn-gold, .btn-ghost, input, textarea, select';
    document.addEventListener('mouseover', function (e) {
      if (e.target.closest(INTERACTIVE)) {
        glow.classList.add('dms-glow-hot');
      }
    });
    document.addEventListener('mouseout', function (e) {
      if (e.target.closest(INTERACTIVE)) {
        glow.classList.remove('dms-glow-hot');
      }
    });
  }

  if (document.body) init();
  else document.addEventListener('DOMContentLoaded', init);
})();
