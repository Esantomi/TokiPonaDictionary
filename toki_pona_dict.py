# 입력받아 뜻 찾아주기
import csv

def searchDict(lukin):
    with open('words_ordered.csv') as csv_dict:
        reader = csv.DictReader(csv_dict)
        # lukin = input("단어를 입력하세요 : ")
        for row in reader:
            # print(row)
            if lukin == row.get('단어'):
                return print(row.get('뜻'))
            else:
                continue

# searchDict('mun')


# PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QDesktopWidget
from PyQt5.QtGui import QIcon

class TokiPonaDictApp(QWidget):

    # 생성자 설정
    def __init__(self):
        super().__init__()
        self.initUI()

    # UI 초기 설정
    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.move(60, 40)

        qle = QLineEdit(self)
        qle.move(60, 100)
        qle.textChanged[str].connect(self.onChanged)

        self.setWindowTitle('한국어-도기 보나 사전')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(300, 300, 300, 200)
        self.center()
        self.show()
    
    # 가운데 정렬
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def onChanged(self, text):
        self.lbl.setText(searchDict(text))
        self.lbl.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TokiPonaDictApp()
    sys.exit(app.exec_())