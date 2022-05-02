import requests
import pickle
import sys
import random 

MODEL_PICKEL_FILENAME = "toxic_msgs_logistic_regression_and_vector.pkl"
def generateID(): 
        return "FED" 

def sendModelToServer(project_id=""):
        #sends model in pickle file to server
        try:
            PROJECT_ID = sys.argv[1]
        except Exception as e : 
            PROJECT_ID = project_id 
        try:

                if(PROJECT_ID == None):
                        PROJECT_ID = project_id
                search_api_url = "http://127.0.0.1:8000/uploadModelToFirebase/" + PROJECT_ID
                
                files = {'upload_file': (generateID() ,open(MODEL_PICKEL_FILENAME,'rb'),"multipart/form-data")}

                resp  = requests.post(url = search_api_url, files=files)
                print("MODEL SENT TO SERVER")
                with open('test.txt', 'w') as f:
                        f.write("MODEL SENT TO SERVER")
                return "sent"
        except Exception as e : 
                print(e)
                return "!sent"
        #throws error if 
        #request denied 

# sendModelToServer()
print("calling SendModel")