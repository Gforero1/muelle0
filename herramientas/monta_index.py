import json,re
res=json.load(open('herramientas/trazos-logo.json'))
W,H,gp,rp=res['logo']; gp=sorted(gp,key=lambda t:-t[1])
logo=f'<svg viewBox="0 0 {W:.0f} {H:.0f}" role="img" aria-labelledby="t-logo"><title id="t-logo">muelle0</title><path class="letras" fill-rule="evenodd" d="{gp[0][2]}"/><path class="ola" fill-rule="evenodd" d="{gp[1][2]}"/><path class="cero" fill-rule="evenodd" d="{rp[0][2]}"/></svg>'
cero=f'<svg viewBox="355 0 254 440" aria-hidden="true"><path fill-rule="evenodd" d="{res["mono"][3][0][2]}"/></svg>'
V='1'
def caso(n,nombre,clave,url,urltxt,datos,pc,movil,alt):
    dl=''.join(f'<div><dt data-i="k.{k}">{kt}</dt><dd{(" data-i=%s.%s"%(clave,k)) if tr else ""}>{val}</dd></div>' for k,kt,val,tr in datos)
    tel=f'''
        <figure class="ventana telefono" aria-hidden="true"><div class="lienzo"><img src="trabajos/{movil[0]}.webp?v={V}" width="585" height="{movil[1]}" alt="" loading="lazy" decoding="async"></div></figure>''' if movil else ''
    return f'''
    <article class="caso">
      <div class="ficha">
        <span class="num dato" data-i="{clave}.lugar">{n}</span>
        <h3>{nombre}</h3>
        <p class="resumen" data-i="{clave}.r">{RES[clave]}</p>
        <dl>{dl}</dl>
        <a class="ver" href="{url}" target="_blank" rel="noopener"><b data-i="ver">Ver la web</b> <span aria-hidden="true">↗</span></a>
      </div>
      <div class="pantallas{' con-telefono' if movil else ''}">
        <figure class="ventana"><figcaption><span>{urltxt}</span><span>{n[:3]}</span></figcaption><div class="lienzo"><img src="trabajos/{pc[0]}.webp?v={V}" width="1400" height="{pc[1]}" alt="{alt}" loading="lazy" decoding="async"></div></figure>{tel}
      </div>
    </article>'''
RES={
 'c1':'Catálogo de arte en español e inglés. Cada obra lleva sus medidas y su precio, y la consulta va directa al WhatsApp de Adriana Moncayo. Detrás hay un admin donde ella sube la foto de un cuadro y lo ve colgado, a escala, en una sala.',
 'c2':'Portafolio de una creadora UGC de beauty. Vídeos ordenados por categoría, las marcas con las que ha trabajado y una forma clara de pedir presupuesto. En español e inglés, sobre Shopify y con dominio propio.',
 'c3':'Tienda de más de 140 productos sin pasarela de pago: el cliente arma su pedido y lo envía por WhatsApp. Los precios salen en dólares y en bolívares a la tasa BCV del día, y la dueña cambia productos, precios y fotos desde su propio panel.',
}
casos=caso('001 · Lechería, Venezuela · Arte','Creamdo Art','c1','https://gforero1.github.io/creamdo/','gforero1.github.io/creamdo',
  [('tipo','Tipo','Catálogo con admin privado',1),('idiomas','Idiomas','ES / EN',0),('pedido','Pedido','Consulta por WhatsApp, obra por obra',1)],('creamdo-pc',3970),('creamdo-movil',2747),'Recorrido por la web de Creamdo Art: portada, obras con medidas y precio, y servicios')
casos+=caso('002 · Barcelona · Creadora UGC','Omary Belisario','c2','https://omaryugc.com/','omaryugc.com',
  [('tipo','Tipo','Portafolio de vídeo',1),('plataforma','Plataforma','Shopify, tema propio',1),('idiomas','Idiomas','ES / EN',0)],('omary-pc',3971),None,'Recorrido por el portafolio de Omary Belisario: portada, sobre mí y vídeos de skincare y makeup')
casos+=caso('003 · Lechería, Venezuela · Fisioterapia','La Tiendita del Fisio','c3','https://gforero1.github.io/latienditadelfisio/','gforero1.github.io/latienditadelfisio',
  [('tipo','Tipo','Tienda con pedido por WhatsApp',1),('monedas','Monedas','$ y Bs, tasa BCV automática',1),('catalogo','Catálogo','Google Sheets con panel privado',1)],('fisio-pc',3315),('fisio-movil',2747),'Recorrido por La Tiendita del Fisio: buscador, categorías y productos con precio en dólares y bolívares')
html=f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>muelle0 · Estudio web</title>
<meta name="description" content="Estudio web con raíces venezolanas. Montamos a mano páginas, catálogos y tiendas para marcas pequeñas, con un panel propio para que las lleven sin nosotros.">
<meta name="theme-color" content="#F2EEE6">
<link rel="icon" href="marca/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="marca/icono-180.png">
<meta property="og:title" content="muelle0 · Estudio web">
<meta property="og:description" content="Páginas, catálogos y tiendas hechas a mano para marcas pequeñas.">
<meta property="og:image" content="https://gforero1.github.io/muelle0/marca/compartir.png">
<meta property="og:type" content="website">
<link rel="preload" href="fuentes/schibsted.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="estilo.css?v={V}">
</head>
<body>
<header class="portada" id="inicio">
  <div class="cabecera">
    <a class="marca" href="#inicio" aria-label="muelle0, inicio"><img src="marca/mono.svg" width="608" height="531" alt=""></a>
    <nav aria-label="Secciones">
      <a href="#trabajos" data-i="nav.trabajos">Trabajos</a>
      <a href="#modo" data-i="nav.modo">Cómo trabajamos</a>
      <a href="#contacto" data-i="nav.contacto">Contacto</a>
    </nav>
    <div class="idioma" role="group" aria-label="Idioma / Language">
      <button type="button" value="es" aria-pressed="true">ES</button>
      <button type="button" value="en" aria-pressed="false">EN</button>
    </div>
  </div>
  <div class="portada-cuerpo">
    <p class="logo-grande">{logo}</p>
    <div class="presenta">
      <h1 data-i="titulo"><b>Estudio web.</b> Montamos a mano páginas, catálogos y tiendas para marcas pequeñas, y las dejamos con un panel propio para que sus dueños las lleven sin nosotros.</h1>
      <p class="relojes dato"><span>Barcelona <b id="h-bcn">--:--</b></span><span>Lechería <b id="h-lch">--:--</b></span><span data-i="reloj.raices">Raíces venezolanas</span></p>
      <a class="ir" href="#trabajos"><b data-i="ir">Ver trabajos</b> <span aria-hidden="true">↓</span></a>
    </div>
  </div>
  <div class="agua">
    <canvas aria-hidden="true"></canvas>
    <button class="flotador" type="button" aria-label="El 0 de muelle0 flotando. Enter lo lanza al aire.">{cero}</button>
    <span class="pista dato" aria-hidden="true"><span data-i="pista">Agárralo y lánzalo</span> →</span>
    <button class="pausa dato" type="button" aria-pressed="false">Pausar movimiento</button>
  </div>
</header>

<main>
  <section class="bajo-agua" id="trabajos">
    <div class="entrada">
      <h2 data-i="trabajos.t">Trabajos</h2>
      <p class="dato" data-i="trabajos.p">Tres webs en marcha. Cada captura es la web real, recorriéndose.</p>
    </div>
    {casos}
    <aside class="libre">
      <div>
        <span class="num dato" data-i="libre.n">004 · Atracadero libre</span>
        <h3 data-i="libre.t">Este puesto está libre.</h3>
        <p data-i="libre.p">Cuéntanos qué vendes y cómo te compran hoy. Te respondemos con lo que montaríamos.</p>
      </div>
      <a class="ver" href="mailto:muelle0agencia@gmail.com"><b data-i="libre.a">Escríbenos</b> <span aria-hidden="true">↗</span></a>
    </aside>
  </section>

  <section class="modo" id="modo">
    <h2 data-i="modo.t">Cómo <em>trabajamos</em></h2>
    <ol class="pasos">
      <li><span class="dato">01</span><h3 data-i="p1.t">Miramos lo que ya tienes</h3><p data-i="p1.p">Tu Instagram, tu logo, tus fotos y cómo te compran hoy. De ahí salen los colores, el tono y la estructura, no de una plantilla.</p></li>
      <li><span class="dato">02</span><h3 data-i="p2.t">La montamos a mano</h3><p data-i="p2.p">Código propio, ligero y en los idiomas que necesites. Si tu negocio pide Shopify, la hacemos en Shopify.</p></li>
      <li><span class="dato">03</span><h3 data-i="p3.t">Te la dejamos lista para usar</h3><p data-i="p3.p">Con un panel privado para cambiar precios, fotos y productos desde el teléfono, sin escribirnos.</p></li>
      <li><span class="dato">04</span><h3 data-i="p4.t">Queda a tu nombre</h3><p data-i="p4.p">Dominio, cuentas y contenido son tuyos desde el primer día.</p></li>
    </ol>
    <ul class="montamos" aria-label="Qué montamos">
      <li data-i="m1">Catálogos</li><li data-i="m2">Portafolios</li><li data-i="m3">Tiendas</li><li data-i="m4">Paneles privados</li>
    </ul>
  </section>

  <section class="contacto" id="contacto">
    <h2 data-i="contacto.t">Contacto</h2>
    <a class="correo" href="mailto:muelle0agencia@gmail.com">muelle0agencia<wbr>@gmail.com</a>
    <div class="otros">
      <a href="https://www.instagram.com/muelle0agencia/" target="_blank" rel="noopener">Instagram @muelle0agencia</a>
      <p data-i="contacto.p">Respondemos en español o en inglés.</p>
    </div>
  </section>
</main>

<footer class="pie">
  <img src="marca/logo-crema.svg" width="1433" height="684" alt="muelle0">
  <p class="dato" data-i="pie">muelle0 · Estudio web · Raíces venezolanas</p>
</footer>
<script src="muelle.js?v={V}" defer></script>
</body>
</html>
'''
open('index.html','w').write(html)
print(len(html))
