from PyQt5.QtWidgets import *

import sys #for CLI args

# Only need one QApplication instance per application
# Pass in sys.argv to allow CLI for the app
app = QApplication(sys.argv)

# Create a Qt widget -- the window 
window = QMainWindow()
window.show() # NOTE: windows are hidden by default

# Start the event loop
app.exec() 
