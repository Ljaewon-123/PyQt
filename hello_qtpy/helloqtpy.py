import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# ui파일 가져옴  
form_class = uic.loadUiType('C:\\Work_spaces\\PyQt\\hello_qtpy\\hello_qtpy_text.ui')[0]
class WindowClass(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# 어플리케이션 실행 가능한 앱이라는 놈을 만듬
# 실행시 argv 요청이되면 argv를 전달
app = QApplication(sys.argv)

mainWindow = WindowClass()
mainWindow.show()
app.exec_()  # app실행
