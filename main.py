from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/login")
def login():
    return "loginform.html"

@app.route("/hello/<name>")
def hellow(name=None):
    return render_template("hello.html",name=name)


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/charts")
def charts():
    return render_template("charts.html")


@app.route("/tables")
def tables():
    return render_template("tables.html")




if __name__=="__main__":
    app.run(host='0.0.0.0',port=8089,debug=True)
