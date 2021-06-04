from flask import Flask, jsonify
from flask_restful import Api

#from app.common.error_handling import ObjectNotFound, AppErrorBaseClass
from app.git_info.api_v1_0.resources import git_info_v1_0_bp

def create_app(setting_module):
    app = Flask(__name__)
    app.config.from_object(setting_module)

    # Catch all 404 errors
    Api(app, catch_all_404s=True)

    # Deactivate URL strict slashes
    app.url_map.strict_slashes = False

    # Register Blueprint
    app.register_blueprint(git_info_v1_0_bp)

    # Register custom error handlers
    register_error_handlers(app)

    return app

def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_exception_error(e):
        return jsonify({'msg': 'Internal server error'}), 500

    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify({'msg': 'Method not allowed'}), 405

    @app.errorhandler(403)
    def handle_403_error(e):
        return jsonify({'msg': 'Forbidden error'}), 403

    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify({'msg': 'Not found error'}), 404