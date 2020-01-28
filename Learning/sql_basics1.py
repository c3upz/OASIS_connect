import mysql.connector

myDB = mysql.connector.connect(
    host = "localhost"
    user = "myusername"
    password = "mypassword"
    database = "mydatabase"
)
myCursor = myDB.cursor()

# for x in myCursor:
#     print(x)

myCursor.execute("""CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(255)
    )""")
myCursor.execute("""INSERT INTO Customers (Customer_id) 
    VALUES (421Billy)
    """)

changeValues("421Billy", "Billy_The_Cursed")

myDB.commit()





def changeValues(changeValue, someValue):
    # Update the Customers ID with a new value
    myCursor.execute(""" UPDATE Customers (
        SET customer_id = '%s' WHERE customer_id = '%s')""", 
        (changeValue, someValue))
