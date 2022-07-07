import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.text_area = QtWidgets.QLineEdit() # Now we'll be able to take input from the user
        self.text_area2 = QtWidgets.QLabel("Print Button Hasn't Been Clicked Yet")
        self.count = 0
        self.clean = QtWidgets.QPushButton("Clean")
        self.print = QtWidgets.QPushButton("Print")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.text_area)
        v_box.addWidget(self.clean)
        v_box.addWidget(self.print)
        v_box.addWidget(self.text_area2)
        v_box.addStretch()

        self.setLayout(v_box)

        self.clean.clicked.connect(self.click)
        self.print.clicked.connect(self.click)

        self.show()

    # We use "sender" function from QWidget here which understands which button is clicked
    def click(self):
        sender = self.sender()

        if sender.text() == "Clean":
            self.text_area.clear() # This function clear everything in text_area
        else:
            self.count += 1
            self.text_area2.setText("Clicked Print " + str(self.count) + " times")
            print(self.text_area.text())


app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())