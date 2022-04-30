from flask import Flask,render_template,request

import ml

app=Flask(__name__,template_folder='templates')

@app.route("/")
def home():
    if request.method == "POST":
        fake=request.form['username']

    return render_template('./index.html') 


@app.route("/sub",methods=['POST'])
def submit():
    if request.method =="POST":
        name=request.form["username"]

    return render_template("sub.html",n=name)

if __name__ == "__main__":
    app.run(debug=True) 