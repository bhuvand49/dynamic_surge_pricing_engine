import psycopg2
from psycopg2 import sql
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

    def close(self):
        self.cursor.close()
        self.conn.close()


# Test run (optional)
if __name__ == "__main__":
    db = DBClient()
    db.create_table()
    db.insert_record("zone_1", 10, 5, 2.0)
    db.close()