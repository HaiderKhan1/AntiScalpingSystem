import pyodbc
import random
from cryptography.fernet import Fernet

# server = 'personalprojectdb.database.windows.net'
# database = 'AntiScalpingSystemDB'
# username = 'Haider'
# password = '{786Admin}'   
# driver= '{ODBC Driver 17 for SQL Server}'

# db = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = db.cursor()
# cursor.execute("CREATE TABLE USERDATA (upc INT NOT NULL, cc_number VARCHAR(60) NOT NULL, transaction_date DATETIME NOT NULL, PRIMARY KEY(cc_number));")

for i in range(0,100):
    upc = str(random.randint(100000000000,999999999999))
    cc = str(random.randint(1000000000000000,9999999999999999))
    print("%s - %s"%(upc, cc))

 