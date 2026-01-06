import os
import webbrowser

# 1. Definimos la estructura del diagrama en lenguaje Mermaid
# Usamos "==>" para resaltar las flechas de la ruta crítica
diagrama_mermaid = """
graph LR
    %% --- Estilos de los Nodos ---
    classDef normal fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef critica fill:#ffcdd2,stroke:#b71c1c,stroke-width:4px,color:#b71c1c,font-weight:bold;

    %% --- Definición de Actividades y Duraciones ---
    A[A: Inicio<br>20 días]:::critica
    B[B: Actividad<br>10 días]:::critica
    C[C: Actividad<br>8 días]:::critica
    D[D: Actividad<br>11 días]:::normal
    E[E: Unión<br>7 días]:::critica
    F[F: Fin 1<br>6 días]:::normal
    G[G: Actividad<br>12 días]:::normal
    H[H: Actividad<br>13 días]:::critica
    I[I: Fin Final<br>5 días]:::critica

    %% --- Definición de Conexiones ---
    %% Ruta Crítica (Flechas gruesas)
    A ==> B
    B ==> C
    C ==> E
    E ==> H
    H ==> I

    %% Rutas Normales (Flechas delgadas)
    A --> D
    D --> E
    D --> G
    E --> F
    G --> I
    
    %% --- Leyenda (Subgrafo invisible para orden) ---
    subgraph Leyenda
    direction LR
    L1[Ruta Normal]:::normal
    L2[Ruta Crítica]:::critica
    end
"""

# 2. Creamos el contenido HTML
# Insertamos el código Mermaid dentro de una plantilla HTML básica
html_content = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Diagrama de Ruta Crítica (CPM)</title>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ startOnLoad: true }});
    </script>
    <style>
        body {{ font-family: sans-serif; text-align: center; background-color: #f4f4f4; padding: 20px; }}
        h1 {{ color: #333; }}
        .container {{ background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); display: inline-block; }}
        .info {{ margin-top: 10px; color: #666; font-size: 0.9em; }}
    </style>
</head>
<body>
    <h1>Diagrama de Red del Proyecto (CPM)</h1>
    <div class="container">
        <div class="mermaid">
            {diagrama_mermaid}
        </div>
    </div>
    <div class="info">
        <p>🔴 <strong>Rojo:</strong> Ruta Crítica (Determina la duración total de 63 días)</p>
        <p>🔵 <strong>Azul:</strong> Actividades con holgura</p>
    </div>
</body>
</html>
"""

# 3. Guardar el archivo HTML y abrirlo automáticamente
nombre_archivo = "diagrama_cpm.html"
ruta_completa = os.path.abspath(nombre_archivo)

try:
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(html_content)
    
    print(f"✅ Archivo creado exitosamente en: {ruta_completa}")
    print("🚀 Abriendo el diagrama en tu navegador...")
    
    # Abrir en el navegador predeterminado
    webbrowser.open('file://' + ruta_completa)

except Exception as e:
    print(f"❌ Error al crear el archivo: {e}")