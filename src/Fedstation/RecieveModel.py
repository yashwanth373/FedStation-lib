import shutil
import sys
import requests

MODEL_PICKEL_FILENAME = "model.pkl"
PROJECT_ID = ""
def recieveModelFromServer(project_id = ""): 
        #recieve model from server
        try:
            PROJECT_ID = sys.argv[1]
        except Exception as e : 
            PROJECT_ID = project_id
        try:
            search_api_url = "https://fedstation-ml-service.herokuapp.com/getGlobalModelFile/" + PROJECT_ID
            
            with requests.get(search_api_url, stream=True) as r:
                with open(MODEL_PICKEL_FILENAME, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
            return "recieved"
        except Exception as e : 
            print(e)
            return "!recieved"
                


recieveModelFromServer()

