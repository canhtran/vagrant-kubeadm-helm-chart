import pickle
import numpy as np
from flask import (
    Flask,
    jsonify,
    request
)


app = Flask(__name__)
with open('model.pkl', 'rb') as handle:
    app.model = pickle.load(handle,  encoding='latin1')


@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    return 'ok'


@app.route('/predict', methods=['POST'])
def predict():
    payload = request.get_json()
    np_array = np.expand_dims(list(payload.values()), 0)

    pred = app.model.predict(np_array)
    if pred is None:
        return jsonify({'error': 'Model cannot predict with input'})
    else:
        return jsonify({'result': str(pred[0])})


if __name__ == "__main__":
    app.run()
