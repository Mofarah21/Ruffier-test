# write code here for the second screen of the application
# write a code for the second app
# write here a code for the main app and the first screen
from PyQt5.QtCore import (Qt, QTimer,QTime,QLocale)
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, QHBoxLayout,QVBoxLayout)
from instr import *
from final_win import Screen3
from PyQt5.QtGui import QFont
#Classes

class Experiment():
    def __init__(self, name, age, test1, test2, test3):
        self.name = name
        self.age = age
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3


        
class Screen2(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
        self.connect()
        self.setAppear()
        self.show()
    def UI(self):
        self.title = QLabel("Enter your full name:")
        self.name = QLineEdit("Full name")
        self.instruction1 = QLabel("Full years")
        self.age = QLineEdit("0")
        self.instruction2 = QLabel("Lie on your back and take your pulse for 15 sec. Click the Start first Button  to start the timer." )
        self.button = QPushButton("start the first test")
        self.pulse = QLineEdit("0")
        self.instruction3 = QLabel("Perform 30 squats in 45 seconds.To do this click the Start doing Squats Button to start the counter")
        self.button2 = QPushButton("Start doing squats")
        self.instruction4 = QLabel("Lie on your back and take your pulse for the first 15 sec of the min, then for the last 15 sec of the min Press the start final test Button to start the timer")
        self.button3 = QPushButton("Start the final test")
        self.test1 = QLineEdit("0")
        self.test2 = QLineEdit("0")
        self.clock = QLabel("00:00:00")
        self.button4 = QPushButton("Send the results")

        self.Left_layout = QVBoxLayout()
        self.Right_layout = QVBoxLayout()
        self.H_layout= QHBoxLayout()
        self.Right_layout.addWidget(self.clock, alignment= Qt.AlignCenter)
        self.Left_layout.addWidget(self.title, alignment= Qt.AlignLeft)
        self.Left_layout.addWidget(self.name, alignment= Qt.AlignLeft)
        self.Left_layout.addWidget(self.instruction1, alignment= Qt.AlignLeft)
        self.Left_layout.addWidget(self.age, alignment= Qt.AlignLeft)
        self.Left_layout.addWidget(self.instruction2, alignment= Qt.AlignLeft)
        self.Left_layout.addWidget(self.button, alignment= Qt.AlignLeft)
        self.Left_layout.addWidget(self.pulse, alignment= Qt.AlignLeft)
        self.Left_layout.addWidget(self.instruction3, alignment= Qt.AlignLeft)
        self.Left_layout.addWidget(self.button2, alignment= Qt.AlignLeft)
        self.Left_layout.addWidget(self.instruction4, alignment= Qt.AlignLeft)
        self.Left_layout.addWidget(self.button3, alignment= Qt.AlignLeft)
        self.Left_layout.addWidget(self.test1, alignment= Qt.AlignLeft)
        self.Left_layout.addWidget(self.test2, alignment= Qt.AlignLeft)
        self.Left_layout.addWidget(self.button4, alignment= Qt.AlignCenter)
        
        self.H_layout.addLayout(self.Left_layout)
        self.H_layout.addLayout(self.Right_layout)
        self.setLayout(self.H_layout)

    def Start(self):
        self.exp = Experiment(self.name.text(), int(self.age.text()),int(self.pulse.text()),int(self.test1.text()),int(self.test2.text()))
        self.hide()
        self.win = Screen3(self.exp)

    
    def Timer1(self):
        global time 
        time = QTime(0,0,15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.Timer1Event)
        self.timer.start(1000)

    def Timer2(self):
        global time 
        time = QTime(0,0,45)
        self.timer = QTimer()
        self.timer.timeout.connect(self.Timer2Event)
        self.timer.start(1500)

    def Timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.clock.setText(time.toString("hh:mm:ss"))
        #self.clock.setFont(QFont("Times New Roman",40,QFont.bold))
        self.clock.setStyleSheet("color: rgb(255,255,255)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    
    def Timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.clock.setText(time.toString("hh:mm:ss"))
        #self.clock.setFont(QFont("Times New Roman",40,QFont.bold))
        self.clock.setStyleSheet("color: rgb(255,255,255)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def Timer3(self):
        global time 
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.Timer3Event)
        self.timer.start(500)

    def Timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.clock.setText(time.toString("hh:mm:ss"))
        #self.clock.setFont(QFont("Times New Roman",40,QFont.bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

        if int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.clock.setStyleSheet("color: rgb(255,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 45:
            self.clock.setStyleSheet("color: rgb(255,0,0)")
        else:
            self.clock.setStyleSheet("color: rgb(255,255,255)")
        




    
    def connect(self):
        self.button4.clicked.connect(self.Start)
        self.button.clicked.connect(self.Timer1)
        self.button2.clicked.connect(self.Timer2)
        self.button3.clicked.connect(self.Timer3)



    def setAppear(self):
        self.setWindowTitle("Health")
        self.resize(winWidth,winHeight)
        self.move(winx,winy)
