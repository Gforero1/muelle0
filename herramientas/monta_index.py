import json,re,pathlib
res=json.load(open('herramientas/trazos-logo.json'))
W,H,gp,rp=res['logo']; gp=sorted(gp,key=lambda t:-t[1])
logo=f'<svg viewBox="0 0 {W:.0f} {H:.0f}" role="img" aria-labelledby="t-logo"><title id="t-logo">muelle0</title><path class="letras" fill-rule="evenodd" d="{gp[0][2]}"/><path class="ola" fill-rule="evenodd" d="{gp[1][2]}"/><path class="cero" fill-rule="evenodd" d="{rp[0][2]}"/></svg>'
cero=f'<svg viewBox="355 0 254 440" aria-hidden="true"><path fill-rule="evenodd" d="{res["mono"][3][0][2]}"/></svg>'
# La ola del logo, tal cual, como subrayado (solo se estira a lo ancho)
for nombre,color in [('coral','#F0694C'),('minio','#D2452D'),('verde','#0F3B3A')]:
    pathlib.Path(f'marca/subrayado-{nombre}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="236 374 1194 310" preserveAspectRatio="none"><path fill="{color}" fill-rule="evenodd" d="{gp[1][2]}"/></svg>')
V='6'
FL='<svg class="flecha" viewBox="0 0 100 70" aria-hidden="true"><path d="M6 12 C 38 4, 72 18, 86 54"/><path d="M66 46 L 87 56 L 94 33"/></svg>'
def lienzo(img,h,alt): return f'<div class="lienzo"><img src="trabajos/{img}.webp?v={V}" width="1400" height="{h}" alt="{alt}" loading="lazy" decoding="async"></div>'
def clip(n,label): return f'<figure class="movil"><video data-src="clips/{n}.mp4?v={V}" poster="clips/{n}.jpg?v={V}" muted loop playsinline preload="none" aria-label="{label}"></video></figure>'
html=f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>muelle0 | Diseño y desarrollo web a medida</title>
<meta name="description" content="Desarrollamos webs y herramientas a medida para negocios que venden en línea: catálogos, tiendas, paneles de gestión y automatizaciones con IA.">
<meta name="theme-color" content="#F2EEE6">
<link rel="icon" href="marca/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="marca/icono-180.png">
<meta property="og:title" content="muelle0 | Diseño y desarrollo web a medida">
<meta property="og:description" content="Webs y herramientas a medida para negocios que venden en línea.">
<meta property="og:image" content="https://muelle0.com/marca/compartir.png">
<meta property="og:type" content="website">
<meta property="og:url" content="https://muelle0.com/">
<link rel="canonical" href="https://muelle0.com/">
<link rel="alternate" hreflang="es" href="https://muelle0.com/">
<link rel="alternate" hreflang="en" href="https://muelle0.com/en/">
<link rel="alternate" hreflang="x-default" href="https://muelle0.com/">
<meta property="og:locale" content="es_ES">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"ProfessionalService","name":"muelle0","url":"https://muelle0.com/","logo":"https://muelle0.com/marca/icono-180.png","image":"https://muelle0.com/marca/compartir.png","description":"Diseño y desarrollo de webs y herramientas a medida para negocios que venden en línea: catálogos, tiendas, paneles de gestión y automatizaciones con IA.","email":"muelle0agencia@gmail.com","sameAs":["https://www.instagram.com/muelle0agencia/"],"knowsLanguage":["es","en"]}}</script>
<link rel="preload" href="fuentes/recursive-brocha.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="estilo.css?v={V}">
</head>
<body>
<header class="cielo" id="inicio">
  <div class="barra">
    <a class="marca" href="#inicio" aria-label="muelle0, inicio"><img src="marca/mono.svg" width="608" height="531" alt=""></a>
    <a class="sec" href="#trabajos" data-i="nav.trabajos">Proyectos</a>
    <a class="sec opcional" href="#tuyo" data-i="nav.tuyo">Servicios</a>
    <a class="sec" href="#contacto" data-i="nav.contacto">Contacto</a>
    <div class="idioma" role="group" aria-label="Idioma / Language">
      <a href="./" hreflang="es" lang="es" aria-current="true" aria-label="Español">ES</a>
      <a href="en/" hreflang="en" lang="en" aria-label="English">EN</a>
    </div>
  </div>
  <div class="portada">
    <p class="logo-grande">{logo}</p>
    <div class="dice">
      <h1 class="brocha" data-i="titulo">Desarrollamos webs y herramientas a medida para negocios que venden en línea.</h1>
      <p class="quienes" data-i="quienes">Catálogos, tiendas, portafolios y paneles de gestión. Cada proyecto parte de cómo vende hoy el negocio y termina en algo que su equipo puede manejar sin depender de nosotros.</p>
      <a class="ola-enlace" href="#trabajos" data-i="ir">Ver proyectos</a>
    </div>
  </div>
  <div class="agua">
    <canvas aria-hidden="true"></canvas>
    <button class="flotador" type="button" aria-label="El 0 de muelle0 flotando. Enter lo lanza al aire.">{cero}</button>
    <span class="pista" aria-hidden="true" data-i="pista">Arrástralo</span>
    <button class="pausa" type="button" aria-pressed="false">Pausar movimiento</button>
  </div>
</header>

<main>
  <section class="mar" id="trabajos">
    <h2 class="brocha entrada" data-i="entrada">Proyectos recientes, <span>y el problema que resolvió cada uno.</span></h2>

    <article class="caso">
      <div class="cuenta">
        <p class="de-quien" data-i="a.quien">Creamdo Art, catálogo de arte</p>
        <h3 class="brocha" data-i="a.t">De una foto de teléfono a una obra presentada en sala, a escala real.</h3>
        <p data-i="a.p1">Mostrar cada obra en un espacio real exigía editar a mano cada fotografía, y eso retrasaba la publicación del catálogo.</p>
        <p data-i="a.p2">Desarrollamos un panel privado con asistencia de IA. Quien gestiona el catálogo sube la foto, indica las medidas y elige una sala. El sistema endereza la imagen, la coloca a escala y la deja lista para publicar.</p>
      </div>
      <div class="demo a">
        <div class="col-movil">
          {clip('creamdo-admin','Grabación del panel de Creamdo: se sube la foto de un cuadro, se marcan las esquinas, se escriben las medidas y aparece colgado en una sala')}
          <p class="nota" data-i="a.n1">Grabación del panel en uso.</p>
        </div>
        <div class="antes">
          <figure class="papel foto"><img src="trabajos/creamdo-foto.webp?v={V}" width="720" height="960" alt="Foto de un cuadro tomada con el teléfono, torcida y con la pared alrededor" loading="lazy"><figcaption data-i="a.c1">Foto original, tomada con un teléfono.</figcaption></figure>
          <div class="paso">{FL}<p class="nota" data-i="a.n2">Cinco pasos guiados.</p></div>
        </div>
        <figure class="papel sala"><img src="trabajos/creamdo-sala.webp?v={V}" width="900" height="1350" alt="El mismo cuadro, enderezado y colgado a escala sobre un sofá en una sala con vista al mar" loading="lazy"><figcaption data-i="a.c2">Resultado: la misma obra, corregida y a escala real (120 × 90 cm). Imagen referencial.</figcaption></figure>
      </div>
      <ul class="puntos"><li><p data-i="a.e1"><b>Fidelidad de la obra.</b> La IA solo ajusta la luz y la sombra del entorno. La obra publicada es siempre la fotografía original.</p></li><li><p data-i="a.e2"><b>Control automático.</b> Si la IA altera la pieza, el sistema lo detecta y descarta el resultado.</p></li><li><p data-i="a.e3"><b>Escala real.</b> Siete salas calibradas para que las dimensiones de cada obra correspondan a las reales.</p></li><li><p data-i="a.e4"><b>Sin curva de aprendizaje.</b> Un flujo guiado que se usa desde el teléfono, sin formación previa.</p></li></ul>
      <div class="demo solo pantallas">
        {lienzo('creamdo-pc',3970,'Recorrido por la web de Creamdo Art: portada, obras con medidas y precio, y servicios')}
        <p class="nota" data-i="a.w">El catálogo público: bilingüe, con ficha por obra y consulta directa por WhatsApp.</p>
      </div>
      <p class="cierre"><a class="ola-enlace" href="https://gforero1.github.io/creamdo/" target="_blank" rel="noopener" data-i="a.ver">Ver el catálogo</a></p>
    </article>

    <article class="caso">
      <div class="cuenta">
        <p class="de-quien" data-i="b.quien">La Tiendita del Fisio, tienda de equipos de fisioterapia</p>
        <h3 class="brocha" data-i="b.t">Venta en dos monedas, con el tipo de cambio actualizado cada hora.</h3>
        <p data-i="b.p1">Un catálogo de más de 140 productos con precios en dólares y cobro en moneda local, en un mercado donde el tipo de cambio varía a diario y una pasarela de pago no es viable para un comercio pequeño.</p>
        <p data-i="b.p2">La tienda calcula cada precio en ambas monedas con la tasa oficial del día y convierte el carrito en un pedido completo, que el cliente envía por WhatsApp.</p>
      </div>
      <div class="demo b pantallas">
        <div class="col-movil">
          {clip('fisio-pedido','Grabación de un pedido en La Tiendita del Fisio: se añaden tres productos y se abre el pedido con el total en dólares y en moneda local')}
          <p class="nota" data-i="b.n0">Grabación de un pedido en la tienda.</p>
        </div>
        {lienzo('fisio-pc',3315,'Recorrido por La Tiendita del Fisio: buscador, categorías y productos con precio en dos monedas')}
      </div>
      <ul class="puntos"><li><p data-i="b.n1"><b>Tipo de cambio automático.</b> La tasa oficial se consulta cada hora, sin intervención manual.</p></li><li><p data-i="b.n2"><b>Dos monedas.</b> Cada producto y el total del pedido se muestran en ambas.</p></li><li><p data-i="b.n3"><b>Pedido estructurado.</b> Llega por WhatsApp con productos, cantidades y total, y queda registrado.</p></li><li><p data-i="b.n4"><b>Gestión autónoma.</b> La propietaria actualiza productos, precios y fotos desde su panel.</p></li></ul>
      <p class="cierre"><a class="ola-enlace" href="https://gforero1.github.io/latienditadelfisio/" target="_blank" rel="noopener" data-i="b.ver">Ver la tienda</a></p>
    </article>

    <article class="caso">
      <div class="cuenta">
        <p class="de-quien" data-i="c.quien">Omary Belisario, creadora de contenido</p>
        <h3 class="brocha" data-i="c.t">Un portafolio que presenta su trabajo a una marca en menos de un minuto.</h3>
        <p data-i="c.p1">Omary produce vídeo para marcas de belleza. Su portafolio era una presentación; ahora es un sitio propio, con el trabajo organizado por categoría y un canal directo para solicitar presupuesto.</p>
      </div>
      <div class="demo c pantallas">
        {lienzo('omary-pc',3971,'Recorrido por el portafolio de Omary Belisario en escritorio: portada, sobre mí y vídeos por categoría')}
        <div class="col-movil">
          <figure class="movil"><div class="lienzo"><img src="trabajos/omary-movil.webp?v={V}" width="585" height="5447" alt="Recorrido por el portafolio de Omary Belisario en un teléfono" loading="lazy" decoding="async"></div></figure>
          <p class="nota" data-i="c.n0">El mismo portafolio, en el teléfono.</p>
        </div>
      </div>
      <ul class="puntos"><li><p data-i="c.n1"><b>Diseño propio.</b> Desarrollado a partir de su identidad visual, sin plantilla.</p></li><li><p data-i="c.n2"><b>Vídeo tratado.</b> Cada pieza se procesa para conservar el color original.</p></li><li><p data-i="c.n3"><b>Bilingüe.</b> Español o inglés, según el idioma del visitante.</p></li></ul>
      <p class="cierre"><a class="ola-enlace" href="https://omaryugc.com/" target="_blank" rel="noopener" data-i="c.ver">Ver el portafolio</a></p>
    </article>
  </section>

  <section class="tuyo" id="tuyo">
    <h2 class="brocha" data-i="tuyo.t">Qué desarrollamos</h2>
    <p class="bajada" data-i="tuyo.p">Trabajamos sobre problemas concretos de venta y de gestión. Estos son los más habituales.</p>
    <ul class="preguntas">
      <li><h3 data-i="q1">Catálogos y tiendas en línea</h3><p data-i="r1">Con pedido por WhatsApp o con pago en línea, según cómo venda el negocio.</p></li>
      <li><h3 data-i="q2">Paneles de gestión</h3><p data-i="r2">Para actualizar productos, precios y contenido sin depender de un desarrollador.</p></li>
      <li><h3 data-i="q3">Herramientas con IA</h3><p data-i="r3">Automatizan tareas repetitivas, como preparar las fotos de producto, con controles que verifican el resultado.</p></li>
      <li><h3 data-i="q4">Precios en varias monedas</h3><p data-i="r4">Conversión automática al tipo de cambio del día, en cada producto y en el total.</p></li>
      <li><h3 data-i="q5">Sitios en varios idiomas</h3><p data-i="r5">El contenido se muestra en el idioma de cada visitante.</p></li>
      <li><h3 data-i="q6">Automatizaciones</h3><p data-i="r6">Pedidos que se registran solos y datos conectados con las herramientas que el negocio ya usa.</p></li>
    </ul>
  </section>

  <svg class="rompiente" viewBox="0 0 1440 110" preserveAspectRatio="none" aria-hidden="true"><path d="M0 62 C 160 20, 300 96, 470 60 S 760 8, 930 52 S 1250 100, 1440 38 V110 H0Z"/></svg>
  <section class="orilla" id="contacto">
    <h2 class="brocha" data-i="contacto.t">Cuéntanos qué necesita tu negocio.</h2>
    <p class="bajada" data-i="contacto.p">Describe qué vendes y qué problema quieres resolver. Respondemos con una propuesta concreta, en español o en inglés.</p>
    <a class="correo" href="mailto:muelle0agencia@gmail.com">muelle0agencia<wbr>@gmail.com</a>
    <div class="mas">
      <a class="ola-enlace" href="https://www.instagram.com/muelle0agencia/" target="_blank" rel="noopener">Instagram @muelle0agencia</a>
    </div>
    <footer class="pie">
      <img src="marca/logo.svg" width="1433" height="684" alt="muelle0">
      <p data-i="pie">Diseño y desarrollo web a medida.</p>
    </footer>
  </section>
</main>
<script src="muelle.js?v={V}" defer></script>
</body>
</html>
'''
open('index.html','w').write(html)

# ---------- Versión en inglés: misma página, textos de _src/en.json, en /en/ ----------
import os
EN=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'en.json')))
en=html
for k,v in EN.items():
    pat=re.compile(r'(<(\w+)[^>]*data-i="'+re.escape(k)+r'"[^>]*>)(.*?)(</\2>)',re.S)
    en=pat.sub(lambda m:m.group(1)+v+m.group(4),en)
ATR=[
 ('<html lang="es">','<html lang="en">'),
 ('<title>muelle0 | Diseño y desarrollo web a medida</title>','<title>muelle0 | Custom web design and development</title>'),
 ('content="muelle0 | Diseño y desarrollo web a medida"','content="muelle0 | Custom web design and development"'),
 ('content="Desarrollamos webs y herramientas a medida para negocios que venden en línea: catálogos, tiendas, paneles de gestión y automatizaciones con IA."','content="We build custom websites and tools for businesses that sell online: catalogues, shops, admin panels and AI automation."'),
 ('content="Webs y herramientas a medida para negocios que venden en línea."','content="Custom websites and tools for businesses that sell online."'),
 ('"description":"Diseño y desarrollo de webs y herramientas a medida para negocios que venden en línea: catálogos, tiendas, paneles de gestión y automatizaciones con IA."','"description":"Custom web design and development for businesses that sell online: catalogues, shops, admin panels and AI automation."'),
 ('<meta property="og:url" content="https://muelle0.com/">','<meta property="og:url" content="https://muelle0.com/en/">'),
 ('<link rel="canonical" href="https://muelle0.com/">','<link rel="canonical" href="https://muelle0.com/en/">'),
 ('content="es_ES"','content="en_GB"'),
 ('<a href="./" hreflang="es" lang="es" aria-current="true" aria-label="Español">ES</a>','<a href="../" hreflang="es" lang="es" aria-label="Español">ES</a>'),
 ('<a href="en/" hreflang="en" lang="en" aria-label="English">EN</a>','<a href="./" hreflang="en" lang="en" aria-current="true" aria-label="English">EN</a>'),
 ('aria-label="muelle0, inicio"','aria-label="muelle0, home"'),
 ('aria-label="El 0 de muelle0 flotando. Enter lo lanza al aire."','aria-label="The 0 from muelle0, floating. Press Enter to throw it in the air."'),
 ('>Pausar movimiento<','>Pause motion<'),
 ('alt="El mismo cuadro, enderezado y colgado a escala sobre un sofá en una sala con vista al mar"','alt="The same painting, straightened and hung to scale above a sofa in a room with a sea view"'),
 ('alt="Foto de un cuadro tomada con el teléfono, torcida y con la pared alrededor"','alt="Photo of a painting taken on a phone, skewed and with the wall around it"'),
 ('alt="Recorrido por La Tiendita del Fisio: buscador, categorías y productos con precio en dos monedas"','alt="Scroll through La Tiendita del Fisio: search, categories and products priced in two currencies"'),
 ('alt="Recorrido por el portafolio de Omary Belisario en escritorio: portada, sobre mí y vídeos por categoría"','alt="Scroll through Omary Belisario\'s portfolio on desktop: home, about and videos by category"'),
 ('alt="Recorrido por el portafolio de Omary Belisario en un teléfono"','alt="Scroll through Omary Belisario\'s portfolio on a phone"'),
 ('alt="Recorrido por la web de Creamdo Art: portada, obras con medidas y precio, y servicios"','alt="Scroll through the Creamdo Art site: home, artworks with measurements and price, and services"'),
 ('aria-label="Grabación de un pedido en La Tiendita del Fisio: se añaden tres productos y se abre el pedido con el total en dólares y en moneda local"','aria-label="Recording of an order in La Tiendita del Fisio: three products are added and the order opens with the total in dollars and local currency"'),
 ('aria-label="Grabación del panel de Creamdo: se sube la foto de un cuadro, se marcan las esquinas, se escriben las medidas y aparece colgado en una sala"','aria-label="Recording of the Creamdo admin panel: a photo of a painting is uploaded, its corners are marked, its measurements are entered and it appears hung in a room"'),
]
for a,b in ATR:
    assert a in en,a
    en=en.replace(a,b)
for pre in ['href="estilo.css','src="muelle.js','src="marca/','href="marca/','src="trabajos/','src="clips/','poster="clips/','href="fuentes/']:
    en=en.replace(pre, pre.replace('="','="../'))
os.makedirs(os.path.join(os.path.dirname(os.path.abspath('index.html')),'en'),exist_ok=True)
open('en/index.html','w').write(en)
