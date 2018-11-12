import numpy as np
from flask import (
    current_app,
    Blueprint,
    jsonify,
    make_response,
    request
)
from util import predict_model

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/predict', methods=['POST'])
def predict():
    payload = request.get_json()['payload']
    data = process_data(payload)
    np_array = np.expand_dims(data, 0)

    with predict_model(current_app.model, np_array) as pred:
        if pred is None:
            return jsonify({'error': 'Model cannot predict with input'})
        else:
            return jsonify({'result': pred[0]})


def process_data(payload):
    data = [
        payload['Pclass'],
        payload['is_male'],
        payload['Age'],
        payload['Fare'],
        payload['family_size'],
        payload['has_cabin'],
        payload['Embarked_C'],
        payload['Embarked_Q'],
        payload['Embarked_S']
    ]
    return data

