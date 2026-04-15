import psycopg2
from datetime import datetime


class DBClient:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="surge_db",
            user="postgres",
            password="password"
        )
        self.cursor = self.conn.cursor()

    # -------------------------------
    # CREATE TABLE (US-013)
    # -------------------------------
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS surge_pricing (
            id SERIAL PRIMARY KEY,
            zone VARCHAR(50),
            demand INT,
            supply INT,
            surge_multiplier FLOAT,
            timestamp TIMESTAMP
        );
        """
        self.cursor.execute(query)
        self.conn.commit()

    # -------------------------------
    # INSERT DATA (US-013)
    # -------------------------------
    def insert_record(self, zone, demand, supply, surge_multiplier):
        query = """
        INSERT INTO surge_pricing (zone, demand, supply, surge_multiplier, timestamp)
        VALUES (%s, %s, %s, %s, %s);
        """
        self.cursor.execute(query, (
            zone,
            demand,
            supply,
            surge_multiplier,
            datetime.now()
        ))
        self.conn.commit()

    # -------------------------------
    # GET ALL RECORDS (US-014)
    # -------------------------------
    def get_all_records(self):
        query = "SELECT * FROM surge_pricing;"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    # -------------------------------
    # GET RECORDS BY ZONE (US-014)
    # -------------------------------
    def get_records_by_zone(self, zone):
        query = """
        SELECT * FROM surge_pricing
        WHERE zone = %s;
        """
        self.cursor.execute(query, (zone,))
        return self.cursor.fetchall()

    # -------------------------------
    # GET RECENT RECORDS (US-014)
    # -------------------------------
    def get_recent_records(self):
        query = """
        SELECT * FROM surge_pricing
        WHERE timestamp >= NOW() - INTERVAL '10 minutes';
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    # -------------------------------
    # CLOSE CONNECTION
    # -------------------------------
    def close(self):
        self.cursor.close()
        self.conn.close()


# -------------------------------
# TEST BLOCK (OPTIONAL)
# -------------------------------
if __name__ == "__main__":
    db = DBClient()
    db.create_table()

    # Insert sample data
    db.insert_record("zone_1", 10, 5, 2.0)

    # Fetch data
    print("All Records:", db.get_all_records())
    print("Zone Records:", db.get_records_by_zone("zone_1"))
    print("Recent Records:", db.get_recent_records())

    db.close()