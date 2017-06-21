from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/welcome", methods=['POST','GET'])
def welcome():
    user_name = request.args.get('username')
    return render_template('welcome.html',user_name=user_name)

@app.route("/", methods=['POST','GET'])
def index():
    if request.method=="POST":
        #initialize error vairables as empty strings (assume no errors)
        user_name_error = ""
        password1_error = ""
        password2_error = ""
        email_error = ""
        #get input from the form (post request)
        user_name = cgi.escape(request.form['username'], quote=True)
        password1 = cgi.escape(request.form['password'], quote=True)
        password2 = cgi.escape(request.form['vfypassword'], quote=True)
        email_address = cgi.escape(request.form['email'], quote=True)
        #validate the user name
        if user_name == "":
            user_name_error = "Please enter a valid username."
        if len(user_name) > 20:
            user_name_error = "Username must be less than 20 characters."
        if len(user_name) < 3:
            user_name_error = "Username must be more than 3 characters."
        if " " in user_name:
            user_name_error = "Username cannot contain any spaces."
        #validate password1
        if password1 == "":
            password1_error = "Please enter a valid password."
        if len(password1) > 20:
            password1_error = "Password must be less than 20 characters."
        if len(password1) < 3:
            password1_error = "Password must be more than 3 characters."
        if " " in user_name:
            password1_error = "Password cannot contain any spaces."
        #validate password2
        if password2 != password1:
            password2_error = "Passwords must match."
        #validate email:
        if email_address != "":
            if "@" not in email_address and "." not in email_address:
                email_error = "Please enter a valid email address."
            if len(email_address) > 20:
                email_error = "Email must be less than 20 characters (this makes no sense)."
            if len(email_address) < 3:
                email_error = "Email must be more than 3 characters (why??)."
            if " " in email_address:
                email_error = "Email cannot contain any spaces."

        if user_name_error == "" and password1_error == "" and password2_error == "" and email_error == "":
            return redirect('/welcome?username=' + user_name)

        return render_template('index.html',user_name=user_name,email_address=email_address,user_name_error=user_name_error,password1_error=password1_error,password2_error=password2_error,email_error=email_error)
    else:
        return render_template('index.html')

app.run()