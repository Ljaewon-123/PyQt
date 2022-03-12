import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# ui파일 가져옴  
form_class = uic.loadUiType('C:\\Work_spaces\\PyQt\\03_notepad_Menubar\\note_pad.ui')[0]
class WindowClass(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.actionopen.triggered.connect(self.openFunction)
        self.actionsave.triggered.connect(self.saveFunction)
    def openFunction(self):
        print('open!!')

    def saveFunction(self):
        print('save!!')
# 어플리케이션 실행 가능한 앱이라는 놈을 만듬
# 실행시 argv 요청이되면 argv를 전달
app = QApplication(sys.argv)

mainWindow = WindowClass()
mainWindow.show()
app.exec_()  # app실행
