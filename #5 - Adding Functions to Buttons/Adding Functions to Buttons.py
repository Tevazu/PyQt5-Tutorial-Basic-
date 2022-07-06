import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):  # This will be a normal window, and we'll be able to add functions
    def __init__(self):
        super().__init__()  # To use the __init__ in QWidget and create a window
        self.init_ui()  # We assigned this below

    def init_ui(self):
        self.button = QtWidgets.QPushButton("Click Me")
        self.text_area = QtWidgets.QLabel("I Haven't Been Clicked Yet")
        self.count = 0  # It will count how many times you clicked to the button

        # To set a vertical layout
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.button)
        v_box.addWidget(self.text_area)
        v_box.addStretch()

        # To add vertical layout into horizontal layout
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)  # To set the type of Layout

        self.button.clicked.connect(self.click)  # To connect the function

        self.show()  # To show the window

    def click(self):  # We change the text_area's text as how many times we clicked the button
        self.count += 1
        self.text_area.setText("Clicked me " + str(self.count) + " times")


app = QtWidgets.QApplication(sys.argv)

window = Window()  # To run the program

sys.exit(app.exec_())


