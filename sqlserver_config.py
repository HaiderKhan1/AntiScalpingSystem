import pyodbc
import random
from cryptography.fernet import Fernet

server = 'personalprojectdb.database.windows.net'
database = 'AntiScalpingSystemDB'
username = 'Haider'
password = '{786Admin}'   
driver= '{ODBC Driver 17 for SQL Server}'

# initalize the cryptography library
key = "1kzTkTXWNjrV3wHfAZUKIJI8CkvzwB0nmVH_S10lpe0="
fernet = Fernet(key)

#initalize database
db = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = db.cursor()

#create the database table
# cursor.execute("CREATE TABLE TRANSACTIONDATA (upc VARCHAR(12) NOT NULL, cc_number NVARCHAR(1000) NOT NULL, transaction_date DATE NOT NULL, PRIMARY KEY(cc_number));")


for i in range(0,100):
    #generate random upc and cc
    upc = str(random.randint(100000000000,999999999999))
    cc = str(random.randint(1000000000000000,9999999999999999))
    cc_encrypted = fernet.encrypt(cc.encode())
    #prepare credit card number to be pushed to the database
    char_cc = list(cc_encrypted.decode())
    char_cc.insert(0,"'")
    char_cc.insert(len(char_cc), "'")
    cc_encrypted = ''.join(char_cc)

    #prepare upc to be pushed to the db
    db_upc = list(upc)
    db_upc.insert(0, "'")
    db_upc.insert(len(char_cc), "'")
    upc = "".join(db_upc)

    #push info to the database
    query = "INSERT INTO TRANSACTIONDATA (upc, cc_number, transaction_date) VALUES ({}, {}, '2021-08-14')".format(upc, cc_encrypted)
    cursor.execute(query)
    db.commit()






 