import sqlite3
import pandas as pd
from datetime import datetime

DB_NAME = "yumpick_log.db"

def init_db():
    """DB가 없으면 새로 만듭니다."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS user_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            city TEXT,
            weather TEXT,
            temp REAL,
            recommended_menu TEXT,
            reaction TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_log(city, weather, temp, menu, reaction):
    """추천 기록을 저장합니다."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO user_logs (timestamp, city, weather, temp, recommended_menu, reaction) VALUES (?, ?, ?, ?, ?, ?)",
              (now, city, weather, temp, menu, reaction))
    conn.commit()
    conn.close()

def get_all_logs():
    """저장된 모든 기록을 가져옵니다 (관리자용)."""
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql("SELECT * FROM user_logs", conn)
    conn.close()
    return df