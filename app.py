from flask import Flask          # from flask library imported the reqired class


# __name__ is a special Python variable and helps Flask know where to find resources like templates and static files.
app = Flask(__name__)   # tells Flask this file is the starting point of the app.


# creating first endpoint
@app.route("/")           #  tells Flask when URL (http..)is accessed, run the home() function
@app.route("/hoiii")                 #    route that triggers the same function,

def home()  :  # the home endpt
	return "<h1>Aho , Mangala Tai pustak(book) Vacha ki -_- -_-</h1>"              # gives back an html response in browser

# This is called routing – connecting a URL path to a Python function

@app.route("/about")      # the about endpoint
def about()  :
	return "<h2>Welcome to the about page</h2>"



@app.route("/about/<name>")      # This route is dynamic – it accepts a variable part-i/p in the URL 
def welcome(name) :
	return f"<h1>hey, {name.title()} u are warmly welcomed to our home page </h1>"   # here,use the formatted string for variable insertion
#title() for only first char ofeachword


# <int:...> the inputs gets automatically converted from string to integer.
@app.route("/operation/<int:num1>/<int:num2>")                  
def op(num1,num2) :                                                         # same parameter as given the path parameter
	return f"<h1> namsate , the multiplication of {num1} , {num2} is  {num1*num2}</h1>"





if __name__ == "__main__":    #  This block checks if the script is run directly, not imported

	app.run(debug=True)    #  starts the Flask development server

# debug=True enables - Auto-reload on code changes and helpful debug error page when errors occur.

