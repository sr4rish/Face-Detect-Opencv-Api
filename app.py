from flask import Flask, request, jsonify
from detectFaces import detectFaces

app = Flask(__name__)

@app.route('/image/', methods=['POST'])
def detect():
    imgUrl = request.json['imgUrl']
    faces = detectFaces(imgUrl)
    response = jsonify(faces)
    return response


if __name__ == "__main__":
    app.run()