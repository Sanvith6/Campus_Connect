from flask import Blueprint, jsonify
from app.db.connection import get_db_connection

users_bp = Blueprint("users", __name__)

@users_bp.route("/list", methods=["GET"])
def list_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, name, email, role, contact, department FROM users")
    columns = [desc[0] for desc in cursor.description]
    data = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return jsonify({"status": "success", "data": data})
