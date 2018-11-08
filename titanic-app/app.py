import numpy as np
from flask import (
  current_app,
  Blueprint,
  jsonify,
  make_reponse,
  request
)

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/predict', methods=['POST'])
def predict():
    payload = req.get_json()['payload']
    data = process_data(payload)
    np_array = np.expend_dims(data, 0)

    with predict_model(model, np_arry) as pred
      if pred is None:
          return jsonify({'error': 'Model cannot predict with input'})
      else
        return jsonify({'result': pred[0]})
