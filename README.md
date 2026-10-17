# muelle0

Web del estudio: portafolio de lo que montamos. Estática, sin dependencias.

- `index.html` (español) y `en/index.html` (inglés): se generan con `python3 herramientas/monta_index.py`. Cada texto va en pareja español/inglés dentro del script (`X(clave, es, en)` y `A(es, en)` para atributos); `herramientas/en.json` se reescribe como registro.
- `estilo.css`: estilos. `muelle.js`: idioma, agua, clips y recorrido de las capturas.
- `marca/`: logo y monograma vectorizados desde el manual de marca de Canva, la ola del logo como subrayado, favicon e imagen para compartir.
- `trabajos/`: capturas largas de cada web y el antes y después de Creamdo (WebP).
- `clips/`: grabaciones reales, mudas y en bucle (MP4 H.264 de 390 px de ancho, con póster).
- `fuentes/`: Recursive recortada a dos archivos.

## Dirección de diseño

Sale del manual de marca ("Manual de marca muelle0" en Canva) y del logo, que es letra de brocha.

- **Idea:** la página es el mar. Arriba, el cielo crema con el logo; la línea del agua, con el 0 flotando; los trabajos, bajo el agua sobre verde; al final, la orilla, donde está el contacto.
- **Color:** verde bahía `#0F3B3A` es la base. Crema `#F2EEE6` para cielo, papel y arena. Coral `#F0694C` solo sobre verde; rojo minio `#D2452D` solo sobre crema. Negro `#161616` solo en el marco del teléfono.
- **Tipografía:** una sola familia, Recursive, con dos voces. "Brocha" (Casual, cursiva, peso 800 a 900) es letra de rotulista y acompaña al logo: titulares y notas a mano. "Texto" (lineal, peso 400) para leer. Sin mayúsculas sostenidas, sin monoespaciada, sin etiquetas encima de los títulos.
- **Logo:** nunca se deforma ni se recolorea. La ola del logo se usa tal cual como subrayado de los enlaces (solo se estira a lo ancho).
- **Proyectos:** los tres siguen el mismo orden: relato, demostración, puntos y enlace. En la demostración siempre hay un teléfono (grabación o captura móvil) con su nota, y una captura de escritorio.
- **Reglas de componente:** teléfonos y capturas van rectos; solo las fotos sueltas (papel) se inclinan. Una única sombra (`--sombra`). Los puntos de cada proyecto usan el mismo componente (`.puntos`). Solo hay una flecha, la que une la foto original con el resultado. Los espacios verticales salen de `--e1`, `--e2` y `--e3`. En teléfono, cada proyecto enseña primero el móvil y luego la captura.
- **Movimiento:** el logo se traza al cargar; el agua responde al ratón y el 0 se puede agarrar y lanzar; los clips y las capturas se mueven solo mientras están en pantalla. Un enlace pausa todo y nada se mueve con `prefers-reduced-motion`.
- **Textos:** sobrios y concretos. Cada proyecto se cuenta como problema, solución y prueba; los servicios, como lo que el cliente consigue. Sin lemas, sin frases promocionales y sin insistir en el origen del estudio. Llamada a la acción única: escribir contando el problema.
- **Lo que no tiene:** numeración decorativa, tarjetas, contadores, testimonios, iconos de línea.

## Estructura de proyectos (octubre 2026)

- **Destacados** (relato, demostración, puntos y enlace, con la ficha de marca del cliente: sus colores y tipografías reales): Creamdo, Gioia y Calu (misma base, dos marcas), Atempo (editor) y 0701 Ingeniería (memoria por obra).
- **Más proyectos**, formato compacto (teléfono, relato, tres puntos): Avanza con Gabriel, Omary, La Tiendita del Fisio.
- **Boyas:** los nombres de los proyectos flotan en el agua de la portada y llevan a cada uno. Derivan despacio, se paran con el ratón o el foco y quedan en fila con movimiento reducido.
- **Servicios:** cada uno enlaza al proyecto donde se ve ("Lo ves en").
- Clips nuevos: `atempo-editor` (escritorio, en `.ventana`), `gioia-admin` y `avanza-cv` (teléfono). Grabados con Playwright sobre cada repo servido en local (Wrangler para Gioia, Calu y Atempo).

## Cómo se hicieron los clips

- `creamdo-admin`: el panel real de Creamdo servido en local con su servidor de pruebas (`pruebas/servidor.js`), recorrido en vista de teléfono con una obra del catálogo. El resultado es el montaje a escala del propio panel.
- `fisio-pedido`: la tienda real servida en local con su `datos.json`, armando un pedido de tres productos.

## Añadir un trabajo

1. Material real: grabación de pantalla o capturas largas, en `clips/` y `trabajos/`.
2. Un `<article class="caso">` nuevo en `herramientas/monta_index.py`: de quién es, qué hubo que inventar y las notas.
3. Sus textos en inglés van en la misma llamada `X(...)`.
4. Subir la versión `V` del script y ejecutar `python3 herramientas/monta_index.py`.

## Contacto que aparece en la web

muelle0agencia@gmail.com · Instagram @muelle0agencia
