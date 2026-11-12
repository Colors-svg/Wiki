# Proceso Clave: Inicio Formal de Proyectos

La aprobación de un proyecto en una convocatoria no autoriza de manera automática el gasto de los recursos ni el reconocimiento oficial de tiempos. Para ello se requiere el **Inicio Formal**, un hito administrativo y legal que marca el paso del estado **Aprobado** al estado **En ejecución**.

```mermaid
flowchart TD
    classDef aprobado fill:#081810,stroke:#35944B,stroke-width:1.5px,color:#E1EFE6,rx:6px,ry:6px;
    classDef req fill:#0D2115,stroke:#026937,stroke-width:2px,color:#FFFFFF,rx:6px,ry:6px;
    classDef reg fill:#112B1B,stroke:#8DC63F,stroke-width:2px,color:#FFFFFF,rx:6px,ry:6px;
    classDef ejec fill:#026937,stroke:#8DC63F,stroke-width:2px,color:#FFFFFF,rx:8px,ry:8px;

    APROB["Proyecto en Estado Aprobado<br><small>Asignación presupuestal oficial de la convocatoria</small>"]:::aprobado --> REQ

    subgraph REQ ["1. Verificación y Aporte de Requisitos Previos"]
        direction TB
        R1["Centro de Costos Institucional<br><small>Código contable expedido por Presupuesto</small>"]:::req
        R2["Pólizas de Garantía y Amparos<br><small>Buen manejo, cumplimiento y calidad</small>"]:::req
        R3["Contrato o Convenio Legalizado<br><small>Minuta suscrita con el ente financiador</small>"]:::req
        R4["Aval Ético y Permisos Ambientales<br><small>Concepto definitivo comités de ética</small>"]:::req
    end

    REQ --> REG_SIIU

    subgraph REG_SIIU ["2. Diligenciamiento en SIIU (Vicerrectoría)"]
        direction TB
        S1["Vinculación de Amparos de Pólizas<br><small>Vigencias, valores asegurados y compañías</small>"]:::reg
        S2["Asignación de Centro de Costos<br><small>Articulación contable en SIIU</small>"]:::reg
        S3["Fijación de Cronograma Oficial<br><small>Fechas exactas de inicio y terminación</small>"]:::reg
        S4["Firma y Publicación de Acta de Inicio<br><small>Acto administrativo formal de apertura</small>"]:::reg
    end

    REG_SIIU --> EJEC["Estado: EN EJECUCIÓN<br><small>Habilitación de rubros presupuestales y novedades</small>"]:::ejec
```


---

## 1. Requisitos Previos al Inicio Formal

Antes de tramitar el acta de inicio formal en el SIIU, se deben consolidar los siguientes instrumentos:

1. **Centro de Costos (Centro Administrativo / Financiero):** Código contable asignado por el Departamento de Presupuesto para la ejecución de los recursos en el sistema financiero institucional.
2. **Pólizas de Garantía (cuando aplique por cuantía o convenio externo):**
   - Amparo de Buen Manejo y Correcta Inversión del Anticipo.
   - Amparo de Cumplimiento del Contrato.
   - Amparo de Salarios, Prestaciones Sociales e Indemnizaciones.
   - Amparo de Calidad de los Bienes o Servicios.
3. **Contratos o Convenios Interinstitucionales:** En proyectos con financiación externa o convenios marco entre universidades o empresas.
4. **Aval Ético Definitivo:** Certificación expedida por el Comité de Ética de la Investigación (humana o animal) correspondiente.

---

## 2. Diligenciamiento del Inicio Formal en el SIIU (Rol Vicerrectoría)

- **Ruta SIIU:** `Trámites administrativos >> Inicio formal de proyectos`
- 📘 Guía oficial: [VI-GU-15](../archivo_maestro/VI-GU-15.md)

### Pasos Operativos:
1. **Búsqueda del Proyecto:** Localizar el proyecto en estado **Aprobado**.
2. **Pestaña Pólizas y Contratos:**
   - Registrar la aseguradora, número de póliza, fecha de expedición, fecha de vigencia y valores asegurados por cada amparo.
   - Adjuntar el PDF de la póliza aprobada por la Dirección Jurídica o División de Asesoría Jurídica.
3. **Pestaña Centro de Costos:**
   - Vincular el código financiero alfanumérico generado en el sistema central de presupuesto.
4. **Pestaña Fechas Oficiales:**
   - **Fecha de Inicio Formal:** Día oficial a partir del cual rige la vigencia legal del proyecto.
   - **Fecha de Terminación Oficial:** Calculada automáticamente con base en los meses de duración aprobados.
5. **Generación del Acta de Inicio:**
   - El sistema compila la información y genera el documento formal del **Acta de Inicio**.
   - Se legalizan las firmas del Investigador Principal, el Jefe de Centro y el Delegado de la Vicerrectoría.
6. Al presionar **CONFIRMAR INICIO FORMAL**, el proyecto adquiere formalmente el estado **En ejecución**.

---

## 3. ¿Qué ocurre si se vence el plazo sin iniciar?

!!! danger "VENCIMIENTO DEL PLAZO DE INICIO"
    Si los trámites de pólizas o contratos toman más tiempo del reglamentario, el proyecto puede caer en estado **No iniciado** o ser **Cancelado**.  
    Para evitar esto, el Investigador Principal debe solicitar oportunamente una **Prórroga de Inicio** mediante el menú de trámites administrativos mientras el proyecto aún figure en estado **Aprobado**.  
    Consulta: [Modificaciones y Tramites](../02_PROCESOS_CLAVE/Modificaciones_y_Tramites.md#prorroga-de-proyecto).

---

## 🔗 Próximo Paso en el Flujo
Con el proyecto **En ejecución**, se habilitan las compras, contrataciones, solicitudes de cambio de presupuesto y adición de tiempo:
Consulta **[Modificaciones y Tramites](../02_PROCESOS_CLAVE/Modificaciones_y_Tramites.md)** y **[Gestion Compromisos](../02_PROCESOS_CLAVE/Gestion_Compromisos.md)**.
