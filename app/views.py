from flask import render_template, request, redirect, url_for, jsonify, flash

@app.route("/", methods=["GET","POST"])
@app.route("/index", methods=["GET","POST"])
def index():
    return "index goes here"#render_template("index.html")

@app.route("/add/<int:first>/<int:second>")
@app.route("/add")
def add(first='',second=''):
    if first == '':
        first = int(request.get("first"))
    if second == '':
        second = int(request.get("second"))
    result = first + second
    return "add"#render_template("index.html",result=result)

@app.route("/check_length")
def check_length():
    username = request.get("username")
    if len(username) > 15:
        flash("You entered a very long user name..Please reconsider your life choices")
    return "thing"
@app.route("send_data")
def send_data():
    data={"Eric Schles":"eric.schles@syncano.com",
          "job":"developer evangelist",
          "mission":"end slavery",
          "training for":"the olympics",
          "hobbies":["guitar","rock climbing"],
          "friends":"everyone"
          }
    return "stuff"#jsonify(data)
