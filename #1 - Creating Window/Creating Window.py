import sys
from PyQt5 import QtWidgets

def Window():
    app = QtWidgets.QApplication(sys.argv) # We need an application object

    window = QtWidgets.QWidget() # To create a window

    window.setWindowTitle("PyQt5 Template") # To set an header to the window

    window.show() # To show the window

    sys.exit(app.exec_()) # Program will be running until we click to the cross button

Window() # To run the program