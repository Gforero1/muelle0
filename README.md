# muelle0

Web del estudio: portafolio de lo que montamos. Estática, sin dependencias.

- `index.html`: se genera con `herramientas/monta_index.py` (inyecta los trazos del logo). Los textos en español están ahí; el inglés, en `muelle.js` (`EN`).
- `estilo.css`: estilos. `muelle.js`: idioma, relojes, agua, clips y recorrido de las capturas.
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
- **Trabajos:** cada uno cuenta qué hubo que inventar, no solo qué web es. Se enseña con material real: grabación del panel o del pedido, fotos pegadas como en un corcho, y notas a mano con flechas señalando lo que se hizo a medida. Cada trabajo tiene una composición distinta.
- **Movimiento:** el logo se traza al cargar; el agua responde al ratón y el 0 se puede agarrar y lanzar; los clips y las capturas se mueven solo mientras están en pantalla. Un enlace pausa todo y nada se mueve con `prefers-reduced-motion`.
- **Textos:** en primera persona del plural, con datos reales de cada cliente. La plataforma no es el mensaje: se vende la solución.
- **Lo que no tiene:** numeración decorativa, tarjetas, contadores, testimonios, iconos de línea.

## Cómo se hicieron los clips

- `creamdo-admin`: el panel real de Creamdo servido en local con su servidor de pruebas (`pruebas/servidor.js`), recorrido en vista de teléfono con una obra del catálogo. El resultado es el montaje a escala del propio panel.
- `fisio-pedido`: la tienda real servida en local con su `datos.json`, armando un pedido de tres productos.

## Añadir un trabajo

1. Material real: grabación de pantalla o capturas largas, en `clips/` y `trabajos/`.
2. Un `<article class="caso">` nuevo en `herramientas/monta_index.py`: de quién es, qué hubo que inventar y las notas.
3. Sus textos en inglés en `muelle.js` (`EN`).
4. Subir la versión `V` del script y ejecutar `python3 herramientas/monta_index.py`.

## Contacto que aparece en la web

muelle0agencia@gmail.com · Instagram @muelle0agencia
