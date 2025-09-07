from flask import Blueprint, jsonify
from app.db.connection import get_db_connection
from app.utils.logger import logger
from app.utils.exception import CEMSException

reports_bp = Blueprint("reports", __name__)

# Registrations Report
@reports_bp.route("/registrations", methods=["GET"])
def registrations_report():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT e.title, COUNT(r.user_id) AS total_registrations
            FROM events e
            LEFT JOIN attendance r ON e.event_id = r.event_id
            GROUP BY e.event_id
        """)
        columns = [desc[0] for desc in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        logger.error(f"Failed to fetch registrations report: {e}")
        raise CEMSException("Unable to fetch registrations report", 500)

# Attendance Report
@reports_bp.route("/attendance", methods=["GET"])
def attendance_report():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT e.title,
                   ROUND(SUM(CASE WHEN a.user_id IS NOT NULL THEN 1 ELSE 0 END)/COUNT(u.user_id)*100,2) AS attendance_percentage
            FROM events e
            CROSS JOIN users u
            LEFT JOIN attendance a ON e.event_id = a.event_id AND u.user_id = a.user_id
            GROUP BY e.event_id
        """)
        columns = [desc[0] for desc in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        logger.error(f"Failed to fetch attendance report: {e}")
        raise CEMSException("Unable to fetch attendance report", 500)

# Top Students
@reports_bp.route("/top-students", methods=["GET"])
def top_students_report():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT u.name, COUNT(a.event_id) AS events_participated
            FROM users u
            JOIN attendance a ON u.user_id = a.user_id
            WHERE u.role='STUDENT'
            GROUP BY u.user_id
            ORDER BY events_participated DESC
            LIMIT 5
        """)
        columns = [desc[0] for desc in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        logger.error(f"Failed to fetch top students report: {e}")
        raise CEMSException("Unable to fetch top students report", 500)
