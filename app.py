import requests
from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/flowers", methods=["POST"])
def save_location():
    data = request.get_json()
    print("Received data:", data)  # 👈 Add this line

    if not data:
        return "No data received", 400

    lat = data.get("latitude")
    lon = data.get("longitude")
    timestamp = datetime.utcnow().isoformat()
    with open("locations.txt", "a") as f:
        f.write(f"{timestamp} - Lat: {lat}, Lon: {lon}\n")
    return "Location saved", 200

def get_location_from_ip(ip):
    # Using ipinfo.io as an example. You may need an API key.
    api_url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(api_url)
        data = response.json()
        loc = data.get('loc', '').split(',')
        if len(loc) == 2:
            return {
                'latitude': float(loc[0]),
                'longitude': float(loc[1])
            }
    except requests.RequestException as e:
        print(f"Error fetching location for IP {ip}: {e}")
    return None

if __name__ == "__main__":
    app.run(debug=True)
