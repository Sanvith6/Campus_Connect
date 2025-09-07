# run.py
from flask import Flask
from app.routes.users import users_bp
from app.routes.events import events_bp
from app.routes.attendance import attendance_bp
from app.routes.feedback import feedback_bp
from app.routes.reports import reports_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(events_bp, url_prefix="/events")
app.register_blueprint(attendance_bp, url_prefix="/attendance")
app.register_blueprint(feedback_bp, url_prefix="/feedback")
app.register_blueprint(reports_bp, url_prefix="/reports")

if __name__ == "__main__":
    # Debug=True will auto reload when you change backend code
    app.run(host="127.0.0.1", port=5000, debug=True)
