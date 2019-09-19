from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired

app = Flask(_name_)


@app.route ("/")
def member():
    return render_template('add.html')

@app.route ("/", methods=["post"])
def register():
    return 'Register Ok';

if _name_ == "_main_":
    app.run(debug=True)
