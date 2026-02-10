import sys 
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                              QVBoxLayout, QHBoxLayout, QDesktopWidget)
from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget): 
    def __init__(self): 
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00:00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.running = False
        self.initUI()

    def central_widget(self): 
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showEvent(self, event): 
        self.central_widget() 
        super().showEvent(event)

    def initUI(self): 
        self.setWindowTitle("Stop Watch")
        self.setFocusPolicy(Qt.StrongFocus)
        
        vbox = QVBoxLayout() 
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        
        vbox.addLayout(hbox)

        #You can pick the color from any color picker online
        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 10px; 
            }
            QPushButton{
                font-size: 30px;
                border-radius: 20px;
                background-color: #d6d6d6;
                border: 2px solid #888;
                border-radius: 15px;
                font-family: VT323;
            }
            QPushButton:hover{
                background-color: #e6e6e6;
            }
            QPushButton:pressed{
                background-color: #c6c6c6;
            }
            QLabel{
                font-size: 100px;       
                background-color: hsl(0, 76%, 84%);      
                border-radius: 20px;
                font-family: share tech mono;
            }
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self): 
        self.timer.start(10)
        self.running = True
        self.setFocus()

    def stop(self): 
        self.timer.stop()
        self.running = False
    
    def reset(self): 
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time): 
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() //10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self): 
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space and not event.isAutoRepeat():
            if self.running: 
                self.stop()
            else: 
                self.start()

def main(): 
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())

if __name__ == "__main__": 
    main()