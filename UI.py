from PyQt5 import QtCore, QtWidgets

class Ui_Form(object):
    def setupUi(self, page):
        form_w = 440
        form_h = 160
        page.resize(form_w, form_h)
        page.setWindowTitle('HoloCure修改器 by AUSTIN2526')
        
        self.makelabel(page, 105, 10, 2000, 30,'【啟動遊戲後按偵測按鈕遊戲即可啟用功能】')
        #偵測遊戲
        self.page_button = QtWidgets.QPushButton(page)
        self.page_button.setGeometry(QtCore.QRect(10,10,100,30))
        self.page_button.setText('偵測遊戲')
        
        #入場前數據
        func_name = ['鎖血無敵', '無限特殊技能', '全圖撿物','增加HoloCoin', '增加攻擊力', '增加Haste']
        self.makelabel(page, 10, 50, 2000, 30,'↓↓↓↓↓↓↓↓↓↓功能選擇區↓↓↓↓↓↓↓↓↓↓')
        self.extra_func = []
        for i in range(3):
            for j in range(2):
                index = j + i * 2
                self.extra_func.append(QtWidgets.QCheckBox(page))
                self.extra_func[index].setGeometry(QtCore.QRect(10 + 140*i, 80 + j*30, 2000, 30))
                self.extra_func[index].setText(func_name[index])
                self.extra_func[index].setEnabled(False)
           
    def makelabel(self, page, x=10, y=10, w=10, h=20, text='', s=True):
        self.label = QtWidgets.QLabel(page)
        self.label.setGeometry(QtCore.QRect(x, y, w, h))
        self.label.setObjectName('label')
        self.label.setText(text)
        self.label.setEnabled(s)

