# app/__init__.py
from flask import Flask, jsonify
from app.utils.exception import CEMSException

def create_app():
    app = Flask(__name__)

    # Import blueprints
    from app.routes.users import users_bp
    from app.routes.events import events_bp
    from app.routes.registrations import registrations_bp
    from app.routes.feedback import feedback_bp
    from app.routes.attendance import attendance_bp
    from app.routes.reports import reports_bp

    # Register blueprints with URL prefixes
    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(events_bp, url_prefix="/events")
    app.register_blueprint(registrations_bp, url_prefix="/registrations")
    app.register_blueprint(feedback_bp, url_prefix="/feedback")
    app.register_blueprint(attendance_bp, url_prefix="/attendance")
    app.register_blueprint(reports_bp, url_prefix="/reports")

    # Global CEMSException handler
    @app.errorhandler(CEMSException)
    def handle_cems_exception(error):
        response = jsonify({
            "status": "error",
            "message": str(error),                # Convert exception to string
            "code": getattr(error, "code", 500)  # Default to 500 if no code
        })
        response.status_code = getattr(error, "code", 500)
        return response

    # Optional: handle 404 errors globally
    @app.errorhandler(404)
    def handle_404(error):
        return jsonify({"status": "error", "message": "Endpoint not found"}), 404

    # Optional: handle 500 errors globally
    @app.errorhandler(500)
    def handle_500(error):
        return jsonify({"status": "error", "message": "Internal server error"}), 500

    return app
