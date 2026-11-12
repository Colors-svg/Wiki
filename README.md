# Documentación y Base de Conocimiento del SIIU
### Vicerrectoría de Investigación — Universidad de Antioquia

Portal técnico y operativo del **Sistema de Información para la Investigación Universitaria (SIIU)**, diseñado para la consulta integral de procesos, convocatorias, trámites administrativos y normatividad vigente.

> **Acceso a la Wiki Interactiva en Línea:**  
> Navegue por la documentación estructurada con buscador integrado, diagramas de proceso y barra lateral de navegación en:  
> **[https://colors-svg.github.io/Wiki/](https://colors-svg.github.io/Wiki/)**

---

## Estructura de la Documentación

### 1. Manuales Operativos por Perfil
- **Investigador Principal / Tutor:** Formulación, radicación, gestión de compromisos académicos, cupos de Joven Investigador y trámites administrativos.
- **Centro de Investigación / Extensión:** Evaluación técnica formal, devoluciones para ajustes, emisión de avales institucionales y aprobación de trámites.
- **Vicerrectoría de Investigación:** Parametrización del sistema, gestión de convocatorias, asignación de evaluadores pares, trámites en instancias centrales (CODI) y liquidación de proyectos.

### 2. Procesos Clave del Ciclo de Vida
- **Matrícula e Inscripción:** Proyectos en convocatoria interna, proyectos inscritos con financiación externa y primer proyecto.
- **Evaluación y Aval:** Criterios de evaluación técnica de Centro, protocolo de subsanación y asignación de pares evaluadores.
- **Inicio Formal:** Verificación de pólizas, contratos, centros de costo y formalización de acta de inicio.
- **Modificaciones Administrativas:** Prórrogas de ejecución, traslados presupuestales (cambio de rubro) y modificaciones en el equipo de trabajo.
- **Compromisos y Seguimiento:** Carga de informes parciales, finales, productos y solicitudes de plazo.
- **Programa Joven Investigador:** Matrícula de cupos asignados, verificación de requisitos bancarios y solicitudes de prórroga.
- **Cierre y Liquidación:** Emisión de paz y salvos técnicos, acta de cierre y liquidación financiera.
- **Reportes y Certificaciones:** Emisión de certificados de participación, constancias de evaluación y reportes consolidados.

### 3. Normativa Institucional y Archivo Maestro
- **Archivo Maestro de Procesos (31 Documentos):** Transcripción fidedigna de las 21 guías de proceso (`VI-GU-*`) y 10 instructivos técnicos (`VI-IN-*`).
- **Archivo Maestro de Legalidad (21 Documentos):** Transcripción íntegra de las 21 leyes, acuerdos superiores y resoluciones rectorales que rigen la investigación en la UdeA (`archivo_maestro/legalidad/`).
- **Marco Normativo Wiki (21 Fichas Didácticas):** Fichas operativas con diagramas Mermaid, tablas de impacto y enlaces cruzados hacia el SIIU (`wiki/05_MARCO_NORMATIVO/`).
- **Matriz de Concordancia Normativa:** Mapa central de contenido que articula trámites del SIIU con normas habilitantes (`wiki/00_INICIO_Y_MOCS/MOC_Marco_Normativo.md`).

---

## Organización del Repositorio

```text
├── mkdocs.yml                      # Configuración de compilación para GitHub Pages
├── docs/                          # Directorio fuente de la documentación web
├── wiki/                          # Base de conocimiento modular y didáctica
│   ├── 00_INICIO_Y_MOCS/          # Mapas de contenido (Ciclo, Roles, Trámites, Marco Normativo)
│   ├── 01_ROLES/                  # Manuales por rol operativo (Investigador, Centro, Vicerrectoría)
│   ├── 02_PROCESOS_CLAVE/         # Procedimientos secuenciales detallados
│   ├── 03_GUIAS_RAPIDAS_CHEAT_SHEETS/ # Resúmenes ejecutivos y reglas de oro
│   ├── 04_GLOSARIO_Y_CONCEPTOS/   # Glosario oficial y catálogo de 31 docs
│   └── 05_MARCO_NORMATIVO/        # 21 fichas didácticas del marco legal UdeA
├── archivo_maestro/               # Transcripciones fidedignas 1 a 1
│   ├── VI-GU-* / VI-IN-*          # 31 documentos de guías e instructivos
│   └── legalidad/                 # 21 documentos normativos íntegros (Leyes, CSU, Resoluciones)
├── fuentes_pdf/                   # Documentos PDF originales de la Vicerrectoría
└── Legalidad/                     # Normativa legal original en PDF de la Universidad
```
