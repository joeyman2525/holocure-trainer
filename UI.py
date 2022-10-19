from PyQt5 import QtCore, QtWidgets

class Ui_Form(object):
    def setupUi(self, page):
        form_w = 655
        form_h = 160
        page.resize(form_w, form_h)
        page.setWindowTitle('HoloCure Modifier by AUSTIN2526, Translated by joeyman2525')

        self.makelabel(page, 160, 10, 2500, 30,'【After starting the game, press the detection button to enable modifier functionality】')
        #detect game
        self.page_button = QtWidgets.QPushButton(page)
        self.page_button.setGeometry(QtCore.QRect(10,10,140,30))
        self.page_button.setText('Detect game instance')

        #Data before entry
        func_name = ['Invincibility', 'Unlimited Special Attack', 'Unlimited Pickup Range','Unlimited Holocoins', 'Increase Attack', 'Increase Haste']
        self.makelabel(page, 10, 50, 2000, 30,'↓↓↓↓↓↓↓↓↓↓Modifier selection↓↓↓↓↓↓↓↓↓↓')
        self.extra_func = []
        for i in range(3):
            for j in range(2):
                index = j + i * 2
                self.extra_func.append(QtWidgets.QCheckBox(page))
                self.extra_func[index].setGeometry(QtCore.QRect(10 + 165*i, 80 + j*30, 2000, 30))
                self.extra_func[index].setText(func_name[index])
                self.extra_func[index].setEnabled(False)

    def makelabel(self, page, x=10, y=10, w=10, h=20, text='', s=True):
        self.label = QtWidgets.QLabel(page)
        self.label.setGeometry(QtCore.QRect(x, y, w, h))
        self.label.setObjectName('label')
        self.label.setText(text)
        self.label.setEnabled(s)
