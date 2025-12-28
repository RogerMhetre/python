import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup, QPushButton

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__()
        self.setGeometry(700, 300, 250, 250)
        self.radio1 = QRadioButton("Visa", self)            #Creating radiobutton
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("Gift card", self)
        self.radio4 = QRadioButton("In-Store", self) 
        self.radio5 = QRadioButton("Online", self)
        self.button_group1 = QButtonGroup(self)     #Creating Buttongroup
        self.button_group2 = QButtonGroup(self)
        self.initUI()

    def initUI(self): 
        self.radio1.setGeometry(0, 0, 300, 50)      #setGeometry 
        self.radio2.setGeometry(0, 30, 300, 50)     #you can even use layouts for working dynamic
        self.radio3.setGeometry(0, 60, 300, 50)
        self.radio4.setGeometry(0, 90, 300, 50)
        self.radio5.setGeometry(0, 120, 300, 50)

        self.setStyleSheet("""
                           QRadioButton{
                            font-size: 25px;
                            font-family: IBM Plex Mono;
                            padding: 10px;
                            font-weight: bold;
                           }""")
        
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)

        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)      #connecting signal
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)   
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self): 
        radio_button = self.sender()  #Determines which button is touched 
        if radio_button.isChecked(): 
            print(f"{radio_button.text()} is selected")

def main(): 
    app = QApplication(sys.argv) 
    window = MainWindow() 
    window.show() 
    sys.exit(app.exec_())

if __name__ == "__main__": 
    main()