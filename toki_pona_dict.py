# PyQt5
import sys, os, csv
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import uic

# UI파일 연결
form_class = uic.loadUiType(os.path.join(os.path.abspath('TokiPonaDictionary'), 'ui.ui'))[0]

#화면을 띄우는데 사용되는 Class 선언
class TokiPonaDictionary(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('lipu nimi pi toki Anku')
        self.setWindowIcon(QIcon(os.path.join(os.path.abspath('TokiPonaDictionary'), 'icon.png')))

        #버튼에 기능을 연결하는 코드
        self.pushButton.clicked.connect(self.searchButtonFunction)

    # 검색 버튼 클릭 시 발생 이벤트
    def searchButtonFunction(self) :
        with open(os.path.join(os.path.abspath('TokiPonaDictionary/data'), 'words_ordered.csv'), encoding = 'UTF8') as csv_dict:
            reader = csv.DictReader(csv_dict)
            for row in reader:
                # print(row)  # 전체 행 출력
                if self.lineEdit.text() == row.get('단어'):
                    # print(row.get('단어'))  # 입력한 단어 하나만
                    self.lineEdit.setText(row.get('뜻'))
                else:
                    continue

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tp_program = TokiPonaDictionary() 
    tp_program.show()
    app.exec_()