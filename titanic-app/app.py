from flask import (
    Flask,
    jsonify,
    make_response
)
from prediction import main_blueprint
from util import read_model_from_pickle


def create_app():
    app = Flask(__name__)
    app.model = read_model_from_pickle('model.pkl')
    app.register_blueprint(main_blueprint, url_prefix='/api/v1')

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error':'Not found'}), 404)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
