from flask import Blueprint, request, jsonify
from app.db.connection import get_db_connection
from app.utils.logger import logger
from app.utils.exception import CEMSException

attendance_bp = Blueprint("attendance", __name__)

# Mark Attendance
@attendance_bp.route("/mark", methods=["POST"])
def mark_attendance():
    try:
        data = request.get_json()
        user_id = data.get("user_id")
        event_id = data.get("event_id")

        if not all([user_id, event_id]):
            return jsonify({"status": "error", "message": "user_id and event_id are required"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO attendance (user_id, event_id) VALUES (%s, %s)",
            (user_id, event_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"status": "success", "message": "Attendance marked"})
    except Exception as e:
        logger.error(f"Failed to mark attendance: {e}")
        raise CEMSException("Unable to mark attendance", 500)
