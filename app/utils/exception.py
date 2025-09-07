from flask import jsonify

class CEMSException(Exception):
    """Custom exception for CEMS"""
    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.status_code = status_code

def register_error_handlers(app):
    @app.errorhandler(CEMSException)
    def handle_cems_exception(e):
        return jsonify({"error": str(e)}), e.status_code

    @app.errorhandler(404)
    def handle_404(e):
        return jsonify({"error": "Resource not found"}), 404

    @app.errorhandler(500)
    def handle_500(e):
        return jsonify({"error": "Internal server error"}), 500
