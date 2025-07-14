from flask import Flask , make_response , request

opi = Flask(__name__)


@opi.route("/")
def hom() :

    resp = make_response("<h1> Welcome to the Home Page !</h1>")
    return resp


@opi.route("/set_cookie")

def s_cookie() :

    resp = make_response("<h1> Welcome to the Set Cookie Page !</h1>")
    resp.set_cookie("cookie_name" , "cookie_value")
    return resp


@opi.route("/get_cookie")
def g_cookie() :

    val= request.cookies.get("cookie_name")
    resp = make_response(f"<h1> The cookie value is <i> {val} </i> </h1>")

    return resp

if __name__ == "__main__" :

    opi.run(debug=True)

