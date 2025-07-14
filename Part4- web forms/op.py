from flask import Flask , render_template , url_for , redirect , flash

from forms1 import signupform , loginform               # imported classes from the forms1    

op = Flask(__name__)
op.config["SECRET_KEY"] = "x-gang sudampuri"         # if not then , #RuntimeError: A secret key is required to use CSRF


@op.route("/")
@op.route("/home")

def h() :
    return render_template("home.html" , title="Home")


@op.route("/signup" , methods =["GET","POST"])              # if not then , The method is not allowed for the requested URL means to say about responding to the request which is made bythePOST

def sign() :
    form = signupform()

    if form.validate_on_submit() :
        flash(f" {form.username.data} !! You have Successfully registered  ")  # fo.username.data the values that the user entered and will be seeen only one time
        return redirect(url_for("h"))
    
    return render_template("signup.html" , title="Signup " , fo = form)


@op.route("/login" , methods=["GET","POST"])

def log() :
    form = loginform()

    em = form.email.data
    pw = form.password.data

    if form.validate_on_submit() :
        if em == "ur@gmail.com" and pw == "7895" :
            flash(f" {form.username.data} you are logged in ")  # fo.username.data the values that the user entered and will be seeen only one time
            return redirect(url_for("h"))

        else :
            flash(" Incorrect Password or Email -_-")  # fo.username.data the values that the user entered and will be seeen only one time

        
    return render_template("login.html" , title=" Login  " , fo = form)



if __name__== "__main__" :
    op.run(debug=True)


