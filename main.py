import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from brainMirror import temp, conditions, time

class Win(QWidget):

    def paintEvent(self, event):

        font = QFont("Times new Roman", 50)

        painter = QPainter(self)
        painter.setFont(font)

        painter.save()
        painter.translate(150, 100)
        painter.scale(2, 2)
        painter.rotate(0)
        painter.drawText(0, 0, str(time))
        painter.restore()

        painter.save()
        painter.translate(100, 300)
        painter.scale(0.7, 0.7)
        painter.rotate(0)
        painter.drawText(0, 0, str(round(temp[-1], 1)))
        painter.restore()

        painter.save()
        painter.translate(200, 300)
        painter.scale(0.9, 0.9)
        painter.rotate(0)
        painter.drawText(0, 0, str(conditions[-1]))
        painter.restore()

app = QApplication(sys.argv)
win = Win()
win.show()

app.exec_()
