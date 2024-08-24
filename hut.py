from flask import Flask,render_template,request,redirect
from ka import *

app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    msg=""
    if request.method=="POST":
        if request.form["name"]!="":
            registration(request.form["name"],request.form["age"],request.form["address"],request.form["course"])
            msg="message"
        else:
            msg="info required"

    data=read_json()
    return render_template("hi.html",han=data["students"],message=msg)
@app.route("/delete/<id>")
def delete(id):
    delete_stud(id)
    return redirect("/")

@app.route("/update/<id>",methods=["POST"])
def update(id):
    if request.method=="POST":
        update_stud(id,request.form["name"],request.form["age"],request.form["address"],request.form["course"])
    return redirect("/")
if __name__=="__main__":
 app.run(debug=True,host="0.0.0.0")

    