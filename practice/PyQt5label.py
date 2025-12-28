import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont 
from PyQt5.QtCore import Qt 

class MainWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Nothing")
        self.setGeometry(0,0, 250, 250)
        
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0,0,500, 500)
        label.setStyleSheet("color: lightgreen;"
                            "background-color: black;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        
        # label.setAlignment(Qt.AlignTop)     #vertically top 
        # label.setAlignment(Qt.AlignBottom)      #vertically bottom
        # label.setAlignment(Qt.AlignVCenter)    #Vertically center
                
        # label.setAlignment(Qt.AlignRight)       #Horizantal right
        # label.setAlignment(Qt.AlignLeft)        #Horizontal left
        # label.setAlignment(Qt.AlignHCenter)      #Horizontally center 

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)      to join two flags

        # label.setAlignment(Qt.AlignCenter)


        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 20))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: lightgreen;"
                            "background-color: black;"
                            "font-weight: bold;"
                                "font-style: italic;"
                            "text-decoration: underline;")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()