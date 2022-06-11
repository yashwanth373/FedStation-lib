import sys
from Fedstation import Fedstation

if __name__ == "__main__":
        fed = Fedstation()
        fed.sendModelToServer(sys.argv[1])