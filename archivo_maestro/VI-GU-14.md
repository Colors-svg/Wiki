---
codigo: "VI-GU-14"
titulo: "Guía para configurar trámites administrativos en el SIIU"
version: "01"
fecha_aprobacion: "2024-04-29"
institucion: "Universidad de Antioquia"
dependencia: "Vicerrectoría de Investigación"
sistema: "SIIU (Sistema de Información para la Investigación Universitaria – SIIU)"
documento_fuente: "VI-GU-14.pdf"
roles_involucrados:
  - "Usuario con rol Administrador Proyecto"
tags:
  - "archivo_maestro"
  - "guia"
  - "siiu"
  - "configuracion"
  - "tramites_administrativos"
  - "flujo_procesos"
  - "niveles_administrativos"
  - "avales_y_aprobaciones"
---

# GUÍA PARA CONFIGURAR TRÁMITES ADMINISTRATIVOS EN EL SIIU

> [!NOTE] Información de Control Documental
> **Código**: VI-GU-14  
> **Versión**: 01 / 29-ABR-2024  
> *Aviso legal institucional*: La impresión o copia digital de este documento se considera "COPIA NO CONTROLADA". Solo se garantiza la actualización de la documentación en el sitio oficial `http://www.udea.edu.co`.

---

## Contenido

1. [Definición](#1-definición)
2. [Contenido](#2-contenido)
   - 2.1. [Requisitos para la configuración de permisos de usuarios](#21-requisitos-para-la-configuración-de-permisos-de-usuarios)
   - 2.2. [Usuarios que intervienen en el proceso](#22-usuarios-que-intervienen-en-el-proceso)
   - 2.3. [Ingreso al SIIU](#23-ingreso-al-siiu)
   - 2.4. [Configuración trámites administrativos](#24-configuración-trámites-administrativos)
     - 2.4.1. [Filtros de búsqueda y selección de convocatoria/proceso](#filtros-de-búsqueda-y-selección-de-convocatoriaproceso)
     - 2.4.2. [Agregar y parametrizar tipos de trámite administrativo](#agregar-y-parametrizar-tipos-de-trámite-administrativo)
     - 2.4.3. [Configuración de Niveles Administrativos (Avalar y Aprobar)](#configuración-de-niveles-administrativos-avalar-y-aprobar)
     - 2.4.4. [Asociación de Centros de Gestión](#asociación-de-centros-de-gestión)
     - 2.4.5. [Activación y Resumen del Trámite](#activación-y-resumen-del-trámite)
     - 2.4.6. [Inactivación de la Configuración del Trámite](#inactivación-de-la-configuración-del-trámite)
3. [Nota de cambio](#3-nota-de-cambio)
4. [Registro de Control y Firmas](#registro-de-control-y-firmas)

---

## 1. Definición

Este documento se ha elaborado con el fin de ayudar y capacitar los administradores del Sistema de Información para la Investigación Universitaria – SIIU. En la configuración de permisos de usuarios. Dado lo anterior se aclara que esta guía no hace parte de la normativa universitaria y solamente se debe utilizar como una herramienta que orienta los pasos a seguir en el aplicativo.

---

## 2. Contenido

### 2.1 Requisitos para la configuración de permisos de usuarios

- El usuario con rol de administrador debe estar registrado en el portal institucional y tener acceso a SIIU.
- El usuario con rol de administrador debe tener acceso a la opción de permisos.

### 2.2 Usuarios que intervienen en el proceso

- **Usuario con rol Administrador Proyecto**.

---

### 2.3 Ingreso al SIIU

El investigador principal o responsable del proyecto (o usuario administrador) debe autenticarse en el portal de la Universidad de Antioquia, `http://www.udea.edu.co`, buscar la opción aplicaciones y entre ellas elegir el SIIU, así:

1. Ingresa al portal de la Universidad: `http://www.udea.edu.co`, en el encabezado seleccione **Ingresar >> Iniciar sesión** (Ver figura 1).

   ![[VI-GU-14-figura-01.png]]
   *Figura 1 - Ingreso al portal de la Universidad de Antioquia*

2. Aparece pantalla para ingresar su usuario y contraseña, seleccione *No soy un Robot* (el sistema le puede pedir realizar validaciones) finalmente presione clic en el botón **CONECTAR**. (Ver figura 2).

   ![[VI-GU-14-figura-02.png]]
   *Figura 2 - Conectar al portal*

3. Presione clic en la opción **Enlaces de Interés** y seleccione **Mis aplicaciones**, así: `Enlaces de interés → Mis aplicaciones`. (Ver figura 3).

   ![[VI-GU-14-figura-03.png]]
   *Figura 3 - Enlaces de interés*

4. Se abrirá una ventana con las aplicaciones de la Universidad; seleccione **SIIU**. (Ver figura 4).

   ![[VI-GU-14-figura-04.png]]
   *Figura 4 - Seleccione SIIU*

> [!IMPORTANT]
> Se abre una nueva ventana con la aplicación SIIU. Si la ventana no abre inmediatamente, es necesaria la configuración de ventanas emergentes en el navegador y seleccionar la opción que autorice el SIIU.

---

### 2.4 Configuración trámites administrativos

Estando en el SIIU ingrese por el menú **Convocatorias** luego por la opción **Flujo procesos administrativos y novedades**, tal como muestra la figura 5.

Ruta: `Convocatorias / Flujo procesos administrativos y novedades`

![[VI-GU-14-figura-05.png]]
*Figura 5 - Convocatorias/ Flujo procesos administrativos y novedades*

---

#### Filtros de búsqueda y selección de convocatoria/proceso

El sistema abre formulario con los campos:
- **Tipo de proyecto**: con las opciones *Investigación*, *Extensión*, *Posgrados*.
- **Tipo de trámite**: habilita las diferentes solicitudes administrativas que se pueden realizar por SIIU.
- **Mostrar inactivos**: casilla de verificación (check) para observar los procesos que ya se encuentran inactivos.
- Botones **Consultar** y **Limpiar**. (Ver figura 6).

![[VI-GU-14-figura-06.png]]
*Figura 6 - Filtro de búsqueda*

Al seleccionar el tipo de proyecto se habilitan los botones de selección:
- **Convocatoria**
- **Proceso de selección**

Para indicar al sistema el tipo de trámite que desea consultar o configurar. (Ver figura 7).

![[VI-GU-14-figura-07.png]]
*Figura 7 - Convocatoria o proceso de selección*

- **Caso Convocatoria**: Elija la opción convocatoria; observe que se despliega la lista de convocatorias disponibles. Elija la convocatoria que requiere para la configuración del trámite administrativo. (Ver figura 8).

  ![[VI-GU-14-figura-08.png]]
  *Figura 8 - Listado de convocatorias*

- **Caso Proceso de selección**: De igual manera sucede al seleccionar la opción proceso de selección; el sistema lista los procesos de selección habilitados para la configuración del trámite administrativo. (Ver figura 9).

  ![[VI-GU-14-figura-09.png]]
  *Figura 9 - Listado proceso de selección*

---

#### Agregar y parametrizar tipos de trámite administrativo

Cuando se presiona **Consultar** y el sistema muestra el mensaje *"No se obtuvieron registros para la consulta especificada"*, significa que el trámite no ha sido configurado aún. En este caso, presione el icono **+** que aparece al costado derecho de la pantalla. (Ver figura 10).

> [!NOTE] Definición de Novedad en el sistema
> Una *"Novedad"* se refiere a: cambios (en tiempo, presupuesto, personas o compromisos de un proyecto) que ya fueron aprobados por (co)financiador(es) externos.

![[VI-GU-14-figura-10.png]]
*Figura 10 - Icono para agregar trámite administrativo*

Una vez se ha presionado el icono **+**, el sistema habilita un nuevo formulario donde se seleccionan los trámites que se desean configurar, el número de veces sin pasar por la vicerrectoría, además de la descripción del trámite.

En las figuras 11 y 12 observe que el campo **Tipo de trámite** muestra todos los trámites administrativos configurados en SIIU:
- *Adición Presupuestal*
- *Cambio de Participantes*
- *Cambio Rubro*
- *Cancelar Proyecto*
- *Homologación de Compromisos*
- *Modificación de ítems del proyecto*
- *Plazo para entrega de compromisos*
- *Prórroga*

Pasos de diligenciamiento:
1. Seleccione con un check cada uno de los tipos de trámite que desea configurar.
2. Asigne el **Número de veces sin pasar por Vicerrectoría** (por ejemplo: `3`).
3. Indique una **Descripción** para el trámite (por ejemplo: `solicitud administrativa`).
4. Presione la opción **Guardar**. (Ver figuras 11 y 12).

![[VI-GU-14-figura-11.png]]
*Figura 11 - Resultado de la búsqueda*

![[VI-GU-14-figura-12.png]]
*Figura 12 - Diligenciar configuración*

Una vez se presiona el botón **Guardar**, el sistema genera el mensaje *"Creado exitosamente"* y habilita los botones **Activar** y **Siguiente**. Presione el botón **Siguiente** para dirigirse a la pestaña **Nivel administrativo**. (Ver figura 13).

![[VI-GU-14-figura-13.png]]
*Figura 13 - Botones Activar y Siguiente*

---

#### Configuración de Niveles Administrativos (Avalar y Aprobar)

Una vez se ha presionado la opción siguiente, el sistema se dirige a la pestaña **Nivel Administrativo**. Presione el icono **+** para configurar las acciones de avalar y aprobar el trámite. (Ver figura 14).

![[VI-GU-14-figura-14.png]]
*Figura 14 - Pestaña Nivel administrativo*

Al presionar el icono **+**, el sistema abre un nuevo formulario con los siguientes campos:

| Campo | Detalle |
| :--- | :--- |
| **Secuencia** | Por defecto aparece en uno (`1`). |
| **Nivel administrativo** | Lista desplegable que contiene todas las unidades académicas / dependencias (`Centro de Docencia`, `Centro de Extensión`, `Centro de Investigación`, `Comité`, `Comité Ética`, `Dependencias en PlanView equivalentes a los centros de investigación`, `Dirección`, `Escuela`, `Facultad`, `Instituto`, `QA prueba`, `Rectoría`, `Unidad Académica Posgrados`, etc.). |
| **Recomendación** | Lista desplegable que contiene las opciones `Aprobar` o `Avalar`. |
| **Omitir** | Casilla para omitir la configuración del trámite. |
| **Notas** | Agregue información del trámite que está configurando, ya sea para avalar o aprobar. |
| **Guardar** | Almacena el registro. |
| **Cancelar** | Cancela la opción. |

![[VI-GU-14-figura-15.png]]
*Figura 15 - Agregar Nivel administrativo*

Diligencie los campos del formulario de acuerdo con la configuración requerida para los trámites administrativos:
- **Regla general**: El centro avala mientras que la vicerrectoría aprueba.
- **Caso especial**: Un solo nivel donde la vicerrectoría aprueba directamente (por ejemplo, cupos de Joven Investigador o proyectos inscritos).

Esta opción depende del tipo de proyecto o convocatoria que se esté configurando. (Ver figura 16).

![[VI-GU-14-figura-16.png]]
*Figura 16 - Configuración del trámite*

##### Paso 1: Configurar Nivel Aval (Centro de Investigación)
En las figuras 17 y 18 se muestra la configuración del trámite administrativo para el proceso de avalar la solicitud administrativa, donde el centro es quien realiza el aval:
- **Secuencia**: `1`
- **Nivel Administrativo**: `Centro de Investigación`
- **Recomendación**: `Avalar`
- **Notas**: `Avalar proyecto`
- Presione **Guardar** para continuar.

![[VI-GU-14-figura-17.png]]
*Figura 17 - Centro Avala*

![[VI-GU-14-figura-18.png]]
*Figura 18 - Centro Avala*

Una vez guardado el registro de aval, el sistema abre una nueva opción para seleccionar la instancia administrativa que va a realizar el proceso de avales a las solicitudes. (Ver figura 19).

![[VI-GU-14-figura-19.png]]
*Figura 19 - Seleccionar instancia administrativa*

Despliegue la lista de la opción **Seleccione**, y el sistema mostrará todos los centros de investigación o extensión, según el caso:
- Se puede seleccionar un centro específico, o
- Se pueden seleccionar todos los centros eligiendo la opción **Todos**, de manera que todos los centros queden habilitados para realizar el proceso de aval.
- Presione el botón **Agregar**. (Ver figura 20).

![[VI-GU-14-figura-20.png]]
*Figura 20 - Todos los centros*

Al seleccionar todos los centros, el sistema presenta la información en los campos:
- **Código Instancia**
- **Nombre Instancia**
- Acción de eliminación (icono `x`) para retirar cualquier centro no requerido.
- Presione el botón **Guardar** para continuar. (Ver figura 21).

![[VI-GU-14-figura-21.png]]
*Figura 21 - Seleccionar centros*

> [!TIP] Continuación o edición en caso de interrupción
> Si el sistema se cierra por inactividad o debe continuar luego el proceso, realice la consulta de acuerdo con los filtros de búsqueda descritos anteriormente. Al consultar el trámite aparece el icono **lápiz**, el cual le permitirá editar el trámite y continuar con la configuración. (Ver figuras 22 y 23).

![[VI-GU-14-figura-22.png]]
*Figura 22 - Resumen de la configuración*

![[VI-GU-14-figura-23.png]]
*Figura 23 - Editar trámite administrativo*

##### Paso 2: Configurar Nivel Aprobación (Vicerrectoría)
Para agregar una nueva recomendación para aprobar:
1. Presione el icono **+**.
2. Observe que ha aumentado el valor en el campo **Secuencia** (pasa a `2`).
3. En el campo **Nivel administrativo**, seleccione `Vicerrectoría`.
4. En el campo **Recomendación**, seleccione `Aprobar`.
5. En **Notas**, ingrese la indicación correspondiente (ejemplo: `Aprobar`).
6. Presione **Guardar**. (Ver figura 24).

![[VI-GU-14-figura-24.png]]
*Figura 24 - Aprobar trámite*

Una vez guardada la recomendación de Aprobación, el sistema abre un nuevo campo para seleccionar la instancia administrativa que realizará el proceso de aprobación. Aparecen las siguientes opciones:
- *Vicerrectoría de Extensión*
- *Vicerrectoría Administrativa*
- *Vicerrectoría de Docencia*
- *Vicerrectoría de Investigación*

Seleccione de acuerdo con su necesidad y luego presione **Guardar**. (Ver figuras 25 y 26).

![[VI-GU-14-figura-25.png]]
*Figura 25 - Instancia que aprueba*

Una vez seleccionada la instancia, identifique que aparece el código de la instancia y el nombre de la instancia definida para la aprobación. (Ver figura 26).

![[VI-GU-14-figura-26.png]]
*Figura 26 - Nombre instancia que aprueba*

Al presionar el botón **Guardar**, el sistema muestra un resumen de la configuración en la pestaña *Nivel administrativo* con las recomendaciones definidas de acuerdo con la configuración establecida para cada instancia. (Ver figura 27).

> [!NOTE] Criterio Operativo Institucional
> Normalmente el **Centro Avala** y la **Vicerrectoría Aprueba** las solicitudes administrativas.
> Puede suceder, como en el caso del cupo de Joven Investigador o proyectos inscritos, que la Vicerrectoría realiza el proceso de aprobación sin pasar por el centro para avalar; para este caso específico solo se configura la recomendación **Aprobar**.

![[VI-GU-14-figura-27.png]]
*Figura 27 - Resumen de recomendaciones x instancias*

---

#### Asociación de Centros de Gestión

Una vez guardados y agregados los niveles administrativos, presione la opción **Siguiente** para dirigirse a la pestaña **Centros**. Allí podrá seleccionar el centro o centros que podrán utilizar la configuración del trámite administrativo para la solicitud requerida; de esta manera, el investigador principal podrá tramitarla.

En el campo **Centro administrativo**:
- Seleccione la opción **Todos los de investigación**, o
- Seleccione **Todos los de Extensión**, o
- Seleccione uno o varios centros específicos de la lista desplegable.
- Finalmente presione **Agregar**. (Ver figura 28).

![[VI-GU-14-figura-28.png]]
*Figura 28 - Pestaña Centros*

Al seleccionar la opción *Todos los centros*, nótese que en la columna **Nombre** aparece la lista completa de los centros de investigación o extensión correspondientes. A su vez, aparece una columna con el icono `x`, tal como muestra la figura 29, la cual indica que puede eliminarse un centro individualmente si no aplica.

![[VI-GU-14-figura-29.png]]
*Figura 29 - Todos los centros*

---

#### Activación y Resumen del Trámite

Una vez configurados los centros:
1. Diríjase nuevamente a la pestaña **Información general**.
2. Verifique que tenga la información completa en la ventana.
3. Presione la opción **Guardar**.
4. Luego presione el botón **Activar**. De esta manera queda configurado y disponible el proceso de Trámites administrativos para que el investigador principal pueda realizar solicitudes administrativas de acuerdo a su necesidad. (Ver figura 30).

![[VI-GU-14-figura-30.png]]
*Figura 30 - Activar configuración*

Una vez activado el trámite, el sistema muestra el resumen con las siguientes columnas:

| Columna | Detalle |
| :--- | :--- |
| **Código de trámite** | Código del trámite configurado. |
| **Tipo de trámite** | Nombre del trámite configurado. |
| **Tipo de solicitud** | Interna o Novedad (Aplica para inscritos). |
| **Estado** | Estado del trámite: `Activo` o `Inactivo`. |
| **Inicio de vigencia** | Fecha en que se activó el trámite. |
| **Fin Vigencia** | Campo vacío (o fecha límite si aplica). |

![[VI-GU-14-figura-31.png]]
*Figura 31 - Resumen de trámite configurado*

---

#### Inactivación de la Configuración del Trámite

Si en la pantalla de resumen descrita anteriormente se presiona el icono **lápiz**, el sistema abre una nueva ventana con el botón **Inactivar**, tal como muestra la figura 32.

> [!WARNING] Advertencia sobre Inactivación
> Tenga en cuenta que si presiona la opción **Inactivar**, la configuración deja de estar disponible en el sistema y se deberá crear una nueva configuración del trámite para reemplazar el trámite inactivo. (Ver figura 32).

![[VI-GU-14-figura-32.png]]
*Figura 32 - Inactivar*

Una vez terminado el proceso de configuración del trámite administrativo, el investigador principal o coordinador del proyecto podrá realizar la solicitud del trámite administrativo y podrá enviarla al centro para su aval o a la vicerrectoría para su aprobación, según el caso configurado.

> [!NOTE]
> Todas las imágenes corresponden a la configuración general de proyectos del trámite de solicitudes administrativas.

---

## 3. Nota de cambio

- No aplica para la primera versión.

---

## Registro de Control y Firmas

| Rol | Nombre | Cargo / Dependencia | Fecha |
| :--- | :--- | :--- | :--- |
| **Elaboró** | Sandra Patricia Zabala Orrego | Contratista, Vicerrectoría Investigación | 16-FEB-2024 |
| **Revisó** | Kerlin Yohana Bedoya Agudelo | Analista de Procesos, División de Arquitectura de Procesos | 29-ABR-2024 |
| **Aprobó** | Gloria Valencia Bustamante | Asistente, Vicerrectoría de Investigación | 29-ABR-2024 |
