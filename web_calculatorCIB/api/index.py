from flask import Flask, render_template, request
from sklearn.preprocessing import PolynomialFeatures
# from ml_script import predict_value
# import pickle
import joblib
import json

import os
from pprint import pprint


# Obtener la ruta al directorio del script
script_dir = os.path.dirname(os.path.abspath(__file__))
modelo_path = os.path.join(script_dir, 'modelo.pkl')
json_patch = os.path.join(script_dir,'listado_upz.json')

print("Ruta completa al modelo:", modelo_path)
 
app=Flask(__name__)
try:
    model = joblib.load(modelo_path)
except Exception as e:
    print("Error al cargar el modelo:", str(e))

with open(json_patch,'r') as archivo:
 upz_list=json.load(archivo)

@app.route('/')
def home():

  return render_template('index.html', upz_list=upz_list)

@app.route('/predecir', methods={'POST'})
def predecir():
  upz=int(request.form['upz'])
  area=int(request.form['area'])
  habitaciones=int(request.form['habitaciones'])
  banos=int(request.form['banos'])
  tipo=int(request.form['tipo'])

  poly = PolynomialFeatures(degree=2)

  Xpred=[[habitaciones,banos,area,upz,tipo]]

  Xpred=poly.fit_transform(Xpred)

  prediccion=model.predict(Xpred)

  prediccion=round(prediccion[0],2)
  
  return render_template('index.html', prediccion_text=f'<div class="alert alert-success" role="alert"><h4 class="alert-heading">¡Calculo realizado!</h4><p> El valor aproximado para un inmueble con esas caracteristicas es de: {prediccion} millones de pesos.</p></div></div>', upz_list=upz_list)


@app.route('/about')
def about():
  return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
