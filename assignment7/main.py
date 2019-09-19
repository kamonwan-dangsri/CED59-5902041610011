from flask import Flask,render_template , request
from wtforms import StringField,PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email


app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'

class ParnRegister(FlaskForm):
    Fname = StringField("FirstName", validators=[InputRequired()])
    Lname = StringField("Lastname", validators=[InputRequired()])
    Email = StringField("E-mail",  validators=[InputRequired("Please enter your email."), Email("Please enter your email again.")])
    Uname = StringField("Username", validators=[InputRequired()])
    Pass = PasswordField("Password", validators=[InputRequired(), Length(min=8, message="Please enter password 8 character.")])

@app.route('/')
def student():
    form = ParnRegister()
    return render_template('Register.html', form=form)


@app.route('/test', methods=["GET", "POST"])
def test():
    form = ParnRegister()
    if form.validate_on_submit():
        return "OK"
    return render_template('Register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)