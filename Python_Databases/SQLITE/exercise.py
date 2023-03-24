import sqlite3

data = (
    ("Jean-Baptise Zorge", "Human", 122),
    ("Korben Dallas", "Meat Popsicle", 100),
    ("Ak'not", "Mangalore", -5)
)

with sqlite3.connect("RosterDB.db") as connection:
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Roster")
    cursor.execute(
        """CREATE TABLE Roster(
            Name TEXT,
            Species TEXT,
            IQ INT
        );"""
    )
    cursor.executemany("INSERT INTO Roster VALUES(?, ?, ?);", data)

# updating.
cursor.execute(
     "UPDATE Roster SET Name=? WHERE Name=?", ("Korben Dallas", "Human")
 )

# names and IQ's classified as humans.
cursor.execute("SELECT Name, IQ FROM Roster WHERE Species='Human'")
for row in cursor.fetchall():
    print(row)