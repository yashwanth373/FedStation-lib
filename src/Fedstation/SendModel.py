import requests
import pickle



MODEL_PICKEL_FILENAME = "toxic_msgs_logistic_regression_and_vector.pkl"
def getModel(): 
        #retrieves the model from the pickle file 
        #and returns the Model 
        model = ""
        
        with open(MODEL_PICKEL_FILENAME, 'rb') as f:
                vectorizer, model = pickle.load(f)
       

        
        return model
        #throws errors 
        #if pickle file not found or empty 

def sendModelToServer():
        #sends model in pickle file to server 
        
        model = getModel()
        search_api_url = "http://127.0.0.1:8000/uploadModelToFirebase/k_k"
        
        files = {'upload_file': open(MODEL_PICKEL_FILENAME,'rb')}
        
        headers = {
                'Content-Type' : 'application/octet-stream'
        }

        resp  = requests.post(url = search_api_url, files=files , headers=headers)
        print(resp.json , "RESPONSE   SS")


        print("MODEL SENT TO SERVER")
        with open('test.txt', 'w') as f:
            f.write("MODEL SENT TO SERVER")
        #throws error if 
        #request denied 


sendModelToServer()