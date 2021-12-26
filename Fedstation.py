#importing required Libraries 
from datetime import datetime
import json
import requests 
# import numpy
import pickle
import os 

#Single Class for Project 
class Fedstation : 
    #App attributes 
    pre_scheduled_month  = None 
    project_id = 0 
    project_key = 0 
    project_meta_data = {}
    model_pickel_filename = "toxic_msgs_logistic_regression_and_vector.pkl"
    __primary_server_package_url  = "http://localhost:8080/packageApi/"

    __project_details_url  = __primary_server_package_url + "getProjectDetails"
    __MIN_KEY_LEN = 20 
    #add required later 

    
    def initializeProject(self, project_id, project_key):
        #Identify User(Dev)  using PROJECT_ID 

        #Authenticate User using PROJECT_KEY
        #calling getProjectMetaData()

        if( project_id == None or 
            project_key == None or  
            len(project_id) == 0 or 
            len(project_key) < self.__MIN_KEY_LEN):

             raise Exception("invalid Parameters Passed")
        PARAMS  = {
            'projectId' : project_id, 
            'projectKey' : project_key,
        }
        resp  = requests.get(self.__project_details_url , params= PARAMS)
        print(resp)
        if(resp.status_code == 200):
            self.project_meta_data = resp.json()
            print(self.project_meta_data)
        elif(resp.status_code == 404) : 
            raise Exception("Project Not found")
        elif (resp.status_code in [403 , 401]) : 
            raise Exception("unauthorized or Forbiden")
        else : 
            raise Exception("unable to retrive data")
         
        #throws error if unable to inititalize the Project
        #project details doesn't match
        #attributes missing 


        #user authentication and identification is Done 
        #run the schedule tasks as window service 
        curr_month  = datetime.now().month
        if(self.pre_scheduled_month == None or curr_month != self.pre_scheduled_month):
            self.scheduleTasks() 
            self.pre_scheduled_month  = curr_month

    
    def verifyModel(self , model):
        #verify the model using the extracted Model meta data
        #from the Primary Server

        return True 
    def saveModel(self , new_model):
        #verifies model and then 
        #creates pickle file if not found 
        #else replaces the model in the file
        if(self.verifyModel(new_model) == False):
            raise Exception("Invalid Model")

        filename = self.model_pickle_filename
        with open(filename, 'wb') as fout:
            pickle.dump(new_model, fout)
        
        #throws error if
        #invald model is provided 
    
    def getModel(self): 
        #retrieves the model from the pickle file 
        #and returns the Model 
        with open(self.model_pickel_filename, 'rb') as f:
            model = pickle.load(f)
        return model
        #throws errors 
        #if pickle file not found or empty 
        
    
    def scheduleSendTask(self):
        #schedules send & recieve of the model
        import datetime
        import win32com.client

        scheduler = win32com.client.Dispatch('Schedule.Service')
        scheduler.Connect()
        root_folder = scheduler.GetFolder('\\')
        task_def = scheduler.NewTask(0)

        # Create trigger
        #send_hour = int(self.project_meta_data["startAtTime"])
        send_hour  = 2
        start_time = datetime.datetime.now()
        start_time  = (start_time.replace(day=1) + datetime.timedelta(days=32)).replace(day=1 , hour=send_hour , minute=0 , second= 0 , microsecond= 0)
        print(start_time)
        
        #temp code 
        start_time  = datetime.datetime.now() + datetime.timedelta(seconds=3)
        #end temp code

        TASK_TRIGGER_TIME = 1
        trigger = task_def.Triggers.Create(TASK_TRIGGER_TIME)
        trigger.StartBoundary = start_time.isoformat()

        # Create action
        TASK_ACTION_EXEC = 0
        action = task_def.Actions.Create(TASK_ACTION_EXEC)
        action.ID = 'send'
        action.Path = '%windir%\system32\cmd.exe'
        action.Arguments = "/c python D:\Projects\FedStation-lib\SendModel.py"
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
            'Send Model',  # Task name
            task_def,
            TASK_CREATE_OR_UPDATE,
            '',  # No user
            '',  # No password
            TASK_LOGON_NONE)
        
    def scheduleRecieveTask(self): 
        #schedules send & recieve of the model
        import datetime
        import win32com.client

        scheduler = win32com.client.Dispatch('Schedule.Service')
        scheduler.Connect()
        root_folder = scheduler.GetFolder('\\')
        task_def = scheduler.NewTask(0)

        # Create trigger
        #send_hour = int(self.project_meta_data["startAtTime"])
        send_hour  = 6
        start_time = datetime.datetime.now()
        start_time  = (start_time.replace(day=1) + datetime.timedelta(days=32)).replace(day=1 , hour=send_hour , minute=0 , second= 0 , microsecond= 0)
        print(start_time)
        
        #temp code 
        start_time  = datetime.datetime.now() + datetime.timedelta(seconds=10)
        #end temp code
        TASK_TRIGGER_TIME = 1
        trigger = task_def.Triggers.Create(TASK_TRIGGER_TIME)
        trigger.StartBoundary = start_time.isoformat()

        # Create action
        TASK_ACTION_EXEC = 0
        action = task_def.Actions.Create(TASK_ACTION_EXEC)
        action.ID = 'recieve'
        action.Path = '%windir%\system32\cmd.exe'
        action.Arguments = "/c python D:\Projects\FedStation-lib\RecieveModel.py"
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
            'Recieve Model',  # Task name
            task_def,
            TASK_CREATE_OR_UPDATE,
            '',  # No user
            '',  # No password
            TASK_LOGON_NONE) 

    def scheduleTasks(self): 
        self.scheduleSendTask()
        self.scheduleRecieveTask()



if __name__ == "__main__" :
    F = Fedstation()
    F.initializeProject("projectZee" , "1639466861939JQSI8LK")
