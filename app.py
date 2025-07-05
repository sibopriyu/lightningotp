
from flask import Flask, request, jsonify
import razorpay

app = Flask(__name__)

# Razorpay Live Keys
razorpay_client = razorpay.Client(auth=("rzp_live_FvXcnskY9fqeEK", "JgfaXbqSvDoNrASgPm5mPXDz"))

@app.route("/")
def home():
    return "LIGHTNING OTP Backend is Running!"

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

if name == "main":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
