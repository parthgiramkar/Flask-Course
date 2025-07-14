import time
from flask import Flask , redirect , url_for

app = Flask(__name__)


@app.route("/")
def home() :
    return "<h1>welcome to the Home Page</h1>"

@app.route("/pass/<tname>/<marks>")
def p(tname,marks)  :
    return f"<h1> Congratsss {tname},  you have passed with {marks} !</h1>"

@app.route("/fail/<tname>/<marks>")
def f(tname,marks)  :
    return f"<h1> Sorry {tname},  you'll failed  with score of {marks} -_- </h1>"



# Main Route Logic
@app.route("/score/<name>/<int:n>")
def about(name,n) :
    if n>30 :
        # redirecting user to the page p  ,  #  url_for("function_name", key=value) 
        return redirect(url_for("p" , tname = name , marks = n) )      # to the pass endpoint
    else :
        # redirecting to the page f
        return redirect(url_for("f" , tname = name , marks = n ) ) 


if __name__ == "__main__" :
    app.run(debug=True)

