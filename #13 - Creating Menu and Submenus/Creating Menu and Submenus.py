import sys
from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow
#All menus should be created in QMainWindow. It's a main window and we can add our other widgets (windows) in this main window


class Menu (QMainWindow): # We changed the module here to create menus
    def __init__(self):

        super().__init__()

        menubar = self.menuBar()  # We should add a menubar because all menus will be in here

        file = menubar.addMenu("File")  # To add 'File' menu
        edit = menubar.addMenu("Edit")  #To add 'Edit' menu

        #--------------------------- Now we will add actions to these menus ---------------------------
        open_file = QAction("Open File",self)  # If we don't write self, it will be ineffective
        open_file.setShortcut("Ctrl+O")  # We added a shortcut (You shouldn't leave spaces between words)

        save_file = QAction("Save File",self)
        save_file.setShortcut("Ctrl+S")

        exit = QAction("Exit",self)
        exit.setShortcut("Ctrl+Q")

        # The actions are not added to the menus yet, because we have to add them to the file menu

        file.addAction(open_file)  # We added 'Open File' action to 'File' menu
        file.addAction(save_file)  # We added 'Save File' action to 'File' menu
        file.addAction(exit)  # We added 'Exit' action to 'File' menu

        #--------------------------- Now we will add a submenu to Edit menu ---------------------------
        find_and_replace = edit.addMenu("Find and Replace")  # To add submenu inside 'Edit' menu


        find = QAction("Find",self)  #Do same things as 'File' menu
        replace = QAction("Replace",self)
        clean_up = QAction("Clean Up",self)

        find_and_replace.addAction(find)  # We added 'Find' action to 'Find and Replace' submenu
        find_and_replace.addAction(replace)  # We added 'Replace' action to 'Find and Replace' submenu
        edit.addAction(clean_up) # We added 'Clean Up' action to 'Edit' menu

        #--------------------------- Now we will add functions to actions ---------------------------

        exit.triggered.connect(self.quit)  # To set a exit function

        file.triggered.connect(self.response)  # To understand which action is triggered

        # You can add other functions to actions

        self.setWindowTitle("Menus")

        self.show()

    def quit(self):
        qApp.quit()  # We use quit function to quit the app when the Exit button is triggered

    def response(self,action): # When we created this function above, Python automatically created a variable. So we assigned it to as 'action'
        if action.text() == "Open File":
            print("Clicked 'Open File'")  # Program will write this in your IDE's run panel

        elif action.text() == "Save File":
            print("Clicked 'Save File'")  # Program will write this in your IDE's run panel

        elif action.text() == "Exit":
            print("Clicked 'Exit'")  # Program will write this in your IDE's run panel

app = QApplication(sys.argv)

menu = Menu()

sys.exit(app.exec_())
