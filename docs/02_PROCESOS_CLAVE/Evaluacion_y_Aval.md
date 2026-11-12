# Proceso Clave: Evaluación Técnica, Aval y Subsanación

Una vez que el Investigador Principal radica su propuesta en el SIIU, se inicia la fase de control de calidad institucional, compuesta por la **revisión técnica formal del Centro**, el ciclo de **subsanación de inconsistencias** y la **evaluación académica por pares**.

```mermaid
sequenceDiagram
    autonumber
    actor IP as Investigador
    participant SIIU as 💻 SIIU
    actor CEN as Centro de Investigación
    actor PAR as Evaluador Par

    IP->>SIIU: Envía proyecto a Centro
    Note over IP,SIIU: Estado: Enviado a Centro
    CEN->>SIIU: Realiza Evaluación Técnica Formal
    
    alt Alguna condición No Cumple (Devolución)
        CEN->>SIIU: Autoriza Actualización (Secciones + Plazo)
        Note over CEN,SIIU: Estado: Pendiente Actualización
        SIIU-->>IP: Notifica correo con secciones a corregir
        IP->>SIIU: Edita secciones autorizadas y Guarda
        IP->>SIIU: Registra comentarios y presiona "Enviar a Centro"
        Note over IP,SIIU: Estado: Actualizado
        CEN->>SIIU: Reevalúa condiciones corregidas
    end

    CEN->>SIIU: Emite Aval Técnico del Centro
    Note over CEN,SIIU: Estado: Avalado por Centro
    CEN->>SIIU: Asigna Evaluadores Pares (Internos / Externos)
    SIIU-->>PAR: Notifica asignación y envía formato
    PAR->>SIIU: Califica criterios y emite concepto
    Note over PAR,SIIU: Estado: Evaluado (Puntaje Promedio)
```


---

## 1. Evaluación Técnica de Centro

El Centro de Investigación o Extensión revisa el cumplimiento de los Términos de Referencia de la convocatoria.

- **Ruta SIIU:** `Convocatorias >> Proyectos en evaluación >> Filtros de consulta >> Acciones (...) >> Realizar evaluación técnica`
- **Condiciones Evaluadas:**
  - Pertenencia del equipo investigador al grupo avalador.
  - Dedicación horaria semanal coherente con la normativa de vinculación docente.
  - Estructuración del presupuesto según los topes de la convocatoria.
  - Soportes éticos y de comités pertinentes.
- **Opciones de Calificación por Condición:**
  - `Cumple`
  - `No cumple`
  - `No aplica`
- 📘 Guía oficial: [VI-GU-08](../../archivo_maestro/VI-GU-08.md)

---

## 2. Devolución para Ajustes (Rol Centro)

Si una o más condiciones son marcadas como **"No cumple"**, el Centro no debe rechazar la propuesta inmediatamente, sino abrir un periodo de subsanación:

1. Al guardar la evaluación con un "No cumple", presione el botón **`Autorizar actualización`**.
2. Parámetros de configuración obligatorios:
   - **Evaluación:** Tipo de evaluación formal.
   - **Fecha y Hora Límite:** Plazo improrrogable concedido al investigador para corregir.
   - **Secciones del proyecto:** Seleccionar las pestañas específicas que requieren ajuste (ej. Presupuesto, Metodología, Documentos Soporte).
   - **Cambios solicitados:** Texto explicativo detallado con las observaciones técnicas (hasta 400 caracteres).
3. Presione **AUTORIZAR ACTUALIZACIÓN** y confirme la alerta.
4. El proyecto queda en estado **Pendiente de actualización**.
- 📘 Instructivo oficial: [VI-IN-12](../../archivo_maestro/VI-IN-12.md)

---

## 3. Subsanación y Ajustes de Proyectos Devueltos (Rol Investigador)

Cuando el IP recibe notificación de devolución:

1. **Ruta SIIU:** `Convocatorias >> Proyectos en proceso >> Estado: "Pendiente Actualización" >> Acciones (...) >> Editar`
2. **Revisión de Observaciones:** En la pestaña *Información general* verá un banner azul con el plazo límite y las secciones autorizadas. Ingrese a la pestaña **`Actualización`** para leer en detalle los comentarios del Centro.
3. **Edición:** Diríjase a las secciones habilitadas, realice las correcciones solicitadas y presione **GUARDAR**.
4. **Registro de Respuestas:** Regrese a la pestaña **`Actualización`**, despliegue las opciones de *Comentarios*, haga clic en **Editar**, describa los cambios realizados y guarde.
5. **Reenvío:** Vaya a la pestaña final **`Enviar`**, presione **"Enviar a Centro"** y confirme.
6. El proyecto pasa a estado **Actualizado** para que el Centro proceda con la aprobación final.
- 📘 Instructivo oficial: [VI-IN-05](../../archivo_maestro/VI-IN-05.md)

---

## 4. Asignación de Evaluadores Pares

Una vez subsanadas las observaciones y emitido el aval del Centro:

- **Ruta SIIU:** `Convocatorias >> Aval de proyectos >> Seleccionar proyecto >> Asignar evaluador`
- **Criterios de Asignación:**
  - Evaluador Interno (docente UdeA de otra unidad académica sin conflicto de interés).
  - Evaluador Externo (investigador nacional o internacional registrado en el banco de evaluadores).
  - Definición del número de evaluadores (habitualmente 2 evaluadores titulares y 1 de desempate).
- **Consolidación de Calificaciones:** El sistema calcula automáticamente el promedio ponderado de las evaluaciones registradas.
- 📘 Guía oficial: [VI-GU-06](../../archivo_maestro/VI-GU-06.md)

---

## 5. Configuración de Convocatorias (Rol Vicerrectoría)

La Vicerrectoría de Investigación es la responsable de parametrizar las reglas de juego de cada convocatoria:

- **Ruta SIIU:** `Configuración >> Convocatorias >> Gestión de convocatorias`
- **Parámetros configurables:**
  - Fechas de apertura, cierre de inscripción, evaluación de centros y publicación de resultados.
  - Rubros presupuestales financiables y porcentajes máximos por rubro.
  - Criterios de evaluación y ponderaciones de la rúbrica de calificación.
  - Formatos y documentos soporte obligatorios.
- 📘 Guía oficial: [VI-GU-07](../../archivo_maestro/VI-GU-07.md)

---

## 🔗 Próximo Paso en el Flujo
Una vez aprobado el proyecto por el Comité o CODI:
Consulta **[Inicio Formal](../02_PROCESOS_CLAVE/Inicio_Formal.md)**.
