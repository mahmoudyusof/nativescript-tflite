import io
import numpy as np
from PIL import Image
import base64
from flask import Flask, jsonify
from flask import request
import tensorflow_hub as hub
import tensorflow as tf

app = Flask(__name__)


hub_module = hub.load(
    'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/1')


def tensor_to_image(tensor):
    tensor = tensor*255
    tensor = np.array(tensor, dtype=np.uint8)
    print(tensor.shape)
    if np.ndim(tensor) > 3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
    return Image.fromarray(tensor)


def read_img(img):
    max_dim = 512
    img = tf.cast(np.array(img), tf.float32)

    shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    long_dim = max(shape)
    scale = max_dim / long_dim

    new_shape = tf.cast(shape * scale, tf.int32)

    img = tf.image.resize(img, new_shape)
    img = img[tf.newaxis, :]
    return img


def load_img(path_to_img):
    max_dim = 512
    img = tf.io.read_file(path_to_img)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)

    shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    long_dim = max(shape)
    scale = max_dim / long_dim

    new_shape = tf.cast(shape * scale, tf.int32)

    img = tf.image.resize(img, new_shape)
    img = img[tf.newaxis, :]
    return img


@app.route("/", methods=['GET', 'POST', 'OPTIONS'])
def index():
    input_image = base64.b64decode(request.json.get('img'))
    content = read_img(Image.open(io.BytesIO(input_image)))

    style = load_img('style.png')

    stylized_image = hub_module(tf.constant(content), tf.constant(style))[0]
    output_img = tensor_to_image(stylized_image)

    buffer = io.BytesIO()
    output_img.save(buffer, format="JPEG")
    response = base64.b64encode(buffer.getvalue())
    
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
