from flask_wtf import FlaskForm

from wtforms import SubmitField , StringField , SubmitField

from wtforms.validators import DataRequired , Length

class loginform(FlaskForm) :

    username = StringField("UserName - " , validators=[DataRequired() , Length(4,50) ] )

    password = StringField("PassWord - " , validators=[DataRequired() , Length(4,50)] )

    submit = SubmitField("Login ")

