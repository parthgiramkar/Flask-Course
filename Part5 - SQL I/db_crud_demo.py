#  For one-to-one Mapping 

from flask import Flask
from flask_sqlalchemy import SQLAlchemy        # tool that helps Flask connect to a database and use Python code instead of SQL queries 

apy = Flask(__name__)

#SQLite, relative to Flask instance path - sqlite:///project.db       , connect file called employees.db using sqlite

apy.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employees_db.db"                               # sqlalchemy database uri
apy.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False                 # this line disables a warning ,dont need any modification_tracking genlly useforadv_stuff


db = SQLAlchemy(apy)      # object of database


# tabels represented as classes
class Employ(db.Model) :           # SQLAlchemy model                  

    id = db.Column(db.Integer , primary_key=True )
    name = db.Column(db.String(50) , nullable=False)      # should_be compulsorilywritten
    age = db.Column(db.Integer , nullable=False)
    email = db.Column(db.String(50) , nullable=False , unique=True)  
    
    def __repr__(self) :

       return f" Employee (  '{self.name}','{self.email}',{self.age} ) " 


if __name__ == "__main__" :

    apy.run(debug=True)


