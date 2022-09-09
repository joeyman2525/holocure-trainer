import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget
from UI import Ui_Form
from pymem import *
from pymem.process import *
import threading

class AppWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        #偵測按鈕
        self.ui.page_button.clicked.connect(self.find_windows)  
        
        #多線程執行
        self.ui.extra_func[0].clicked.connect(lambda: self.threading(self.ui.extra_func[0].text()))
        self.ui.extra_func[1].clicked.connect(lambda: self.threading(self.ui.extra_func[1].text()))
        self.ui.extra_func[2].clicked.connect(lambda: self.threading(self.ui.extra_func[2].text()))
        self.ui.extra_func[3].clicked.connect(lambda: self.threading(self.ui.extra_func[3].text()))
           
        self.move(40, 40)
        self.show()
        
    def find_windows(self):
        try:
            #視窗名稱
            self.windows = Pymem("HoloCure.exe")
            #取得dll
            self.game_module = module_from_name(self.windows.process_handle, "HoloCure.exe").lpBaseOfDll
            #啟用功能
            for cnt,i in enumerate(self.ui.extra_func):
                if cnt == 5 or cnt == 4:
                    continue
                i.setEnabled(True)
            QMessageBox.information(None, '掃描', '已掃描到遊戲')
        except:
            QMessageBox.critical(None, '錯誤', '請先開啟遊戲後再按偵測程式')
            
    def threading(self, text):   
        t = threading.Thread(target = self.Enable,args = (text,))
        #防止子線程未關閉
        t.setDaemon(True)
        t.start()
        #print(threading.active_count()) 
    
    def Enable(self,text):
        #index, base address, offsets
        options_info = {
                     '鎖血無敵':[0,0x006FBD7C,[0x1900,0x140,0x24,0x10,0x144,0x4],1200470147],
                     '無限特殊技能':[1,0x006FBD7C, [0x1900,0x140,0x24,0x10,0x2DC,0x04],1100470147],
                     '全圖撿物':[2,0x006FBD7C,[0x18FC,0x144,0x140,0x140,0x140,0x24,0x10,0x798,0x04],1100470147],
                     '增加HoloCoin':[3,0x00448E48, [0x270,0xc,0x24,0x494],1100470147],
                    }
        index, address, offsets,value = options_info[text]
        
       
        #鎖定數據
        while(1):
            if self.ui.extra_func[index].isChecked():
                try:
                    addr_tmp  = self.Hacking(self.game_module + address, offsets)
                    #動態獲取數據有時會判斷錯誤，若數值低於1070000000則為錯誤地址
                    if self.windows.read_int(addr_tmp) > 1070000000:
                        addr = addr_tmp
                    self.windows.write_int(addr, value)
                except:
                    pass
            else:
                break

    def Hacking(self, address, offsets):
        addr = self.windows.read_int(address)
        for cnt,offset in enumerate(offsets):
            if cnt+1 != len(offsets):
                addr = self.windows.read_int(addr + offset)           
        return addr + offsets[-1]
        



app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
