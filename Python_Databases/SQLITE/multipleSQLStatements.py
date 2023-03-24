# Executing Multiple SQL Statements.
import sqlite3
with sqlite3.connect("testDatabase.db") as connection:
    cursor = connection.cursor()
    cursor.executescript(
        """DROP TABLE IF EXISTS People;
           CREATE TABLE People(
                FirstName TEXT,
                LastName TEXT,
                Age INT
            );
            INSERT INTO People VALUES(
                'Ron',
                'Obvious',
                42
            );"""
    )

people_values = (
    ("Luigi", "Vercotti", 43),
    ("Arthur", "Belling", 28)
)

# Parameterized statement.
cursor.executemany("INSERT INTO People VALUES(?, ?, ?)", people_values)
connection.commit()
connection.close()