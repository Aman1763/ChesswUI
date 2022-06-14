import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Chess_View(QMainWindow):

    def __init__(self):
        #Initializing the basic chess screen
        super().__init__()
        self.setWindowTitle("Chess")
        self.setFixedSize(1400, 1400)
        self.move(250, 0)
        self.setStyleSheet("background-color: lightgray")

        #Setting the ideal chess board widget for the entire screen
        self.chessWidget = QWidget(self)
        self.chessWidget.move(0, 0)
        self.chessWidget.setFixedSize(1200, 1200)

        #Creating a chess layout using grid layouts
        self.chessBoard = QGridLayout()
        self.__createChessBoard()

    def __createChessBoard(self):
        #Placing the notations on the chess board
        self.notations = {(0,0): "8", (1, 0): "7", (2, 0): "6", (3, 0): "5", (4, 0): "3", (5, 0): "2", (6, 0): "2", (7, 0): "1",
                          (8,0): "", (8,1): "A", (8,2): "B", (8,3): "C", (8,4): "D", (8,5): "E", (8,6): "F", (8,7): "G", (8,8): "H"}

        for pos in self.notations:
            oneNotation = QLabel(self.notations[pos], self)
            oneNotation.setFont(QFont("Calibri", 12))
            self.chessBoard.addWidget(oneNotation, pos[0], pos[1])

        #Placing the black and white squares on the screen
        self.userWhiteButtons = {}
        self.whiteButtons = {(0, 1), (0, 3), (0, 5), (0, 7)}

        self.userBrownButtons = {}
        self.brownButtons = {(0,2), (0,4), (0,6), (0,8)}

        for pos in self.whiteButtons:
            self.userWhiteButtons[pos] = QPushButton()
            self.userWhiteButtons[pos].setStyleSheet("background-color: white")
            self.chessBoard.addWidget(self.userWhiteButtons[pos], pos[0], pos[1])

        for pos in self.brownButtons:
            self.userBrownButtons[pos] = QPushButton()
            self.userBrownButtons[pos].setStyleSheet("background-color: lightbrown")
            self.chessBoard.addWidget(self.userBrownButtons[pos], pos[0], pos[1])

        self.chessWidget.setLayout(self.chessBoard)
