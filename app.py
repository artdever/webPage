from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/flowers", methods=["POST"])
def save_location():
    data = request.get_json()
    lat = data.get("latitude")
    lon = data.get("longitude")
    timestamp = datetime.utcnow().isoformat()
    with open("locations.txt", "a") as f:
        f.write(f"{timestamp} - Lat: {lat}, Lon: {lon}\n")
    return "Location saved", 200

if __name__ == "__main__":
    app.run()
