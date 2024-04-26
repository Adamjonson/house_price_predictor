from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS module
import util

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
@app.route("/get_location_names")
def get_location_names():

    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    area = float(request.form['total_sqft'])
    location = request.form['location']
    rooms = int(request.form['bhk'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,area,rooms)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
if __name__ == "__main__":
    print("Starting Python Server")
    print(util.get_location_names())
    app.run()