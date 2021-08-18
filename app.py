from flask import Flask, render_template, url_for, redirect, request
from cryptography.fernet import Fernet
import pyodbc

app = Flask(__name__)

key = "1kzTkTXWNjrV3wHfAZUKIJI8CkvzwB0nmVH_S10lpe0="
fernet = Fernet(key)

server = 'personalprojectdb.database.windows.net'
database = 'AntiScalpingSystemDB'
username = 'Haider'
password = '{}'   
driver= '{ODBC Driver 17 for SQL Server}'

#initalize database
db = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = db.cursor()

@app.route("/")
def main_page():
    return render_template("home.html")

@app.route("/post_data", methods = ['GET', 'POST'])
def process_data():
    upc_num = request.form["upc"]
    cc = request.form["cc"]
    
    #run sql query
    query = "SELECT UPC, cc_number, transaction_date FROM TRANSACTIONDATA WHERE UPC = {}".format(upc_num)
    cursor.execute(query)
    records = cursor.fetchall()
    
    # #decrypt credit card
    decMessage = fernet.decrypt(records[0][1].encode()).decode()
    
    if decMessage == cc:
        print("They're the same")
        print(records[0][2])

    
    #check weather this exists in the database
    return render_template("home.html")

    

if __name__ == "__main__":
    app.run(debug = True)
