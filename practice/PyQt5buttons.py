import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout


class Mainwindow(QMainWindow): 
    def __init__(self): 
        super().__init__()
        self.button = QPushButton("Click me Nigga!! yayyyy", self)
        self.setGeometry(700, 500, 500, 500)
        self.initUI() 

    def initUI(self): 
        self.setWindowTitle("Nigga")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.button.setStyleSheet("font-size:16px ;padding: 10px")

        layout.addWidget(self.button)

        self.button.clicked.connect(self.on_click)
        
    def on_click(self): 
        self.button.setText("the button was clicked")

def main(): 
    app = QApplication(sys.argv)
    window = Mainwindow() 
    window.show() 
    sys.exit(app.exec_())

if __name__ == "__main__": 
    main()