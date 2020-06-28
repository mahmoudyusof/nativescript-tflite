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
    input_image = base64.b64decode(request.json.get('img'))
    input_array = np.array(Image.open(io.BytesIO(input_image)))
    output_img = Image.fromarray(input_array, 'RGB')
    buffer = io.BytesIO()
    output_img.save(buffer, format="JPEG")
    response = base64.b64encode(buffer.getvalue())
    print(request.json.get('img')[:20])
    print(str(response[:20]))
    return request.json.get('img')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
