from flask import Flask, request, jsonify, render_template
import razorpay

app = Flask(__name__)

razorpay_client = razorpay.Client(auth=("rzp_live_FvXcnskY9fqeEK", "JgfaXbqSvDoNrASgPm5mPXDz"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/create_order", methods=["POST"])
def create_order():
    data = request.json
    amount = int(data.get("amount", 1)) * 100
    payment = razorpay_client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": "1"
    })
    return jsonify(payment)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    username = request.form.get("username")
    password = request.form.get("password")

    if not name or not username or not password:
        return "All fields are required", 400

    return render_template("dashboard.html")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
