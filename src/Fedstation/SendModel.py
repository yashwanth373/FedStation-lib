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
        search_api_url = "https://insight-middleware-service.herokuapp.com/send-model"
        
        
        data = {
            'classes_': model.classes_.tolist() ,
            'coef_':model.coef_.tolist() ,
            'intercept_': model.intercept_.tolist() ,
            'n_iter_': model.n_iter_.tolist()
        }
        

        while(True):
                resp  = requests.post(url = search_api_url, json=data)
                if(resp.status_code == 200):
                        break 


        print("MODEL SENT TO SERVER")
        with open('test.txt', 'w') as f:
            f.write("MODEL SENT TO SERVER")
        #throws error if 
        #request denied 


sendModelToServer()