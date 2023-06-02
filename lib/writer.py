"""
    Class that handles file writting
"""

import os
from datetime import datetime

class Writer(object):
    """
        Writer class for file handling and writting
        It will write to a file with the name of the message being
        analysed, ex: 'The Instar Emergence.txt'
    """

    # File to write to
    file_path: str

    # Directory where files are stored
    directory_path: str

    # Full pat (directory_path + / + file_path)
    full_path: str

    def __init__(self, message:str, clear = True) -> None:
        self.directory_path = "outputs/"
        self.file_path = f"{message}.txt"
        self.full_path = os.path.join(self.directory_path, self.file_path)
        
        if not self.directory_exists():
            os.makedirs(self.directory_path)

        # if already exists clear contents
        with open(self.full_path, 'w' if clear else 'a') as f:
            f.divisor(f)
            f.write(f"COMPUTING \"{message}\" STARTED AT {str(datetime.now())}\n")
            self.divisor(f)
    
    def write(self, string: str) -> None:
        """Writes into file"""
        with open(self.full_path, 'a') as f:
            f.write(f"{string} >>> {str(datetime.now())}\n")
    
    def divisor(self, f) -> None:
        """Puts divisor in a file obj"""
        f.write("-" * 512 + "\n")

    def title(self, string:str) -> None:
        """Prints tilte-like string in txt file"""
        with open(self.full_path, 'a') as f:
            self.divisor(f)
            f.write(f"   {string} >>> {str(datetime.now())}\n")
            self.divisor(f)

    def directory_exists(self) -> bool:
        """Checks if output files directory exists"""
        return os.path.exists(self.directory_path)

    def file_exists(self) -> bool:
        """Checks if file already exists"""
        return os.path.exists(self.full_path)
