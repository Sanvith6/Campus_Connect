# test.api.py
import requests

BASE_URL = "http://127.0.0.1:5000"

# Sample Users (already seeded, so we use their user_ids)
students = [
    "f6be04bb-8b1b-11f0-bfa6-b44506d8ec7f",  # Aarav Sharma
    "f6be056b-8b1b-11f0-bfa6-b44506d8ec7f"   # Priya Mehta
]
faculty = [
    "f6bdf8c0-8b1b-11f0-bfa6-b44506d8ec7f",  # Alice
    "f6bdff0e-8b1b-11f0-bfa6-b44506d8ec7f"   # Bob
]

# Sample Events (already seeded)
events = [
    {"title": "Tech Talk", "date": "2025-09-10", "location_id": "ffa3bf36-8b1b-11f0-bfa6-b44506d8ec7f"},
    {"title": "Art Workshop", "date": "2025-09-11", "location_id": "ffa4bd38-8b1b-11f0-bfa6-b44506d8ec7f"}
]

def add_events():
    print("Adding Events:")
    for e in events:
        resp = requests.post(f"{BASE_URL}/events/add", json=e)
        print(e["title"], resp.json())

def get_event_ids():
    import pymysql
    from app.db.connection import get_db_connection  # assuming same as app
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT event_id FROM events")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    # if DictCursor is used
    event_ids = [row['event_id'] for row in rows]
    return event_ids

def mark_attendance(event_ids):
    print("\nMarking Attendance:")
    for uid in students + faculty:
        for eid in event_ids:
            data = {"user_id": uid, "event_id": eid}
            resp = requests.post(f"{BASE_URL}/attendance/mark", json=data)
            print(uid, eid, resp.json())

def submit_feedback(event_ids):
    print("\nSubmitting Feedback:")
    ratings = [4, 5]  # Sample ratings
    for uid in students:
        for i, eid in enumerate(event_ids):
            data = {"user_id": uid, "event_id": eid, "rating": ratings[i % len(ratings)]}
            resp = requests.post(f"{BASE_URL}/feedback/submit", json=data)
            print(uid, eid, resp.json())

def generate_reports():
    print("\nGenerating Reports:")

    reports = ["registrations", "attendance", "feedback", "top-students"]
    for r in reports:
        resp = requests.get(f"{BASE_URL}/reports/{r}")
        print(r, resp.json())

if __name__ == "__main__":
    add_events()
    event_ids = get_event_ids()
    mark_attendance(event_ids)
    submit_feedback(event_ids)
    generate_reports()
