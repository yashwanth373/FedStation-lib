import shutil
import sys
import requests
import pickle
import numpy


MODEL_PICKEL_FILENAME = "toxic_msgs_logistic_regression_and_vector.pkl"
PROJECT_ID = sys.argv[1]
def getModel(): 
        #retrieves the model from the pickle file 
        #and returns the Model 
        with open(MODEL_PICKEL_FILENAME , 'rb') as f:
            model = pickle.load(f)
        return model
        #throws errors 
        #if pickle file not found or empty 
def recieveModelFromServer(): 
        #recieve model from server
        search_api_url = "http://127.0.0.1:8000/getGlobalModelFile/" + PROJECT_ID
        
        with requests.get(search_api_url, stream=True) as r:
            with open(MODEL_PICKEL_FILENAME, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
                


recieveModelFromServer()

