# CONTEXTO DEL PROYECTO PARA AGENTES IA

Este documento condensa la arquitectura, estado de avance, convenciones operativas y reglas técnicas del repositorio **Wiki SIIU**, permitiendo que cualquier agente IA retome el trabajo con contexto completo y sin fricciones.

---

## 1. Identidad y Misión del Proyecto

- **Entidad:** Universidad de Antioquia (UdeA) — Vicerrectoría de Investigación y Vicerrectoría de Extensión.
- **Objeto:** Plataforma de documentación técnica, operativa y jurídica del **Sistema de Información para la Investigación Universitaria (SIIU)**.
- **Repositorio Oficial:** `https://github.com/Colors-svg/Wiki`
- **Sitio Público en Vivo (GitHub Pages):** `https://colors-svg.github.io/Wiki/`
- **Diseño de Marca Oficial:** Sistema Cromático Institucional UdeA (`https://github.com/Colors-svg/Paleta-Udea`):
  - Verde Bosque Institucional: `#026937` (Pantone 349 C)
  - Verde Follaje Vivo: `#35944B` (Pantone 7740 C)
  - Verde Lima Acento: `#8DC63F` (Pantone 375 C)
  - Turquesa Caribe: `#3EBDAC` (Pantone 7465 C)
  - Dark Mode Slate Institucional: Fondo `#0B0F15`, Superficies `#111722`, Bordes `#1E293B`.

---

## 2. Arquitectura de Carpetas

```text
├── docs/                                # Directorio raíz para MkDocs Material
│   ├── index.md                         # Portada oficial de la Wiki
│   ├── 00_INICIO_Y_MOCS/                # Mapas de Contenido (MOCs temáticos)
│   ├── 01_ROLES/                        # Manuales operativos por rol (Investigador, Centro, Vicerrectoría)
│   ├── 02_PROCESOS_CLAVE/               # Flujos paso a paso de los 8 procesos del ciclo de vida
│   ├── 03_GUIAS_RAPIDAS_CHEAT_SHEETS/   # Cheat Sheets y Reglas de Oro operativas
│   ├── 04_GLOSARIO_Y_CONCEPTOS/         # Glosario canónico de 17 estados y catálogo de 31 docs
│   ├── 05_MARCO_NORMATIVO/              # Síntesis didáctica de las 21 normas institucionales
│   ├── archivo_maestro/                 # Transcripciones 1 a 1 de las 31 guías e instructivos
│   │   └── legalidad/                   # Transcripciones 1 a 1 de las 21 normas institucionales
│   ├── assets/                          # Logotipos SVG, favicon e iconografía
│   │   └── figuras/                     # 1.574 capturas de pantalla reales extraídas de los PDFs
│   └── stylesheets/extra.css            # Estilos personalizados, tipografía Inter y animaciones
│
├── archivo_maestro/                     # Espejo de preservación archivística estricta 1 a 1
│   ├── VI-GU-01.md a VI-GU-25.md        # 21 Guías oficiales completas con figuras vinculadas
│   ├── VI-IN-01.md a VI-IN-12.md        # 10 Instructivos oficiales completos con figuras
│   └── legalidad/                       # 21 Normas UdeA transcritas íntegramente
│
├── fuentes_pdf/                         # 31 PDFs originales de la Vicerrectoría
├── Legalidad/                           # 21 PDFs originales de Acuerdos Superiores y Resoluciones
├── scripts/                             # Scripts de automatización en Python (PyMuPDF)
│   ├── extract_all_figures.py           # Extractor masivo de figuras desde los PDFs
│   └── link_figures.py                  # Vinculador de imágenes en los archivos Markdown
├── mkdocs.yml                           # Configuración de MkDocs Material, navegación y extensiones
└── README.md                            # Portada principal del repositorio de GitHub
```

---

## 3. Estado de Avance Consolidado

1. **Transcripción Fidedigna (Fase 1):** 100% completada (31 guías e instructivos + 21 normas institucionales transcritas y normalizadas).
2. **Wiki Didáctica (Fase 2):** 100% estructurada con manuales de rol, procesos clave, MOCs interactivos y glosario canónico.
3. **Capturas de Pantalla:** 1.574 capturas reales extraídas quirúrgicamente de los PDFs con PyMuPDF y vinculadas en las guías maestras.
4. **Marco Jurídico e Institucional:** 21 normas (Acuerdos Superiores 01/1994, 083/1996, 086/1996, 121/1997, 124/1997, 204/2001, 253/2003, 284/2004, 350/2007, 418/2014, 419/2014, 451/2018, 466/2020; Resoluciones Rectorales 21231/2005, 39475/2014, 39477/2014, 49544/2022, 51525/2024, 00968/2026; Ley 1838/2017 y Manual DJ-MA-02) disponibles en síntesis didáctica y texto maestro.
5. **Generador y Despliegue:** MkDocs Material con tema Slate, layout amplio (1650px / 1060px), Admonitions nativos y despliegue a la rama `gh-pages`.

---

## 4. Reglas Técnicas para Agentes

- **Sintaxis de Callouts:** Utilizar la sintaxis nativa de MkDocs Material: `!!! note "Título"`, `!!! warning "Título"`, `!!! danger "Título"`, `!!! tip "Título"` con sangría de 4 espacios. NO usar blockquotes planos `> **ADVERTENCIA:**`.
- **Diagramas de Flujo:** Usar bloques ` ```mermaid ` con formato `flowchart TD` o `flowchart LR`. Evitar `stateDiagram` apiñados. Utilizar `classDef` institucionales (`#026937`, `#35944B`, `#8DC63F`).
- **Navegación e Índices:** Al crear nuevos documentos en `docs/`, agregarlos explícitamente en el bloque `nav:` de `mkdocs.yml`.
- **Comandos de Construcción y Despliegue:**
  - Build local: `uv run --python 3.12 --with mkdocs-material mkdocs build`
  - Deploy a GitHub Pages: `uv run --python 3.12 --with mkdocs-material mkdocs gh-deploy --force`
  - Sincronización a main: `git add .`, `git commit -m "..."`, `git push origin main`
