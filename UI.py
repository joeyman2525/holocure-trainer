from PyQt5 import QtCore, QtWidgets

class Ui_Form(object):
    def setupUi(self, page):
        form_w = 440
        form_h = 300
        page.resize(form_w, form_h)
        page.setWindowTitle('HoloCure修改器 by AUSTIN2526')
        
        self.makelabel(page, 105, 10, 2000, 30,'【啟動遊戲後按偵測按鈕遊戲即可啟用功能】')
        #偵測遊戲
        self.page_button = QtWidgets.QPushButton(page)
        self.page_button.setGeometry(QtCore.QRect(10,10,100,30))
        self.page_button.setText('偵測遊戲')
        
        #第一關數據
        func_name = ['鎖血無敵', '無限特殊技能', '全圖撿物']
        self.makelabel(page, 10, 50, 2000, 30,'Stage1 修改區')
        self.stage_1 = []
        for index in range(3):
            self.stage_1.append(QtWidgets.QCheckBox(page))
            self.stage_1[index].setGeometry(QtCore.QRect(10 + 140*index, 80 , 2000, 30))
            self.stage_1[index].setText(func_name[index])
            self.stage_1[index].setEnabled(False)
            
        #第二關數據
        func_name = ['鎖血無敵', '無限特殊技能', '全圖撿物']
        self.makelabel(page, 10, 110, 2000, 30,'Stage2 修改區')
        self.stage_2 = []
        for index in range(3):
            self.stage_2.append(QtWidgets.QCheckBox(page))
            self.stage_2[index].setGeometry(QtCore.QRect(10 + 140*index, 140 , 2000, 30))
            self.stage_2[index].setText(func_name[index])
            self.stage_2[index].setEnabled(False)
            
        
        func_name = ['鎖血無敵', '無限特殊技能', '全圖撿物']
        self.makelabel(page, 10, 170, 2000, 30,'Stage3 修改區')
        self.stage_3 = []
        for index in range(3):
            self.stage_3.append(QtWidgets.QCheckBox(page))
            self.stage_3[index].setGeometry(QtCore.QRect(10 + 140*index, 200 , 2000, 30))
            self.stage_3[index].setText(func_name[index])
            self.stage_3[index].setEnabled(False)
        
        #其他功能
        func_name = ['無限HoloCoin']
        self.makelabel(page, 10, 230, 2000, 30,'其他   修改區')
        self.other = []
        for index in range(1):
            self.other.append(QtWidgets.QCheckBox(page))
            self.other[index].setGeometry(QtCore.QRect(10 + 140*index, 260 , 2000, 30))
            self.other[index].setText(func_name[index])
            self.other[index].setEnabled(False)
           
    def makelabel(self, page, x=10, y=10, w=10, h=20, text='', s=True):
        self.label = QtWidgets.QLabel(page)
        self.label.setGeometry(QtCore.QRect(x, y, w, h))
        self.label.setObjectName('label')
        self.label.setText(text)
        self.label.setEnabled(s)

