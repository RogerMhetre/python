import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 250, 250)

        label = QLabel(self)
        label.setGeometry(0,0,150, 150)

        pixmap = QPixmap("Python-Code/Tame-Impala-Currents-final-packshot-1200px_1000.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry((self.width()- label.width()) // 2, 
                            (self.height() - label.height())//2, 
                            label.width(), 
                            label.height())

def main(): 
    app = QApplication(sys.argv)
    window = MainWindow() 
    window.show()
    sys.exit(app.exec_())

if __name__  == "__main__": 
    main()