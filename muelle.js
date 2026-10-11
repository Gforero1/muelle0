/* muelle0: idioma, relojes, agua con el 0 flotando y recorrido de las capturas. Sin dependencias. */
(function () {
  'use strict';
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---------- Idioma: el del dispositivo, o el que la persona elija ---------- */
  var EN = {
    'nav.trabajos': 'Work', 'nav.modo': 'How we work', 'nav.contacto': 'Contact',
    'titulo': '<b>Web studio.</b> We hand-build sites, catalogues and shops for small brands, and leave each one with its own admin so the owner can run it without us.',
    'reloj.raices': 'Venezuelan roots',
    'ir': 'See the work', 'pista': 'Grab it and throw it', 'pausa.on': 'Pause motion', 'pausa.off': 'Resume motion',
    'trabajos.t': 'Work', 'trabajos.p': 'Three sites live. Each capture is the real site, scrolling.',
    'k.tipo': 'Type', 'k.idiomas': 'Languages', 'k.pedido': 'Orders', 'k.plataforma': 'Platform', 'k.dominio': 'Domain', 'k.monedas': 'Currencies', 'k.catalogo': 'Catalogue',
    'ver': 'Visit the site',
    'c1.lugar': '001 · Lechería, Venezuela · Art',
    'c1.r': 'An art catalogue in Spanish and English. Every piece shows its measurements and price, and enquiries go straight to Adriana Moncayo on WhatsApp. Behind it sits an admin where she uploads a photo of a painting and sees it hung, to scale, in a room.',
    'c1.tipo': 'Catalogue with private admin', 'c1.pedido': 'Enquiry by WhatsApp, one piece at a time',
    'c2.lugar': '002 · Barcelona · UGC creator',
    'c2.r': 'Portfolio for a beauty UGC creator. Videos sorted by category, the brands she has worked with and a clear way to ask for a quote. In Spanish and English, on Shopify, on her own domain.',
    'c2.tipo': 'Video portfolio', 'c2.plataforma': 'Shopify, custom theme',
    'c3.lugar': '003 · Lechería, Venezuela · Physiotherapy',
    'c3.r': 'A shop with over 140 products and no payment gateway: customers build their order and send it by WhatsApp. Prices show in dollars and bolívares at the day\'s official BCV rate, and the owner changes products, prices and photos from her own admin.',
    'c3.tipo': 'Shop with WhatsApp ordering', 'c3.monedas': '$ and Bs, BCV rate updated automatically', 'c3.catalogo': 'Google Sheets with a private admin',
    'libre.n': '004 · Free berth', 'libre.t': 'This spot is open.', 'libre.p': 'Tell us what you sell and how people buy from you today. We reply with what we would build.', 'libre.a': 'Write to us',
    'modo.t': 'How we <em>work</em>',
    'p1.t': 'We look at what you already have', 'p1.p': 'Your Instagram, your logo, your photos and how people buy from you today. Colours, tone and structure come from there, not from a template.',
    'p2.t': 'We build it by hand', 'p2.p': 'Our own code, light, in the languages you need. If your business calls for Shopify, we build it on Shopify.',
    'p3.t': 'We leave it ready to run', 'p3.p': 'With a private admin to change prices, photos and products from your phone, without writing to us.',
    'p4.t': 'It stays in your name', 'p4.p': 'Domain, accounts and content are yours from day one.',
    'm1': 'Catalogues', 'm2': 'Portfolios', 'm3': 'Shops', 'm4': 'Private admins',
    'contacto.t': 'Contact', 'contacto.p': 'We answer in Spanish or English.',
    'pie': 'muelle0 · Web studio · Venezuelan roots'
  };
  var ES = {};
  $$('[data-i]').forEach(function (el) { ES[el.getAttribute('data-i')] = el.innerHTML; });
  ES['pausa.on'] = 'Pausar movimiento'; ES['pausa.off'] = 'Reanudar movimiento';
  var idioma = 'es';
  function leer() { try { return localStorage.getItem('m0-idioma'); } catch (e) { return null; } }
  function poner(l, guardar) {
    idioma = l === 'en' ? 'en' : 'es';
    var T = idioma === 'en' ? EN : ES;
    $$('[data-i]').forEach(function (el) { var k = el.getAttribute('data-i'); if (T[k] != null) el.innerHTML = T[k]; });
    document.documentElement.lang = idioma;
    $$('.idioma button').forEach(function (b) { b.setAttribute('aria-pressed', String(b.value === idioma)); });
    pintaPausa();
    if (guardar) { try { localStorage.setItem('m0-idioma', idioma); } catch (e) {} }
  }
  $$('.idioma button').forEach(function (b) { b.addEventListener('click', function () { poner(b.value, true); }); });

  /* ---------- Relojes ---------- */
  function hora(zona) {
    try { return new Intl.DateTimeFormat('es-ES', { hour: '2-digit', minute: '2-digit', hour12: false, timeZone: zona }).format(new Date()); }
    catch (e) { return ''; }
  }
  function relojes() {
    var a = $('#h-bcn'), b = $('#h-lch');
    if (a) a.textContent = hora('Europe/Madrid');
    if (b) b.textContent = hora('America/Caracas');
  }
  relojes(); setInterval(relojes, 20000);

  /* ---------- Pausa única para todo lo que se mueve ---------- */
  var pausado = false;
  var btnPausa = $('.pausa');
  function pintaPausa() {
    if (!btnPausa) return;
    var T = idioma === 'en' ? EN : ES;
    btnPausa.textContent = pausado ? T['pausa.off'] : T['pausa.on'];
    btnPausa.setAttribute('aria-pressed', String(pausado));
  }
  if (btnPausa) {
    if (reduce) btnPausa.hidden = true;
    btnPausa.addEventListener('click', function () {
      pausado = !pausado;
      document.body.classList.toggle('quieto', pausado);
      pintaPausa();
      if (!pausado) arranca();
    });
  }

  /* ---------- Capturas que se recorren solas mientras están en pantalla ---------- */
  var lienzos = $$('.lienzo');
  function mide(l) {
    var img = $('img', l); if (!img) return;
    var alto = l.clientHeight, total = img.clientHeight;
    l.style.setProperty('--alto', alto + 'px');
    l.style.setProperty('--seg', Math.max(12, Math.round((total - alto) / 34)) + 's');
  }
  lienzos.forEach(function (l) {
    var img = $('img', l);
    if (img.complete) mide(l); else img.addEventListener('load', function () { mide(l); });
  });
  addEventListener('resize', function () { lienzos.forEach(mide); });
  if ('IntersectionObserver' in window) {
    var vigia = new IntersectionObserver(function (es) {
      es.forEach(function (e) { e.target.classList.toggle('viva', e.isIntersecting); });
    }, { threshold: 0.25 });
    $$('.pantallas').forEach(function (p) { vigia.observe(p); });
  }

  /* ---------- Agua ---------- */
  var caja = $('.agua'), lona = caja && $('canvas', caja), flot = $('.flotador'), pista = $('.pista');
  var ctx, W = 0, H = 0, base = 0, N = 0, h = [], v = [], t = 0, enMarcha = false, visible = true;
  var PASO = 9;
  var c = { x: 0, y: 0, vx: 0, vy: 0, a: 0.12, va: 0, t: 90, alto: 150, coge: false, dentro: false };
  var VERDE = '#0F3B3A';

  function oleaje(x) { return 8 * Math.sin(x * 0.0075 + t * 0.9) + 4.5 * Math.sin(x * 0.019 - t * 1.35); }
  function resorte(x) {
    var f = x / PASO, i = Math.max(0, Math.min(N - 2, Math.floor(f))), r = f - i;
    return h[i] * (1 - r) + h[i + 1] * r;
  }
  function nivel(x) { return base + oleaje(x) + resorte(x); }
  function empuja(x, fuerza, ancho) {
    var i0 = Math.round(x / PASO);
    for (var k = -ancho; k <= ancho; k++) {
      var i = i0 + k; if (i < 0 || i >= N) continue;
      v[i] += fuerza * (1 - Math.abs(k) / (ancho + 1));
    }
  }
  function talla() {
    var r = caja.getBoundingClientRect(), dpr = Math.min(2, devicePixelRatio || 1);
    W = r.width; H = r.height; base = Math.max(46, H * 0.36);
    lona.width = Math.round(W * dpr); lona.height = Math.round(H * dpr);
    ctx = lona.getContext('2d'); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    var n = Math.ceil(W / PASO) + 2;
    if (n !== N) { N = n; h = []; v = []; for (var i = 0; i < N; i++) { h.push(0); v.push(0); } }
    c.t = Math.max(50, Math.min(86, W * 0.065)); c.alto = c.t * 1.77;
    flot.style.setProperty('--t', c.t + 'px');
    if (c.x === 0) { c.x = W * (W < 700 ? 0.7 : 0.6); c.y = reduce ? base - c.alto * 0.2 : -c.alto * 2.2; }
    c.x = Math.min(W - c.t * 0.5, Math.max(c.t * 0.5, c.x));
  }
  function fisica() {
    var i, K = 0.018, ROCE = 0.035, CONTAGIO = 0.2;
    for (i = 0; i < N; i++) { v[i] += -K * h[i] - ROCE * v[i]; h[i] += v[i]; }
    for (var p = 0; p < 3; p++) {
      for (i = 0; i < N; i++) {
        if (i > 0) { var d = CONTAGIO * (h[i] - h[i - 1]); v[i - 1] += d * 0.5; h[i - 1] += d * 0.5; }
        if (i < N - 1) { var e = CONTAGIO * (h[i] - h[i + 1]); v[i + 1] += e * 0.5; h[i + 1] += e * 0.5; }
      }
    }
    if (c.coge) return;
    var sup = nivel(c.x), hondo = (c.y + c.alto * 0.2) - sup;
    c.vy += 0.42; c.vx *= 0.994;
    if (hondo > 0) {
      if (!c.dentro && c.vy > 2.5) empuja(c.x, Math.min(26, c.vy * 2.1), 4);
      c.vy -= Math.min(hondo, c.alto * 0.6) * 0.013; c.vy *= 0.88; c.vx *= 0.975;
      var cuesta = (nivel(c.x + 14) - nivel(c.x - 14)) / 28;
      c.va += ((0.12 + Math.atan(cuesta) * 0.9) - c.a) * 0.012; c.vx += cuesta * 0.05;
    }
    c.dentro = hondo > 0;
    c.vx += 0.0035 * Math.sin(t * 0.31);
    c.va *= 0.93; c.a += c.va + c.vx * 0.0015;
    c.x += c.vx; c.y += c.vy;
    var m = c.t * 0.5;
    if (c.x < m) { c.x = m; c.vx = Math.abs(c.vx) * 0.5; }
    if (c.x > W - m) { c.x = W - m; c.vx = -Math.abs(c.vx) * 0.5; }
    if (c.y > H - c.alto * 0.35) { c.y = H - c.alto * 0.35; c.vy = -Math.abs(c.vy) * 0.3; }
  }
  function pinta() {
    ctx.clearRect(0, 0, W, H);
    var x;
    ctx.beginPath(); ctx.moveTo(0, H);
    for (x = 0; x <= W + PASO; x += PASO) ctx.lineTo(x, base - 11 + 11 * Math.sin(x * 0.0058 - t * 0.62 + 2) + resorte(Math.min(x, W)) * 0.5);
    ctx.lineTo(W, H); ctx.closePath(); ctx.fillStyle = 'rgba(15,59,58,.26)'; ctx.fill();
    ctx.beginPath(); ctx.moveTo(0, H);
    for (x = 0; x <= W + PASO; x += PASO) ctx.lineTo(x, nivel(Math.min(x, W)));
    ctx.lineTo(W, H); ctx.closePath(); ctx.fillStyle = VERDE; ctx.fill();
    flot.style.transform = 'translate(' + (c.x - c.t / 2).toFixed(1) + 'px,' + (c.y - c.alto / 2).toFixed(1) + 'px) rotate(' + c.a.toFixed(3) + 'rad)';
    if (pista && !pista.classList.contains('fuera')) pista.style.transform = 'translate(' + Math.max(4, c.x - c.t * 0.8 - pista.offsetWidth).toFixed(0) + 'px,' + (c.y - c.alto * 0.62).toFixed(0) + 'px)';
  }
  function vuelta() {
    if (pausado || !visible || reduce) { enMarcha = false; return; }
    t += 1 / 60; fisica(); pinta();
    requestAnimationFrame(vuelta);
  }
  function arranca() { if (!enMarcha && !reduce && !pausado && visible && caja) { enMarcha = true; requestAnimationFrame(vuelta); } }

  if (caja && lona && flot) {
    talla(); pinta();
    addEventListener('resize', function () { talla(); pinta(); });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) { visible = es[0].isIntersecting; arranca(); }, { rootMargin: '300px 0px' }).observe(caja);
    }
    document.addEventListener('visibilitychange', function () { visible = !document.hidden; arranca(); });

    /* El ratón remueve la superficie al cruzarla */
    var ux = null, uy = null;
    addEventListener('pointermove', function (e) {
      if (reduce || pausado) return;
      var r = caja.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top;
      if (c.coge) return;
      if (ux !== null && x >= 0 && x <= W) {
        var s = nivel(x);
        if ((uy - s) * (y - s) <= 0 || Math.abs(y - s) < 16) empuja(x, Math.max(-9, Math.min(9, (y - uy) * 0.45)), 2);
      }
      ux = x; uy = y;
    }, { passive: true });

    /* Arrastrar y soltar el 0 */
    var px = 0, py = 0;
    flot.addEventListener('pointerdown', function (e) {
      if (reduce) return;
      c.coge = true; flot.setPointerCapture(e.pointerId); px = e.clientX; py = e.clientY; c.vx = c.vy = 0;
      if (pista) pista.classList.add('fuera');
      e.preventDefault();
    });
    flot.addEventListener('pointermove', function (e) {
      if (!c.coge) return;
      var dx = e.clientX - px, dy = e.clientY - py; px = e.clientX; py = e.clientY;
      var antes = c.y;
      c.x = Math.min(W - c.t * 0.5, Math.max(c.t * 0.5, c.x + dx)); c.y += dy;
      c.vx = c.vx * 0.5 + dx * 0.5; c.vy = c.vy * 0.5 + dy * 0.5; c.va += dx * 0.0012;
      var s = nivel(c.x);
      if ((antes - s) * (c.y - s) <= 0) empuja(c.x, Math.max(-16, Math.min(16, dy * 0.8)), 3);
    });
    function suelta() {
      if (!c.coge) return;
      c.coge = false; c.dentro = (c.y + c.alto * 0.2) > nivel(c.x);
      c.vx = Math.max(-11, Math.min(11, c.vx)); c.vy = Math.max(-17, Math.min(17, c.vy));
    }
    flot.addEventListener('pointerup', suelta); flot.addEventListener('pointercancel', suelta);
    /* Teclado: Enter o espacio lo lanzan al aire */
    flot.addEventListener('keydown', function (e) {
      if (reduce || (e.key !== 'Enter' && e.key !== ' ')) return;
      e.preventDefault(); c.vy = -15; c.vx += (Math.random() - 0.5) * 6; c.va += 0.05;
      if (pista) pista.classList.add('fuera');
    });
    setTimeout(function () { if (pista) pista.classList.add('fuera'); }, 14000);
  }

  var guardado = leer();
  poner(guardado || ((navigator.language || 'es').toLowerCase().indexOf('es') === 0 ? 'es' : 'en'), false);
  arranca();
})();
