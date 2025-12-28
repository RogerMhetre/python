import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt, QPoint, QRect, QPropertyAnimation
from PyQt5.QtGui import QPainter, QPolygon, QColor, QRegion, QPen

class CustomWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(600, 400)
        self.cut = 25
        self.drag_pos = None
        self.resizing = False

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.close_btn = QPushButton("✕", self)
        self.min_btn = QPushButton("–", self)

        for b in (self.close_btn, self.min_btn):
            b.setFixedSize(30, 30)
            b.setCursor(Qt.PointingHandCursor)

        self.close_btn.clicked.connect(self.closeAnimated)
        self.min_btn.clicked.connect(self.showMinimized)

        self.close_btn.setStyleSheet(
            "background:#e74c3c;color:white;border:none;"
        )
        self.min_btn.setStyleSheet(
            "background:#555;color:white;border:none;"
        )

        self.opacity_anim = QPropertyAnimation(self, b"windowOpacity")
        self.opacity_anim.setDuration(300)

        self.updateShape()

    def updateShape(self):
        w, h = self.width(), self.height()
        c = self.cut

        self.polygon = QPolygon([
            QPoint(c, 0),
            QPoint(w - c, 0),
            QPoint(w, c),
            QPoint(w, h - c),
            QPoint(w - c, h),
            QPoint(c, h),
            QPoint(0, h - c),
            QPoint(0, c)
        ])

        self.setMask(QRegion(self.polygon))

    def resizeEvent(self, event):
        self.updateShape()
        self.close_btn.move(self.width() - 40, 10)
        self.min_btn.move(self.width() - 80, 10)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setBrush(QColor(0, 0, 0, 130))
        painter.setPen(Qt.NoPen)
        painter.drawPolygon(self.polygon.translated(6, 6))

        painter.setBrush(QColor(30, 30, 30))
        painter.drawPolygon(self.polygon)

        painter.setPen(QPen(QColor(90, 90, 90), 1.5))
        painter.setBrush(Qt.NoBrush)
        painter.drawPolygon(self.polygon)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            if QRect(self.width()-20, self.height()-20, 20, 20).contains(event.pos()):
                self.resizing = True

    def mouseMoveEvent(self, event):
        if self.resizing:
            self.resize(event.pos().x(), event.pos().y())
        elif self.drag_pos and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_pos)

    def mouseReleaseEvent(self, event):
        self.drag_pos = None
        self.resizing = False

    def showEvent(self, event):
        self.setWindowOpacity(0)
        self.opacity_anim.setStartValue(0)
        self.opacity_anim.setEndValue(1)
        self.opacity_anim.start()

    def closeAnimated(self):
        self.opacity_anim.setStartValue(1)
        self.opacity_anim.setEndValue(0)
        self.opacity_anim.finished.connect(self.close)
        self.opacity_anim.start()


class MainWindow(CustomWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chamfered Window")

def main(): 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
