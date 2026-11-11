# 🏛️ Repositorio Archivístico y Base de Conocimiento SIIU
### Vicerrectoría de Investigación — Universidad de Antioquia

Este repositorio contiene la digitalización archivística, transcripción fidedigna 1 a 1 y base de conocimiento interactiva del **Sistema de Información para la Investigación Universitaria (SIIU)**, optimizado para navegación web en **GitHub**, consulta directa en **Obsidian** y publicación en generadores estáticos (**Quartz 4.0** / **MkDocs Material**).

---

## 🧭 Acceso Directo a la Wiki

> 🚀 **[Comenzar en el Portal Principal de la Wiki (HOME.md)](wiki/00_INICIO_Y_MOCS/HOME.md)**
>
> 🗄️ **[Consultar el Catálogo Normativo Indexado (31 Documentos Oficiales)](wiki/04_GLOSARIO_Y_CONCEPTOS/Catalogo_Normativo_31_Docs.md)**

### 🗺️ Navegación por Perfiles de Usuario
- 🧑‍🔬 **[Manual del Investigador Principal / Tutor](wiki/01_ROLES/Rol_Investigador.md)**
- 🏢 **[Manual del Centro de Investigación / Extensión](wiki/01_ROLES/Rol_Centro_Investigacion.md)**
- 🏛️ **[Manual de la Vicerrectoría de Investigación](wiki/01_ROLES/Rol_Vicerrectoria.md)**

### ⚡ Mapas de Contenido y Vías Rápidas
- 🔄 **[Ciclo de Vida de los Proyectos](wiki/00_INICIO_Y_MOCS/MOC_Ciclo_de_Vida_Proyectos.md)** *(Matrícula ➔ Evaluación ➔ Inicio ➔ Trámites ➔ Cierre)*
- 📋 **[Trámites y Solicitudes Administrativas](wiki/00_INICIO_Y_MOCS/MOC_Tramites_y_Solicitudes.md)** *(Prórrogas, Rubros, Participantes)*
- 📊 **[Reportes y Constancias Oficiales](wiki/00_INICIO_Y_MOCS/MOC_Reportes_y_Constancias.md)** *(Participación, Evaluadores, Historial)*
- 🛡️ **[Reglas de Oro del SIIU](wiki/03_GUIAS_RAPIDAS_CHEAT_SHEETS/Reglas_Oro_SIIU.md)** *(Archivos adjuntos, pop-ups, cuentas bancarias permitidas)*
- 📖 **[Glosario de Términos y Estados](wiki/04_GLOSARIO_Y_CONCEPTOS/Glosario_Terminos_SIIU.md)** *(Los 17 estados del proyecto y conceptos clave)*

---

## 📁 Arquitectura del Repositorio

```text
Documentos/
├── 📚 wiki/                       # FASE 2: Base de Conocimiento Modular & Didáctica (21 Módulos)
│   ├── 00_INICIO_Y_MOCS/         # Portal de bienvenida y Mapas de Contenido (MOC)
│   ├── 01_ROLES/                 # Manuales organizados por perfil operativo
│   ├── 02_PROCESOS_CLAVE/        # Flujos paso a paso con diagramas Mermaid interactivos
│   ├── 03_GUIAS_RAPIDAS_CHEAT_SHEETS/ # Rutas directas, checklists y reglas de oro
│   └── 04_GLOSARIO_Y_CONCEPTOS/  # Glosario canónico y Catálogo cruzado indexado
│
├── 🗄️ archivo_maestro/            # FASE 1: Transcripción Fidedigna 1 a 1 (31 Documentos)
│   ├── VI-GU-01.md a VI-GU-25.md # 21 Guías Oficiales completas (tablas, notas, firmas)
│   └── VI-IN-01.md a VI-IN-12.md # 10 Instructivos Oficiales de consulta y reportes
│
├── 📂 fuentes_pdf/                # 31 PDFs originales de la Vicerrectoría de Investigación
├── ⚖️ Legalidad/                  # Acuerdos Superiores y Resoluciones Rectorales UdeA
└── 📄 README.md                  # Portada central del repositorio
```

---

## 🌟 Características Técnicas

1. **Fidelidad Archivística Absoluta (`archivo_maestro/`):**
   - Transcripción exhaustiva 1 a 1 de las 21 guías operativas y los 10 instructivos técnicos.
   - Metadatos YAML estandarizados, tablas de formularios originales, advertencias de control de copias y firmas institucionales de elaboración, revisión y aprobación.
   - 658 figuras normalizadas con trazabilidad catalogada: `![[VI-XX-YY-figura-ZZ.png]]`.

2. **Navegabilidad Dual (GitHub + Obsidian):**
   - Enlaces relativos estándar compatibles con el renderizador web de GitHub.
   - Wikilinks bidireccionales `[[...]]` para visualización de grafo relacional en **Obsidian**.
   - Diagramas interactivos nativos de **Mermaid** (diagramas de flujo de decisiones y diagramas de secuencia).
   - Bloques destacados en formato GitHub Flavored Markdown (`> [!NOTE]`, `> [!WARNING]`, `> [!CAUTION]`, `> [!TIP]`, `> [!IMPORTANT]`).

---

## 🚀 Guía de Uso Local y en Línea

- **En GitHub:** Haz clic en cualquiera de los enlaces de este README o explora [wiki/00_INICIO_Y_MOCS/HOME.md](wiki/00_INICIO_Y_MOCS/HOME.md).
- **En Obsidian:** Abre esta carpeta (`Documentos`) como una bóveda (**Open folder as vault**), abre `wiki/00_INICIO_Y_MOCS/HOME.md` y presiona `Ctrl + G` para ver el grafo interactivo completo.
