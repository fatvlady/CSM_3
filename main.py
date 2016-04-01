# coding: utf8

import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow
from model import FadingOscillation

app = QApplication(sys.argv)
app.setApplicationName('CSM_3')
# -----------------------------------------------------#

form = MainWindow()
form.setWindowTitle('Лабораторная работа №3')
form.show()
f = FadingOscillation(1,2)
f.test_ls()
# -----------------------------------------------------#
sys.exit(app.exec_())
