from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 

import sys #for CLI args

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    def __init__(self): # Constructor
        super().__init__() 

        self.setWindowTitle("Click Me Michael")

        self.button = QPushButton("Press Me Michael!")
        
        self.button.clicked.connect(self.buttonClicked) # sends a boolean value representing the check state to the buttonToggled()
    

        self.setCentralWidget(self.button) # Set the central widget of the window

        # self.setFixedSize(QSize(400, 300)) # Set window size (width, height
        self.setMinimumSize(QSize(400, 400)) # Set minimum window size
        self.setMaximumSize(QSize(800, 800)) # Set maximum window size

    def buttonClicked(self):
        self.button.setText("You can't click me anymore. No more spamming!")
        self.button.setEnabled(False)

        self.setWindowTitle("Don't Click Me Michael")


# Only need one QApplication instance per application
# Pass in sys.argv to allow CLI for the app
app = QApplication(sys.argv)

# Create a Qt widget -- the window 
window = MainWindow()
window.show() # NOTE: windows are hidden by default

# Start the event loop
app.exec() 
