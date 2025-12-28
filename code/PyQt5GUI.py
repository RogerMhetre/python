import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Nothing")
        self.setWindowIcon(QIcon("Python-Code/Tame-Impala-Currents-final-packshot-1200px_1000.jpg"))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()