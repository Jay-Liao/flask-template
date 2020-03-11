from flask import Flask, Blueprint
from web_app.api.restplus import api
from web_app.api.task.route import tasks_namespace


def create_app(testing=False):
    a_flask_app = Flask(__name__)
    a_flask_app.config["SWAGGER_UI_DOC_EXPANSION"] = "list"
    a_flask_app.config["RESTPLUS_VALIDATE"] = True
    a_flask_app.config["RESTPLUS_MASK_SWAGGER"] = False
    # a_flask_app.config['ERROR_404_HELP'] = False
    if testing:
        a_flask_app.config["TESTING"] = True
        a_flask_app.config["WTF_CSRF_ENABLED"] = False
        a_flask_app.config["DEBUG"] = False
    blueprint = Blueprint("api", __name__, url_prefix="/api")
    api.init_app(blueprint)
    api.add_namespace(tasks_namespace)
    a_flask_app.register_blueprint(blueprint)
    return a_flask_app


if __name__ == "__main__":
    app = create_app()
    app.run(host="127.0.0.1", port=9453, debug=True)
