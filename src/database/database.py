"""
SQLite database layer for the Network Monitoring System.
"""

import sqlite3
from pathlib import Path

DATABASE_NAME = "era_devices.db"


class Database:
    """
    Handles all SQLite database operations.
    """

    def __init__(self, database_name=DATABASE_NAME):

        self.database = Path(database_name)

        self.connection = sqlite3.connect(self.database)

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):
        """
        Create database tables if they do not exist.
        """

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS devices(

            mac TEXT PRIMARY KEY,

            ips TEXT,

            vendor TEXT,

            status TEXT,

            confidence INTEGER,

            ports TEXT,

            seen_by TEXT,

            first_seen TEXT,

            last_seen TEXT

        )
        """)

        self.connection.commit()

    def save_device(self, device):
        """
        Insert or update a device.
        """

        data = device.to_dict()

        self.cursor.execute("""
        INSERT OR REPLACE INTO devices
        VALUES (?,?,?,?,?,?,?,?,?)
        """, (

            data["mac"],

            data["ips"],

            data["vendor"],

            data["status"],

            data["confidence"],

            data["ports"],

            data["seen_by"],

            data["first_seen"],

            data["last_seen"]

        ))

        self.connection.commit()

    def get_devices(self):
        """
        Return all devices.
        """

        self.cursor.execute("SELECT * FROM devices")

        return self.cursor.fetchall()

    def close(self):
        """
        Close SQLite connection.
        """

        self.connection.close()