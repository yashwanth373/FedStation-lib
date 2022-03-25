import requests
import pickle
import numpy


MODEL_PICKEL_FILENAME = "toxic_msgs_logistic_regression_and_vector"

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
        search_api_url = "https://insight-middleware-service.herokuapp.com/get-best-model"

        
        resp = None 
        while(True):
                resp = requests.get(url = search_api_url)
                print(resp)
                resp = resp.json()
                if(resp.status_code  == 200):
                        break 
        

        
        #update Model 
        model  = getModel()
        model.classes_ = numpy.array(resp["classes_"])
        model.coef_ = numpy.array(resp["coef_"])
        model.intercept_ = numpy.array(resp["intercept_"])
        model.n_iter_ = numpy.array(resp["n_iter_"])

        filename = MODEL_PICKEL_FILENAME 

        with open(filename, 'wb') as fout:
            pickle.dump(model, fout)

        print("MODEL RECEIVED FROM SERVER")
        print(model)

        with open('test.txt', 'w') as f:
            f.write("MODEL RECEIVED FROM SERVER")


recieveModelFromServer()

