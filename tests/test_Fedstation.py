from Fedstation.Fedstation import Fedstation
from Fedstation.RecieveModel import recieveModelFromServer
from Fedstation.SendModel import sendModelToServer


class TestFedstation:
    def test_initialize(self):
        f = Fedstation()
        assert f.initializeProject("exp_track" , "16513167670717TZV0KI","C:\\Users\\Yashw\\Documents\\4-2\\Major Project\\Code\\THE FRONT\\ExpTrack\\trainAndSave.py") == "done"
    def test_sendModel(self):
        response = sendModelToServer("exp_track") 
        assert response == "sent"