from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , DateField , SubmitField , BooleanField , SelectField


from wtforms.validators import  DataRequired , Length , Email,Optional,EqualTo

class signupform(FlaskForm) :
    username = StringField("UserName " ,            # here username is label as passed in para,also with it validator ispassed
             validators=[ DataRequired() , Length(2,30) ] ) 

    email = StringField("EMail " , validators=[ DataRequired() , Email()])

    gender = SelectField("Gender ", choices = ["male","female","other"] , validators=[Optional()])

    dob = DateField("Date of Birth " , validators=[Optional()] )

    password = PasswordField("PassWord " , validators=[DataRequired() , Length(2,25) ] )
    confirm_password = PasswordField("Confirme PassWord " , validators=[DataRequired() , EqualTo( "password")] )

    submit = SubmitField("Sign Up ")




class loginform(FlaskForm) :

    username = StringField("UserName " ,            # here username is label as passed in para,also with it validator ispassed
             validators=[ DataRequired() , Length(2,30) ] ) 

    email = StringField("EMail " , validators=[ DataRequired() , Email()])

    password = PasswordField("PassWord " , validators=[DataRequired() , Length(2,25) ])
    
    remember_passkey= BooleanField("Remember Me")
    submit = SubmitField("Login ")



