import sys
import os  # Because we will open and save file
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QFileDialog,QVBoxLayout,QHBoxLayout


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

        self.show()

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

app = QApplication(sys.argv)

notepad = Notepad()

sys.exit(app.exec_())