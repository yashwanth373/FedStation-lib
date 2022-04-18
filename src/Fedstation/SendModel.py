import requests
import pickle
import sys
import random 

MODEL_PICKEL_FILENAME = "toxic_msgs_logistic_regression_and_vector.pkl"
PROJECT_ID = sys.argv[1] 
def generateID(): 
        return "FED" 

def sendModelToServer():
        #sends model in pickle file to server 
        
        search_api_url = "http://127.0.0.1:8000/uploadModelToFirebase/" + PROJECT_ID
        
        files = {'upload_file': (generateID() ,open(MODEL_PICKEL_FILENAME,'rb'),"multipart/form-data")}

        resp  = requests.post(url = search_api_url, files=files)
        print(resp.json , "RESPONSE   SS")


        print("MODEL SENT TO SERVER")
        with open('test.txt', 'w') as f:
            f.write("MODEL SENT TO SERVER")
        #throws error if 
        #request denied 

sendModelToServer()