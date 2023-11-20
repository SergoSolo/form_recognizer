from flask import Flask, jsonify, request

from core import load_data_to_db, logger_config  # isort: skip
from utils import find_matching_template  # isort: skip

app = Flask(__name__)


@app.route("/get_form", methods=["POST"])
def hello_world():
    return jsonify(find_matching_template(request.args))


if __name__ == "__main__":
    logger_config()
    load_data_to_db()
    app.run(host='0.0.0.0')
