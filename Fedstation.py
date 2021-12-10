#Single Class for Project 
class Fedstation : 
    #App attributes 
    project_id = 0 
    project_key = 0 
    project_meta_data = {}
    #add required later 

    def initializeProject(self, project_id, project_key):
        #Identify User(Dev)  using PROJECT_ID 

        #Authenticate User using PROJECT_KEY
        #calling getProjectMetaData() 


        #throws error if unable to inititalize the Project
        #project details doesn't match
        #attributes missing 

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

        #throws error if
        #invald model is provided 

        pass
    
    def getModel(self): 
        #retrieves the model from the pickle file 
        #and returns the Model 

        #throws errors 
        #if pickle file not found or empty 
        
        pass
    
    def sendModelToServer(self):
        #sends model in pickle file to server 

        #throws error if 
        #request denied 
        pass
    def recieveModelFromServer(self): 
        #recieve model from server 

        pass
    def scheduleTasks(self): 
        #schedules send & recieve of the model
        pass 



