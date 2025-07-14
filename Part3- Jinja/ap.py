from flask import Flask  , render_template , url_for        # from flask library imported the reqired class

from employees import employees_data

# __name__ is a special Python variable and helps Flask know where to find resources like templates and static files.
ap = Flask(__name__)    # tells Flask this file is the starting point of the app.


# creating first endpoint
@ap.route("/")           #  tells Flask when URL (http..)is accessed, run the home() function
@ap.route("/hoiii")                 #    route that triggers the same function,

def home()  :  # the home endpt
	# return render_template("home.html")  here title is acting as the parameter  

	return render_template("home.html" , title="Home Page")          

# This is called routing – connecting a URL path to a Python function

@ap.route("/about")      # the about endpoint
def about()  :
	return render_template("about.html" , title="About Page") 


@ap.route("/evalu/<int:num>")
def eva(num) :
	
	return render_template("evaluate.html" , title =" Evaluate Paging team" , number = num)


@ap.route("/employ")
def employe() :
	return render_template("employess.html" , title = "Employees Roles" , emplo = employees_data)
 
@ap.route("/employ/mang")
def mag() :

	return render_template("mangers.html" , title = "Managers Roles Holding Individuals" , emplo = employees_data)
 
def employe() :
	return render_template("employess.html" , title = "Employees work culture " , emplo = employees_data)
 





if __name__ == "__main__":    #  This block checks if the script is run directly, not imported

	ap.run(debug=True)    #  starts the Flask development server

# debug=True enables - Auto-reload on code changes and helpful debug error page when errors occur.

