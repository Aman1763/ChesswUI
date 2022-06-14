# Imports
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Chess_View import Chess_View

if __name__ == '__main__':
    pychess = QApplication(sys.argv)
    view = Chess_View()
    view.show()

    sys.exit(pychess.exec_())


