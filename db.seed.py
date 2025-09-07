import pymysql
from datetime import datetime

# ---- DB connection ----
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="Sanvith@12345",  # replace with your MySQL password
    database="DBCollege"
)
cursor = conn.cursor()

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ---- USERS ----
users = [
    ("f6bdf8c0-8b1b-11f0-bfa6-b44506d8ec7f","Alice","alice@college.edu","FACULTY","9123456780","Computer Science"),
    ("f6bdff0e-8b1b-11f0-bfa6-b44506d8ec7f","Bob","bob@college.edu","FACULTY","9123456781","Arts"),
    ("f6bdffff-8b1b-11f0-bfa6-b44506d8ec7f","Charlie","charlie@college.edu","FACULTY","9123456782","Engineering"),
    ("f6be006a-8b1b-11f0-bfa6-b44506d8ec7f","David","david@college.edu","FACULTY","9123456783","Engineering"),
    ("f6be00f0-8b1b-11f0-bfa6-b44506d8ec7f","Eva","eva@college.edu","FACULTY","9123456784","Arts"),
    ("f6be01ad-8b1b-11f0-bfa6-b44506d8ec7f","Frank","frank@college.edu","FACULTY","9123456785","Arts"),
    ("f6be0210-8b1b-11f0-bfa6-b44506d8ec7f","Grace","grace@college.edu","FACULTY","9123456786","Engineering"),
    ("f6be02b1-8b1b-11f0-bfa6-b44506d8ec7f","Hannah","hannah@college.edu","FACULTY","9123456787","Sports"),
    ("f6be0382-8b1b-11f0-bfa6-b44506d8ec7f","Ian","ian@college.edu","FACULTY","9123456788","Civil"),
    ("f6be0429-8b1b-11f0-bfa6-b44506d8ec7f","Jack","jack@college.edu","FACULTY","9123456789","Computer Science"),
    ("f6be04bb-8b1b-11f0-bfa6-b44506d8ec7f","Aarav Sharma","aarav@student.college.edu","STUDENT","9001002001","Computer Science"),
    ("f6be056b-8b1b-11f0-bfa6-b44506d8ec7f","Priya Mehta","priya@student.college.edu","STUDENT","9001002002","Arts"),
    ("f6be062d-8b1b-11f0-bfa6-b44506d8ec7f","Rohan Verma","rohan@student.college.edu","STUDENT","9001002003","Engineering"),
    ("f6be06ca-8b1b-11f0-bfa6-b44506d8ec7f","Sneha Kapoor","sneha@student.college.edu","STUDENT","9001002004","Arts"),
    ("f6be075a-8b1b-11f0-bfa6-b44506d8ec7f","Aditya Singh","aditya@student.college.edu","STUDENT","9001002005","Engineering"),
    ("f6be07c2-8b1b-11f0-bfa6-b44506d8ec7f","Neha Gupta","neha@student.college.edu","STUDENT","9001002006","Computer Science"),
    ("f6be0823-8b1b-11f0-bfa6-b44506d8ec7f","Vikram Rao","vikram@student.college.edu","STUDENT","9001002007","Arts"),
    ("f6be088f-8b1b-11f0-bfa6-b44506d8ec7f","Isha Patel","isha@student.college.edu","STUDENT","9001002008","Engineering"),
    ("f6be0909-8b1b-11f0-bfa6-b44506d8ec7f","Karan Malhotra","karan@student.college.edu","STUDENT","9001002009","Computer Science"),
    ("f6be0980-8b1b-11f0-bfa6-b44506d8ec7f","Ananya Nair","ananya@student.college.edu","STUDENT","9001002010","Arts")
]

for u in users:
    cursor.execute("""
        INSERT IGNORE INTO users (user_id, name, email, role, contact, department, created_at)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (*u, now))

# ---- VENUES ----
venues = [
    ("ffa3bf36-8b1b-11f0-bfa6-b44506d8ec7f","Auditorium A","Block A, 1st Floor",100),
    ("ffa4bd38-8b1b-11f0-bfa6-b44506d8ec7f","Auditorium B","Block B, 1st Floor",150),
    ("ffa4beb5-8b1b-11f0-bfa6-b44506d8ec7f","Auditorium C","Block C, 1st Floor",120),
    ("ffa4bf20-8b1b-11f0-bfa6-b44506d8ec7f","Open Grounds","Main Campus Open Area",500),
    ("ffa4bf82-8b1b-11f0-bfa6-b44506d8ec7f","Sports Ground","Sports Complex",200),
    ("ffa4bfe7-8b1b-11f0-bfa6-b44506d8ec7f","Lab Complex","Engineering Labs",80),
    ("ffa4c0f2-8b1b-11f0-bfa6-b44506d8ec7f","Innovation Center","Tech Hub",120),
    ("ffa4c1bf-8b1b-11f0-bfa6-b44506d8ec7f","Main Hall","Arts Block",250),
    ("ffa4c231-8b1b-11f0-bfa6-b44506d8ec7f","Athletics Ground","Sports Complex",400),
    ("ffa4c294-8b1b-11f0-bfa6-b44506d8ec7f","Civil Block","Civil Engineering Dept",100)
]

for v in venues:
    cursor.execute("""
        INSERT IGNORE INTO venues (venue_id, name, location, capacity, created_at)
        VALUES (%s,%s,%s,%s,%s)
    """, (*v, now))

# ---- SAMPLE EVENTS ----
events = [
    ("e1a2b3c4-1111-4444-8888-abcdef123456","Workshop on AI","ffa3bf36-8b1b-11f0-bfa6-b44506d8ec7f","2025-09-10"),
    ("e2b2c3d4-2222-5555-9999-fedcba654321","Sports Meet","ffa4bf82-8b1b-11f0-bfa6-b44506d8ec7f","2025-09-12"),
    ("e3c3d4e5-3333-6666-aaaa-bcdef123987","Tech Fest","ffa4c0f2-8b1b-11f0-bfa6-b44506d8ec7f","2025-09-15")
]

for e in events:
    cursor.execute("""
        INSERT IGNORE INTO events (event_id, title, venue_id, date, created_at)
        VALUES (%s,%s,%s,%s,%s)
    """, (*e, now))

# ---- COMMIT & CLOSE ----
conn.commit()
cursor.close()
conn.close()
print("DB seeded successfully ✅")
