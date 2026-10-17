# Genera index.html (español) y en/index.html (inglés).
# Uso, desde la raíz del repo: python3 herramientas/monta_index.py
# Los textos van en pareja: X('clave', 'español', 'inglés') para el contenido y A('español', 'inglés') para atributos (alt, aria-label).
import json, re, pathlib, os

RAIZ = pathlib.Path(__file__).resolve().parent.parent
os.chdir(RAIZ)
res = json.load(open('herramientas/trazos-logo.json'))
W, H, gp, rp = res['logo']; gp = sorted(gp, key=lambda t: -t[1])
logo = f'<svg viewBox="0 0 {W:.0f} {H:.0f}" role="img" aria-labelledby="t-logo"><title id="t-logo">muelle0</title><path class="letras" fill-rule="evenodd" d="{gp[0][2]}"/><path class="ola" fill-rule="evenodd" d="{gp[1][2]}"/><path class="cero" fill-rule="evenodd" d="{rp[0][2]}"/></svg>'
cero = f'<svg viewBox="355 0 254 440" aria-hidden="true"><path fill-rule="evenodd" d="{res["mono"][3][0][2]}"/></svg>'
# La ola del logo, tal cual, como subrayado (solo se estira a lo ancho)
for nombre, color in [('coral', '#F0694C'), ('minio', '#D2452D'), ('verde', '#0F3B3A')]:
    pathlib.Path(f'marca/subrayado-{nombre}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="236 374 1194 310" preserveAspectRatio="none"><path fill="{color}" fill-rule="evenodd" d="{gp[1][2]}"/></svg>')

V = '11'
EN = {}
ATR = []
def X(k, es, en):
    EN[k] = en
    return es
def A(es, en):
    ATR.append((es, en))
    return es

FL = '<svg class="flecha" viewBox="0 0 100 70" aria-hidden="true"><path d="M6 12 C 38 4, 72 18, 86 54"/><path d="M66 46 L 87 56 L 94 33"/></svg>'

def lienzo(img, h, alt_es, alt_en):
    return f'<div class="lienzo"><img src="trabajos/{img}.webp?v={V}" width="1400" height="{h}" alt="{A(alt_es, alt_en)}" loading="lazy" decoding="async"></div>'
def movil_clip(n, es, en):
    return f'<figure class="movil"><video data-src="clips/{n}.mp4?v={V}" poster="clips/{n}.jpg?v={V}" muted loop playsinline preload="none" aria-label="{A(es, en)}"></video></figure>'
def movil_captura(n, h, es, en):
    return f'<figure class="movil"><div class="lienzo"><img src="trabajos/{n}.webp?v={V}" width="585" height="{h}" alt="{A(es, en)}" loading="lazy" decoding="async"></div></figure>'
def ventana_clip(n, es, en):
    return f'<figure class="ventana"><video data-src="clips/{n}.mp4?v={V}" poster="clips/{n}.jpg?v={V}" muted loop playsinline preload="none" aria-label="{A(es, en)}"></video></figure>'
def nota(k, es, en):
    return f'<p class="nota" data-i="{k}">{X(k, es, en)}</p>'
def puntos(items):
    return '<ul class="puntos">' + ''.join(f'<li><p data-i="{k}">{X(k, es, en)}</p></li>' for k, es, en in items) + '</ul>'
def ficha(colores, fuentes):
    """Muestrario de la marca del cliente: colores reales (hex de su README) y sus tipografías."""
    sw = ''.join(f'<i style="--c:{c}" title="{c}"></i>' for c in colores)
    return f'<p class="ficha"><span class="muestras" aria-hidden="true">{sw}</span><span>{fuentes}</span></p>'
def cabecera(k, quien_es, quien_en, t_es, t_en, ps, colores=None, fuentes=None):
    f = ficha(colores, fuentes) if colores else ''
    cuerpo = ''.join(f'<p data-i="{k}.p{i+1}">{X(f"{k}.p{i+1}", es, en)}</p>' for i, (es, en) in enumerate(ps))
    return f'''<div class="cuenta">
        <p class="de-quien" data-i="{k}.quien">{X(k+'.quien', quien_es, quien_en)}</p>
        {f}
        <h3 class="brocha" data-i="{k}.t">{X(k+'.t', t_es, t_en)}</h3>
        {cuerpo}
      </div>'''
def ver(k, url, es, en):
    return f'<p class="cierre"><a class="ola-enlace" href="{url}" target="_blank" rel="noopener" data-i="{k}.ver">{X(k+".ver", es, en)}</a></p>'

# ---------- Proyectos destacados ----------
creamdo = f'''<article class="caso" id="p-creamdo">
      {cabecera('cr', 'Creamdo Art, catálogo de arte', 'Creamdo Art, art catalogue',
        'De una foto de teléfono a una obra presentada en sala, a escala real.', 'From a phone photo to an artwork shown in a room, at real scale.',
        [('Mostrar cada obra en un espacio real exigía editar a mano cada fotografía, y eso retrasaba la publicación del catálogo.',
          'Showing each piece in a real space meant editing every photograph by hand, which delayed publishing the catalogue.'),
         ('Desarrollamos un panel privado con asistencia de IA. Quien gestiona el catálogo sube la foto, indica las medidas y elige una sala. El sistema endereza la imagen, la coloca a escala y la deja lista para publicar.',
          'We built a private admin panel with AI assistance. Whoever manages the catalogue uploads the photo, enters the measurements and picks a room. The system straightens the image, places it to scale and leaves it ready to publish.')],
        ['#111111', '#009ED8', '#F26122', '#EC1163'], 'Archivo')}
      <div class="demo a">
        <div class="col-movil">
          {movil_clip('creamdo-admin', 'Grabación del panel de Creamdo: se sube la foto de un cuadro, se marcan las esquinas, se escriben las medidas y aparece colgado en una sala', 'Recording of the Creamdo admin panel: a photo of a painting is uploaded, its corners are marked, its measurements are entered and it appears hung in a room')}
          {nota('cr.n1', 'Grabación del panel en uso.', 'Recording of the panel in use.')}
        </div>
        <div class="antes">
          <figure class="papel foto"><img src="trabajos/creamdo-foto.webp?v={V}" width="720" height="960" alt="{A('Foto de un cuadro tomada con el teléfono, torcida y con la pared alrededor', 'Photo of a painting taken on a phone, skewed and with the wall around it')}" loading="lazy"><figcaption data-i="cr.c1">{X('cr.c1', 'Foto original, tomada con un teléfono.', 'Original photo, taken on a phone.')}</figcaption></figure>
          <div class="paso">{nota('cr.n2', 'Cinco pasos guiados.', 'Five guided steps.')}{FL}</div>
        </div>
        <figure class="papel sala"><img src="trabajos/creamdo-sala.webp?v={V}" width="900" height="1350" alt="{A('El mismo cuadro, enderezado y colgado a escala sobre un sofá en una sala con vista al mar', 'The same painting, straightened and hung to scale above a sofa in a room with a sea view')}" loading="lazy"><figcaption data-i="cr.c2">{X('cr.c2', 'Resultado: la misma obra, corregida y a escala real (120 × 90 cm). Imagen referencial.', 'Result: the same piece, corrected and at real scale (120 × 90 cm). Reference image.')}</figcaption></figure>
      </div>
      {puntos([
        ('cr.e1', '<b>Fidelidad de la obra.</b> La IA solo ajusta la luz y la sombra del entorno. La obra publicada es siempre la fotografía original.', '<b>Faithful to the artwork.</b> The AI only adjusts the light and shadow of the setting. The published piece is always the original photograph.'),
        ('cr.e2', '<b>Control automático.</b> Si la IA altera la pieza, el sistema lo detecta y descarta el resultado.', '<b>Automatic check.</b> If the AI alters the piece, the system detects it and discards the result.'),
        ('cr.e3', '<b>Escala real.</b> Siete salas calibradas para que las dimensiones de cada obra correspondan a las reales.', '<b>Real scale.</b> Seven calibrated rooms, so the dimensions of each piece match the real ones.'),
        ('cr.e4', '<b>Sin curva de aprendizaje.</b> Un flujo guiado que se usa desde el teléfono, sin formación previa.', '<b>No learning curve.</b> A guided flow used from a phone, with no training needed.')])}
      <div class="demo d pantallas">
        {lienzo('creamdo-pc', 3970, 'Recorrido por la web de Creamdo Art: portada, obras con medidas y precio, y servicios', 'Scroll through the Creamdo Art site: home, artworks with measurements and price, and services')}
        {nota('cr.w', 'El catálogo público: bilingüe, con ficha por obra y consulta directa por WhatsApp.', 'The public catalogue: bilingual, with a page per piece and direct enquiries over WhatsApp.')}
      </div>
      {ver('cr', 'https://gforero1.github.io/creamdo/', 'Ver el catálogo', 'View the catalogue')}
    </article>'''

tiendas = f'''<article class="caso" id="p-gioia">
      {cabecera('gc', 'Gioia y Calu, tiendas de accesorios y trajes de baño', 'Gioia and Calu, accessories and swimwear shops',
        'Dos tiendas con la misma base y la identidad de cada marca.', 'Two shops on the same base, each with its own brand identity.',
        [('Las dos venden por Instagram y WhatsApp, con catálogos que vivían en presentaciones de Canva. Necesitaban una tienda donde el cliente arme su pedido y una forma de actualizarla sin pedírselo a nadie.',
          'Both sell through Instagram and WhatsApp, with catalogues that lived in Canva presentations. They needed a shop where customers build their order, and a way to update it without asking anyone.'),
         ('Desarrollamos una tienda con carrito que envía el pedido completo por WhatsApp y un panel para la dueña. La segunda tienda partió de la primera: misma base probada, con el diseño sacado del catálogo y el logo de cada marca.',
          'We built a shop whose cart sends the complete order over WhatsApp, plus an admin panel for the owner. The second shop started from the first: the same tested base, with a design taken from each brand\'s catalogue and logo.')],
        ['#FFF4EC', '#D95E7D', '#7A5241', '#C79797', '#2B2424'], 'Fraunces · Marcellus')}
      <div class="demo b pantallas">
        <div class="col-movil">
          {movil_clip('gioia-admin', 'Grabación del panel de Gioia en un teléfono: se cambia el precio de un collar y el cambio aparece en la tienda', 'Recording of the Gioia admin panel on a phone: the price of a necklace is changed and the change appears in the shop')}
          {nota('gc.n1', 'Gioia: se cambia un precio en el panel y la tienda lo muestra al momento.', 'Gioia: a price is changed in the panel and the shop shows it straight away.')}
        </div>
        {lienzo('gioia-pc', 4472, 'Recorrido por la tienda de Gioia: portada, categorías y collares con precio en dos monedas', 'Scroll through the Gioia shop: home, categories and necklaces priced in two currencies')}
      </div>
      <div class="demo c pantallas">
        {lienzo('calu-pc', 4472, 'Recorrido por la tienda de Calu: trajes de baño por categoría, con la prenda saliéndose del marco', 'Scroll through the Calu shop: swimwear by category, with each garment breaking out of its frame')}
        <div class="col-movil">
          {movil_captura('calu-movil', 6750, 'Recorrido por la tienda de Calu en un teléfono', 'Scroll through the Calu shop on a phone')}
          {nota('gc.n2', 'Calu: la prenda se sale del marco, como en su catálogo impreso.', 'Calu: each garment breaks out of its frame, as in her printed catalogue.')}
        </div>
      </div>
      {puntos([
        ('gc.e1', '<b>Panel desde el teléfono.</b> Productos, fotos, precios, agotados y pedidos, sin tocar código.', '<b>Admin from a phone.</b> Products, photos, prices, sold-out items and orders, without touching code.'),
        ('gc.e2', '<b>Catálogo migrado.</b> Más de 200 piezas pasadas de su catálogo de Canva a la tienda, con su foto recortada.', '<b>Catalogue migrated.</b> Over 200 pieces moved from her Canva catalogue into the shop, each with its cropped photo.'),
        ('gc.e3', '<b>Pedidos fiables.</b> El servidor recalcula precios y totales antes de registrar el pedido.', '<b>Reliable orders.</b> The server recalculates prices and totals before logging the order.'),
        ('gc.e4', '<b>Hecho a la medida de cada una.</b> Calu filtra por talla y suma el delivery según la zona; Gioia aplica su precio al mayor.', '<b>Fitted to each one.</b> Calu filters by size and adds delivery by area; Gioia applies its wholesale price.')])}
      <p class="cierre dos"><a class="ola-enlace" href="https://gioiavnzla.pages.dev/" target="_blank" rel="noopener" data-i="gc.ver1">{X('gc.ver1', 'Ver Gioia', 'Visit Gioia')}</a><a class="ola-enlace" href="https://calushop.pages.dev/" target="_blank" rel="noopener" data-i="gc.ver2">{X('gc.ver2', 'Ver Calu', 'Visit Calu')}</a></p>
    </article>'''

atempo = f'''<article class="caso" id="p-atempo">
      {cabecera('at', 'Atempo, consulta de psicología online', 'Atempo, online psychology practice',
        'Una web que su dueña edita sola: textos, foto, precios y hasta la tipografía.', 'A site its owner edits herself: copy, photo, fees and even the typography.',
        [('Una psicóloga que atiende en español y en inglés quería presentarse con calma y que la contactaran. Y no depender de nadie para cambiar un precio o una frase.',
          'A psychologist who works in Spanish and English wanted to present herself calmly and be easy to contact. And not depend on anyone to change a fee or a sentence.'),
         ('Desarrollamos la web y un editor propio con vista previa en vivo. Toca cualquier texto, lo cambia y decide cuándo publicarlo.',
          'We built the site and a custom editor with a live preview. She taps any text, changes it and decides when to publish.')],
        ['#E6E1DA', '#C2BECB', '#5A391E', '#A5676F'], 'Newsreader · Albert Sans')}
      <div class="demo e">
        {ventana_clip('atempo-editor', 'Grabación del editor de Atempo: se prueban cuatro parejas tipográficas y un color de acento, y la vista previa del teléfono cambia al momento', 'Recording of the Atempo editor: four type pairings and an accent colour are tried, and the phone preview changes straight away')}
        {nota('at.n1', 'Grabación del editor: cada cambio se ve en la vista previa antes de publicar.', 'Recording of the editor: every change shows in the preview before publishing.')}
      </div>
      {puntos([
        ('at.e1', '<b>Editor tipo tienda en línea.</b> Textos, foto, honorarios y datos de contacto, en español y en inglés.', '<b>An online-shop style editor.</b> Copy, photo, fees and contact details, in Spanish and English.'),
        ('at.e2', '<b>Diseño con límites.</b> Cuatro parejas tipográficas cerradas y un aviso si un color deja el texto poco legible.', '<b>Design with guardrails.</b> Four fixed type pairings and a warning if a colour makes text hard to read.'),
        ('at.e3', '<b>Nada se pierde.</b> Cada publicación guarda la versión anterior; se puede volver a cualquiera de las últimas 30.', '<b>Nothing gets lost.</b> Each publish keeps the previous version; any of the last 30 can be restored.'),
        ('at.e4', '<b>Concepto propio.</b> "A tempo" es volver al tiempo original: una línea que respira a seis respiraciones por minuto recorre la página.', '<b>Its own concept.</b> "A tempo" means returning to the original tempo: a line breathing at six breaths a minute runs through the page.')])}
      {ver('at', 'https://atempopsychology.com/', 'Ver la web', 'Visit the site')}
    </article>'''

ingenieria = f'''<article class="caso" id="p-0701">
      {cabecera('ob', '0701 Ingeniería, ingeniería y construcción', '0701 Ingeniería, engineering and construction',
        'Cada obra con su memoria descriptiva, como se presenta ante un cliente industrial.', 'Every project with its own technical report, the way it is presented to an industrial client.',
        [('Una empresa con veinte años de obras tenía su trayectoria en un brochure en PDF, con fotos pequeñas y difíciles de compartir.',
          'A company with twenty years of projects had its track record in a PDF brochure, with small photos that were hard to share.'),
         ('Desarrollamos una web que traslada la identidad del brochure y da a cada obra su propia página: objeto, alcance, datos técnicos y registro fotográfico.',
          'We built a site that carries over the brochure\'s identity and gives each project its own page: scope, works carried out, technical data and photo record.')],
        ['#0D2A4A', '#F1B432', '#1D4569', '#F2F4F7'], 'Red Hat Display · Red Hat Text')}
      <div class="demo c pantallas">
        {lienzo('0701-pc', 7393, 'Recorrido por la web de 0701 Ingeniería: portada, servicios y obras recientes', 'Scroll through the 0701 Ingeniería site: home, services and recent projects')}
        <div class="col-movil">
          {movil_captura('0701-obra-movil', 6750, 'Memoria descriptiva de una obra de 0701 Ingeniería en un teléfono', 'Technical report of a 0701 Ingeniería project on a phone')}
          {nota('ob.n1', 'La memoria descriptiva de una obra, en el teléfono.', 'A project\'s technical report, on a phone.')}
        </div>
      </div>
      {puntos([
        ('ob.e1', '<b>Una página por obra.</b> Memoria descriptiva con índice, datos técnicos y visor de fotos, lista para enviar a un cliente.', '<b>A page per project.</b> A technical report with contents, technical data and photo viewer, ready to send to a client.'),
        ('ob.e2', '<b>La identidad del brochure.</b> El techo de la portada, el amarillo y el 0701 gigante salen de su material impreso.', '<b>The brochure\'s identity.</b> The roof shape, the yellow and the giant 0701 come from their printed material.'),
        ('ob.e3', '<b>Fotos recuperadas.</b> Las imágenes del brochure llegaban pequeñas; se ampliaron y corrigieron una a una.', '<b>Photos recovered.</b> The brochure images came in small; each one was enlarged and corrected.'),
        ('ob.e4', '<b>Logo en vector.</b> Redibujado a partir del original para que se vea nítido a cualquier tamaño.', '<b>Vector logo.</b> Traced from the original so it stays sharp at any size.')])}
      {ver('ob', 'https://0701-ingenieria.pages.dev/', 'Ver la web', 'Visit the site')}
    </article>'''

# ---------- Más proyectos (formato compacto) ----------
def compacto(k, id_, quien_es, quien_en, t_es, t_en, p_es, p_en, media, items, url, ver_es, ver_en):
    return f'''<article class="compacto pantallas" id="{id_}">
        <div class="medio">{media}</div>
        <div class="texto">
          <p class="de-quien" data-i="{k}.quien">{X(k+'.quien', quien_es, quien_en)}</p>
          <h3 class="brocha" data-i="{k}.t">{X(k+'.t', t_es, t_en)}</h3>
          <p data-i="{k}.p1">{X(k+'.p1', p_es, p_en)}</p>
          {puntos(items)}
          {ver(k, url, ver_es, ver_en)}
        </div>
      </article>'''

avanza = compacto('av', 'p-avanza', 'Avanza con Gabriel, sesiones de CV y entrevistas', 'Avanza con Gabriel, CV and interview sessions',
    'Una web que aplica lo que enseña: se lee como un buen CV.', 'A site that practises what it teaches: it reads like a good CV.',
    'Gabriel ayuda a preparar el currículum y las entrevistas. La web muestra su método con un ejemplo real y deja reservar la sesión sin salir de la página.',
    'Gabriel helps people prepare their CV and interviews. The site shows his method with a real example and lets people book a session without leaving the page.',
    movil_clip('avanza-cv', 'Grabación de la web de Avanza con Gabriel: un CV de ejemplo cambia entre la versión de antes y la de después', 'Recording of the Avanza con Gabriel site: a sample CV switches between the before and after versions'),
    [('av.e1', '<b>Antes y después.</b> Un CV de ejemplo que cambia al tocarlo, con las frases clave subrayadas.', '<b>Before and after.</b> A sample CV that switches with a tap, with key phrases underlined.'),
     ('av.e2', '<b>Reserva en la página.</b> El calendario se abre ahí mismo, sin cargar nada hasta que se pide.', '<b>Booking on the page.</b> The calendar opens right there, loading nothing until it is asked for.'),
     ('av.e3', '<b>Fotos recortadas a mano.</b> Gabriel aparece por delante de la hoja de CV.', '<b>Hand-cut photos.</b> Gabriel stands in front of the CV sheet.')],
    'https://avanzacongabriel.pages.dev/', 'Ver la web', 'Visit the site')

omary = compacto('om', 'p-omary', 'Omary Belisario, creadora de contenido', 'Omary Belisario, content creator',
    'Un portafolio que presenta su trabajo a una marca en menos de un minuto.', 'A portfolio that presents her work to a brand in under a minute.',
    'Omary produce vídeo para marcas de belleza. Su portafolio era una presentación; ahora es un sitio propio, con el trabajo por categoría y un canal directo para pedir presupuesto.',
    'Omary produces video for beauty brands. Her portfolio used to be a slide deck; it is now a site of her own, with the work by category and a direct channel to request a quote.',
    movil_captura('omary-movil', 5447, 'Recorrido por el portafolio de Omary Belisario en un teléfono', 'Scroll through Omary Belisario\'s portfolio on a phone'),
    [('om.e1', '<b>Diseño propio.</b> Desarrollado a partir de su identidad visual, sin plantilla.', '<b>Custom design.</b> Developed from her visual identity, with no template.'),
     ('om.e2', '<b>Vídeo tratado.</b> Cada pieza se procesa para conservar el color original.', '<b>Processed video.</b> Each piece is treated to keep its original colour.'),
     ('om.e3', '<b>Bilingüe.</b> Español o inglés, según el idioma del visitante.', '<b>Bilingual.</b> Spanish or English, depending on the visitor\'s language.')],
    'https://omaryugc.com/', 'Ver el portafolio', 'View the portfolio')

fisio = compacto('fi', 'p-fisio', 'La Tiendita del Fisio, equipos de fisioterapia', 'La Tiendita del Fisio, physiotherapy equipment',
    'Venta en dos monedas, con el tipo de cambio actualizado cada hora.', 'Selling in two currencies, with the exchange rate updated every hour.',
    'Más de 140 productos con precio en dólares y cobro en moneda local. La tienda calcula cada precio con la tasa oficial del día y convierte el carrito en un pedido por WhatsApp.',
    'Over 140 products priced in dollars and paid in local currency. The shop works out every price at the official rate of the day and turns the cart into a WhatsApp order.',
    movil_clip('fisio-pedido', 'Grabación de un pedido en La Tiendita del Fisio: se añaden tres productos y se abre el pedido con el total en dólares y en moneda local', 'Recording of an order in La Tiendita del Fisio: three products are added and the order opens with the total in dollars and local currency'),
    [('fi.e1', '<b>Tipo de cambio automático.</b> La tasa oficial se consulta cada hora, sin intervención manual.', '<b>Automatic exchange rate.</b> The official rate is checked every hour, with no manual work.'),
     ('fi.e2', '<b>Pedido estructurado.</b> Llega por WhatsApp con productos, cantidades y total, y queda registrado.', '<b>Structured order.</b> It arrives on WhatsApp with products, quantities and total, and is logged.'),
     ('fi.e3', '<b>Gestión autónoma.</b> La dueña actualiza productos, precios y fotos desde su panel.', '<b>Self-managed.</b> The owner updates products, prices and photos from her panel.')],
    'https://gforero1.github.io/latienditadelfisio/', 'Ver la tienda', 'View the shop')

# ---------- Boyas: los proyectos flotan en el agua y llevan a cada uno ----------
BOYAS = [('p-creamdo', 'Creamdo Art'), ('p-gioia', 'Gioia'), ('p-atempo', 'Atempo'), ('p-0701', '0701 Ingeniería'),
         ('p-gioia', 'Calu'), ('p-avanza', 'Avanza con Gabriel'), ('p-omary', 'Omary Belisario'), ('p-fisio', 'La Tiendita del Fisio')]
boyas = ''.join(f'<a class="boya" href="#{i}">{n}</a>' for i, n in BOYAS)

# ---------- Servicios, cada uno con el proyecto donde se ve ----------
def servicio(k, t_es, t_en, d_es, d_en, prueba):
    enl = ' '.join(f'<a href="#{i}">{n}</a>' for i, n in prueba)
    return f'<li><h3 data-i="{k}.t">{X(k+".t", t_es, t_en)}</h3><p><span data-i="{k}.d">{X(k+".d", d_es, d_en)}</span> <span class="prueba"><span data-i="lovesen">{X("lovesen", "Lo ves en", "See it in")}</span> {enl}</span></p></li>'
servicios = ''.join([
    servicio('s1', 'Tiendas y catálogos', 'Shops and catalogues', 'Con pedido por WhatsApp o con pago en línea, según cómo venda el negocio.', 'With WhatsApp ordering or online payment, depending on how the business sells.', [('p-gioia', 'Gioia'), ('p-gioia', 'Calu'), ('p-fisio', 'La Tiendita del Fisio')]),
    servicio('s2', 'Paneles de gestión', 'Admin panels', 'Para actualizar productos, precios y pedidos desde el teléfono, sin depender de un desarrollador.', 'To update products, prices and orders from a phone, without depending on a developer.', [('p-gioia', 'Gioia'), ('p-creamdo', 'Creamdo')]),
    servicio('s3', 'Editores de contenido', 'Content editors', 'Para cambiar textos, fotos y precios de una web de servicios, con vista previa antes de publicar.', 'To change the copy, photos and fees of a services site, with a preview before publishing.', [('p-atempo', 'Atempo')]),
    servicio('s4', 'Herramientas con IA', 'AI tools', 'Automatizan tareas repetitivas, como preparar fotos de producto, con controles que verifican el resultado.', 'They automate repetitive work, such as preparing product photos, with checks that verify the result.', [('p-creamdo', 'Creamdo')]),
    servicio('s5', 'Webs corporativas', 'Company websites', 'Trayectoria, servicios y una página por proyecto, con la identidad que la empresa ya tiene.', 'Track record, services and a page per project, using the identity the company already has.', [('p-0701', '0701 Ingeniería')]),
    servicio('s6', 'Portafolios y reservas', 'Portfolios and bookings', 'Para mostrar el trabajo y que el cliente reserve o pida presupuesto sin salir de la página.', 'To show the work and let clients book or ask for a quote without leaving the page.', [('p-avanza', 'Avanza'), ('p-omary', 'Omary')]),
    servicio('s7', 'Varias monedas e idiomas', 'Currencies and languages', 'Precios convertidos al tipo de cambio del día y contenido en el idioma de cada visitante.', 'Prices converted at the day\'s exchange rate and content in each visitor\'s language.', [('p-fisio', 'La Tiendita del Fisio'), ('p-atempo', 'Atempo')]),
])

html = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{A('muelle0 | Diseño y desarrollo web a medida', 'muelle0 | Custom web design and development')}</title>
<meta name="description" content="{A('Desarrollamos webs a medida y las herramientas para que cada negocio las gestione solo: tiendas con pedido por WhatsApp, paneles y editores de contenido, webs corporativas y herramientas con IA.', 'We build custom websites and the tools for each business to run them on its own: shops with WhatsApp ordering, admin panels and content editors, company websites and AI tools.')}">
<meta name="theme-color" content="#F2EEE6">
<link rel="icon" href="marca/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="marca/icono-180.png">
<meta property="og:title" content="{A('muelle0 | Diseño y desarrollo web a medida', 'muelle0 | Custom web design and development')}">
<meta property="og:description" content="{A('Webs a medida y las herramientas para gestionarlas.', 'Custom websites and the tools to run them.')}">
<meta property="og:image" content="https://muelle0.com/marca/compartir.png">
<meta property="og:type" content="website">
<meta property="og:url" content="https://muelle0.com/">
<link rel="canonical" href="https://muelle0.com/">
<link rel="alternate" hreflang="es" href="https://muelle0.com/">
<link rel="alternate" hreflang="en" href="https://muelle0.com/en/">
<link rel="alternate" hreflang="x-default" href="https://muelle0.com/">
<meta property="og:locale" content="es_ES">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"ProfessionalService","name":"muelle0","url":"https://muelle0.com/","logo":"https://muelle0.com/marca/icono-180.png","image":"https://muelle0.com/marca/compartir.png","description":"{A('Diseño y desarrollo de webs a medida y de las herramientas para gestionarlas: tiendas, paneles de gestión, editores de contenido, webs corporativas y herramientas con IA.', 'Custom web design and development, plus the tools to run each site: shops, admin panels, content editors, company websites and AI tools.')}","email":"muelle0agencia@gmail.com","sameAs":["https://www.instagram.com/muelle0agencia/"],"knowsLanguage":["es","en"]}}</script>
<link rel="preload" href="fuentes/recursive-brocha.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="estilo.css?v={V}">
</head>
<body>
<header class="cielo" id="inicio">
  <div class="barra">
    <a class="marca" href="#inicio" aria-label="{A('muelle0, inicio', 'muelle0, home')}"><img src="marca/mono.svg" width="608" height="531" alt=""></a>
    <a class="sec" href="#trabajos" data-i="nav.trabajos">{X('nav.trabajos', 'Proyectos', 'Work')}</a>
    <a class="sec opcional" href="#tuyo" data-i="nav.tuyo">{X('nav.tuyo', 'Servicios', 'Services')}</a>
    <a class="sec" href="#contacto" data-i="nav.contacto">{X('nav.contacto', 'Contacto', 'Contact')}</a>
    <div class="idioma" role="group" aria-label="Idioma / Language">
      <a href="./" hreflang="es" lang="es" aria-current="true" aria-label="Español">ES</a>
      <a href="en/" hreflang="en" lang="en" aria-label="English">EN</a>
    </div>
  </div>
  <div class="portada">
    <p class="logo-grande">{logo}</p>
    <div class="dice">
      <h1 class="brocha" data-i="titulo">{X('titulo', 'Desarrollamos webs a medida y las herramientas para que cada negocio las gestione solo.', 'We build custom websites, and the tools for each business to run them on its own.')}</h1>
      <p class="quienes" data-i="quienes">{X('quienes', 'Tiendas con pedido por WhatsApp, webs de servicios, portafolios y webs corporativas. Cada proyecto parte de cómo trabaja hoy el negocio y termina en algo que su equipo maneja sin depender de nosotros.', 'Shops with WhatsApp ordering, services sites, portfolios and company websites. Every project starts from how the business works today and ends in something its team runs without depending on us.')}</p>
      <a class="ola-enlace" href="#trabajos" data-i="ir">{X('ir', 'Ver proyectos', 'See the work')}</a>
    </div>
  </div>
  <div class="agua">
    <canvas aria-hidden="true"></canvas>
    <nav class="boyas" aria-label="{A('Proyectos', 'Projects')}">{boyas}</nav>
    <button class="flotador" type="button" aria-label="{A('El 0 de muelle0 flotando. Enter lo lanza al aire.', 'The 0 from muelle0, floating. Press Enter to throw it in the air.')}">{cero}</button>
    <span class="pista" aria-hidden="true" data-i="pista">{X('pista', 'Arrástralo', 'Drag it')}</span>
    <button class="pausa" type="button" aria-pressed="false">{A('Pausar movimiento', 'Pause motion')}</button>
  </div>
</header>

<main>
  <section class="mar" id="trabajos">
    <h2 class="brocha entrada" data-i="entrada">{X('entrada', 'Proyectos recientes, <span>y el problema que resolvió cada uno.</span>', 'Recent projects, <span>and the problem each one solved.</span>')}</h2>

    {creamdo}

    {tiendas}

    {atempo}

    {ingenieria}

    <div class="mas-proyectos">
      <h2 class="brocha" data-i="mas.t">{X('mas.t', 'Más proyectos', 'More projects')}</h2>
      {avanza}
      {omary}
      {fisio}
    </div>
  </section>

  <section class="tuyo" id="tuyo">
    <h2 class="brocha" data-i="tuyo.t">{X('tuyo.t', 'Qué desarrollamos', 'What we build')}</h2>
    <p class="bajada" data-i="tuyo.p">{X('tuyo.p', 'Trabajamos sobre problemas concretos de venta y de gestión. Cada servicio está en al menos un proyecto de esta página.', 'We work on specific sales and operations problems. Every service is in at least one project on this page.')}</p>
    <ul class="preguntas">{servicios}</ul>
  </section>

  <svg class="rompiente" viewBox="0 0 1440 110" preserveAspectRatio="none" aria-hidden="true"><path d="M0 62 C 160 20, 300 96, 470 60 S 760 8, 930 52 S 1250 100, 1440 38 V110 H0Z"/></svg>
  <section class="orilla" id="contacto">
    <h2 class="brocha" data-i="contacto.t">{X('contacto.t', 'Cuéntanos qué necesita tu negocio.', 'Tell us what your business needs.')}</h2>
    <p class="bajada" data-i="contacto.p">{X('contacto.p', 'Describe qué vendes y qué problema quieres resolver. Respondemos con una propuesta concreta, en español o en inglés.', 'Describe what you sell and the problem you want to solve. We reply with a specific proposal, in Spanish or English.')}</p>
    <a class="correo" href="mailto:muelle0agencia@gmail.com">muelle0agencia<wbr>@gmail.com</a>
    <div class="mas">
      <a class="ola-enlace" href="https://www.instagram.com/muelle0agencia/" target="_blank" rel="noopener">Instagram @muelle0agencia</a>
    </div>
    <footer class="pie">
      <img src="marca/logo.svg" width="1433" height="684" alt="muelle0">
      <p data-i="pie">{X('pie', 'Diseño y desarrollo web a medida.', 'Custom web design and development.')}</p>
    </footer>
  </section>
</main>
<script src="muelle.js?v={V}" defer></script>
</body>
</html>
'''
open('index.html', 'w').write(html)

# ---------- Inglés ----------
en = html
for k, v in EN.items():
    pat = re.compile(r'(<(\w+)[^>]*data-i="' + re.escape(k) + r'"[^>]*>)(.*?)(</\2>)', re.S)
    en, n = pat.subn(lambda m: m.group(1) + v + m.group(4), en)
    assert n >= 1, k
FIJOS = [
    ('<html lang="es">', '<html lang="en">'),
    ('<meta property="og:url" content="https://muelle0.com/">', '<meta property="og:url" content="https://muelle0.com/en/">'),
    ('<link rel="canonical" href="https://muelle0.com/">', '<link rel="canonical" href="https://muelle0.com/en/">'),
    ('content="es_ES"', 'content="en_GB"'),
    ('<a href="./" hreflang="es" lang="es" aria-current="true" aria-label="Español">ES</a>', '<a href="../" hreflang="es" lang="es" aria-label="Español">ES</a>'),
    ('<a href="en/" hreflang="en" lang="en" aria-label="English">EN</a>', '<a href="./" hreflang="en" lang="en" aria-current="true" aria-label="English">EN</a>'),
]
for a, b in FIJOS:
    assert a in en, a
    en = en.replace(a, b)
for a, b in set(ATR):
    hecho = False
    for izq, der in (('"', '"'), ('>', '<')):
        if izq + a + der in en:
            en = en.replace(izq + a + der, izq + b + der); hecho = True
    assert hecho, a
for pre in ['href="estilo.css', 'src="muelle.js', 'src="marca/', 'href="marca/', 'src="trabajos/', 'data-src="clips/', 'poster="clips/', 'href="fuentes/']:
    en = en.replace(pre, pre.replace('="', '="../'))
os.makedirs('en', exist_ok=True)
open('en/index.html', 'w').write(en)
json.dump(EN, open('herramientas/en.json', 'w'), ensure_ascii=False, indent=1)
print('ok', len(html), len(en), len(EN))
