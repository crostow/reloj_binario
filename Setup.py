from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QApplication
import time
import Interfaz
import segundos, minutos, horas
import sys


class Reloj(QWidget):
    def __init__(self, parent = None):
        super(Reloj, self).__init__(parent)

        self.ui = Interfaz.Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("Reloj binario")
        timer = QTimer(self)
        timer.timeout.connect(self.reloj)
        timer.start(1000)


    def reloj(self):
        self.ui.label_25.setText(time.strftime("%H:%M:%S"))
        self.ui.label_25.setAlignment(Qt.AlignCenter)
        self.ui.label_25.setFont(QFont("arial",16))
        h = (time.strftime("%H"))
        m = (time.strftime("%M"))
        s = (time.strftime("%S"))
        self.segundo(s,m,h)

    def segundo(self, s, m, h):
        vs = s
        vm = m
        vh = h
        segundos.seg(self,vs)
        minutos.min(self, vm)
        horas.hrs(self, vh)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Reloj()
    ventana.show()
    sys.exit(app.exec())
