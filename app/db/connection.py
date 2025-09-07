import pymysql
from app.utils.logger import logger
from app.utils.exception import CEMSException

def get_db_connection():
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="Sanvith@12345",
            database="DBCollege",
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        raise CEMSException("Database connection error", 500)
