from flask import Flask , redirect , render_template , url_for , flash  , request , make_response

from form import loginform   # imported the class

aps = Flask(__name__) 

aps.config["SECRET_KEY"] = "hao kya" # as we are working with the wtforms

# endpoint
@aps.route("/")
@aps.route("/hao")


def homi() :
    return render_template("home.html" , readme = "Home" )



@aps.route("/contacts")
def conts() :

    user_name = request.cookies.get("user_name")     # cookies name

    if user_name is None :

        flash("Login Required ")
        return redirect( url_for('log', next=request.url ))  # request holds the http request

    else :
        flash(f"Hi {user_name} , have a good day! ")

    return render_template("contact.html" , readme = "Contacts") 
    

@aps.route("/about")
def abt() :

    user_name = request.cookies.get("user_name")     # cookies name

    if user_name is None :

        flash("Login Required ")
        return redirect( url_for('log', next=request.url ))  # request holds the http request

    else :
        flash(f"Hi {user_name} , have a good day! ")

    return render_template("about.html" , readme = "About")



@aps.route("/login" ,  methods=["GET","POST"] )
def log() :
    
    fish = loginform()
    if fish.validate_on_submit() :
        
        user_name = fish.username.data
        resp = make_response("")
        resp.set_cookie("user_name " , user_name )     # here user_name is value , also instringvaluehavebeenset

        flash(f"Successfully logged in as {user_name.title()} ! ")

        next_url = request.args.get("next") or url_for("homi")
        resp.headers["Location"] = next_url

        resp.status_code = 302  # redirection status_code
        return resp

    return render_template("login.html" , readme = "Login" , fo=fish )



if __name__ == "__main__" :

    aps.run(debug=True)







# seeing from cookies and then conv into base64encode&decode ucan see this as it saves to the browser side not in database
# {"csrf_token":"f5d00e526d401b32726fa47448ab1b3133f3555c","user_name":"max"}7pM*F1d*H




