import json
import pickle
import numpy as np
__locations = None
__data_columns = None
__model = None

def get_estimated_price(address,area,room):
    #loc_index = np.where(X.columns==address)[0][0]
    try:
        loc_index = __data_columns.index(address.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = area
    x[1] = room
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2)
def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[2:]
    global __model
    with open("./artifacts/housePrice_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading the artifacts is done")
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('Ahang',100, 2))
    print(get_estimated_price('Waterfall', 1000, 2))
    print(get_estimated_price('Velenjak', 70, 2)) # other location
    print(get_estimated_price('Abbasabad', 125, 4))  # other location