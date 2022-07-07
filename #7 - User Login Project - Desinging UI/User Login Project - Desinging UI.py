import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.user_name = QtWidgets.QLineEdit() # Take input from user as user name
        self.password = QtWidgets.QLineEdit() # Take input from user as password
        self.password.setEchoMode(QtWidgets.QLineEdit.Password) # To make password "******"
        self.login = QtWidgets.QPushButton("Login")
        self.text_area = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.user_name)
        v_box.addWidget(self.password)
        v_box.addWidget(self.text_area)
        v_box.addStretch()
        v_box.addWidget(self.login)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()


        self.setLayout(h_box)

        self.setWindowTitle("User Login")
        self.show()


app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())







