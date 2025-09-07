from flask import Blueprint, request, jsonify
from app.db.connection import get_db_connection
from app.utils.logger import logger
from app.utils.exception import CEMSException
import uuid

events_bp = Blueprint("events", __name__)

# Add Event
@events_bp.route("/add", methods=["POST"])
def add_event():
    try:
        data = request.get_json()
        title = data.get("title")
        date = data.get("date")
        location_id = data.get("location_id")

        if not all([title, date, location_id]):
            return jsonify({"status": "error", "message": "title, date, and location_id are required"}), 400

        event_id = str(uuid.uuid4())
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO events (event_id, title, date, location_id) VALUES (%s, %s, %s, %s)",
            (event_id, title, date, location_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"status": "success", "event_id": event_id, "message": "Event added successfully"})
    except Exception as e:
        logger.error(f"Failed to add event: {e}")
        raise CEMSException("Unable to add event", 500)

# List Events
@events_bp.route("/list", methods=["GET"])
def list_events():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT event_id, title, date, location_id FROM events")
        columns = [desc[0] for desc in cursor.description]
        events = [dict(zip(columns, row)) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return jsonify({"status": "success", "data": events})
    except Exception as e:
        logger.error(f"Failed to fetch events: {e}")
        raise CEMSException("Unable to fetch events", 500)
