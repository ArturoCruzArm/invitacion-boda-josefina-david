💒 Invitación de Boda Digital - Paulina & Daniel
Invitación web elegante con diseño inspirado en invitaciones botánicas de alta calidad, con peonías y eucalipto.

🎨 Cambios Principales Implementados
✨ Diseño Renovado
Nueva Paleta de Colores
Crema cálido (
#F8F6F0) como fondo principal
Verde eucalipto (
#4A6B54) para acentos
Dorado elegante (
#D4AF37) para detalles
Beige taupe (
#C9B8A3) para bordes y decoraciones
Tipografía Mejorada
Mr De Haviland: Para los nombres (estilo caligrafía elegante)
Cormorant Garamond: Para títulos y números
Montserrat: Para texto general (con tracking amplio)
Hero Section Rediseñado
Layout minimalista con espaciado amplio
Decoraciones florales en las esquinas (peonías + eucalipto)
Marco geométrico sutil
Tipografía con letter-spacing amplio
Estructura: TE INVITAMOS A → NUESTRA BODA → Nombres → Fecha
📁 Archivos Modificados
invitacion-boda/
├── index.html          ← ACTUALIZADO ✅
├── styles.css          ← ACTUALIZADO ✅
├── script.js           ← ACTUALIZADO ✅
├── README.md           ← Este archivo
├── contrato.html       (sin cambios)
├── DATOS_PARA_PERSONALIZAR.txt (sin cambios)
└── .gitignore          (sin cambios)
🖼️ Imágenes Necesarias
Para que el diseño funcione perfectamente, necesitas agregar estas imágenes:

Decoraciones Florales (IMPORTANTE)
Crea o descarga imágenes PNG con fondo transparente:

peonia-left.png (esquina superior izquierda)
Dimensiones recomendadas: 500x500px
Contenido: Peonías blancas + hojas de eucalipto
Estilo: Acuarela suave, orientada hacia abajo-derecha
peonia-right.png (esquina inferior derecha)
Dimensiones recomendadas: 550x550px
Contenido: Peonías blancas + hojas de eucalipto
Estilo: Acuarela suave, orientada hacia arriba-izquierda
¿Dónde conseguir las imágenes florales?
Opción 1: Usar marcadores de posición temporales

bash
# Las decoraciones están configuradas pero serán invisibles sin las imágenes
# El sitio funcionará perfectamente mientras consigues las imágenes finales
Opción 2: Generarlas con IA

Usa DALL-E, Midjourney o Stable Diffusion
Prompt sugerido: "watercolor white peony flowers with eucalyptus leaves, botanical illustration, transparent background, soft colors, elegant wedding style"
Opción 3: Descargar de bancos de imágenes

Freepik.com (busca "watercolor peony eucalyptus PNG")
Pngtree.com
Vecteezy.com
Opción 4: Contratar diseñador

Fiverr: $5-20 USD
Upwork: $10-50 USD
Otras Imágenes Requeridas
invitacion.jpeg
Tu foto actual de pareja
Dimensiones: 800x800px mínimo
Ya la tienes ✅
musica-fondo.mp3 (opcional)
Canción romántica de 2-3 minutos
Formato: MP3
Bitrate: 128kbps
favicon.svg (opcional)
Ícono del sitio (aparece en la pestaña del navegador)
Puedes usar un emoji: 💍 o 💐
🚀 Instalación Rápida
1. Estructura de Archivos
Asegúrate de tener esta estructura:

boda-daniel-paulina/
├── index.html
├── styles.css
├── script.js
├── invitacion.jpeg
├── peonia-left.png        ← AGREGAR
├── peonia-right.png       ← AGREGAR
├── musica-fondo.mp3       ← OPCIONAL
├── favicon.svg            ← OPCIONAL
└── README.md
2. Publicar en GitHub Pages
bash
# 1. Crear repositorio en GitHub
# Ve a github.com y crea un nuevo repositorio público

# 2. Inicializar Git local
git init
git add .
git commit -m "Invitación de boda - Diseño actualizado"

# 3. Conectar con GitHub
git remote add origin https://github.com/TU_USUARIO/boda-paulina-daniel.git
git branch -M main
git push -u origin main

# 4. Activar GitHub Pages
# Ve a: Settings → Pages → Source: main branch → Save
Tu sitio estará en: https://TU_USUARIO.github.io/boda-paulina-daniel/

3. Opcional: Dominio Personalizado
Si quieres un dominio como paulinaydaniel.com:

Compra el dominio en Namecheap, GoDaddy, etc. (~$10-15 USD/año)
En GitHub Pages settings, agrega el dominio personalizado
Configura los DNS según las instrucciones de GitHub
🎨 Personalización Adicional
Cambiar Colores
En styles.css, líneas 5-15:

css
:root {
    --crema-calido: #F8F6F0;        /* Fondo principal */
    --verde-eucalipto: #4A6B54;     /* Color primario */
    --verde-salvia: #A3B18A;        /* Color secundario */
    --beige-taupe: #C9B8A3;         /* Bordes y detalles */
    --dorado-elegante: #D4AF37;     /* Acentos dorados */
}
Cambiar Fuentes
Si quieres usar otras fuentes, modifica en index.html (línea 10):

html
<link href="https://fonts.googleapis.com/css2?family=TuFuenteAqui&display=swap" rel="stylesheet">
Y actualiza en styles.css:

css
:root {
    --font-script: 'TuFuenteScript', cursive;
    --font-serif: 'TuFuenteSerif', serif;
    --font-sans: 'TuFuenteSans', sans-serif;
}
Modificar Textos
Todos los textos están en index.html. Busca y reemplaza según necesites:

Nombres de los novios
Nombres de los padres
Fechas y horarios
Direcciones
Números de teléfono
Redes sociales
📱 Características Implementadas
✅ Funcionalidades Activas
 Diseño responsivo (móvil, tablet, desktop)
 Cuenta regresiva en tiempo real
 Música de fondo con control
 Botones de Google Maps y Waze
 Integración con WhatsApp para RSVP
 Compartir invitación (Web Share API)
 Animaciones suaves al hacer scroll
 Lazy loading de imágenes
 Decoraciones florales animadas
 Textura de papel en el fondo
 SEO optimizado
🎯 Checklist Pre-Lanzamiento
Antes de compartir la invitación, verifica:

Contenido
 Nombres correctos de novios y padres
 Fecha y hora correctas (19 de Diciembre 2025, 7:00 PM)
 Direcciones verificadas
 Links de Google Maps funcionando
 Links de Waze funcionando
 Números de WhatsApp correctos
 Redes sociales actualizadas
 Hashtag personalizado
Diseño
 Imágenes florales agregadas (peonia-left.png, peonia-right.png)
 Foto de pareja cargada (invitacion.jpeg)
 Colores ajustados a tu gusto
 Fuentes cargando correctamente
Funcionalidad
 Contador regresivo funcionando
 Música de fondo (si la agregaste)
 Botones de mapa abriendo correctamente
 WhatsApp redirigiendo bien
 Botón compartir funcionando
 Responsive en móvil
Testing
 Probado en Chrome
 Probado en Safari
 Probado en Firefox
 Probado en móvil iPhone
 Probado en móvil Android
 Velocidad de carga aceptable
🐛 Solución de Problemas
Las decoraciones florales no se ven
Problema: Faltan las imágenes PNG Solución:

Agrega peonia-left.png y peonia-right.png a la raíz del proyecto
O temporalmente comenta las líneas en index.html:
html
<!-- <div class="floral-decoration top-left">... -->
<!-- <div class="floral-decoration bottom-right">... -->
La música no se reproduce automáticamente
Problema: Los navegadores bloquean autoplay Solución: Es normal. El usuario debe hacer clic en el botón 🔇 para activar la música. El sitio intentará reproducirla automáticamente después de la primera interacción.

Los mapas no abren
Problema: Coordenadas incorrectas Solución: Verifica las coordenadas en Google Maps y actualiza los enlaces en index.html.

El contador muestra números negativos
Problema: La fecha ya pasó (modo de prueba) Solución: Verifica la fecha en script.js línea 36:

javascript
const weddingDate = new Date('2025-12-19T19:00:00').getTime();
El sitio se ve mal en móvil
Problema: Caché del navegador Solución:

Forzar recarga: Ctrl+Shift+R (Windows) o Cmd+Shift+R (Mac)
Limpiar caché del navegador
Verificar que styles.css tenga las media queries (@media)
📊 Comparación: Antes vs Después
Aspecto	Antes	Después
Tipografía	Fuentes genéricas	Mr De Haviland (script elegante)
Paleta	Verde oliva/dorado	Crema/eucalipto/dorado
Hero	Simple con fondo	Decoraciones florales + marco geométrico
Espaciado	Compacto	Amplio y respirable (letter-spacing)
Estilo	Moderno	Elegante botánico (peonía/eucalipto)
Textura	Sin textura	Textura de papel sutil
Animaciones	Básicas	Suaves y naturales
🎓 Aprende Más
Recursos Útiles
Paletas de colores: coolors.co, color.adobe.com
Fuentes gratis: fonts.google.com
Imágenes: unsplash.com, pexels.com, freepik.com
Íconos: fontawesome.com, heroicons.com
Testing: browserstack.com (cross-browser testing)
Inspiración de Diseño
Pinterest: "botanical wedding invitation"
Dribbble: "elegant wedding website"
Behance: "wedding invitation design"
💡 Ideas Adicionales (Futuras Mejoras)
Si quieres agregar más funcionalidades:

Galería de fotos completa
Lightbox para ver fotos en grande
Grid de múltiples fotos de la pareja
Mapa de la ciudad
Mapa interactivo con Leaflet.js
Marcadores de iglesia, salón, hoteles
Timeline de la relación
Historia de cómo se conocieron
Momentos importantes
Livestream
Para invitados que no puedan asistir
Integración con YouTube/Zoom
Libro de firmas digital
Formulario para mensajes
Galería de mensajes de invitados
Contador de confirmados
"X de Y personas han confirmado"
Barra de progreso visual
📞 Contacto del Fotógrafo
Foro 7 - Arturo Cruz

📱 Teléfono: 477-920-3776
📸 Servicios: Fotografía y Video profesional
📍 Ubicación: León, Guanajuato
🎉 ¡Listo para Compartir!
Una vez que hayas:

✅ Agregado las imágenes florales
✅ Verificado todos los datos
✅ Probado en diferentes dispositivos
✅ Publicado en GitHub Pages
Comparte tu invitación:

Por WhatsApp
En redes sociales
Crea un código QR con tu URL
Envía por email
¡Felicidades por tu boda! 💑✨

Desarrollado con amor para Paulina & Daniel 19 de Diciembre, 2025

