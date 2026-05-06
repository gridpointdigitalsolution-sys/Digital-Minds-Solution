/* ============================================================
   DMS PROMO POPUP — exit-intent + time-on-page trigger
   Fires once per session. Two triggers:
     1) Exit intent (mouse leaves top of viewport)
     2) After 45 seconds on page
   Suppressed on /contact.html (already CTA-heavy).
   ============================================================ */
(function () {
  'use strict';

  // Skip on contact page (user already booking)
  var path = location.pathname.toLowerCase();
  if (path.indexOf('contact') !== -1) return;

  // Skip if previously dismissed this session
  try {
    if (sessionStorage.getItem('dms-promo-dismissed') === '1') return;
  } catch (e) {}

  var BOOK_URL    = 'https://meet.google.com/qrs-uxig-cwo';
  var CONTACT_URL = 'contact.html';
  var TIME_DELAY  = 45000; // ms

  var fired = false;
  var overlay = null;
  var timerId = null;

  function build() {
    var ov = document.createElement('div');
    ov.id = 'dms-promo-overlay';
    ov.setAttribute('role', 'dialog');
    ov.setAttribute('aria-modal', 'true');
    ov.setAttribute('aria-labelledby', 'dmsPromoTitle');

    ov.innerHTML =
      '<div id="dms-promo-card">' +
        '<button class="dms-promo-close" aria-label="Close popup">&times;</button>' +
        '<div class="dms-promo-eyebrow"><span class="dms-pulse"></span>Free Strategy Session</div>' +
        '<h2 id="dmsPromoTitle">Hello! Are you ready to <span class="dms-promo-gold">start your project</span>?</h2>' +
        '<p class="dms-promo-sub">Jump on a free 30-minute call with our team. No pitch deck, no commitment. Just a clear conversation about your goals and what we\'d do about them.</p>' +
        '<a class="dms-promo-cta" href="' + BOOK_URL + '" target="_blank" rel="noopener">' +
          'Book My Free Call <span aria-hidden="true">&rarr;</span>' +
        '</a>' +
        '<button type="button" class="dms-promo-cta-secondary" id="dmsPromoSendMsg">Or send us a message instead</button>' +
        '<div class="dms-promo-trust">' +
          '<span>&#10003; 30-minute call</span>' +
          '<span>&#10003; No sales pitch</span>' +
          '<span>&#10003; Honest fit assessment</span>' +
        '</div>' +
      '</div>';

    document.body.appendChild(ov);
    return ov;
  }

  function show() {
    if (fired) return;
    fired = true;
    overlay = build();
    // Force reflow so transition runs
    overlay.offsetHeight;
    overlay.classList.add('dms-promo-show');
    document.body.style.overflow = 'hidden';

    // Wire close handlers
    overlay.querySelector('.dms-promo-close').addEventListener('click', dismiss);
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) dismiss();
    });
    overlay.querySelector('#dmsPromoSendMsg').addEventListener('click', function () {
      try { sessionStorage.setItem('dms-promo-dismissed', '1'); } catch (e) {}
      window.location.href = CONTACT_URL;
    });
    document.addEventListener('keydown', escClose);

    // CTA click counts as conversion + dismiss
    overlay.querySelector('.dms-promo-cta').addEventListener('click', function () {
      try { sessionStorage.setItem('dms-promo-dismissed', '1'); } catch (e) {}
    });
  }

  function dismiss() {
    if (!overlay) return;
    overlay.classList.remove('dms-promo-show');
    document.body.style.overflow = '';
    document.removeEventListener('keydown', escClose);
    try { sessionStorage.setItem('dms-promo-dismissed', '1'); } catch (e) {}
    setTimeout(function () {
      if (overlay && overlay.parentNode) overlay.parentNode.removeChild(overlay);
    }, 400);
  }

  function escClose(e) {
    if (e.key === 'Escape' || e.keyCode === 27) dismiss();
  }

  // Trigger 1: time on page
  function init() {
    timerId = setTimeout(show, TIME_DELAY);

    // Trigger 2: exit intent (desktop only)
    if (window.matchMedia('(pointer: coarse)').matches) return;
    document.addEventListener('mouseout', function (e) {
      if (fired) return;
      // Mouse left through the top edge of the viewport
      if (!e.relatedTarget && e.clientY <= 0) {
        clearTimeout(timerId);
        show();
      }
    });
  }

  if (document.body) init();
  else document.addEventListener('DOMContentLoaded', init);
})();
