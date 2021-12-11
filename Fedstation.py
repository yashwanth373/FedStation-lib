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

        self.scheduleTasks() 

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
        import datetime
        import win32com.client

        scheduler = win32com.client.Dispatch('Schedule.Service')
        scheduler.Connect()
        root_folder = scheduler.GetFolder('\\')
        task_def = scheduler.NewTask(0)

        # Create trigger
        start_time = datetime.datetime.now() + datetime.timedelta(seconds=5)
        TASK_TRIGGER_TIME = 1
        trigger = task_def.Triggers.Create(TASK_TRIGGER_TIME)
        trigger.StartBoundary = start_time.isoformat()

        # Create action
        TASK_ACTION_EXEC = 0
        action = task_def.Actions.Create(TASK_ACTION_EXEC)
        action.ID = 'DO NOTHING'
        action.Path = 'D:\Projects\FedStation-lib\scheduleTasks.py'
        action.WorkingDirectory = "D:\Projects\FedStation-lib\\"

        # Set parameters
        task_def.RegistrationInfo.Description = 'Test Task'
        task_def.Settings.Enabled = True
        task_def.Settings.StopIfGoingOnBatteries = False

        # Register task
        # If task already exists, it will be updated
        TASK_CREATE_OR_UPDATE = 6
        TASK_LOGON_NONE = 0
        root_folder.RegisterTaskDefinition(
            'Send or Recieve Model',  # Task name
            task_def,
            TASK_CREATE_OR_UPDATE,
            '',  # No user
            '',  # No password
            TASK_LOGON_NONE)
        pass 



if __name__ == "__main__" :
    F = Fedstation()
    F.initializeProject("88" , "88")
