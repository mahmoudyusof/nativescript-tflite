import io
import numpy as np
from PIL import Image
import base64
from flask import Flask, jsonify
from flask import request
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST', 'OPTIONS'])
def index():
    image = base64.b64decode(request.json.get('img'))
    image = np.array(Image.open(io.BytesIO(image)))
    print(image.shape)
    return "hi"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
