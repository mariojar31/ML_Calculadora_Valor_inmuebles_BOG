# ML_Calculadora_Valor_inmuebles_BOG

Aplicativo creado utilizando datos extraidos de bases de datos del DANE y de datos abiertos del gobierno colombiano, con el cual se ha entrenado un modelo de Machine Learning que permite predecir los valores aproximados de Inmuebles tipo casas y apartamentos segun el sector donde se encuentre y caracteristicas como número de habitaciones, número de baños y Área del predio.

El modelo de Machine Learning fue creado con la técnica de Regresión linear múltiple, utilizando librerias como Pandas, SkLearn y Numpy en Python y la Api web con el framework Flask y html.

Este repositorio contiene: 

Main Branch:
1. Cuaderno de Google Colab con todo el proceso de limpieza de datos, preparación de la vista mineable y entrenamiento y prueba del modelo.
2. Sitio Web Estatico (Sin funcionalidad). 

Master Branch:
1. Archivos Py y html del aplicativo web.
2. Archivo pkl con el modelo entrenado.

Desarrollado por: Mario Acendra Retamozo  


------------------------------------------------------------------------------------------------------------------------------------------

##Para Ejecutar la App Web:

1) Descargar los archivos en tu ordenador.
2) Crear un entorno virtual con venv, puedes hacerlo de la siguiente forma:
   Desde la consola de PowerShell:

   Abre la consola de WindowsPowerShell desde windows. Esto lo puedes hacer desde la consola de sistema, tecleando 'powershell'.

   Para crear un entorno virtual, ingresa al directorio del proyecto y ejecuta el módulo venv como script con la ruta a la carpeta:

      python -m venv myvenv

   Luego, activa el entorno virtual con el comando "activate"

   Después de esto, ejecuta el siguiente comando para instalar los requerimientos en tu entorno:

     pip install -r requirements.txt

4) Luego, puedes ejecutar el archivo index.py desde la consola ejecutando el siguiente comando:

    python index.py

   Recuerda que debes estar en el directorio del proyecto. 


