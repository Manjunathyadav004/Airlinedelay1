import json
import pickle
import numpy as np

__Day_Of_Week = None
__Airline = None
__Origin_airport = None
__Destination_airport = None
__data_columns = None
__model = None

def get_Predicted_delay(MONTH, DAY, DAY_OF_WEEK, AIRLINE, ORIGIN_AIRPORT,
       DESTINATION_AIRPORT, SCHEDULED_TIME, DISTANCE,
       ARRIVAL_DELAY, Scheduled_dep_hour, Scheduled_dep_min,
       Scheduled_arr_hour, Scheduled_arr_min):
    try:
        DAY_OF_WEEK_index = __data_columns.index(DAY_OF_WEEK.lower())
        AIRLINE_index = __data_columns.index(AIRLINE.lower())
        ORIGIN_AIRPORT_index = __data_columns.index(ORIGIN_AIRPORT.lower())
        DESTINATION_AIRPORT_index = __data_columns.index(DESTINATION_AIRPORT.lower())
    except:
        DAY_OF_WEEK_index  = -1
        AIRLINE_index = -1
        ORIGIN_AIRPORT_index = -1
        DESTINATION_AIRPORT_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = MONTH
    x[1] = DAY
    x[2] = SCHEDULED_TIME
    x[3] = DISTANCE
    x[4] = ARRIVAL_DELAY
    x[5] = Scheduled_dep_hour
    x[6] = Scheduled_dep_min
    x[7] = Scheduled_arr_hour
    x[8] = Scheduled_arr_min
    if DAY_OF_WEEK_index >= 0:
        x[DAY_OF_WEEK_index] = 1

    if AIRLINE_index >= 0:
        x[AIRLINE_index] = 1

    if ORIGIN_AIRPORT_index >= 0:
        x[ORIGIN_AIRPORT_index] = 1

    if DESTINATION_AIRPORT_index >= 0:
        x[DESTINATION_AIRPORT_index] = 1
    return float("{:.2f}".format(__model.predict([x])[0]))


def get_DAY_OF_WEEK():
    return __Day_Of_Week

def get_AIRLINE():
    return __Airline

def get_Origin_airport():
    return __Origin_airport

def get_Destination_airport():
    return __Destination_airport

def load_saved_artifacts():
    print("Loading saved saved artifacts...start")
    global  __data_columns
    global  __Day_Of_Week
    global __Airline
    global __Origin_airport
    global __Destination_airport

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __Day_Of_Week = __data_columns[9:16]  # first  9 columns are month, day, SCHEDULED_TIME, DISTANCE, arrival_delay, scheduled_dep_hour, scheduled_dep_min, scheduled_arr_hour, scheduled_arr_min

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __Airline = __data_columns[16:30]

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __Origin_airport = __data_columns[30:]

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __Destination_airport = __data_columns[30:]

    global __model
    if __model is None:
        with open('./artifacts/gbr.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_DAY_OF_WEEK())
    print(get_AIRLINE())
    print(get_Origin_airport())
    print(get_Destination_airport())
    print("%.2f" % get_Predicted_delay(8,2,'Sunday','MQ','DFW','SPS',53.0,113,-15.0,21,45,22,38))
    print("%.2f" % get_Predicted_delay(12,16,'Wednesday','WN','LAX','SJC',70.0,308,-11.0,13,55,15,5))