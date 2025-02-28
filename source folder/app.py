from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from twilio.rest import Client

app = Flask(__name__)
app.secret_key = "secret123"  # Secret key for session management

# Twilio Credentials
SID = 'ACe50aceb83710a9bd6f71cc4392c80881'
TOKEN = '958d1f80e91293813997a023b3fc54fb'
TWILIO_NUMBER = '+15344002098'  # Your Twilio Number

# Initialize Twilio Client
client = Client(SID, TOKEN)

# Dummy user credentials and profile data
USER_CREDENTIALS = {"24uad233": "2025"}
USER_PROFILES = {
    "24uad233": {
        "phone": "9600944550",
        "location": "Chennai",
        "bus_route": "Route 42"
    }
}

# Dummy driver credentials
DRIVER_CREDENTIALS = {"driver42": "buspass"}

@app.route("/")
def frontpage():
    return render_template("frontpage.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

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
    
    USER_PROFILES[username]["phone"] = request.form["phone"]
    USER_PROFILES[username]["location"] = request.form["location"]
    USER_PROFILES[username]["bus_route"] = request.form["bus_route"]

    return redirect(url_for("profile"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("driver", None)
    return redirect(url_for("login"))

@app.route("/signout")
def signout():
    session.pop("user", None)
    session.pop("driver", None)
    return redirect(url_for("login_driver"))

@app.route("/about")  
def about():
    return render_template("about.html")

@app.route('/map')
def map():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template('map.html')

@app.route('/rot')
def rot():
    return render_template('rot.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/noti')
def noti():
    return render_template('noti.html')

@app.route('/message')
def message():
    return render_template('message.html')

# 🚀 SMS Notification Route
@app.route('/send-notification', methods=['POST'])
def send_notification():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 403

    username = session["user"]
    user_data = USER_PROFILES.get(username, {})
    phone_number = user_data.get("phone")

    if not phone_number:
        return jsonify({"error": "Phone number not found"}), 400

    try:
        message = client.messages.create(
            body="Your bus has arrived at your station!",
            from_=TWILIO_NUMBER,
            to=f"+91{phone_number}"
        )
        return jsonify({"status": "success", "message_sid": message.sid})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})

# Driver Login Route
@app.route("/login_driver", methods=["GET", "POST"])
def login_driver():
    if request.method == "POST":
        driver_id = request.form.get("driver_id")
        password = request.form.get("password")

        if driver_id in DRIVER_CREDENTIALS and DRIVER_CREDENTIALS[driver_id] == password:
            session["driver"] = driver_id  # Store driver session
            return redirect(url_for("driver_dashboard"))
        else:
            return render_template("login_driver.html", error="Invalid Driver ID or Password")

    return render_template("login_driver.html", error=None)

# Driver Dashboard Route
@app.route("/driver_dashboard")
def driver_dashboard():
    if "driver" not in session:
        return redirect(url_for("login_driver"))  # Redirect to driver login
    return render_template("driver_dashboard.html", username=session["driver"])

@app.route('/students_list')
def students_list():
    return render_template('students_list.html') 

@app.route('/drivenoti')
def drivenoti():
    return render_template('drivenoti.html')

@app.route('/driver_message')
def driver_message():
    return render_template('driver_message.html')


@app.route('/')
def home():
    return render_template('drivenoti.html')

@app.route('/send_call', methods=['POST'])
def send_call():
    try:
        twiml_response = '<Response><Say voice="alice" language="en-GB">Hello! This is your bus tracking system notification. Your bus will arrive at your station in 10 minutes. So hurry up!</Say></Response>'
        call = client.calls.create(
            twiml=twiml_response,
            to= +919600944550,
            from_= +15344002098
        )
        return jsonify({"message": f"Call initiated! Call SID: {call.sid}"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/send_sms', methods=['POST'])
def send_sms():
    try:
        message = client.messages.create(
            body="Hello! Your bus will arrive at your station in 10 minutes. Hurry up!",
            from_=+15344002098,
            to=+919600944550
        )
        return jsonify({"message": f"SMS sent! Message SID: {message.sid}"})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
