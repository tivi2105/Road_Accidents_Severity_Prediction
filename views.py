from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import json

class Person:
	name = ''
	age = 0
	def __init__(self, name, age):
		self.name = name
		self.age = age


views = Blueprint(__name__, "views")

@views.route("/home")
def home():
	return render_template("index.html", name="This is a sample flask app")

@views.route("/profile/<username>")
def profile(username):
	return render_template("index.html", name=username)

@views.route("/json")
def get_json():
	return jsonify({'name': 'trivi', 'age': 25})

@views.route("/get_data", methods=['POST'])
def get_data():
	data = request.form['sampleText']
	print(data)
	return redirect(url_for("views.profile", username=data))

@views.route("/data", methods=['POST'])
def data():
	data = request.json
	print(data)
	person = Person("Trivikram", 25)
	return json.dumps(person.__dict__)

@views.route("/dashboard")
def dashboard():
	args = request.args
	username = args.get('username')
	return render_template("Dashboard.html", username=username)