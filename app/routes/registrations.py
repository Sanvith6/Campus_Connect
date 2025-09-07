from flask import Blueprint, jsonify
from app.db.connection import get_db_connection
from app.utils.logger import logger
from app.utils.exception import CEMSException

registrations_bp = Blueprint("registrations", __name__)

@registrations_bp.route("/list", methods=["GET"])
def list_registrations():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT r.registration_id, u.name AS student_name, e.title AS event_title
            FROM registrations r
            LEFT JOIN users u ON r.student_id = u.user_id
            LEFT JOIN events e ON r.event_id = e.event_id
        """)
        registrations = cursor.fetchall()
        conn.close()

        logger.info(f"Fetched {len(registrations)} registrations successfully.")
        return jsonify({
            "status": "success",
            "data": registrations,
            "count": len(registrations)
        })
    except Exception as e:
        logger.error(f"Failed to fetch registrations: {str(e)}")
        raise CEMSException("Unable to fetch registrations data", 500)
