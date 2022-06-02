from flask import Flask, request
import model as m
import io
from PIL import Image
import base64
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/",methods=['GET', 'POST'])
# def hello_world():
#     return "<p>Hello, World!</p>"

def predictions():
    if request.method == 'GET':
        return f'<form action="/" method="POST" enctype="multipart/form-data"> <input type="file" name="image"/> <button>Submit</button></form>'
    if request.method == 'POST':
        print("------------We are here-----------")
        occ = request.files["image"]
        filename = secure_filename(occ.filename)
        occ.save(filename)
        preds = m.predict(filename)
        return preds


if __name__ == "__main__":
    app.run()