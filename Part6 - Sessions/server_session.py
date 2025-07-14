from flask import Flask , redirect , render_template , url_for , flash , session , request

from flask_session import Session

from form import loginform   # imported the class

aps = Flask(__name__) 

aps.config["SECRET_KEY"] = "hao kya" # as we are working with the wtforms
aps.config["SESSION_TYPE"] = "filesystem"

Session(aps)  # this session is now a server_session

# endpoint
@aps.route("/")
@aps.route("/hao")


def homi() :
    return render_template("home.html" , readme = "Home" )



@aps.route("/contacts")
def conts() :
     
    if "user_name" not in session :   # here session is dictionary , where we can create keys to store values in it

        flash("Login Required ")
        return redirect( url_for('log', next=request.url ))  # request holds the http request
    else :
        flash(f"Hi {session['user_name'] } , have a good day! ")

    return render_template("contact.html" , readme = "Contacts")


@aps.route("/about")
def abt() :

    if "user_name" not in session :   # here session is dictionary , where we can create keys to store values in it

        flash("Login Required ")
        return redirect( url_for('log', next=request.url ))  # request holds the http request

    else :
        flash(f"Hi {session['user_name']} , have a good day! ")

    return render_template("about.html" , readme = "About")


@aps.route("/login" ,  methods=["GET","POST"] )
def log() :
    
    fish = loginform()
    if fish.validate_on_submit() :
        
        session["user_name"] = fish.username.data
        flash(f"Successfully logged in as {session['user_name'].title()} ! ")

        next_url = request.args.get("next")
        return redirect( next_url or url_for("homi") )       # directly redirectedtothehomepage if gone througthedirect not any home pagelink

    return render_template("login.html" , readme = "Login" , fo=fish )


if __name__ == "__main__" :

    aps.run(debug=True)








# after base64enocde and decode u willnotsee csrf token username ,as this is the server_session
# :uM}^=I`EۆHQ#o get saves not to the browser side but in the database , so cannot see it





