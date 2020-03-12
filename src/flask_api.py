from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from predictions import prediction_pose
import os

app = Flask(__name__, static_folder='./templates/')


# instancia del objeto Flask
app.config['UPLOAD_FOLDER'] = './real_pics'


@app.route("/")
def upload_file():
    # devolvemos la plantilla "index.html"
    return render_template('index.html')


@app.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        f = request.files["file"]
        print(f)
        filename = secure_filename(f.filename)
        # Guardamos el archivo en el directorio "Archivos PDF"
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Retornamos una respuesta satisfactoria con la predicción
        prediction = prediction_pose(os.path.join(
            app.config['UPLOAD_FOLDER'], filename))
        return render_template("pred.html", prediction=prediction)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, threaded=False, debug=True)
