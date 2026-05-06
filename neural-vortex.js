/* DMS Neural Vortex Background — vanilla canvas, no dependencies
   Klein Blue nodes (#002FA7) + Amber Gold accents (#E5A820)
   z-index:1 + mix-blend-mode:screen (glows on dark, invisible on light)
   index.html: triggers after #services enters view (hero excluded)
   All other pages: starts immediately on load
   Respects prefers-reduced-motion
*/
(function () {
  'use strict';

  var C = {
    node:    '0,47,167',     // Klein Blue
    accent:  '229,168,32',   // Amber Gold
    line:    '36,59,110',    // Cobalt for lines
    accentLine: '229,168,32'
  };

  var CFG = {
    count:       100,
    connectDist: 145,
    speed:       0.28,
    mouseR:      130,
    mouseF:      0.55,
    vortex:      0.012,
    accentRatio: 0.07,
    minR:        1.4,
    maxR:        3.2,
    lineAlpha:   0.25,
    nodeAlpha:   0.9
  };

  var canvas, ctx, nodes = [], mouse = { x: -9999, y: -9999 };
  var raf, running = false, W, H;

  /* ---- Canvas setup ---- */
  function buildCanvas() {
    canvas = document.createElement('canvas');
    canvas.id = 'vortex-canvas';
    canvas.setAttribute('aria-hidden', 'true');
    canvas.style.cssText =
      'position:fixed;top:0;left:0;width:100%;height:100%;' +
      'z-index:1;pointer-events:none;opacity:0;' +
      'mix-blend-mode:screen;transition:opacity 1.4s ease;';
    document.body.appendChild(canvas);
    ctx = canvas.getContext('2d');
    resize();
  }

  function resize() {
    W = canvas.width  = window.innerWidth;
    H = canvas.height = window.innerHeight;
  }

  /* ---- Node class ---- */
  function Node() { this.init(true); }

  Node.prototype.init = function (scatter) {
    this.x  = scatter ? Math.random() * W : (Math.random() < 0.5 ? -12 : W + 12);
    this.y  = scatter ? Math.random() * H : (Math.random() < 0.5 ? -12 : H + 12);
    this.vx = (Math.random() - 0.5) * CFG.speed;
    this.vy = (Math.random() - 0.5) * CFG.speed;
    this.r  = CFG.minR + Math.random() * (CFG.maxR - CFG.minR);
    this.isAccent = Math.random() < CFG.accentRatio;
    this.col  = this.isAccent ? C.accent : C.node;
    this.opa  = 0.45 + Math.random() * 0.55;
    this.ang  = Math.random() * Math.PI * 2;
    this.spin = (Math.random() - 0.5) * CFG.vortex;
  };

  Node.prototype.tick = function () {
    /* gentle vortex drift */
    this.ang += this.spin;
    this.vx  += Math.cos(this.ang) * 0.0028;
    this.vy  += Math.sin(this.ang) * 0.0028;

    /* mouse repulsion */
    var dx = this.x - mouse.x, dy = this.y - mouse.y;
    var d  = Math.sqrt(dx * dx + dy * dy);
    if (d < CFG.mouseR && d > 0.5) {
      var f = (1 - d / CFG.mouseR) * CFG.mouseF;
      this.vx += (dx / d) * f * 0.45;
      this.vy += (dy / d) * f * 0.45;
    }

    /* dampen */
    this.vx *= 0.979;
    this.vy *= 0.979;

    this.x += this.vx;
    this.y += this.vy;

    /* wrap */
    if (this.x < -14) this.x = W + 14;
    if (this.x > W + 14) this.x = -14;
    if (this.y < -14) this.y = H + 14;
    if (this.y > H + 14) this.y = -14;
  };

  Node.prototype.draw = function () {
    var a = this.opa * CFG.nodeAlpha;
    /* glow halo */
    var g = ctx.createRadialGradient(this.x, this.y, 0, this.x, this.y, this.r * 4);
    g.addColorStop(0,   'rgba(' + this.col + ',' + (a * 0.6) + ')');
    g.addColorStop(0.5, 'rgba(' + this.col + ',' + (a * 0.2) + ')');
    g.addColorStop(1,   'rgba(' + this.col + ',0)');
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.r * 4, 0, 6.283);
    ctx.fillStyle = g;
    ctx.fill();
    /* solid core */
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.r, 0, 6.283);
    ctx.fillStyle = 'rgba(' + this.col + ',' + a + ')';
    ctx.fill();
  };

  /* ---- Draw connections ---- */
  function drawLines() {
    var cd = CFG.connectDist;
    for (var i = 0; i < nodes.length; i++) {
      for (var j = i + 1; j < nodes.length; j++) {
        var dx = nodes[i].x - nodes[j].x;
        var dy = nodes[i].y - nodes[j].y;
        var d  = Math.sqrt(dx * dx + dy * dy);
        if (d < cd) {
          var a   = (1 - d / cd) * CFG.lineAlpha;
          var col = (nodes[i].isAccent || nodes[j].isAccent) ? C.accentLine : C.line;
          ctx.beginPath();
          ctx.moveTo(nodes[i].x, nodes[i].y);
          ctx.lineTo(nodes[j].x, nodes[j].y);
          ctx.strokeStyle = 'rgba(' + col + ',' + a + ')';
          ctx.lineWidth   = 0.75;
          ctx.stroke();
        }
      }
    }
  }

  /* ---- Loop ---- */
  function loop() {
    if (!running) return;
    ctx.clearRect(0, 0, W, H);
    drawLines();
    for (var i = 0; i < nodes.length; i++) {
      nodes[i].tick();
      nodes[i].draw();
    }
    raf = requestAnimationFrame(loop);
  }

  function makeNodes() {
    nodes = [];
    for (var i = 0; i < CFG.count; i++) nodes.push(new Node());
  }

  /* ---- Start / stop ---- */
  function start() {
    if (running) return;
    running = true;
    canvas.style.opacity = '1';
    loop();
  }

  function stop() {
    running = false;
    canvas.style.opacity = '0';
    cancelAnimationFrame(raf);
  }

  /* ---- Init ---- */
  function init() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    buildCanvas();
    makeNodes();

    window.addEventListener('resize', function () { resize(); makeNodes(); });

    window.addEventListener('mousemove', function (e) {
      mouse.x = e.clientX; mouse.y = e.clientY;
    });
    window.addEventListener('mouseleave', function () {
      mouse.x = -9999; mouse.y = -9999;
    });
    window.addEventListener('touchmove', function (e) {
      var t = e.touches[0];
      mouse.x = t.clientX; mouse.y = t.clientY;
    }, { passive: true });

    /* Scoping:
       index.html has <section id="hero"> — defer until #services enters view.
       All other pages start immediately. */
    var heroEl    = document.getElementById('hero');
    var servicesEl = document.getElementById('services');

    if (heroEl && servicesEl) {
      /* Homepage: wait until services section crosses viewport */
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { start(); io.disconnect(); }
        });
      }, { threshold: 0.05 });
      io.observe(servicesEl);
    } else {
      /* Every other page: start on load */
      start();
    }
  }

  /* Run after DOM ready */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
}());
