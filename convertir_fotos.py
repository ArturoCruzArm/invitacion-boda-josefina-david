from PIL import Image
from pathlib import Path
import warnings
import os

# Ignorar advertencia de imagen grande
warnings.filterwarnings('ignore', category=Image.DecompressionBombWarning)

def convert_to_webp(source_dir, target_dir, max_width=1920):
    """
    Convierte fotos a WebP optimizado para GitHub Pages

    Args:
        source_dir: Directorio con las fotos originales
        target_dir: Directorio donde se guardarán las fotos convertidas
        max_width: Ancho máximo de la imagen (default 1920px)
    """
    source_dir = Path(source_dir)
    target_dir = Path(target_dir)

    # Crear directorio de destino si no existe
    target_dir.mkdir(exist_ok=True, parents=True)

    # Obtener todas las fotos (jpg, jpeg, png)
    extensions = ['*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG']
    photos = []
    for ext in extensions:
        photos.extend(source_dir.glob(ext))

    photos = sorted(photos)

    print(f"Encontradas {len(photos)} fotos para convertir")
    print("=" * 100)

    converted = 0
    errors = 0

    for i, photo in enumerate(photos, 1):
        try:
            # Abrir imagen
            img = Image.open(photo)

            # Convertir a RGB si es necesario
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')

            width, height = img.size

            # Calcular nuevas dimensiones manteniendo aspecto
            if width > max_width or height > max_width:
                if width > height:
                    new_width = max_width
                    new_height = int(height * (max_width / width))
                else:
                    new_height = max_width
                    new_width = int(width * (max_width / height))

                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                print(f"[{i}/{len(photos)}] {photo.name}: {width}x{height} -> {new_width}x{new_height}")
            else:
                print(f"[{i}/{len(photos)}] {photo.name}: {width}x{height} (sin cambio)")

            # Guardar como WebP con calidad 85
            output_name = f"foto_{i:04d}.webp"
            output_path = target_dir / output_name
            img.save(output_path, 'WEBP', quality=85, method=6)

            converted += 1

        except Exception as e:
            print(f"[{i}/{len(photos)}] ERROR: {photo.name} - {e}")
            errors += 1

    print("\n" + "=" * 100)
    print(f"CONVERSIÓN COMPLETADA")
    print(f"Exitosas: {converted}")
    print(f"Errores: {errors}")
    print(f"Archivos guardados en: {target_dir}")
    print("=" * 100)

    return converted

def update_html_photo_count(html_path, num_photos):
    """
    Actualiza el contador de fotos en el archivo HTML

    Args:
        html_path: Ruta al archivo HTML
        num_photos: Número total de fotos
    """
    html_path = Path(html_path)

    if not html_path.exists():
        print(f"Archivo HTML no encontrado: {html_path}")
        return

    # Leer contenido
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Reemplazar línea de totalPhotos
    old_line = "const totalPhotos = 0; // Se actualizará después de procesar las fotos"
    new_line = f"const totalPhotos = {num_photos};"

    if old_line in content:
        content = content.replace(old_line, new_line)

        # Reemplazar comentario de inicialización
        old_init = "// Inicializar (llamar después de procesar fotos)\n        // generateGallery(totalPhotos);"
        new_init = "// Inicializar\n        generateGallery(totalPhotos);"
        content = content.replace(old_init, new_init)

        # Guardar archivo actualizado
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"\nArchivo HTML actualizado con {num_photos} fotos")
    else:
        print(f"\nNo se pudo actualizar el archivo HTML automáticamente")
        print(f"Por favor, actualiza manualmente 'const totalPhotos = {num_photos};' en {html_path}")

if __name__ == "__main__":
    # === CONFIGURACIÓN ===
    # IMPORTANTE: Actualiza estas rutas según tu sistema

    # Directorio con las fotos editadas de Josefina y David
    # Ella seleccionará 200 fotos entre:
    # - F:\2025\11\15\Josefia y David\editadas (boda iglesia)
    # - E:\Fotos\Editadas\SI\SI (boda civil)

    # Por ahora, especifica la ruta donde están las fotos:
    source_dir = r"F:\2025\11\15\Josefia y David\editadas"

    # Directorio del repositorio
    repo_dir = r"C:\Users\foro7\invitacion-boda-josefina-david"

    # Directorio donde se guardarán las fotos convertidas
    target_dir = os.path.join(repo_dir, "images")

    # HTML a actualizar
    html_path = os.path.join(repo_dir, "seleccionar-fotos.html")

    print("=" * 100)
    print("CONVERTIDOR DE FOTOS A WEBP - JOSEFINA & DAVID")
    print("=" * 100)
    print(f"Origen: {source_dir}")
    print(f"Destino: {target_dir}")
    print("=" * 100)
    print()

    # Verificar que existe el directorio de origen
    if not Path(source_dir).exists():
        print(f"ERROR: No se encuentra el directorio de origen: {source_dir}")
        print("\nPor favor, actualiza la variable 'source_dir' en el script con la ruta correcta.")
        print("\nOpciones:")
        print("  1. F:\\2025\\11\\15\\Josefia y David\\editadas (fotos de iglesia)")
        print("  2. E:\\Fotos\\Editadas\\SI\\SI (fotos de civil)")
        input("\nPresiona Enter para salir...")
        exit(1)

    # Convertir fotos
    num_photos = convert_to_webp(source_dir, target_dir, max_width=1920)

    # Actualizar HTML
    update_html_photo_count(html_path, num_photos)

    print("\n\n" + "=" * 100)
    print("SIGUIENTE PASO:")
    print("=" * 100)
    print("1. Abre 'seleccionar-fotos.html' en tu navegador")
    print("2. Josefina puede seleccionar las fotos que desea")
    print("3. Haz clic en 'Exportar selección' para descargar la lista")
    print("4. Luego podemos hacer commit y push a GitHub Pages")
    print("=" * 100)

    input("\nPresiona Enter para salir...")
