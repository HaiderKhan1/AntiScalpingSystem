from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)
key = "b'1kzTkTXWNjrV3wHfAZUKIJI8CkvzwB0nmVH_S10lpe0='"

@app.route("/")
def main_page():
    return render_template("home.html")

@app.route("/post_data", methods = ['GET', 'POST'])
def process_data():
    upc_num = request.form["upc"]
    cc_num = request.form["cc"]
    
    #check weather this exists in the database
    return render_template("home.html")

    

if __name__ == "__main__":
    app.run(debug = True)


#fill the database with dummy data
#the webpage just displays the upc and asks for a credit number 
#that credit number is checked against the data base, and if we have a hit, then we say you may not purchase the item