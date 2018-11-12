from flask import Blueprint


heartbeat_blueprint = Blueprint('heartbeat', __name__)


@heartbeat_blueprint.route('/heartbeat', methods=['GET'])
def get_heartbeat_api():
    return 'ok'

