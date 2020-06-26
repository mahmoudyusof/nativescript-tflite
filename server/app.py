from flask import Flask
from flask import request
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST', 'OPTIONS'])
def index():
    print(request.form)
    print(request.data)
    print(request.json)
    print(request.values)
    return "Hi"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
