from flask import Flask

app = Flask(__name__)     # create the app instance,it is the starting pt of file

@app.route("/")
def home() :
    return "<h1>welcome to the Home Page</h1>"

@app.route("/welcome/<name>")         # uses the path parameter also the route is dynamic as it's accepting the i/p
def about(name) :
    return f"<h1> Hey , {name} welcome to the Home Page</h1>"


if __name__ =="__main__"  :
    app.run(debug=True)
