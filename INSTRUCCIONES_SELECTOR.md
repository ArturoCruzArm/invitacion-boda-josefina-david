# Selector de Fotos - Josefina & David

## 📸 Descripción

Sistema de selección de fotos para que Josefina pueda elegir las fotos que desea incluir de su boda.

## 🚀 Pasos para usar

### 1. Convertir fotos a WebP

Primero, necesitas convertir las fotos a formato WebP optimizado:

```bash
python convertir_fotos.py
```

**Configuración del script:**
- Abre `convertir_fotos.py` y actualiza estas variables:
  - `source_dir`: Directorio con las fotos originales
    - `F:\2025\11\15\Josefia y David\editadas` (fotos iglesia)
    - `E:\Fotos\Editadas\SI\SI` (fotos civil)
  - El script convertirá automáticamente todas las fotos a WebP

**Nota:** Puedes ejecutar el script múltiples veces con diferentes directorios para incluir fotos de ambas ceremonias (civil e iglesia).

### 2. Abrir el selector de fotos

Una vez convertidas las fotos:

1. Abre el archivo `seleccionar-fotos.html` en tu navegador
2. Verás todas las fotos en una galería elegante
3. Haz clic en cualquier foto para verla en grande

### 3. Seleccionar fotos y categorías

- **Clic en una foto**: Abre el visor de pantalla completa
- **Selecciona una o varias categorías** para cada foto:
  - 📸 **Ampliación** - Para ampliar e imprimir en gran tamaño
  - 🖼️ **Impresión** - Para imprimir en tamaño estándar
  - 📱 **Redes Sociales** - Para compartir en redes sociales
  - 💌 **Inv. Web** - Para usar en la invitación digital
  - 🗑️ **Descartar** - Fotos que no deseas usar
- **Comentarios**: Puedes agregar notas de edición para cada foto
- **Flechas izquierda/derecha**: Navegar entre fotos
- **ESC**: Cerrar el visor
- **Estadísticas en tiempo real**: Muestra cuántas fotos hay en cada categoría

### 4. Filtrar y visualizar

- Usa los **botones de filtro** para ver solo fotos de una categoría específica
- El filtro "Todas las Fotos" muestra toda la galería

### 5. Exportar selección

Cuando termines de categorizar:

1. Haz clic en el botón **"Enviar por WhatsApp"** (color verde)
2. Se abrirá WhatsApp automáticamente con tu selección formateada
3. El mensaje incluye:
   - Resumen general con totales por categoría
   - Lista detallada de fotos por categoría
   - Comentarios y ediciones solicitadas
   - Fecha de generación

### 5. Subir a GitHub Pages

Una vez que tengas las fotos seleccionadas:

```bash
cd C:\Users\foro7\invitacion-boda-josefina-david
git add .
git commit -m "Agregar selector de fotos y fotos convertidas"
git push
```

Luego, configurar GitHub Pages:
1. Ve a Settings → Pages
2. Source: Deploy from a branch
3. Branch: main / (root)
4. Save

La página estará disponible en:
- **Invitación**: https://arturoCruzArm.github.io/invitacion-boda-josefina-david/
- **Selector**: https://arturoCruzArm.github.io/invitacion-boda-josefina-david/seleccionar-fotos.html

## 📁 Estructura de archivos

```
invitacion-boda-josefina-david/
├── index.html                    # Invitación principal
├── seleccionar-fotos.html        # Selector de fotos (NUEVO)
├── convertir_fotos.py            # Script de conversión (NUEVO)
├── images/                       # Fotos convertidas (NUEVO)
│   ├── foto_0001.webp
│   ├── foto_0002.webp
│   └── ...
├── styles.css
├── script.js
└── ...
```

## 🎨 Características del selector

- ✨ Diseño elegante que combina con la invitación
- 🏷️ Sistema de categorías múltiples por foto
- 📊 Estadísticas en tiempo real
- 🔍 Filtros por categoría
- 💬 Comentarios y notas de edición
- 📱 Totalmente responsive (funciona en móviles)
- ⌨️ Navegación con teclado
- 👆 Soporte para gestos táctiles
- 📲 Envío directo por WhatsApp
- 🖼️ Visor de pantalla completa
- ✅ Badges visuales en cada foto

## 🔄 Agregar más fotos después

Si necesitas agregar más fotos después:

1. Coloca las nuevas fotos en el directorio de origen
2. Ejecuta `convertir_fotos.py` nuevamente
3. El script actualizará automáticamente el contador en el HTML
4. Haz commit y push de los cambios

## 📝 Notas

- Las fotos se optimizan automáticamente para web (máx 1920px, calidad 85%)
- El formato WebP reduce el tamaño de archivo sin perder calidad
- El selector guarda la selección localmente (localStorage) mientras trabajas
- Puedes limpiar la selección con el botón "Limpiar selección"

## 🎯 Fotos disponibles

- **Boda Iglesia**: `F:\2025\11\15\Josefia y David\editadas`
- **Boda Civil**: `E:\Fotos\Editadas\SI\SI`
- Josefina elegirá ~200 fotos entre ambas ceremonias
- También seleccionará fotos para ampliación y redes sociales

## 🆘 Solución de problemas

**El script no encuentra las fotos:**
- Verifica que la ruta en `source_dir` sea correcta
- Asegúrate de que las fotos tengan extensión .jpg, .jpeg o .png

**No se actualizó el contador de fotos:**
- Abre `seleccionar-fotos.html` y actualiza manualmente:
  - `const totalPhotos = X;` (donde X es el número de fotos)
  - Descomenta: `generateGallery(totalPhotos);`

**GitHub Pages no muestra las fotos:**
- Las fotos pueden ser demasiado grandes para GitHub
- Considera usar un servicio de hosting de imágenes externo
- O reduce el número de fotos

---

**Creado por:** Foro 7 - Arturo Cruz
**Contacto:** 477-920-3776
