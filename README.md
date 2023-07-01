# ML_Calculadora_Valor_inmuebles_BOG

Aplicativo creado utilizando datos extraidos de bases de datos del DANE y de datos abiertos del gobierno colombiano, con el cual se ha entrenado un modelo de Machine Learning que permite predecir los valores aproximados de Inmuebles tipo casas y apartamentos segun el sector donde se encuentre y caracteristicas como número de habitaciones, número de baños y Área del predio.

El modelo de Machine Learning fue creado con la técnica de Regresión linear múltiple, utilizando librerias como Pandas, SkLearn y Numpy en Python y la Api web con el framework Flask y html.

Este repositorio contiene: 

Master Branch:

   1. Carpera ML-Project:
      
      1.1. Archivos del aplicativo web.

         Archivo index.py (Aplicativo)
      
         Carpeta templates (Templates html de la interfaz del aplicativo)
      
         Archivo pkl con el modelo entrenado.
      
   3. Archivo cuaderno de google colab con todo el procesamiento de los datos y entrenamiento del modelo de MachineLearning. 
   4. Requirements.txt

Main Branch:

   1. Sitio Web Estatico (Sin funcionalidad). 


Desarrollado por: Mario Acendra Retamozo  


------------------------------------------------------------------------------------------------------------------------------------------

#Para Ejecutar la App Web:

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


