import sys
from PyQt5 import QtWidgets

def Window():
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()

    window.setWindowTitle("PyQt5 Template 3")

    button = QtWidgets.QPushButton(window)  # To add buttons
    button.setText("Button 1") # Type button's name
    button.move(160,50) # To change location of the button

    #Second button
    button2 = QtWidgets.QPushButton(window)
    button2.setText("Button 2")
    button2.move(245, 50)

    tag = QtWidgets.QLabel(window)
    tag.setText("Button Selection")
    tag.move(200,30)

    window.setGeometry(100,100,500,500)
    window.show()

    sys.exit(app.exec_())

Window()
