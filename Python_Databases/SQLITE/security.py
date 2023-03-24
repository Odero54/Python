import sqlite3
# Avoid Security Issues With Parametrized
# Statements.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
data = (first_name, last_name, age)

# Execute insert statement for supplied person data.
with sqlite3.connect("testDatabase.db") as connection:
    cursor = connection.cursor()
    cursor.execute("INSERT INTO People VALUES(?, ?, ?);", data) # Parameterized statement.
                                                                # This prevent sql injections.
cursor.execute(
    "UPDATE People SET Age=? WHERE FirstName=? AND LastName=?;",
    (45, 'Luigi', 'Vercotti')
)
