import requests
import pickle
import sys
import random

import os.path

MODEL_PICKEL_FILENAME = "model.pkl"
def generateID():

        ID = "" 

        file_exists = os.path.exists('conf.txt')

        if file_exists:
                with open('conf.txt', 'r') as f:
                        lines = f.readlines()
                        for line in lines:
                                line = line.split(" ")
                                if line[0] == "modelFileName":
                                        ID = line[1]
        else:
                ID = str(random.randint(0, 1000000))
                with open('conf.txt', 'w') as f:
                        f.write("modelFileName " + ID)
        return ID

def sendModelToServer(project_id=""):
        print("Sending Model to Server")
        #sends model in pickle file to server
        try:
            PROJECT_ID = sys.argv[1]
        except Exception as e : 
            PROJECT_ID = project_id
        print(PROJECT_ID) 
        try:

                if(PROJECT_ID == None):
                        PROJECT_ID = project_id
                search_api_url = "https://fedstation-ml-service.herokuapp.com/uploadModelToFirebase/" + PROJECT_ID
                
                files = {'upload_file': (generateID() ,open(MODEL_PICKEL_FILENAME,'rb'),"multipart/form-data")}

                resp  = requests.post(url = search_api_url, files=files)
                print(resp.json())
                with open('test.txt', 'w') as f:
                        f.write(PROJECT_ID)
                return "sent"
        except Exception as e : 
                print(e)
                return "!sent"
        #throws error if 
        #request denied 

sendModelToServer()