---
codigo: "VI-GU-25"
titulo: "Guía CKEditor para la matrícula de proyectos en el SIIU"
version: "01"
fecha_aprobacion: "2024-07-12"
institucion: "Universidad de Antioquia"
dependencia: "Vicerrectoría de Investigación"
sistema: "SIIU (Sistema de Información para la Investigación Universitaria – SIIU)"
documento_fuente: "VI-GU-25.pdf"
roles_involucrados:
  - "Usuario con rol Investigador Principal o Responsable del Proyecto"
tags:
  - "archivo_maestro"
  - "guia"
  - "siiu"
  - "ckeditor"
  - "editor_de_texto"
  - "ecuaciones"
  - "latex"
  - "formulas_matematicas"
  - "matrices"
  - "imagenes"
---

# GUÍA CKEditor PARA LA MATRÍCULA DE PROYECTOS EN EL SIIU

!!! note "Información de Control Documental"
> **Código**: VI-GU-25  
> **Versión**: 01 / 12-JUL-2024  
> *Aviso legal institucional*: La impresión o copia magnética de este documento se considera "COPIA NO CONTROLADA". Solo se garantiza la actualización de la documentación en el sitio oficial `http://www.udea.edu.co`.

---

## Contenido

1. [Definición](#1-definición)
2. [Contenido](#2-contenido)
   - 2.1. [Requisitos para el uso del CKEditor](#21-requisitos-para-el-uso-del-ckeditor)
   - 2.2. [Usuarios que intervienen en el proceso](#22-usuarios-que-intervienen-en-el-proceso)
   - 2.3. [Menú de Opciones del Editor](#23-menú-de-opciones-del-editor)
   - 2.4. [¿Cómo insertar una ecuación?](#24-cómo-insertar-una-ecuación)
   - 2.5. [Insertar fórmula](#25-insertar-fórmula)
   - 2.6. [Agregar color a una fórmula](#26-agregar-color-a-una-fórmula)
   - 2.7. [Agregar espacio a una fórmula](#27-agregar-espacio-a-una-fórmula)
   - 2.8. [Agregar matrices](#28-agregar-matrices)
   - 2.9. [Editar una ecuación](#29-editar-una-ecuación)
   - 2.10. [Agregar imágenes](#210-agregar-imágenes)
3. [Nota de cambio](#3-nota-de-cambio)
4. [Registro de Control y Firmas](#registro-de-control-y-firmas)

---

## 1. Definición

Este documento se ha elaborado con el fin de ayudar y capacitar a los investigadores principales que realizan la matrícula de proyectos en el Sistema de Información para la Investigación Universitaria – SIIU. Dado lo anterior se aclara que esta guía no hace parte de la normativa universitaria y solamente se debe utilizar como una herramienta que orienta los pasos a seguir.

---

## 2. Contenido

### 2.1 Requisitos para el uso del CKEditor

- El usuario con rol de investigador principal o responsable de proyecto debe contar con acceso a la plataforma SIIU en las secciones de descripción del proyecto.

---

### 2.2 Usuarios que intervienen en el proceso

- **Usuario con rol Investigador Principal o Responsable del Proyecto**.

---

### 2.3 Menú de Opciones del Editor

La barra de herramientas del CKEditor en el SIIU proporciona controles de formato de texto, estilos, tablas, enlaces, imágenes y fórmulas matemáticas.

En la figura 1:
- La opción **1** indica el icono a seleccionar en la barra principal cuando se requiere insertar una fórmula matemática.
- El recuadro **2** destaca los iconos específicos: editor de ecuaciones (`fx`), inserción de imágenes y tablas.

![[VI-GU-25-figura-01.png]]
*Figura 1 – Menú CKEditor*

---

### 2.4 ¿Cómo insertar una ecuación?

Para insertar una ecuación matemática en el texto:
1. Haga clic en el icono **fx** (Editor de Ecuaciones) ubicado en el recuadro número 2 de la barra de herramientas.
2. Se abrirá la ventana emergente modal del **CodeCogs Equation Editor** (Ver figura 2).

![[VI-GU-25-figura-02.png]]
*Figura 2 - Editor de Ecuaciones*

---

### 2.5 Insertar fórmula

Para agregar una ecuación matemática:
1. Elija entre los símbolos matemáticos disponibles en los paneles superiores del editor (operadores, letras griegas, flechas, integrales, sumatorias, relaciones lógicas, etc.).
2. Escriba los números o letras correspondientes a la ecuación. En su mayoría, los argumentos van encerrados entre llaves `{}` en sintaxis LaTeX.
3. En el momento en que se coloca el cursor sobre algún símbolo matemático, el editor muestra un tooltip de ayuda con la sintaxis exacta del comando LaTeX. (Ver figura 3).

![[VI-GU-25-figura-03.png]]
*Figura 3 - Ayuda para escribir ecuaciones*

- **Lista de Funciones**: Se pueden visualizar y seleccionar funciones predefinidas (trigonométricas, hiperbólicas, logaritmos, inversas, etc.) haciendo clic en la lista desplegable **Functions**. (Ver figura 4).

![[VI-GU-25-figura-04.png]]
*Figura 4 - Funciones*

- **Operaciones de Potencia y Exponentes**: Para escribir una operación de potencia (ejemplo: $A^{(x)}$), se utiliza la sintaxis `A^{(x)}` o el botón de superíndice. (Ver figura 5).

![[VI-GU-25-figura-05.png]]
*Figura 5 - Escribir una operación de Potencia*

---

### 2.6 Agregar color a una fórmula

Para aplicar color a partes específicas de una ecuación:
1. Haga clic en la lista desplegable **Colors**.
2. Seleccione el color deseado (por ejemplo, `Red`).
3. El editor aplicará la sintaxis LaTeX correspondiente: `{\color{Red} \sin 65}`. En la previsualización inferior se reflejará el texto coloreado. (Ver figura 6).

![[VI-GU-25-figura-06.png]]
*Figura 6 - Color a las funciones*

---

### 2.7 Agregar espacio a una fórmula

En la sintaxis matemática de LaTeX, los espacios normales no se reflejan automáticamente. Para dejar un espacio visible entre los elementos de una ecuación:
- Se debe colocar una barra invertida con un espacio (`\ `), o
- Hacer clic en el icono de espaciado en la barra de herramientas. (Ver figura 7).

![[VI-GU-25-figura-07.png]]
*Figura 7 - Insertar espacio*

---

### 2.8 Agregar matrices

Para insertar matrices:
1. Haga clic en alguno de los iconos de matriz disponibles en el panel de delimitadores (matrices entre paréntesis, corchetes o barras determinantes). (Ver figura 8).

![[VI-GU-25-figura-08.png]]
*Figura 8 - Insertar matrices*

2. El sistema despliega un mensaje del navegador solicitando ingresar las dimensiones de la matriz:
   - Ingrese las filas y columnas separadas por comas (ejemplo: `2,4` para 2 filas y 4 columnas).
   - Haga clic en **Aceptar**. (Ver figura 9).

![[VI-GU-25-figura-09.png]]
*Figura 9 - Dimensiones de la matriz*

3. El editor genera la estructura LaTeX (por ejemplo, `\begin{vmatrix} ... \end{vmatrix}`).
4. Coloque los valores numéricos o variables en cada posición de la matriz, utilizando `&` para separar columnas y `\\` para saltar de fila.
5. Verifique la previsualización y haga clic en **Aceptar**. (Ver figura 10).

![[VI-GU-25-figura-10.png]]
*Figura 10 - Elementos de la matriz*

---

### 2.9 Editar una ecuación

Para editar una ecuación que ya fue insertada en el cuerpo del texto:
1. Seleccione la ecuación en el área de trabajo.
2. Haga clic derecho sobre ella con el ratón.
3. En el menú contextual, elija **Edit Equation**.
4. Se abrirá nuevamente el editor de ecuaciones con la fórmula cargada para realizar los ajustes necesarios.

---

### 2.10 Agregar imágenes

El CKEditor permite incrustar imágenes en las secciones descriptivas de la propuesta:

1. Presione el icono de **Imagen** en la barra de herramientas.
2. Se abrirá la ventana emergente **Propiedades de Imagen** con las pestañas: *Información de imagen*, *Vínculo*, *Cargar*, *Avanzado*. (Ver figura 11).

![[VI-GU-25-figura-11.png]]
*Figura 11 - Agregar imágenes*

3. Procedimiento para cargar desde el computador:
   - Ingrese a la pestaña **Cargar**.
   - Presione **Seleccionar archivo** y elija la imagen guardada en su equipo (formatos PNG, JPG, GIF).
   - Presione el botón **Enviar al Servidor** (este paso es indispensable para subir la imagen a los servidores de la Universidad).
   - Aparece un mensaje emergente confirmando: *"El archivo se ha cargado correctamente"*; haga clic en **Aceptar**.
   - El sistema retorna a la pestaña *Información de imagen* mostrando la URL interna asignada y la previsualización.
   - Ajuste opcionalmente la anchura, altura, borde, espaciado horizontal/vertical o alineación.
   - Presione **Aceptar**. (Ver figura 12).

![[VI-GU-25-figura-12.png]]
*Figura 12 - Enviar al servidor*

4. La imagen quedará insertada en el área de redacción. Para almacenar los cambios en el SIIU:
   - Presione el botón **Guardar** para continuar editando, o
   - Presione **Guardar y salir** para cerrar el editor y retornar al tren de datos. (Ver figura 13).

![[VI-GU-25-figura-13.png]]
*Figura 13 - Guardar imagen*

---

## 3. Nota de cambio

- No aplica para la primera versión.

---

## Registro de Control y Firmas

| Rol | Nombre | Cargo / Dependencia | Fecha |
| :--- | :--- | :--- | :--- |
| **Elaboró** | Sandra Patricia Zabala Orrego | Contratista, Vicerrectoría Investigación | 04-JUL-2024 |
| **Revisó** | Julio César García Castrillón | Analista de Procesos, División de Arquitectura de Procesos | 09-JUL-2024 |
| **Aprobó** | Gloria Valencia Bustamante | Asistente, Vicerrectoría de Investigación | 12-JUL-2024 |
