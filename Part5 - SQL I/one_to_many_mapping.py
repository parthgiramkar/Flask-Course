from flask import Flask

from flask_sqlalchemy import  SQLAlchemy 

opy = Flask(__name__)          # run the flask application in opy 

#SQLite, relative to Flask instance path - sqlite:///project.db

opy.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ipl_db.db"

# optional
opy.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



# obj of database
dbo = SQLAlchemy(opy)


# this is the Team database Model 
class Team(dbo.Model) :

    __tablename__ = "ipl_teams"

    id = dbo.Column(dbo.Integer , primary_key = True)
    team = dbo.Column(dbo.String(50) , nullable=False, unique=True)      #obv's team needstobe_unique

    state = dbo.Column(dbo.String(50) , nullable=False)

    members = dbo.relationship("Players", backref="group")


    def __repr__(self) :         # self ptr tothe currentobject

        return f" Team ( '{ self.team}' , '{self.state}' ) "

# Players database Model 

class Players(dbo.Model) :

    __tablename__ = "player"

    id = dbo.Column(dbo.Integer , primary_key = True)

    name = dbo.Column(dbo.String(50) , nullable=False)
    nationality = dbo.Column(dbo.String(50) , nullable=False)

# now for foreign key which refers from the another table , i.e from tableipl_teams
    team_id = dbo.Column(dbo.Integer ,dbo.ForeignKey("ipl_teams.id"))



    def __repr__(self) :         # self ptr tothe currentobject

        return f" Team ( '{ self.name}' , '{self.nationality}' ) "


if __name__ == "__main__" :

    opy.run(debug=True)

