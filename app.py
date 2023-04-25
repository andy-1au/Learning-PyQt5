from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 

import sys #for CLI args

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self): # Constructor
        super().__init__() 

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        self.setCentralWidget(button) # Set the central widget of the window

# Only need one QApplication instance per application
# Pass in sys.argv to allow CLI for the app
app = QApplication(sys.argv)

# Create a Qt widget -- the window 
window = MainWindow()
window.show() # NOTE: windows are hidden by default

# Start the event loop
app.exec() 
