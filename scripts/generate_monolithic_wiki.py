import os, glob, re

BASE_DIR = "temp_build_mono"
OUTPUT_FILE = os.path.join(BASE_DIR, "WIKI_COMPLETA_SIIU_UDEA.md")

# Helpers to gather subdirectories in 06 and 07
def get_rel_paths(pattern):
    matches = glob.glob(os.path.join(BASE_DIR, pattern), recursive=True)
    return sorted([os.path.relpath(p, BASE_DIR).replace('\\', '/') for p in matches])

# Ordered categories
sections_order = [
    ("1. MANUALES DE ROLES Y GOBERNANZA", [
        "docs/01_ROLES/Rol_Investigador.md",
        "docs/01_ROLES/Rol_Centro_Investigacion.md",
        "docs/01_ROLES/Rol_Vicerrectoria.md",
        "docs/01_ROLES/Ecosistema_Comites_Gobernanza.md",
        "docs/01_ROLES/Caso_Aplicado_Centro_Facultad.md",
    ]),
    ("2. PROCESOS CLAVE DEL CICLO DE VIDA DEL SIIU", [
        "docs/02_PROCESOS_CLAVE/Matricula_Proyectos.md",
        "docs/02_PROCESOS_CLAVE/Evaluacion_y_Aval.md",
        "docs/02_PROCESOS_CLAVE/Convocatorias_y_Fondos_CODI.md",
        "docs/02_PROCESOS_CLAVE/Inicio_Formal.md",
        "docs/02_PROCESOS_CLAVE/Modificaciones_y_Tramites.md",
        "docs/02_PROCESOS_CLAVE/Gestion_Compromisos.md",
        "docs/02_PROCESOS_CLAVE/Programa_Joven_Investigador.md",
        "docs/02_PROCESOS_CLAVE/Cierre_y_Liquidacion.md",
        "docs/02_PROCESOS_CLAVE/Reportes_y_Certificaciones.md",
    ]),
    ("3. GUÍAS RÁPIDAS Y REGLAS DE ORO", [
        "docs/03_GUIAS_RAPIDAS_CHEAT_SHEETS/Reglas_Oro_SIIU.md",
        "docs/03_GUIAS_RAPIDAS_CHEAT_SHEETS/Catalogo_Formatos_Oficiales.md",
        "docs/03_GUIAS_RAPIDAS_CHEAT_SHEETS/CheatSheet_Investigador.md",
        "docs/03_GUIAS_RAPIDAS_CHEAT_SHEETS/CheatSheet_Centro.md",
        "docs/inicio-rapido.md",
        "docs/faq.md",
    ]),
    ("4. INVESTIGACIÓN CENTRAL UDEA — CODI Y VICERRECTORÍA", [
        "docs/07_INVESTIGACION_CENTRAL_UDEA/index.md",
        "docs/07_INVESTIGACION_CENTRAL_UDEA/codi.md",
        "docs/07_INVESTIGACION_CENTRAL_UDEA/catalogo_formatos_descargables.md",
        "docs/07_INVESTIGACION_CENTRAL_UDEA/circulares_vicerrectoria.md",
        "docs/07_INVESTIGACION_CENTRAL_UDEA/vicerrectoria.md",
        "docs/07_INVESTIGACION_CENTRAL_UDEA/siu.md",
        "docs/07_INVESTIGACION_CENTRAL_UDEA/siiu.md",
        "docs/07_INVESTIGACION_CENTRAL_UDEA/comite_central_etica.md",
        "docs/07_INVESTIGACION_CENTRAL_UDEA/convocatorias_codi.md",
        "docs/07_INVESTIGACION_CENTRAL_UDEA/convocatorias_externas.md",
        "docs/07_INVESTIGACION_CENTRAL_UDEA/fondos_investigacion.md",
        "docs/07_INVESTIGACION_CENTRAL_UDEA/fondo_primer_proyecto.md",
        "docs/07_INVESTIGACION_CENTRAL_UDEA/programa_jovenes_investigadores.md",
        "docs/07_INVESTIGACION_CENTRAL_UDEA/procedimientos_formatos.md",
        "docs/07_INVESTIGACION_CENTRAL_UDEA/reglamento_investigacion.md",
        "docs/07_INVESTIGACION_CENTRAL_UDEA/propiedad_intelectual.md",
        "docs/07_INVESTIGACION_CENTRAL_UDEA/acceso_abierto.md",
        "docs/07_INVESTIGACION_CENTRAL_UDEA/conflicto_intereses_financieros.md",
        "docs/07_INVESTIGACION_CENTRAL_UDEA/permisos_investigacion.md",
        "docs/07_INVESTIGACION_CENTRAL_UDEA/atencion_ciudadano.md",
    ]),
    ("5. ECOSISTEMA FACULTAD DE CIENCIAS ECONÓMICAS Y CIC", [
        "docs/06_CIENCIAS_ECONOMICAS_CIC/index.md",
        "docs/06_CIENCIAS_ECONOMICAS_CIC/arquitectura_funcional.md",
        "docs/06_CIENCIAS_ECONOMICAS_CIC/centro_investigacion.md",
        "docs/06_CIENCIAS_ECONOMICAS_CIC/departamentos.md",
        "docs/06_CIENCIAS_ECONOMICAS_CIC/grupos_investigacion_activos.md",
        "docs/06_CIENCIAS_ECONOMICAS_CIC/matriz_conformacion_comites.md",
        "docs/06_CIENCIAS_ECONOMICAS_CIC/directorio_administrativo.md",
        "docs/06_CIENCIAS_ECONOMICAS_CIC/asesorias_consultorias.md",
        "docs/06_CIENCIAS_ECONOMICAS_CIC/centro_documentacion.md",
    ] + get_rel_paths("docs/06_CIENCIAS_ECONOMICAS_CIC/comites/*.md")
      + get_rel_paths("docs/06_CIENCIAS_ECONOMICAS_CIC/semilleros/*.md")
      + get_rel_paths("docs/06_CIENCIAS_ECONOMICAS_CIC/publicaciones/*.md")
    ),
    ("6. MAPAS DE CONTENIDO (MOC) Y CONCEPTOS", [
        "docs/00_INICIO_Y_MOCS/MOC_Ciclo_de_Vida_Proyectos.md",
        "docs/00_INICIO_Y_MOCS/MOC_Por_Roles.md",
        "docs/00_INICIO_Y_MOCS/MOC_Tramites_y_Solicitudes.md",
        "docs/00_INICIO_Y_MOCS/MOC_Reportes_y_Constancias.md",
        "docs/00_INICIO_Y_MOCS/MOC_Marco_Normativo.md",
        "docs/04_GLOSARIO_Y_CONCEPTOS/Glosario_Terminos_SIIU.md",
        "docs/04_GLOSARIO_Y_CONCEPTOS/Catalogo_Normativo_31_Docs.md",
    ]),
    ("7. SÍNTESIS DEL MARCO NORMATIVO INSTITUCIONAL (21 NORMAS)", [
        "docs/05_MARCO_NORMATIVO/AS_01_1994_Estatuto_General.md",
        "docs/05_MARCO_NORMATIVO/AS_083_1996_Estatuto_Profesoral.md",
        "docs/05_MARCO_NORMATIVO/AS_086_1996_Profesores_Catedra_Proyectos.md",
        "docs/05_MARCO_NORMATIVO/AS_121_1997_Estatuto_Presupuestal.md",
        "docs/05_MARCO_NORMATIVO/AS_124_1997_Estatuto_Extension.md",
        "docs/05_MARCO_NORMATIVO/AS_204_2001_Sistema_Universitario_Investigacion.md",
        "docs/05_MARCO_NORMATIVO/AS_253_2003_Docentes_Catedra_Ocasionales.md",
        "docs/05_MARCO_NORMATIVO/AS_284_2004_Gestion_Tecnologica.md",
        "docs/05_MARCO_NORMATIVO/RR_21231_2005_Estatuto_Propiedad_Intelectual.md",
        "docs/05_MARCO_NORMATIVO/AS_350_2007_Estatuto_Financiero.md",
        "docs/05_MARCO_NORMATIVO/AS_418_2014_Politica_Practicas.md",
        "docs/05_MARCO_NORMATIVO/AS_419_2014_Estatuto_Contratacion.md",
        "docs/05_MARCO_NORMATIVO/RR_39475_2014_Reglamento_Contratacion.md",
        "docs/05_MARCO_NORMATIVO/RR_39477_2014_Referente_Etico.md",
        "docs/05_MARCO_NORMATIVO/DJ_MA_02_Manual_Interventoria.md",
        "docs/05_MARCO_NORMATIVO/Ley_1838_2017_Spinoffs.md",
        "docs/05_MARCO_NORMATIVO/AS_451_2018_Politica_Acceso_Abierto.md",
        "docs/05_MARCO_NORMATIVO/AS_466_2020_Estatuto_Financiero_Vigente.md",
        "docs/05_MARCO_NORMATIVO/RR_49544_2022_Nuevo_Estatuto_PI.md",
        "docs/05_MARCO_NORMATIVO/RR_51525_2024_Ajustes_SIIU.md",
        "docs/05_MARCO_NORMATIVO/RR_00968_2026_Modernizacion.md",
    ]),
    ("8. ARCHIVO MAESTRO FIDEDIGNO: 31 GUÍAS E INSTRUCTIVOS OFICIALES Y TÉRMINOS DE REFERENCIA",
        get_rel_paths("archivo_maestro/VI-*.md") + get_rel_paths("archivo_maestro/TR-*.md")
    ),
    ("9. ARCHIVO MAESTRO FIDEDIGNO: 21 NORMAS INSTITUCIONALES COMPLETAS",
        get_rel_paths("archivo_maestro/legalidad/LEG-*.md")
    ),
    ("10. TÉRMINOS LEGALES Y CUMPLIMIENTO", [
        "docs/legal/index.md",
        "docs/legal/terminos.md",
        "docs/legal/privacidad.md",
        "docs/legal/licencias.md",
        "docs/legal/cookies.md",
    ])
]

header = """# COMPENDIO TOTAL Y CANÓNICO DE LA WIKI SIIU Y ECOSISTEMA DE INVESTIGACIÓN UDEA
## Sistema de Información para la Investigación Universitaria — Universidad de Antioquia

> **Documento Consolidado Monolítico (All-in-One)**  
> **Propósito:** Archivo único diseñado para ingesta directa de contexto completo por Agentes Inteligentes (Gemini, Claude, GPT), modelos LLM locales, auditoría documental exhaustiva y lectura offline sin dependencias externas.  
> **Contenido Integrado:** Manuales de roles, 9 macroprocesos operativos, 31 guías e instructivos fidedignos transcritos íntegramente, 21 normas institucionales (síntesis y textos íntegros), gobernanza CODI y Cronograma 2026, catálogo de 18 formatos descargables, 66 circulares oficiales de la Vicerrectoría, arquitectura de la Facultad de Ciencias Económicas y CIC con sus 9 grupos MinCiencias, 20 comités, semilleros y revistas científicas.

---

"""

out_chunks = [header]
total_files_merged = 0
seen_files = set()

for cat_title, file_list in sections_order:
    out_chunks.append(f"\n\n{'='*80}\n# {cat_title}\n{'='*80}\n\n")
    for rel_path in file_list:
        if rel_path in seen_files:
            continue
        full_path = os.path.join(BASE_DIR, rel_path)
        if not os.path.exists(full_path):
            continue
        
        seen_files.add(rel_path)
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read().strip()
        
        # Remove yaml frontmatter if present
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                content = parts[2].strip()

        # Demarcate document clearly
        doc_header = f"\n\n{'-'*60}\n## [DOCUMENTO]: {os.path.basename(rel_path)}\n*Ruta canónica original: `{rel_path}`*\n{'-'*60}\n\n"
        out_chunks.append(doc_header)
        out_chunks.append(content)
        total_files_merged += 1

consolidated_text = "".join(out_chunks)

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(consolidated_text)

size_mb = os.path.getsize(OUTPUT_FILE) / (1024 * 1024)
print(f"Compilación monolítica completada exitosamente.")
print(f"Archivo generado: {OUTPUT_FILE}")
print(f"Total documentos fusionados: {total_files_merged}")
print(f"Peso del archivo único: {size_mb:.2f} MB")
