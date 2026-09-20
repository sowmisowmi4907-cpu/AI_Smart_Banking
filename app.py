from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load transaction dataset
data = pd.read_csv("bank_transactions.csv")

@app.route("/")
def home():

    transactions = []

    for _, row in data.iterrows():

        if row["Is_Fraud"] == 1:
            status = "Suspicious Transaction"
        else:
            status = "Normal Transaction"

        transactions.append({
            "id": row["Transaction_ID"],
            "customer": row["Customer_ID"],
            "amount": row["Transaction_Amount"],
            "type": row["Transaction_Type"],
            "location": row["Location"],
            "status": status
        })

    return render_template(
        "index.html",
        transactions=transactions
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)
