import sys
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout,QHBoxLayout
#We only want these modules so we wrote it like this


class Window(QWidget):
    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.checkbox = QCheckBox("Do you love memes?") # To add a chech box
        self.text_area = QLabel("")
        self.button = QPushButton("Click")

        v_box = QVBoxLayout()
        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.text_area)
        v_box.addWidget(self.button)

        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("Checkbox")


        self.button.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.text_area))
        # If check box is checked then this statement is return True, else False
        # If we don't use lambda, this line becomes a function call. Since we need to send a function object inside the connect object, we convert this call to an object with lambda

        self.show()

    def click(self, checkbox,text_area):
        if checkbox:
            text_area.setText("You are awesome!")
        else:
            self.text_area.setText("Not good for you...")

app = QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())