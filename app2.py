from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys  # for CLI args
from random import choice

# Subclass QMainWindow to customize your application's main window

destruction = [
    'Alive',
    'Still Alive',
    'Almost Dead',
    'Dying',
    'DEAD'
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.timesClicked = 0
        self.gameOver = False

        # Create main button
        self.button = QPushButton("Self Destruct")
        self.button.clicked.connect(self.buttonClicked)

        # Create play again button
        self.playAgainButton = QPushButton("Play Again")
        self.playAgainButton.clicked.connect(self.playAgainClicked)
        self.playAgainButton.hide()  # Initially hidden

        # Add buttons to a layout
        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(self.button)
        buttonLayout.addWidget(self.playAgainButton)

        # Create central widget and set layout
        centralWidget = QWidget()
        centralWidget.setLayout(buttonLayout)
        self.setCentralWidget(centralWidget)

        # Set window size and title
        self.setFixedSize(800, 800)
        self.setWindowTitle("Russian Roulette")

        # Set button style and icon
        self.button.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : red;"
                             "}"
                             )
        pixmapi = QStyle.SP_MessageBoxCritical
        icon = self.style().standardIcon(pixmapi)
        self.button.setIcon(icon)
        self.button.setGeometry(200, 150, 100, 40)

    def buttonClicked(self):
        if self.gameOver:
            return  # Do nothing if game is already over

        newWinTitle = choice(destruction)
        self.setWindowTitle(newWinTitle)
        self.timesClicked += 1

        if newWinTitle == 'DEAD':
            self.gameOver = True
            self.button.setDisabled(True)
            self.button.setText("You died")
            self.playAgainButton.show()  # Show play again button
        else:
            luck = pow(0.2, self.timesClicked)
            self.button.setText(f"Chances: {luck:.8%}")

    def playAgainClicked(self):
        # Reset game state
        self.timesClicked = 0
        self.gameOver = False
        self.button.setDisabled(False)
        self.button.setText("Self Destruct")
        self.playAgainButton.hide()  # Hide play again button

    def changeWindow(self, window_title):
        if window_title == 'DEAD':
            self.button.setDisabled(True)
            self.button.setText("You died")


# Create a Qt widget -- the window
app = QApplication(sys.argv)
window = MainWindow()
window.show()

# Start the event loop
app.exec()

