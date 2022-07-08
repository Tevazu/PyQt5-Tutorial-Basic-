import sys
from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout,QHBoxLayout
                                            # We use RadioButton module


class Window(QWidget):
    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.radio_text = QLabel("Which anime did you watch ?")
        self.onepiece = QRadioButton("One Piece") # Ok I know it hasn't finished yet lol
        self.naruto = QRadioButton("Naruto")
        self.bleach = QRadioButton("Bleach")

        self.text_area = QLabel("")
        self.button = QPushButton("Send")

        v_box = QVBoxLayout()
        v_box.addWidget(self.radio_text)
        v_box.addWidget(self.onepiece)
        v_box.addWidget(self.naruto)
        v_box.addWidget(self.bleach)
        v_box.addStretch()
        v_box.addWidget(self.text_area)
        v_box.addWidget(self.button)

        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("Radio Button")

        self.button.clicked.connect(lambda : self.click(self.onepiece.isChecked(),self.naruto.isChecked(),self.bleach.isChecked(),self.text_area))

        self.show()

    def click(self,onepiece,naruto,bleach,text_area):
        if onepiece:
            text_area.setText("I wanna be Pirate King")
        if naruto:
            text_area.setText("I wanna be Hokage")
        if bleach:
            text_area.setText("Rukia...")
        else:
            text_area.setText("You should watch one of these!(Demon Slayer is also awesome)")
        # Here we used only if because these situations are independent
app = QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())




