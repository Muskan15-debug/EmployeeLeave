from flask import Flask, request, jsonify

app = Flask(__name__)


def check_leave_balance(balance, requested):
    if requested <= 0:
        return False

    if requested > balance:
        return False

    return True

def calculate_remaining_balance(balance,requested):
    if check_leave_balance(balance, requested):
        return balance-requested
    return balance

@app.route("/")
def home():
    return "Employee Leave Management System"


@app.route("/check-leave", methods=["POST"])
def check_leave():
    data = request.get_json()

    balance = data["balance"]
    requested = data["requested"]

    if check_leave_balance(balance, requested):
        return jsonify({
            "message": "Leave approved"
        }), 200

    return jsonify({
        "message": "Insufficient leave balance or invalid request"
    }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)