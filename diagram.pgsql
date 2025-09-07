+-------------+         +-------------+
|   College   |1------< |   Student   |
|-------------|         |-------------|
| college_id PK|         | student_id PK|
| name         |         | name          |
+-------------+         | college_id FK |
                        +-------------+
                               |
                               | many
                               |
                               v
                         +-------------+
                         |   Event     |
                         |-------------|
                         | event_id PK |
                         | name        |
                         | type        |
                         | date        |
                         | college_id FK|
                         +-------------+
                               |
        +----------------------+-------------------+
        |                                          |
        v                                          v
+------------------+                       +-----------------+
|  Registration    |                       |   Attendance    |
|------------------|                       |-----------------|
| reg_id PK        |                       | att_id PK       |
| student_id FK    |                       | student_id FK   |
| event_id FK      |                       | event_id FK     |
| timestamp        |                       | status          |
+------------------+                       | checkin_time    |
                                           +-----------------+
                                                    |
                                                    v
                                           +-----------------+
                                           |   Feedback      |
                                           |-----------------|
                                           | fb_id PK        |
                                           | student_id FK   |
                                           | event_id FK     |
                                           | rating (1–5)    |
                                           | comment         |
                                           +-----------------+
