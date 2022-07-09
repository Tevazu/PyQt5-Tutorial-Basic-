import sys
import os  # Because we will open and save file
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QFileDialog
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QAction,qApp,QMainWindow

class Notepad(QWidget):
    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.text_area = QTextEdit()
        self.text_area2 = QLabel("Enter anything:")
        self.clean = QPushButton("Clean")
        self.open = QPushButton("Open")
        self.save = QPushButton("Save")

        h_box = QHBoxLayout()
        h_box.addWidget(self.clean)
        h_box.addWidget(self.open)
        h_box.addWidget(self.save)

        v_box = QVBoxLayout()
        v_box.addWidget(self.text_area2)
        v_box.addWidget(self.text_area)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.setWindowTitle("NotePad")

        self.clean.clicked.connect(self.clean_text)
        self.open.clicked.connect(self.open_file)
        self.save.clicked.connect(self.save_file)

        #self.show() ----> Now we don't need this no more because we have another and it makes UI looks weird. You can try to check if you want

    def clean_text(self):
        self.text_area.clear()

    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self, "Open File", os.getenv("HOME"))
        #This code will open the file selection window when you click 'Open'
        with open (file_name[0],"r") as file:
            self.text_area.setText((file.read()))  #Now try to open any file that includes text, its content will be printed to the text box

    def save_file(self):
        file_name = QFileDialog.getSaveFileName(self, "Save File", os.getenv("HOME"))
        with open (file_name[0],"w") as file:
            file.write(self.text_area.toPlainText())  #Now we'll be able to save what did we write on text box as file

class Menu(QMainWindow):
    def __init__(self):

        super().__init__()

        self.window = Notepad()  # We created a window, now we need to put it in Menu

        self.setCentralWidget(self.window)  # We add a window in the main window

        self.create_menus()  # We assigned a function

    def create_menus(self):  #Creating the function above
        menubar = self.menuBar()
        file = menubar.addMenu("File")

#----------------------------- Actions -----------------------------

        open_file = QAction("Open File",self)
        open_file.setShortcut("Ctrl+O")

        save_file = QAction("Save File",self)
        save_file.setShortcut("Ctrl+S")

        clean_up = QAction("Clean Up",self)
        clean_up.setShortcut("Ctrl+D")

        exit = QAction("Exit",self)
        exit.setShortcut("Ctrl+Q")

        file.addAction(open_file)
        file.addAction(save_file)
        file.addAction(clean_up)
        file.addAction(exit)

        self.setWindowTitle("Text Editor")

        self.show()

#------------------------- Functions -------------------------

        #exit.triggered.connect(self.quit)
        file.triggered.connect(self.response)

    def response(self,action):
        if action.text() == "Open File":
            print("Clicked 'Open File'")
            self.window.open_file()  # Here we used Notepad class' function because when we typed "self.window = Notepad()" in Menu class' init
                                    # we took all functions from Notepad class, that's why there is no need to write those codes again in Menu class (OOP <3)

        elif action.text() == "Save File":
            print("Clicked 'Save File'")
            self.window.save_file()  # Same as above

        elif action.text() == "Clean Up":
            print("Clicked 'Clean Up'")
            self.window.clean_text()  # Same as above

        elif action.text() == "Exit":
            print("Clicked 'Exit'")
            qApp.quit()

app = QApplication(sys.argv)

menu = Menu()  # We changed this because we want to add menu in this project

sys.exit(app.exec_())