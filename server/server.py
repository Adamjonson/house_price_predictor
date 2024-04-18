from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route("/get_location_names")
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    area = float(request.form['area'])
    location = request.form['location']
    rooms = int(request.form['numb_of_rooms'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,area,rooms)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
if __name__ == "__main__":
    print("Starting Python Server")
    print(util.get_location_names())
    app.run()