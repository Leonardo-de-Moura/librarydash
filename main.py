from flask import Flask
from flask import request
from markupsafe import escape

app= Flask(__name__)

@app.route("/hello")
def init():
	name= request.args.get("name", "flask")
	return f"hello, {escape(name)}!"


