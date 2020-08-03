from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_DAY_OF_WEEK', methods=['GET'])
def get_DAY_OF_WEEK():
    response = jsonify({
        'Day_Of_Week': util.get_DAY_OF_WEEK()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_AIRLINE', methods=['GET'])
def get_AIRLINE():
    response = jsonify({
        'Airline': util.get_AIRLINE()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_Origin_airport', methods=['GET'])
def get_Origin_airport():
    response = jsonify({
        'Origin_airport': util.get_Origin_airport()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_Destination_airport', methods=['GET'])
def get_Destination_airport():
    response = jsonify({
        'Destination_airport': util.get_Destination_airport()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_flights_delay', methods=['GET','POST'])
def predict_flights_delay():
    MONTH = int(request.form['MONTH'])
    DAY = int(request.form['DAY'])
    DAY_OF_WEEK = request.form['DAY_OF_WEEK']
    AIRLINE = request.form['AIRLINE']
    ORIGIN_AIRPORT = request.form['ORIGIN_AIRPORT']
    DESTINATION_AIRPORT = request.form['DESTINATION_AIRPORT']
    SCHEDULED_TIME = float(request.form['SCHEDULED_TIME'])
    DISTANCE = int(request.form['DISTANCE'])
    ARRIVAL_DELAY = float(request.form['ARRIVAL_DELAY'])
    Scheduled_dep_hour = int(request.form['Scheduled_dep_hour'])
    Scheduled_dep_min = int(request.form['Scheduled_dep_hour'])
    Scheduled_arr_hour = int(request.form['Scheduled_arr_hour'])
    Scheduled_arr_min = int(request.form['Scheduled_arr_min'])

    response = jsonify({
        'estimated_delay': util.get_Predicted_delay(MONTH,DAY,DAY_OF_WEEK,AIRLINE,ORIGIN_AIRPORT,DESTINATION_AIRPORT,SCHEDULED_TIME,
                                                    DISTANCE,ARRIVAL_DELAY,Scheduled_dep_hour,Scheduled_dep_min,Scheduled_arr_hour,Scheduled_arr_min)
    })
    response.headers.add('Access-control-allow-origin','*')

    return response


if __name__ == '__main__':
    print("Python flask server for airline delay prediction..")
    util.load_saved_artifacts()
    app.debug = True
    app.run(port=5000)
