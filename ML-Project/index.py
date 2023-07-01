from flask import Flask, render_template, request
from sklearn.preprocessing import PolynomialFeatures
# from ml_script import predict_value
# import pickle
import joblib
 
app=Flask(__name__)
model=joblib.load('modelo_entrenado.pkl')

@app.route('/')
def home():
  return render_template('index.html')

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
  
  return render_template('index.html', prediccion_text=f'<div class="alert alert-success" role="alert"><h4 class="alert-heading">¡Calculo realizado!</h4><p> El valor aproximado para un inmueble con esas caracteristicas es de: {prediccion} millones de pesos.</p></div></div>')


@app.route('/about')
def about():
  return render_template('about.html')


if __name__ == '__main__':
  app.run()
