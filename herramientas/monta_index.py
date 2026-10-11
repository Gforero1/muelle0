import json,re,pathlib
res=json.load(open('herramientas/trazos-logo.json'))
W,H,gp,rp=res['logo']; gp=sorted(gp,key=lambda t:-t[1])
logo=f'<svg viewBox="0 0 {W:.0f} {H:.0f}" role="img" aria-labelledby="t-logo"><title id="t-logo">muelle0</title><path class="letras" fill-rule="evenodd" d="{gp[0][2]}"/><path class="ola" fill-rule="evenodd" d="{gp[1][2]}"/><path class="cero" fill-rule="evenodd" d="{rp[0][2]}"/></svg>'
cero=f'<svg viewBox="355 0 254 440" aria-hidden="true"><path fill-rule="evenodd" d="{res["mono"][3][0][2]}"/></svg>'
# La ola del logo, tal cual, como subrayado (solo se estira a lo ancho)
for nombre,color in [('coral','#F0694C'),('minio','#D2452D'),('verde','#0F3B3A')]:
    pathlib.Path(f'marca/subrayado-{nombre}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="236 374 1194 310" preserveAspectRatio="none"><path fill="{color}" fill-rule="evenodd" d="{gp[1][2]}"/></svg>')
V='2'
FL='<svg class="flecha" viewBox="0 0 100 70" aria-hidden="true"><path d="M6 12 C 38 4, 72 18, 86 54"/><path d="M66 46 L 87 56 L 94 33"/></svg>'
def lienzo(img,h,alt): return f'<div class="lienzo"><img src="trabajos/{img}.webp?v={V}" width="1400" height="{h}" alt="{alt}" loading="lazy" decoding="async"></div>'
def clip(n,label): return f'<figure class="movil"><video data-src="clips/{n}.mp4?v={V}" poster="clips/{n}.jpg?v={V}" muted loop playsinline preload="none" aria-label="{label}"></video></figure>'
html=f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>muelle0, estudio web</title>
<meta name="description" content="Estudio web con raíces venezolanas. Webs hechas a medida y, cuando la web no basta, la herramienta que falta: catálogos con pedido por WhatsApp, precios a la tasa del día, paneles propios y fotos preparadas con IA.">
<meta name="theme-color" content="#F2EEE6">
<link rel="icon" href="marca/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="marca/icono-180.png">
<meta property="og:title" content="muelle0, estudio web">
<meta property="og:description" content="Webs hechas a medida. Y cuando la web no basta, la herramienta que falta.">
<meta property="og:image" content="https://gforero1.github.io/muelle0/marca/compartir.png">
<meta property="og:type" content="website">
<link rel="preload" href="fuentes/recursive-brocha.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="estilo.css?v={V}">
</head>
<body>
<header class="cielo" id="inicio">
  <div class="barra">
    <a class="marca" href="#inicio" aria-label="muelle0, inicio"><img src="marca/mono.svg" width="608" height="531" alt=""></a>
    <a class="sec" href="#trabajos" data-i="nav.trabajos">Trabajos</a>
    <a class="sec" href="#tuyo" data-i="nav.tuyo">Lo que montamos</a>
    <a class="sec" href="#contacto" data-i="nav.contacto">Escríbenos</a>
    <div class="idioma" role="group" aria-label="Idioma / Language">
      <button type="button" value="es" aria-pressed="true">ES</button>
      <button type="button" value="en" aria-pressed="false">EN</button>
    </div>
  </div>
  <div class="portada">
    <p class="logo-grande">{logo}</p>
    <div class="dice">
      <h1 class="brocha" data-i="titulo">Webs hechas a medida. Y cuando la web no basta, la herramienta que falta.</h1>
      <p class="quienes" data-i="quienes">Somos un estudio pequeño con raíces venezolanas. Trabajamos con negocios que venden de verdad: por WhatsApp, en dos monedas y con fotos tomadas con el teléfono.</p>
      <p class="hora" data-i="hora">Ahora mismo son las <b id="h-bcn">--:--</b> en Barcelona y las <b id="h-lch">--:--</b> en Lechería.</p>
      <a class="ola-enlace" href="#trabajos" data-i="ir">Mira lo que hemos montado</a>
    </div>
  </div>
  <div class="agua">
    <canvas aria-hidden="true"></canvas>
    <button class="flotador" type="button" aria-label="El 0 de muelle0 flotando. Enter lo lanza al aire.">{cero}</button>
    <span class="pista" aria-hidden="true" data-i="pista">Agárralo y lánzalo</span>
    <button class="pausa" type="button" aria-pressed="false">Pausar movimiento</button>
  </div>
</header>

<main>
  <section class="mar" id="trabajos">
    <h2 class="brocha entrada" data-i="entrada">Tres trabajos. <span>En cada uno hubo que inventar algo.</span></h2>

    <article class="caso">
      <div class="cuenta">
        <p class="de-quien" data-i="a.quien">Creamdo Art, en Lechería</p>
        <h3 class="brocha" data-i="a.t">Una herramienta para que cada cuadro salga colgado en una sala.</h3>
        <p data-i="a.p1">Adriana Moncayo representa a artistas venezolanos. Enseñar cómo queda una obra en una pared exigía editar cada foto a mano, y eran horas por cuadro.</p>
        <p data-i="a.p2">Le montamos un panel propio. Toma la foto con el teléfono, marca las esquinas, escribe las medidas y elige la sala. La obra aparece colgada a su tamaño real, lista para publicar.</p>
      </div>
      <div class="prueba-a">
        <div class="col-movil">
          {clip('creamdo-admin','Grabación del panel de Creamdo: se sube la foto de un cuadro, se marcan las esquinas, se escriben las medidas y aparece colgado en una sala')}
          <p class="nota" data-i="a.n1">El panel de verdad, grabado con una obra del catálogo.</p>
        </div>
        <div>
          <figure class="papel foto"><img src="trabajos/creamdo-foto.webp?v={V}" width="720" height="960" alt="Foto de un cuadro tomada con el teléfono, torcida y con la pared alrededor" loading="lazy"><figcaption data-i="a.c1">La foto, tal como sale del teléfono.</figcaption></figure>
          <div class="paso">{FL}<p class="nota" data-i="a.n2">Cinco pasos, desde el teléfono.</p></div>
        </div>
        <figure class="papel sala"><img src="trabajos/creamdo-sala.webp?v={V}" width="900" height="1350" alt="El mismo cuadro, enderezado y colgado a escala sobre un sofá en una sala con vista al mar" loading="lazy"><figcaption data-i="a.c2">La misma obra, enderezada y a escala: 120 × 90 cm se ven como 120 × 90 cm. Imagen referencial.</figcaption></figure>
      </div>
      <div class="explica">
        <p data-i="a.e1"><b>La obra no se inventa.</b> La IA solo integra la luz y la sombra de la sala. Después el panel vuelve a pegar encima la foto real.</p>
        <p data-i="a.e2"><b>Se vigila sola.</b> Si la IA movió o cambió la pieza, el panel lo detecta y descarta esa versión.</p>
        <p data-i="a.e3"><b>Cada pared está medida.</b> Siete salas, de un penthouse a una repisa, calibradas para que la escala sea la real.</p>
        <p data-i="a.e4"><b>Hecho para ella.</b> Tres botones grandes, pasos numerados y nada que haya que aprender.</p>
      </div>
      <div class="web pantallas">
        <div class="lado">
          <p class="nota" data-i="a.w">Y la web: catálogo en español e inglés, y cada consulta llega a su WhatsApp con el nombre de la obra.</p>
          <a class="ola-enlace" href="https://gforero1.github.io/creamdo/" target="_blank" rel="noopener" data-i="a.ver">Ver Creamdo Art</a>
        </div>
        {lienzo('creamdo-pc',3970,'Recorrido por la web de Creamdo Art: portada, obras con medidas y precio, y servicios')}
      </div>
    </article>

    <article class="caso">
      <div class="cuenta">
        <p class="de-quien" data-i="b.quien">La Tiendita del Fisio, en Lechería</p>
        <h3 class="brocha" data-i="b.t">Una tienda que cobra en bolívares a la tasa de hoy, sin pasarela de pago.</h3>
        <p data-i="b.p1">Más de 140 productos de fisioterapia con precio en dólares, clientes que pagan en bolívares y una tasa que cambia cada día. Y una pasarela de pago que, en Venezuela, no está al alcance de una tienda pequeña.</p>
        <p data-i="b.p2">Así que el pedido se arma en la web y se envía por WhatsApp, con el total ya calculado en las dos monedas.</p>
      </div>
      <div class="prueba-b">
        <div class="notas izq">
          <p class="nota">{FL}<span data-i="b.n1"><b>La tasa del BCV se actualiza sola</b> cada hora. Nadie tiene que acordarse.</span></p>
          <p class="nota">{FL}<span data-i="b.n2"><b>Cada precio sale dos veces:</b> en dólares y en bolívares.</span></p>
        </div>
        {clip('fisio-pedido','Grabación de un pedido en La Tiendita del Fisio: se añaden tres productos y se abre el pedido con el total en dólares y en bolívares')}
        <div class="notas der">
          <p class="nota">{FL}<span data-i="b.n3"><b>El pedido llega escrito al WhatsApp</b> y además queda anotado en una hoja.</span></p>
          <p class="nota">{FL}<span data-i="b.n4"><b>La dueña lo lleva sola:</b> cambia productos, precios y fotos desde su panel.</span></p>
        </div>
      </div>
      <div class="web al-reves pantallas">
        <div class="lado">
          <p class="nota" data-i="b.w">Buscador, categorías y un catálogo que ella edita cuando quiere.</p>
          <a class="ola-enlace" href="https://gforero1.github.io/latienditadelfisio/" target="_blank" rel="noopener" data-i="b.ver">Ver la tienda</a>
        </div>
        {lienzo('fisio-pc',3315,'Recorrido por La Tiendita del Fisio: buscador, categorías y productos con precio en dólares y bolívares')}
      </div>
    </article>

    <article class="caso">
      <div class="cuenta">
        <p class="de-quien" data-i="c.quien">Omary Belisario, en Barcelona</p>
        <h3 class="brocha" data-i="c.t">Un portafolio para que una marca vea su trabajo en medio minuto.</h3>
        <p data-i="c.p1">Omary graba vídeos de beauty para marcas. Su portafolio era una presentación suelta; ahora es una web suya, con los vídeos ordenados por categoría y una forma directa de pedir presupuesto.</p>
      </div>
      <div class="prueba-c pantallas">
        {lienzo('omary-pc',3971,'Recorrido por el portafolio de Omary Belisario: portada, sobre mí y vídeos de skincare y makeup')}
        <div class="notas">
          <p class="nota">{FL}<span data-i="c.n1"><b>Diseño desde cero,</b> a partir de sus colores y su logo. Sin plantilla.</span></p>
          <p class="nota">{FL}<span data-i="c.n2"><b>Cada vídeo del iPhone se trata</b> para que el color no salga lavado.</span></p>
          <p class="nota">{FL}<span data-i="c.n3"><b>Español o inglés,</b> según quien entra.</span></p>
          <a class="ola-enlace" href="https://omaryugc.com/" target="_blank" rel="noopener" data-i="c.ver">Ver omaryugc.com</a>
        </div>
      </div>
    </article>
  </section>

  <section class="tuyo" id="tuyo">
    <h2 class="brocha" data-i="tuyo.t">¿Y lo tuyo?</h2>
    <p class="bajada" data-i="tuyo.p">Casi todo lo que hemos montado empezó con una frase como estas.</p>
    <ul class="preguntas">
      <li><h3 data-i="q1">“Vendo por WhatsApp y me pierdo entre mensajes.”</h3><p data-i="r1">Un catálogo donde el cliente arma su pedido y te llega escrito, con el total hecho.</p></li>
      <li><h3 data-i="q2">“Cobro en dos monedas.”</h3><p data-i="r2">Precios que se convierten solos a la tasa del día.</p></li>
      <li><h3 data-i="q3">“Las fotos me quitan horas.”</h3><p data-i="r3">Una herramienta con IA que las prepara por ti y no se inventa el producto.</p></li>
      <li><h3 data-i="q4">“Para cambiar un precio tengo que pedírselo a alguien.”</h3><p data-i="r4">Un panel tuyo, desde el teléfono, hecho para que se entienda a la primera.</p></li>
      <li><h3 data-i="q5">“Tengo clientes fuera.”</h3><p data-i="r5">La web en los idiomas que necesites, según quien entra. Y si te conviene una tienda con cobro en línea, la montamos también.</p></li>
      <li><h3 data-i="q6">“Lo mío es raro.”</h3><p data-i="r6">Esos son los encargos que más nos gustan. Si se puede automatizar, medir o simplificar, le buscamos la vuelta.</p></li>
    </ul>
  </section>

  <svg class="rompiente" viewBox="0 0 1440 110" preserveAspectRatio="none" aria-hidden="true"><path d="M0 62 C 160 20, 300 96, 470 60 S 760 8, 930 52 S 1250 100, 1440 38 V110 H0Z"/></svg>
  <section class="orilla" id="contacto">
    <h2 class="brocha" data-i="contacto.t">Cuéntanos qué vendes y cómo te compran hoy.</h2>
    <p class="bajada" data-i="contacto.p">Te respondemos con lo que montaríamos. En español o en inglés.</p>
    <a class="correo" href="mailto:muelle0agencia@gmail.com">muelle0agencia<wbr>@gmail.com</a>
    <div class="mas">
      <a class="ola-enlace" href="https://www.instagram.com/muelle0agencia/" target="_blank" rel="noopener">Instagram @muelle0agencia</a>
    </div>
    <footer class="pie">
      <img src="marca/logo.svg" width="1433" height="684" alt="muelle0">
      <p data-i="pie">Estudio web con raíces venezolanas.</p>
    </footer>
  </section>
</main>
<script src="muelle.js?v={V}" defer></script>
</body>
</html>
'''
open('index.html','w').write(html)
print(len(html))
