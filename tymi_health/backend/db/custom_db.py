import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "../tymi_health.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create patients table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        address TEXT,
        phone TEXT,
        weight REAL,
        height REAL,
        bp TEXT,
        allergies TEXT,
        symptoms TEXT,
        triage_status TEXT,
        recommendation TEXT,
        illness TEXT,
        scan_reports TEXT,
        medicines TEXT,
        nutrition TEXT,
        hydration TEXT,
        rest TEXT,
        avoid TEXT,
        special_notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Insert sample patient if table is empty
    cursor.execute("SELECT COUNT(*) FROM patients")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
        INSERT INTO patients (name, age, address, phone, weight, height, bp, allergies, symptoms, triage_status, recommendation)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            "Mihitha",
            18,
            "No.51, RDA Quarters, Hawaeliya, Nuwara Eliya, Sri Lanka",
            "0777358470",
            65.0,
            170.0,
            "120/80",
            "None",
            "Headache",
            "Green",
            "Rest and monitor temperature."
        ))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print(f"Database initialized at {DB_PATH}")
