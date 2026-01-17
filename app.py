print("Program Starting")

from flask import Flask, jsonify, render_template
import threading
import time

app = Flask(__name__)

current_lights = {"ns": "red", "ew": "red"}

def traffic_light_controller():
    while True:
        # NS GREEN, EW RED
        current_lights["ns"] = "green"
        current_lights["ew"] = "red"
        time.sleep(5)

        # NS YELLOW, EW RED
        current_lights["ns"] = "yellow"
        current_lights["ew"] = "red"
        time.sleep(2)

        # NS RED, EW GREEN
        current_lights["ns"] = "red"
        current_lights["ew"] = "green"
        time.sleep(5)

        # NS RED, EW YELLOW
        current_lights["ns"] = "red"
        current_lights["ew"] = "yellow"
        time.sleep(2)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/lights")
def lights():
    return jsonify(current_lights)

# Main
if __name__ == "__main__":
    t = threading.Thread(target=traffic_light_controller)
    t.daemon = True
    t.start()


    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
