from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import predictions as P
import os

app = Flask(__name__, static_folder='./templates/')


# instancia del objeto Flask
app.config['UPLOAD_FOLDER'] = 'imagenes_web'


@app.route("/")
def upload_file():
    # devolvemos la plantilla "index.html"
    return render_template('index.html')


@app.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        f = request.files["file"]
        filename = secure_filename(f.filename)
        # Guardamos el archivo en el directorio "Archivos PDF"
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Retornamos una respuesta satisfactoria con la predicción
        prediction, probability = P.prediction_pose(os.path.join(
            app.config['UPLOAD_FOLDER'], filename))
        print(prediction)
        return render_template("pred.html", prediction=prediction, probability = probability)


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000, threaded=False)