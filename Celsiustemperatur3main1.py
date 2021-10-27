from flask import Flask
from flask import request
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
def index():
    celsius = request.args.get("celsius", "")
    return   render_template("indexcelcius.html",celsius )
     

def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)