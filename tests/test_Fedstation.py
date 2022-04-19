from Fedstation.Fedstation import Fedstation
from Fedstation.RecieveModel import recieveModelFromServer
from Fedstation.SendModel import sendModelToServer


class TestFedstation:
    def test_initialize(self):
        f = Fedstation()
        assert f.initializeProject("k_k" , "1650096582188HLVXWHJ") == "done"
    def test_sendModel(self):
        response = sendModelToServer("k_k") 
        assert response == "sent"
    def test_recieveModel(self): 
        response = recieveModelFromServer("k_k")
        assert response == "recieved"