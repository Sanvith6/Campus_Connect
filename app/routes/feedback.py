from flask import Blueprint, request, jsonify
from app.db.connection import get_db_connection
from app.utils.logger import logger
from app.utils.exception import CEMSException

feedback_bp = Blueprint("feedback", __name__)

# Submit Feedback
@feedback_bp.route("/submit", methods=["POST"])
def submit_feedback():
    try:
        data = request.get_json()
        user_id = data.get("user_id")
        event_id = data.get("event_id")
        rating = data.get("rating")

        if not all([user_id, event_id, rating]):
            return jsonify({"status": "error", "message": "user_id, event_id and rating are required"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO feedback (user_id, event_id, rating) VALUES (%s, %s, %s)",
            (user_id, event_id, rating)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"status": "success", "message": "Feedback submitted"})
    except Exception as e:
        logger.error(f"Failed to submit feedback: {e}")
        raise CEMSException("Unable to submit feedback", 500)
