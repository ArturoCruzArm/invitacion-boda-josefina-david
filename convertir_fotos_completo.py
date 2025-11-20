from PIL import Image
from pathlib import Path
import warnings
import os
import json

# Ignorar advertencia de imagen grande
warnings.filterwarnings('ignore', category=Image.DecompressionBombWarning)

def convert_to_webp(source_dirs, target_dir, max_width=1920):
    """
    Convierte fotos de múltiples directorios a WebP optimizado

    Args:
        source_dirs: Lista de directorios con las fotos originales
        target_dir: Directorio donde se guardarán las fotos convertidas
        max_width: Ancho máximo de la imagen (default 1920px)
    """
    target_dir = Path(target_dir)
    target_dir.mkdir(exist_ok=True, parents=True)

    # Obtener todas las fotos de todos los directorios
    extensions = ['*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG']
    photos = []

    for source_dir in source_dirs:
        source_path = Path(source_dir)
        if not source_path.exists():
            print(f"ADVERTENCIA: Directorio no encontrado: {source_dir}")
            continue

        print(f"\nBuscando en: {source_dir}")
        for ext in extensions:
            found = list(source_path.glob(ext))
            photos.extend(found)
            if found:
                print(f"  - Encontradas {len(found)} fotos {ext}")

    photos = sorted(photos)

    print(f"\n" + "=" * 100)
    print(f"TOTAL: {len(photos)} fotos para convertir")
    print("=" * 100)

    if len(photos) == 0:
        print("\nERROR: No se encontraron fotos en los directorios especificados.")
        print("\nVerifica que las rutas sean correctas:")
        for dir in source_dirs:
            print(f"  - {dir}")
        input("\nPresiona Enter para salir...")
        return 0, []

    converted = 0
    errors = 0
    photos_list = []

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

            # Agregar a la lista
            photos_list.append({
                'number': i,
                'filename': output_name,
                'original': photo.name
            })

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

    return converted, photos_list

def create_photos_list_js(photos_list, output_file):
    """
    Crea el archivo JavaScript con la lista de fotos

    Args:
        photos_list: Lista de diccionarios con información de fotos
        output_file: Ruta donde guardar el archivo JS
    """
    js_content = "// Lista de fotos generada automáticamente\n"
    js_content += "const photos = [\n"

    for photo in photos_list:
        js_content += f"    {{ name: 'foto_{photo['number']:04d}', path: 'images/{photo['filename']}', filename: '{photo['original']}' }},\n"

    js_content += "];\n"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"\nArchivo photos_list.js creado con {len(photos_list)} fotos")

if __name__ == "__main__":
    # === CONFIGURACIÓN ===
    # Directorios de origen (iglesia + civil)
    source_dirs = [
        r"F:\2025\11\15\Josefia y David\editadas",  # Fotos iglesia
        r"E:\Fotos\Editadas\SI\SI"  # Fotos civil
    ]

    # Directorio del repositorio
    repo_dir = r"C:\Users\foro7\invitacion-boda-josefina-david"

    # Directorio donde se guardarán las fotos convertidas
    target_dir = os.path.join(repo_dir, "images")

    # Archivo JS de lista de fotos
    photos_list_file = os.path.join(repo_dir, "photos_list.js")

    print("=" * 100)
    print("CONVERTIDOR DE FOTOS A WEBP - JOSEFINA & DAVID")
    print("=" * 100)
    print("Origen:")
    for dir in source_dirs:
        print(f"  - {dir}")
    print(f"Destino: {target_dir}")
    print("=" * 100)
    print()

    # Convertir fotos
    num_photos, photos_list = convert_to_webp(source_dirs, target_dir, max_width=1920)

    if num_photos > 0:
        # Crear archivo photos_list.js
        create_photos_list_js(photos_list, photos_list_file)

        print("\n\n" + "=" * 100)
        print("SIGUIENTE PASO:")
        print("=" * 100)
        print("1. Las fotos se han convertido y guardado en: images/")
        print("2. Se ha creado el archivo photos_list.js")
        print("3. Abre 'seleccionar-fotos.html' en tu navegador")
        print("4. Josefina puede seleccionar las fotos que desea")
        print("5. Haz clic en 'Exportar selección' para descargar la lista")
        print("6. Luego podemos hacer commit y push a GitHub Pages")
        print("=" * 100)
    else:
        print("\nNo se pudo completar la conversión.")

    input("\nPresiona Enter para salir...")
