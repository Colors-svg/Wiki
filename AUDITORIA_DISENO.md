# Auditoría de Diseño y Estructura — Wiki SIIU (Fase 0)

**Fecha:** 2026-11-26  
**Alcance:** Diagnóstico completo de `mkdocs.yml`, `docs/`, `wiki/`, `overrides/` y los recursos visuales antes de iniciar el rediseño editorial.  
**Estado de compilación inicial:** `mkdocs build --strict` finaliza con código de salida `0` (sin errores ni advertencias fatales; se registran mensajes informativos `INFO` sobre anclas inexistentes en enlaces internos de `Catalogo_Normativo_31_Docs.md`, `Rol_Vicerrectoria.md` y `CheatSheet_Investigador.md`).

---

## 1. Relación entre `docs/` y `wiki/`

- **`docs/` (Directorio activo de MkDocs Material):** `mkdocs.yml` utiliza la configuración por defecto (`docs_dir: docs`). Contiene **177 archivos Markdown**, además de `assets/`, `stylesheets/`, `javascripts/`, `06_CIENCIAS_ECONOMICAS_CIC/`, `07_INVESTIGACION_CENTRAL_UDEA/`, `archivo_maestro/` y `legal/`.
- **`wiki/` (Directorio histórico / base previa):** Contiene **51 archivos Markdown** correspondientes a la estructura inicial de la wiki (`00_INICIO_Y_MOCS/` a `06_LEGAL/`, `FAQ.md`, `Guia_Inicio_Rapido.md`). No es un symlink ni un `docs_dir`; es un directorio independiente cuyos archivos fueron copiados y expandidos hacia `docs/` en commits anteriores.
- **Implicación operativa:** Todas las modificaciones de estilo y estructura web impactan a `docs/`, `overrides/` y `mkdocs.yml`. Los ajustes de forma (limpieza de encabezados y emojis) se aplicarán en `docs/` y en los archivos homólogos de `wiki/` sin alterar en ningún caso `archivo_maestro/`, `fuentes_pdf/` ni `Legalidad/`.

---

## 2. CSS y JavaScript Extra Actuales

En `mkdocs.yml` se cargan los siguientes recursos estáticos:

| Archivo | Tamaño | Líneas | Función y diagnóstico actual |
| :--- | :---: | :---: | :--- |
| `docs/stylesheets/wiki.css` | 44.1 KB | 1.457 | Hoja de estilos sobredimensionada. Incluye degradados, sombras de color, bordes gruesos de acento (`#8DC63F`, `#026937`), estilos de tarjetas (`.wiki-card`), hero (`.wiki-hero`), botones grandes (`.wiki-btn`), pastillas de footer (`.wiki-footer-pill`), badges en mayúsculas y variables de color saturadas. |
| `docs/javascripts/diagram-zoom.js` | 6.1 KB | 195 | Script para envolver bloques `.mermaid` e inyectar un botón "Ampliar" que abre un `<dialog>` lightbox con zoom (`A-`, `A+`). Útil en diagramas complejos, aunque su estilo visual actual depende de las clases del CSS recargado. |
| `docs/javascripts/site-logo.js` | 1.9 KB | 65 | Fuerza el logotipo blanco (`logo-udea-blanco.svg`) sobre el header oscuro mediante un `MutationObserver`. Si en el nuevo diseño el header en modo claro usa fondo blanco/superficie clara (`#ffffff` o `#f6f8fa`), este script deberá ajustarse o retirarse para alternar adecuadamente entre `logo-udea.svg` y `logo-udea-blanco.svg`. |

---

## 3. Uso de Emojis e Iconos Decorativos

1. **Emojis Unicode en encabezados:**
   - Se detectaron **2 ocurrencias** en títulos de `docs/`:
     - `docs/07_INVESTIGACION_CENTRAL_UDEA/convocatorias_codi.md` (líneas 20 y 22): `### 📅 Histórico de convocatorias CODI...`
   - Adicionalmente, en `docs/00_INICIO_Y_MOCS/MOC_Ciclo_de_Vida_Proyectos.md` (líneas 87, 102, 112, 134) existen caracteres chinos residuales en encabezados (`## 阶段 2:`, `## 阶段 3:`, `## 阶段 4:`, `## 阶段 5:`) que deben limpiarse/normalizarse.
   - En `wiki/` no se encontraron emojis Unicode en encabezados.
2. **Shortcodes de iconos (`pymdownx.emoji`):**
   - `mkdocs.yml` tiene habilitado `pymdownx.emoji` (`twemoji` / `to_svg`).
   - Existen **104 shortcodes de iconos** (`:material-...:`, etc.) distribuidos en **20 archivos** de `docs/` (excluyendo `archivo_maestro/`). Los archivos con mayor concentración son:
     - `docs/03_GUIAS_RAPIDAS_CHEAT_SHEETS/Catalogo_Formatos_Oficiales.md` (24)
     - `docs/02_PROCESOS_CLAVE/Convocatorias_y_Fondos_CODI.md` (12)
     - `docs/02_PROCESOS_CLAVE/Modificaciones_y_Tramites.md` (8)
     - `docs/01_ROLES/Ecosistema_Comites_Gobernanza.md` (6)
     - `docs/00_INICIO_Y_MOCS/MOC_Tramites_y_Solicitudes.md` (6)
     - `docs/02_PROCESOS_CLAVE/Reportes_y_Certificaciones.md` (6)
     - `docs/02_PROCESOS_CLAVE/Evaluacion_y_Aval.md` (6)
     - `docs/00_INICIO_Y_MOCS/MOC_Marco_Normativo.md` (6)

---

## 4. Badges, Botones Grandes, Grids de Tarjetas y Footer

El diseño actual presenta una estética orientada a "landing page / marketing" en las páginas principales:

| Componente / Clase CSS | Ocurrencias | Archivos afectados |
| :--- | :---: | :--- |
| `.wiki-hero` | 4 | `docs/index.md`, `docs/faq.md`, `docs/07_INVESTIGACION_CENTRAL_UDEA/index.md`, `docs/06_CIENCIAS_ECONOMICAS_CIC/index.md` |
| `.wiki-badge` | 1 | `docs/index.md` ("Guía Comunitaria No Oficial · Apoyo SIIU UdeA") |
| `.wiki-actions` / `.wiki-btn` | 1 / 8 | `docs/index.md` (4 botones grandes en el hero) |
| `.wiki-grid` / `.wiki-card` | 5 / 93 | `docs/index.md`, `docs/07_INVESTIGACION_CENTRAL_UDEA/index.md`, `docs/06_CIENCIAS_ECONOMICAS_CIC/index.md` |
| `.wiki-footer-banner` / `.wiki-footer-pill` | 10 / 5 | `overrides/partials/footer.html` (pastillas con SVG y badge "Guía No Oficial") |

---

## 5. Admonitions

- Se contabilizaron **28 bloques de admonition** (`!!!` / `???`) en **19 archivos** de `docs/` (excluyendo `archivo_maestro/`).
- La gran mayoría cumple con el máximo recomendado de 1–2 por página.
- Solo **3 archivos** tienen 3 bloques:
  - `docs/inicio-rapido.md` (3)
  - `docs/07_INVESTIGACION_CENTRAL_UDEA/fondo_primer_proyecto.md` (3)
  - `docs/01_ROLES/Rol_Investigador.md` (3)
- **Problema actual de diseño:** En `wiki.css`, los admonitions emplean fondos tintados, bordes izquierdos gruesos y colores saturados que rompen la sobriedad editorial.

---

## 6. Diagramas Mermaid

- Existen **53 diagramas Mermaid** en **44 archivos** de `docs/` (excluyendo `archivo_maestro/`).
- **Diagnóstico de legibilidad:**
  - En `docs/index.md`, el diagrama **"Mapa General de Navegación"** (`flowchart TD`) contiene nodos con HTML embebido (`<br><i>...</i>`) y ramificación amplia que pierde legibilidad en anchos de lectura estrechos.
  - Varios diagramas en `00_INICIO_Y_MOCS/` y `02_PROCESOS_CLAVE/` superan ampliamente los 8 nodos recomendados (ej. `MOC_Ciclo_de_Vida_Proyectos.md`: ~30 nodos/líneas; `MOC_Marco_Normativo.md`: ~26; `MOC_Por_Roles.md`: ~21; `Programa_Joven_Investigador.md`: ~21; `Matricula_Proyectos.md`: ~18; `Cierre_y_Liquidacion.md`: ~17; `Modificaciones_y_Tramites.md`: ~16).
  - En `wiki.css` se fuerza una paleta verde oscura (`#123A21`, `#35944B`, `#8DC63F`) en lugar de superficies neutras de documentación técnica.

---

## 7. Anidación de Navegación y Jerarquía de Encabezados

1. **Navegación (`mkdocs.yml`):**
   - `navigation.expand` está activado por defecto, lo cual despliega todo el menú lateral simultáneamente y genera sobrecarga visual.
   - `Facultad Ciencias Económicas (CIC)` alcanza **3 niveles de anidación** (Sección $\to$ Subsección `Semilleros de Investigación` / `Publicaciones y Revistas` / `Comités de Gobierno` $\to$ Páginas). El resto de secciones tiene 1 o 2 niveles.
   - El menú conserva títulos extensos y términos redundantes en varias secciones.
2. **Jerarquía de Encabezados (`#`):**
   - Todas las páginas de `docs/` y `wiki/` (excluyendo `archivo_maestro/`) tienen exactamente **1 etiqueta H1**.
   - **Salto de jerarquía detectado:** `docs/00_INICIO_Y_MOCS/HOME.md` (línea 7) y `wiki/00_INICIO_Y_MOCS/HOME.md` (línea 2) saltan directamente de `H1` a `H3` (`### Sistema de Información...`).
   - **Profundidad excesiva (H4+):** `docs/06_CIENCIAS_ECONOMICAS_CIC/grupos_investigacion_activos.md` contiene **54 encabezados de nivel H4 o inferior** (`####`).
   - **Frase de contexto inicial tras H1:** 74 páginas de `docs/` y 8 de `wiki/` inician directamente tras el `H1` con un bloque `<div>`, una tabla (`|`), un encabezado `##` o un bloque de código sin una oración introductoria previa.
   - **Mayúsculas decorativas:** No se detectaron títulos completamente en mayúsculas en `wiki/` ni en `docs/` (salvo siglas válidas y los documentos archivísticos en `archivo_maestro/legalidad/` que no se modifican).
