import sys
from PyQt5 import QtWidgets, QtGui

def Window():
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()

    window.setWindowTitle("PyQt5 Template 2")

    tag = QtWidgets.QLabel(window)  # We create a label to add text
    tag.setText("This a text.") # Type your text
    tag.move(230,30) # To set location of the text

    tag2 = QtWidgets.QLabel(window)  # We create a label to add picture,
                                     # DON'T FORGET TO IMPORT QtGui
    tag2.setPixmap(QtGui.QPixmap("babyking.jpg")) # Select your picture
    tag2.move(110,50) # To set location of your picture

    window.setGeometry(100,100,500,500) # We set first two values to set where the window start from and other two values for it's size.
    window.show()

    sys.exit(app.exec_())

Window()