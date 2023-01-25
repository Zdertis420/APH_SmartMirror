import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import brainMirror

temp = brainMirror.temper
windSpeed = brainMirror.windspeed
time = brainMirror.time


class Win(QWidget):

    def paintEvent(self, event):
        font = QFont("Times New Roman", 50)
        font.setItalic(False)

        painter = QPainter(self)
        painter.setFont(font)

        painter.save()
        painter.translate(100, 100)
        painter.scale(0.7, 0.7)
        painter.rotate(0)
        painter.drawText(0, 0, time)
        painter.restore()

        painter.save()
        painter.translate(100, 200)
        painter.scale(0.7, 0.7)
        painter.rotate(0)
        painter.drawText(0, 0, temp)
        painter.restore()

        painter.save()
        painter.translate(100, 300)
        painter.scale(0.7, 0.7)
        painter.rotate(0)
        painter.drawText(0, 0, f'{windSpeed} м/с')
        painter.restore()


app = QApplication(sys.argv)
win = Win()
win.show()

app.exec_()
