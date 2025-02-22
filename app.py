from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"  # Secret key for session management

# Dummy user credentials and profile data
USER_CREDENTIALS = {"24uad233": "2025"}
USER_PROFILES = {
    "24uad233": {
        "email": "santhosh@example.com",
        "location": "Chennai",
        "bus_route": "Route 42"
    }
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Check credentials
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            session["user"] = username  # Store user session
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid Username or Password")

    return render_template("login.html", error=None)

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", username=session["user"])

@app.route("/profile", methods=["GET"])
def profile():
    if "user" not in session:
        return redirect(url_for("login"))
    
    user_data = USER_PROFILES.get(session["user"], {})
    return render_template("profile.html", username=session["user"], **user_data)

@app.route("/edit_profile", methods=["POST"])
def edit_profile():
    if "user" not in session:
        return redirect(url_for("login"))

    username = session["user"]
    USER_PROFILES[username]["email"] = request.form["email"]
    USER_PROFILES[username]["location"] = request.form["location"]
    USER_PROFILES[username]["bus_route"] = request.form["bus_route"]

    return redirect(url_for("profile"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/about")  
def about():
    return render_template("about.html")

@app.route('/map')
def map():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template('map.html')  # Render the map page


if __name__ == "__main__":
    app.run(debug=True)
