# - paths dev & prod 
import os
from pathlib import Path, PurePosixPath

class PathUtils():
    rootpath = None
    
    def __init__(self):
        if os.getenv("DEBUG", "TRUE") == "TRUE":
            self.rootpath = Path(__file__).parent.parent / "dev_env"
        else:
            self.rootpath = PurePosixPath("/") / "var" / "lib" / "kirbi"
    
    def getRootPath(self) -> Path: 
        """Retrieve the application root path

        Returns:
            Path: path to the root data directory
        """
        return self.rootpath
    
    def getDataPath(self) -> Path:
        """Retrieve the application data path

        Returns:
            Path: path to the data directory
        """
        return self.rootpath / "data"
    
    def getSharedPath(self) -> Path:
        """Retrieve the application shared path

        Returns:
            Path: path to the shared directory
        """
        return self.rootpath / "shared"