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

### 3. Seleccionar fotos

- **Clic en una foto**: Abre el visor de pantalla completa
- **Botón "Seleccionar esta foto"**: Marca/desmarca la foto actual
- **Flechas izquierda/derecha**: Navegar entre fotos
- **ESC**: Cerrar el visor
- **Contador superior izquierdo**: Muestra cuántas fotos has seleccionado

**Límite:** Puedes seleccionar hasta **200 fotos**.

### 4. Exportar selección

Cuando termines de seleccionar:

1. Haz clic en el botón **"Exportar selección"** (esquina inferior derecha)
2. Se descargará un archivo `fotos-seleccionadas-josefina-david.txt`
3. Este archivo contiene la lista de fotos seleccionadas

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
- 🎵 Música de fondo
- 📱 Totalmente responsive (funciona en móviles)
- ⌨️ Navegación con teclado
- 👆 Soporte para gestos táctiles
- 💾 Exportación de selección a archivo de texto
- 🖼️ Visor de pantalla completa
- ✅ Indicadores visuales de fotos seleccionadas

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
