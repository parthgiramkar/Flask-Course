import time             # Python module for handling delays, timestamps etc.
from flask import Flask , redirect , url_for

# Flask for to create the Flask web application.
# redirect - used to redirect users from one route to another.
# url_for - Generates the URL for a specific function name (instead of hardcoding URLs).

app = Flask(__name__)


@app.route("/")           # rule - The @app.route(..) must come directly above the function it binds
def home() :
    return "<h1>welcome to the Home Page</h1>"

@app.route("/pass")
def p()  :
    return "<h1> Congratsss,  you have passed !</h1>"

@app.route("/fail")
def f()  :
    return "<h1> Sorry ,  you'll failed -_- </h1>"



# dynamic route accepting two_values
@app.route("/score/<name>/<int:n>") 
def about(name,n) :
    if n>30 :
        # redirecting user to the page p and with no parameters in it
        return redirect(url_for("p"))      #  url_for("p") -returns the path /pass because p() is the function for that route.
                                            # redirect() sends the user to that URL.
    else :
        # redirecting to the page f
        return redirect(url_for("f")) 

 
if __name__ == "__main__" :      #  runs the app only if the file is executed directly , not the imported one
    app.run(debug=True)           # debug=True , autoloads the code if u change something in the code
 
