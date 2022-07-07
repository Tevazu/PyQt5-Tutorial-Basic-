
# We'll continue from the previous one (#7 project in the github list) but this time we'll create a database
# To create a database we use sqlite3 and a software "DB Browser for SQLite"
# You need a basic sqlite knowledge here. You can check my github, "Sqlite-Tutorial-Basic-" to gain some info about sqlite codes


import sys
import sqlite3
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.create_link() #We'll call this function to create a database
        self.init_ui()

    def create_link(self):
        link = sqlite3.connect("database.db") # We create a database named "database.db"
                                              # DON'T FORGET TO IMPORT sqlite3
        self.cursor = link.cursor() # To wander on this database we need a cursor
        self.cursor.execute("Create Table If not exists members (user_name TEXT, password TEXT)") # We create a table on database
        link.commit() # To make the changes in database valid

    # Now run the program and you'll see a database.db file has been created in the same path as your program
    # You can add a user and password following these steps:
    # 1: Open database file with "DB Browser for Sqlite" / 2: Go to "Enable SQL" / 3: Type Insert into members Values("a user name","a password") / 4: Run
    # Now if you go "Browse Data" you will see what you typed as user name in username table and password in password table
    # You can save and close "DB Browser for Sqlite"


    def init_ui(self):
        self.user_name = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.log_in = QtWidgets.QPushButton("Login")
        self.text_area = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.user_name)
        v_box.addWidget(self.password)
        v_box.addWidget(self.text_area)
        v_box.addStretch()
        v_box.addWidget(self.log_in)

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()


        self.setLayout(h_box)

        self.setWindowTitle("User Login")

        self.log_in.clicked.connect(self.login)

        self.show()

    def login(self):
        names = self.user_name.text()
        pas = self.password.text()

        self.cursor.execute("Select * From members where user_name = ? and password = ?",(names,pas))
        data = self.cursor.fetchall()

        if len(pas) == 0: # If the password is not entered
            self.text_area.setText("Please enter the password.")

        elif len(names) == 0: # If the user name is not entered
            self.text_area.setText("Please enter the user name.")

        elif len(data) == 0: #If the data we entered isn't matching with database
            self.text_area.setText("User name or password is incorrect\nPlease try again.")

        else: # If the data we entered is matching with database
            self.text_area.setText("Welcome " + names)

app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())
