#  How to create a SQLite database
# Creating SQLite database
# use command line or Terminal in Visual Studio Code.

import sqlite3
connection = sqlite3.connect("testDatabase.db")
# type(connection)

# store and retrieve data using cursor() function
# cursor is used to fetch results from the database one at a time
cursor = connection.cursor()
# type(cursor)

# getting current local time.
query = "SELECT datetime('now', 'localtime');"
cursor.execute(query)

# To get query result use fetchone() method.
cursor.fetchone()

# Since fetchone returns string as a tuple, we can unpack by
# chaining .execute() with .fetchone() methods.
time = cursor.execute(query).fetchone()[0]

# closing the database.
connection.close()

# Using with to Manage Your Database Connection.
with sqlite3.connect("testDatabase.db") as connection:
    cursor = connection.cursor()
    query = "SELECT datetime('now', 'localtime');"
    time = cursor.execute(query).fetchone()[0]
# print(time)
connection.close()

# Working With Database Tables.
# Let's create table people
connection = sqlite3.connect("testDatabase.db")
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
)
connection.commit() # Database jargon for saving data
connection.close()

# Deleting table.
cursor.execute("DROP TABLE People;") # Do this on a commandLine.
connection.commit()
connection.close()

# Using with statement to create a table.
# next script.