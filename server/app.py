import io
import numpy as np
from PIL import Image
import base64
from flask import Flask, jsonify
from flask import request
import tensorflow_hub as hub
import tensorflow as tf
app = Flask(__name__)


def tensor_to_image(tensor):
    tensor = tensor*255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor) > 3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
    return Image.fromarray(tensor)


@app.route("/", methods=['GET', 'POST', 'OPTIONS'])
def index():
    image = base64.b64decode(request.json.get('img'))
    image = np.array(Image.open(io.BytesIO(image)))
    print(image.shape)
    return base64.b64encode(image)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
