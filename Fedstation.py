#importing required Libraries 
import requests 
# import numpy
import pickle
import os 

#Single Class for Project 
class Fedstation : 
    #App attributes 
    project_id = 0 
    project_key = 0 
    project_meta_data = {}
    model_pickel_filename = "toxic_msgs_logistic_regression_and_vector.pkl"
    #add required later 

    
    def initializeProject(self, project_id, project_key):
        #Identify User(Dev)  using PROJECT_ID 

        #Authenticate User using PROJECT_KEY
        #calling getProjectMetaData() 


        #throws error if unable to inititalize the Project
        #project details doesn't match
        #attributes missing 


        #user authentication and identification is Done 
        #run the schedule tasks as window service 

        #pre-requisites 
        #dowload NSSM(Non Sucking Service Manager) on to your project main directory
        # python_path_cmd = r'python -c "exec(\"import sys\nprint(sys.executable)\")"'
        # os.system(python_path_cmd)

        create_service_cmd  = "nssm install taskscheduler " + "D:\Python310\python.exe" + " D:\Projects\FedStation-lib\scheduleTasks.py"
        error_log_cmd = r"nssm set taskscheduler AppStderr D:\Projects\FedStation-lib\nssm_error_logs.log"
        output_log_cmd = r"nssm set taskscheduler AppStdout D:\Projects\FedStation-lib\nssm_output_logs.log"

        #creating Window Service to schedule Tasks
        #os.system(create_service_cmd)
        
        # os.system("nssm remove taskscheduler")

        start_service_cmd = "nssm start taskscheduler"
        os.system(start_service_cmd)

        #setting paths to log files 
        #files should already exits

        os.system(error_log_cmd); 
        os.system(output_log_cmd)

        #setting path to log files DONE 

        pass
    def getProjectMetaData(self): 

        #gets projects meta data from the Fedstation Primary Server 
        #throws error if 
        #not an authenticated user 
        #respone not found
        #request denied 

        pass 
    
    def verifyModel(self , model):
        #verify the model using the extracted Model meta data
        #from the Primary Server

        pass
    def saveModel(self , new_model):
        #verifies model and then 
        #creates pickle file if not found 
        #else replaces the model in the file

        filename = self.model_pickle_filename
        with open(filename, 'wb') as fout:
            pickle.dump(new_model, fout)
        
        #throws error if
        #invald model is provided 

        pass
    
    def getModel(self): 
        #retrieves the model from the pickle file 
        #and returns the Model 
        with open(self.model_pickel_filename, 'rb') as f:
            model = pickle.load(f)
        return model
        #throws errors 
        #if pickle file not found or empty 
        
        pass
    
    def sendModelToServer(self):
        #sends model in pickle file to server 
        pass

        model = self.getModel()
        search_api_url = self.project_meta_data.middleware_server_send_url
        data = {
            'classes_': model.classes_.tolist() ,
            'coef_':model.coef_.tolist() ,
            'intercept_': model.intercept_.tolist() ,
            'n_iter_': model.n_iter_.tolist()
        }

        resp  = requests.post(url = search_api_url, json=data)

        #throws error if 
        #request denied 
        
    def recieveModelFromServer(self): 
        #recieve model from server
        pass

        # search_api_url = self.project_meta_data.middleware_server_recieve_url

        # resp = requests.get(url = search_api_url).json()
        # #update Model 
        # model  = self.getModel()
        # model.classes_ = numpy.array(resp["classes_"])
        # model.coef_ = numpy.array(resp["coef_"])
        # model.intercept_ = numpy.array(resp["intercept_"])
        # model.n_iter_ = numpy.array(resp["n_iter_"])

        # filename = self.model_pickle_filename
        # with open(filename, 'wb') as fout:
        #     pickle.dump(model, fout)
        
    def scheduleTasks(self): 
        #schedules send & recieve of the model
        pass 



if __name__ == "__main__" :
    F = Fedstation()
    F.initializeProject("88" , "88")
