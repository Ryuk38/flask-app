from flask import flask
app=Flask(_name_)
@app.route("/")
def home():
  return "Hello  from flask app1"
if _name_=="_main_":
  app.run(host="0.0.0.0",port=5000)
