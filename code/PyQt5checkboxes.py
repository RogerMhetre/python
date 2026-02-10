import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.checkbox = QCheckBox("Do you like something", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("CHeckbox") 
        self.checkbox.setGeometry(0,0,200, 100)
        self.setGeometry(700, 300, 250, 250) 
        self.checkbox.setStyleSheet("font-size: 15px; font-family: Ubuntu Sans Mono")
        self.checkbox.setChecked(False) 
        self.checkbox.stateChanged.connect(self.checkboxchanged)
    
    def checkboxchanged(self, state): 
        if state == Qt.Checked: 
            print("Ooh then fuck yourself nigga")
        else : 
            print("Yea you are boring asl")

def main(): 
    app = QApplication(sys.argv) 
    window = MainWindow() 
    window.show() 
    sys.exit(app.exec_())

if __name__ == "__main__": 
    main()