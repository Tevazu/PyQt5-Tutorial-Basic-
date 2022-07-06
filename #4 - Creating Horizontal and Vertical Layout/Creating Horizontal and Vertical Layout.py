import sys
from PyQt5 import QtWidgets

def Window():
    app = QtWidgets.QApplication(sys.argv)

    # Here instead giving value name "window", we assign button names now
    okay = QtWidgets.QPushButton("OK")
    cancel = QtWidgets.QPushButton("Cancel")

    #--------------------------------- Horizontal Layout ---------------------------------

    h_box = QtWidgets.QHBoxLayout() # "h_box" is now a horizontal box layout
    #h_box.addStretch() # If you put this here, buttons will stick to right
    h_box.addWidget(okay)
    #h_box.addStretch() # If you put this here; okay button will stick to left, cancel button will stick to right
    h_box.addWidget(cancel)
    h_box.addStretch() # If you put this here, buttons will stick to left

    # --------------------------------- Vertical Layout ---------------------------------

    #v_box = QtWidgets.QVBoxLayout()
    # v_box.addStretch() # If you put this here, buttons will stick to bottom
    #v_box.addWidget(okay)
    # v_box.addStretch() # If you put this here; okay button will stick to top, cancel button will stick to down
    #v_box.addWidget(cancel)
    # v_box.addStretch() # If you put this here, buttons will stick to bottom

    #---------------------------------Nested Layouts---------------------------------

    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)

    # To add vertical layout into horizontal layout and make buttons set bottom right
    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)

#----------------------------------------------------------------------------------------
    window = QtWidgets.QWidget()

    window.setWindowTitle("PyQt5 Template 4")

    # For layout, type h_box for horizontal layout, type v_box for vertical layout
    #If you use it for Nested Layout Part you should type v_box
    window.setLayout(v_box) # To set the type of Layout
    window.setGeometry(100,100,500,500)
    window.show()

    sys.exit(app.exec_())

Window()

