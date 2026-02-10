import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QDesktopWidget
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont

class DigitalClock(QWidget): 
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self): 
        self.setWindowTitle("Digital Clock") 
        self.resize(300, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("""
                font-size: 90px; 
                font-family: "VT323";
                color: rgb(252, 0, 0);                     
            """)

        self.setStyleSheet("background-color: black")

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()
    
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

    def center_window(self): 
        qr = self.frameGeometry() 
        cp = QDesktopWidget().availableGeometry().center() 
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showEvent(self, event):  #Without this central_window function will not work
        self.center_window()
        super().showEvent(event)


def main(): 
    app = QApplication(sys.argv) 
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())

if __name__ == "__main__": 
    main()
