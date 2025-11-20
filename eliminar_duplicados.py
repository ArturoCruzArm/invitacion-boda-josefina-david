from pathlib import Path
import json
import os

def eliminar_duplicados():
    """
    Elimina fotos duplicadas en images/ y regenera photos_list.js
    """
    repo_dir = Path(r"C:\Users\foro7\invitacion-boda-josefina-david")
    images_dir = repo_dir / "images"
    photos_list_file = repo_dir / "photos_list.js"

    # Leer el archivo photos_list.js
    with open(photos_list_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extraer la lista de fotos
    import re
    pattern = r"\{ name: '([^']+)', path: '([^']+)', filename: '([^']+)' \}"
    matches = re.findall(pattern, content)

    print(f"Total de fotos en photos_list.js: {len(matches)}")

    # Agrupar por filename original
    fotos_por_nombre = {}
    for name, path, filename in matches:
        if filename not in fotos_por_nombre:
            fotos_por_nombre[filename] = []
        fotos_por_nombre[filename].append((name, path, filename))

    # Identificar duplicados
    duplicados = {k: v for k, v in fotos_por_nombre.items() if len(v) > 1}
    print(f"\nFotos únicas: {len(fotos_por_nombre)}")
    print(f"Fotos con duplicados: {len(duplicados)}")

    # Crear lista limpia (solo primera aparición de cada foto)
    fotos_limpias = []
    foto_counter = 1

    for filename_original in sorted(fotos_por_nombre.keys()):
        # Tomar solo la primera foto de cada grupo
        primera_foto = fotos_por_nombre[filename_original][0]

        # Renombrar secuencialmente
        nuevo_nombre = f"foto_{foto_counter:04d}"
        nuevo_path = f"images/foto_{foto_counter:04d}.webp"

        fotos_limpias.append({
            'numero': foto_counter,
            'nombre': nuevo_nombre,
            'path': nuevo_path,
            'filename_original': filename_original,
            'archivo_viejo': primera_foto[1]  # path original
        })

        foto_counter += 1

    print(f"\nFotos después de eliminar duplicados: {len(fotos_limpias)}")

    # Renombrar archivos físicos
    print("\nRenombrando archivos...")
    temp_dir = images_dir / "temp"
    temp_dir.mkdir(exist_ok=True)

    for foto in fotos_limpias:
        archivo_viejo = repo_dir / foto['archivo_viejo']
        archivo_nuevo = temp_dir / f"{foto['nombre']}.webp"

        if archivo_viejo.exists():
            # Copiar a temp con nuevo nombre
            import shutil
            shutil.copy2(archivo_viejo, archivo_nuevo)

    print(f"Archivos copiados a temp/: {len(list(temp_dir.glob('*.webp')))}")

    # Limpiar carpeta images
    print("\nLimpiando carpeta images...")
    for webp in images_dir.glob("*.webp"):
        webp.unlink()

    # Mover archivos de temp a images
    for webp in temp_dir.glob("*.webp"):
        destino = images_dir / webp.name
        webp.rename(destino)

    # Eliminar carpeta temp
    temp_dir.rmdir()

    print(f"Archivos finales en images/: {len(list(images_dir.glob('*.webp')))}")

    # Generar nuevo photos_list.js
    print("\nGenerando nuevo photos_list.js...")
    js_content = "// Lista de fotos generada automáticamente\n"
    js_content += "const photos = [\n"

    for foto in fotos_limpias:
        js_content += f"    {{ name: '{foto['nombre']}', path: '{foto['path']}', filename: '{foto['filename_original']}' }},\n"

    js_content += "];\n"

    with open(photos_list_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"Archivo photos_list.js actualizado con {len(fotos_limpias)} fotos únicas")

    print("\n" + "=" * 80)
    print("PROCESO COMPLETADO")
    print("=" * 80)
    print(f"Fotos originales: {len(matches)}")
    print(f"Fotos únicas: {len(fotos_limpias)}")
    print(f"Duplicados eliminados: {len(matches) - len(fotos_limpias)}")
    print("=" * 80)

    return len(fotos_limpias)

if __name__ == "__main__":
    try:
        num_fotos = eliminar_duplicados()
        print(f"\n✓ Proceso exitoso. {num_fotos} fotos únicas listas.")
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()

    input("\nPresiona Enter para salir...")
