---
search:
  boost: 2.0
---

# Ecosistema de Comités y Gobernanza de la Investigación

El desarrollo de las actividades de investigación y extensión en la Universidad de Antioquia no opera de manera aislada dentro del sistema informático; el **SIIU** es el reflejo digital de un entramado de decisiones colegiadas y normativas amparadas en el **Acuerdo Superior 204 de 2001** (Sistema Universitario de Investigación) y el **Estatuto General (Acuerdo Superior 01 de 1994)**.

Cada estado, aval, novedad o liquidación dentro del SIIU responde a competencias delegadas en distintos órganos de gobierno y cuerpos colegiados.

```mermaid
flowchart TD
    classDef inst fill:#026937,stroke:#8DC63F,stroke-width:2px,color:#FFFFFF;
    classDef comite fill:#0E7774,stroke:#3EBDAC,stroke-width:1.5px,color:#FFFFFF;
    classDef accion fill:#137598,stroke:#8DC63F,stroke-width:1.5px,color:#FFFFFF;

    CSU["Consejo Superior Universitario<br><i>(Máxima Autoridad Normativa)</i>"]:::inst
    CODI["CODI — Comité para el Desarrollo de la Investigación<br><i>(Políticas, Fondos Centrales y Convocatorias)</i>"]:::inst
    CONSEJO_FAC["Consejo de Facultad / Escuela / Instituto<br><i>(Aval Institucional y Dedicaciones Docentes)</i>"]:::comite
    COMITE_TEC["Comité Técnico del Centro de Investigación<br><i>(Evaluación Académica, Pares y Seguimiento)</i>"]:::comite
    COMITE_DEP["Comité de Investigación de Departamento<br><i>(Pertinencia de Líneas y Grupos)</i>"]:::comite

    CSU --> CODI
    CODI --> CONSEJO_FAC
    CONSEJO_FAC --> COMITE_TEC
    COMITE_TEC --> COMITE_DEP

    COMITE_DEP -. "Filtro inicial de pertinencia" .-> FORMULACION["Matrícula en SIIU"]:::accion
    COMITE_TEC -. "Asignación evaluadores y concepto técnico" .-> AVAL["Aval Técnico del Centro"]:::accion
    CONSEJO_FAC -. "Aprobación de descargue y recursos contrapartida" .-> INICIO["Acta de Inicio Formal"]:::accion
    CODI -. "Resolución de adjudicación y presupuesto central" .-> EJECUCION["Ejecución y Novedades"]:::accion
```

---

## 1. Instancias Colegiadas y su Función en el SIIU

### A. Comités de Investigación por Departamento
- **Nivel:** Unidad académica básica (Departamentos académicos).
- **Integrantes clave:** Jefe de Departamento y Coordinadores de los Grupos de Investigación adscritos.
- **Competencias operativas:**
  1. Revisar la pertinencia de las propuestas postuladas en relación con las líneas activas de los grupos.
  2. Verificar la disponibilidad y capacidad real de dedicación horaria de los profesores proponentes.
  3. Emitir el primer visto bueno que permite al proponente solicitar el aval del Centro de Investigación.

### B. Comité Técnico del Centro de Investigación y Consultorías (CIC)
- **Nivel:** Unidad Académica Mayor (Facultad, Escuela o Instituto) — Regulado por el **Acuerdo Superior 204 de 2001**.
- **Integrantes:**
  - Decano o su delegado (Presidente).
  - Jefe o Director del Centro de Investigación (Secretario).
  - Coordinador de Grupos de Investigación.
  - Coordinadores de Programas de Posgrado (Maestría y Doctorado).
  - Representante de los investigadores con proyectos activos.
  - Representante de Extensión.
- **Acciones directas en el SIIU:**
  - **Revisión Técnico-Formal:** Validación de requisitos de convocatoria, formatos, pólizas y contrapartidas.
  - **Asignación de Evaluadores Pares:** Selección de pares internos o externos calificados para emitir juicio valorativo.
  - **Consolidación de Conceptos:** Emisión del concepto favorable que habilita al Consejo de Facultad a expedir el aval institucional.
  - **Seguimiento a Compromisos y Novedades:** Conceptuar sobre solicitudes de prórrogas de tiempo, cambios de rubro presupuestal o sustitución de coinvestigadores.

### C. Consejo de Facultad
- **Nivel:** Máxima autoridad directiva de la unidad académica.
- **Integrantes:** Decano, Vicedecano, Jefes de Departamento, Director de Centro, Representante Profesoral y Representante Estudiantil.
- **Impacto directo en el flujo SIIU:**
  - **Aprobación de Dedicaciones:** Autoriza formalmente las horas semanales de dedicación lectiva y de investigación de los docentes vinculados al proyecto (Art. 21, AS 083/1996).
  - **Expedición de Avales:** Emite la resolución o acta de aval institucional requerida para la radicación ante convocatorias externas (Minciencias, SGR, agencias internacionales).
  - **Ordenación del Gasto Delegada:** En cabeza del Decano para la suscripción de contratos, órdenes de servicio y convenios derivados del proyecto (Art. 47, AS 121/1997).

### D. CODI (Comité para el Desarrollo de la Investigación)
- **Nivel:** Central — Presidido por la Vicerrectoría de Investigación.
- **Competencias:**
  - Establecer los términos de referencia de las convocatorias internas (programáticas, menor cuantía, apoyo a grupos y fondos de sostenibilidad).
  - Asignar el presupuesto central y dirimir discrepancias en las evaluaciones.
  - Aprobar prórrogas extraordinarias o liquidaciones unilaterales que superen las atribuciones de los Centros.

---

## 2. Comités de Soporte Especializado y Requisitos Previos

En proyectos con componentes de riesgo ético, social o ambiental, el **SIIU** exige adjuntar certificaciones previas emitidas por comités especializados antes de autorizar el desembolso presupuestal:

| Comité Especializado | Objeto de Evaluación | Requisito en SIIU |
| :--- | :--- | :--- |
| **Comité de Ética de la Investigación (Humanos)** | Ensayos clínicos, encuestas biomédicas, tratamiento de datos sensibles, interacción con comunidades vulnerables. | Consentimientos informados y aval ético formal cargado en pestaña *Documentos Soporte*. |
| **Comité Institucional para el Cuidado y Uso de Animales (CICUA)** | Experimentación con modelos animales, bioterios y fauna silvestre. | Certificado de cumplimiento de protocolos de bienestar animal. |
| **Comité de Bioética y Bioseguridad** | Manipulación de microorganismos patógenos, material genético recombinante y agentes biológicos. | Plan de manejo de residuos y bioseguridad en laboratorio avalado. |
| **Comité de Propiedad Intelectual** | Resultados susceptibles de patente, secreto industrial, software o licenciamiento tecnológico (RR 49544/2022). | Acuerdo de titularidad compartida y cesión de derechos de autor patrimoniales. |

---

### A. Comité Central de Ética en Investigación (CCEI)

El **Comité Central de Ética en Investigación (CCEI)** es un organismo adscrito a la Vicerrectoría de Investigación que actúa con autonomía para velar por que los aspectos éticos de la investigación se reflejen en las normas y prácticas investigativas de la Universidad.

- **Marco Normativo:** Reglamentado mediante la [:material-file-pdf-box: Resolución Rectoral 47765 del 15 de marzo de 2021](https://www.udea.edu.co/wps/wcm/connect/udea/04543468-66ad-4015-8850-ee4b36c0d86c/Resolucio%CC%81n+Rectora+47765.pdf?MOD=AJPERES&CVID=nK7Qn4c).
- **Manual Operativo:** Consulta los procedimientos operativos del CCEI y de los distintos Comités de Ética y Bioética de la Universidad en el [:material-file-pdf-box: Manual para el funcionamiento de los Comités de Ética (2.ª versión ajustada)](https://www.udea.edu.co/wps/wcm/connect/udea/8598ab50-c33d-45cf-be1c-b105a884743b/Manual+operativo_Segundaversi%C3%B3n.Ajustada.pdf?MOD=AJPERES&CVID=oUqU4v2).
- **Directrices Temáticas:** Revisa la [:material-file-pdf-box: Circular Única — Tópicos de Interés Ético-Bioético](https://www.udea.edu.co/wps/wcm/connect/udea/52644c75-4996-42c2-8572-c14c2e321ccc/Circular+%C3%9Anica+CCEI+-+FINAL.+Sept29.pdf?MOD=AJPERES&CVID=oeesmid).
- **Contacto:** `direccionsiu@udea.edu.co`.

### B. Permisos Ambientales, Colecta Biológica y Recursos Genéticos

Cuando un proyecto involucra trabajo de campo con diversidad biológica o comunidades étnicas, el SIIU y la normativa nacional exigen tramitar los permisos correspondientes **antes de iniciar la recolección**:

1. **Permiso Marco de Recolección de Especímenes de Especies Silvestres de la Diversidad Biológica con Fines de Investigación Científica No Comercial:**
   Los docentes regulares que aún no estén incorporados al Permiso Marco y requieran realizar actividades de colecta deben solicitar su inclusión ante la Vicerrectoría de Investigación (`viceinvestigacionpa@udea.edu.co`), enviando:
   - Nombre del grupo de investigación.
   - Descripción de las actividades de recolección de especies que realiza el grupo.
   - Nombre completo y número de cédula del investigador.
   - Programa(s) académico(s) que el grupo apoya.
2. **Contrato de Acceso a Recursos Genéticos y Productos Derivados:** Requerido cuando las actividades implican bioprospección o acceso a material genético (Circular 03 de 2019 y Circular 02 de 2016 de la VRI).
3. **Consulta Previa:** Obligatoria cuando los proyectos se desarrollen en territorios o con participación directa de comunidades étnicas reconocidas.

### C. Política de Conflicto de Intereses Financieros (FCOI)

En proyectos financiados por entes externos nacionales o internacionales (incluyendo agencias sujetas al Código de Regulaciones Federales de EE. UU. — **42 CFR Parte 50, Subparte F**), la Universidad aplica la **Política de Gestión de Conflictos de Intereses Financieros** para identificar, eliminar o controlar amenazas a la integridad científica y a la protección de sujetos de investigación:

- **Normativa:** [:material-file-pdf-box: Resolución Rectoral 49547 (Español)](https://www.udea.edu.co/wps/wcm/connect/udea/c6478f87-824e-479e-818a-2f365020e9b9/Resoluci%C3%B3n+Rectoral+49547+-+firmado.pdf?MOD=AJPERES&CVID=ojd.O8p) y [:material-file-pdf-box: Reglamentación FCOI UdeA](https://www.udea.edu.co/wps/wcm/connect/udea/3eacbb03-1660-42b2-a412-f16257bbf588/Reglamentaci%C3%B3n+Pol%C3%ADtica+de+Conflictos+de+Interes+Financieros+VF.pdf?MOD=AJPERES&CVID=ojd.7aW).
- **Declaración Obligatoria:** Diligenciar el [:material-file-word-box: Formato de Declaración de Situaciones de Conflicto de Intereses](https://www.udea.edu.co/wps/wcm/connect/udea/3a7e9c6f-94a3-4661-beed-e6bccbd7d52b/Formato+DECLARACIO%CC%81N+DE+SITUACIONES+DE+CONFLICTO+DE+INTERESES+VerDic20.docx?MOD=AJPERES&CVID=okQM-1u) y cargarlo como soporte en el expediente del proyecto.

---

## 3. Matriz de Trazabilidad: Estado del SIIU vs. Instancia Responsable

| Estado en el SIIU | Instancia Responsable | Documento o Acto Asociado |
| :--- | :--- | :--- |
| **En Formulación** | Investigador Principal / Grupo | Propuesta técnica en borrador |
| **Enviado Centro** | Gestor del Centro / Auxiliar Técnico | Lista de chequeo habilitante |
| **Pendiente Actualización** | Investigador Principal | Subsanación de observaciones |
| **Avalado Centro** | Comité Técnico del Centro / Consejo | Acta de Comité Técnico |
| **En Evaluación Pares** | Evaluadores Pares (Internos / Externos) | Formulario de calificación |
| **Aprobado** | CODI / Ente Financiador Externo | Resolución de adjudicación |
| **Inicio Formal** | Centro de Investigación y Decanatura | Acta de Inicio, Pólizas y Centro de Costos |
| **En Ejecución (Novedad)** | Comité Técnico / Vicerrectoría | Solicitud de Prórroga o Traslado |
| **Finalizado** | Comité Técnico del Centro | Informes y Acta de Cumplimiento |
| **Liquidado** | Decano / Vicerrectoría de Investigación | Acta de Liquidación y Paz y Salvo Presupuestal |

---

## 4. Enlaces de Interés y Rutas Operativas Relacionadas

- Consulta el **[Rol del Investigador Principal](Rol_Investigador.md)** para conocer las rutas de radicación.
- Consulta el **[Rol del Centro de Investigación](Rol_Centro_Investigacion.md)** para el trámite de revisiones y avales.
- Consulta el **[Acuerdo Superior 204 de 2001](../05_MARCO_NORMATIVO/AS_204_2001_Sistema_Universitario_Investigacion.md)** para la estructura jurídica completa del SUI.
