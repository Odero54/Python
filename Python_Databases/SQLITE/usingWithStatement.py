import sqlite3
with sqlite3.connect("testDatabase.db") as connection:
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE People(
            FirstName TEXT,
            LastName TEXT,
            Age INT
            );"""
    )
    cursor.execute(
        """INSERT INTO People VALUES(
            'Ron',
            'Obvious',
            42
        );"""
    ) # No need of using connection.commit() if you've aleady uses
      # with statement since with statement automatically commits when changes are 
      # made to the database. Advantage of using with statement
      # to manage database connection.