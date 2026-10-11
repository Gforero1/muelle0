# muelle0

Web del estudio: portafolio de las webs que montamos. Estática, sin dependencias ni build.

- `index.html`: toda la página. Los textos en español están en el HTML (`data-i`); el inglés, en `muelle.js` (`EN`).
- `estilo.css`: estilos. `muelle.js`: idioma, relojes, agua y recorrido de las capturas.
- `marca/`: logo y monograma vectorizados desde el manual de marca de Canva, favicon e imagen para compartir.
- `trabajos/`: capturas largas de cada web (WebP, 1400 px de ancho en escritorio y 585 px en móvil).
- `fuentes/`: tipografías alojadas aquí.

## Dirección de diseño

Sale del manual de marca ("Manual de marca muelle0" en Canva), no de una plantilla.

- **Color:** verde bahía `#0F3B3A` de base, crema `#F2EEE6`, rojo minio `#D2452D` para destacar sobre crema y coral `#F0694C` solo como acento sobre verde. Negro `#161616` solo en el marco del teléfono.
- **Logo:** nunca se deforma ni se recolorea. Completo en portada y pie; monograma en la cabecera y el favicon. Sobre verde, letras crema y 0 coral.
- **Tipografía:** Big Shoulders Display (rótulos condensados, como los de un muelle) para nombres de proyecto; Schibsted Grotesk para el texto; Spline Sans Mono para datos y etiquetas. El correo y el Instagram van en minúsculas para que el 0 no se confunda con una O.
- **Estructura:** arriba, sobre crema, quiénes somos; la línea del agua separa la portada de los trabajos, que quedan "bajo el agua" sobre verde. Cada trabajo es una ficha con datos reales y la captura de la web real.
- **Movimiento, solo tres gestos:** el logo se traza al cargar; el agua se mueve, responde al ratón y lleva flotando el 0 del logo, que se puede agarrar y lanzar; las capturas se recorren solas mientras están en pantalla. Un botón pausa todo y nada se mueve con `prefers-reduced-motion`.
- **Textos:** qué es cada web, dónde está el cliente y cómo funciona. Sin eslogan, sin testimonios, sin contadores.
- **Idiomas:** español e inglés. Carga en el idioma del dispositivo y recuerda la elección.

## Añadir un trabajo

1. Capturas largas de la web (escritorio y, si se puede, móvil) en `trabajos/` como WebP.
2. Un bloque `<article class="caso">` nuevo en `index.html`, con su número, lugar, resumen y tres datos.
3. Sus textos en inglés en `muelle.js` (`EN`, claves `cN.*`).
4. Subir el número de versión `?v=` de `estilo.css`, `muelle.js` y las imágenes.

## Contacto que aparece en la web

muelle0agencia@gmail.com · Instagram @muelle0agencia

## Regenerar index.html

`index.html` sale de `herramientas/monta_index.py` (inyecta los trazos del logo desde `herramientas/trazos-logo.json`). Para cambiar textos o añadir un trabajo, edita ese script y ejecuta `python3 herramientas/monta_index.py` desde la raíz.
