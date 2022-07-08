import sys
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QHBoxLayout


class Window(QWidget):
    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.text_area = QTextEdit() # Now we can enter input to this text area
        self.clean = QPushButton("Clean")
        self.text_area2 = QLabel("Enter anything:")

        v_box = QVBoxLayout()
        v_box.addWidget(self.text_area2)
        v_box.addWidget(self.text_area)
        v_box.addWidget(self.clean)

        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("Text Area")

        self.clean.clicked.connect(self.click)

        self.show()

    def click(self):
        self.text_area.clear()

app = QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())