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
        
        #stage1
        self.ui.stage_1[0].clicked.connect(lambda: self.stage_1_threading(self.ui.stage_1[0].text()))
        self.ui.stage_1[1].clicked.connect(lambda: self.stage_1_threading(self.ui.stage_1[1].text()))
        self.ui.stage_1[2].clicked.connect(lambda: self.stage_1_threading(self.ui.stage_1[2].text()))        
        #stage2
        self.ui.stage_2[0].clicked.connect(lambda: self.stage_2_threading(self.ui.stage_2[0].text()))
        self.ui.stage_2[1].clicked.connect(lambda: self.stage_2_threading(self.ui.stage_2[1].text()))
        self.ui.stage_2[2].clicked.connect(lambda: self.stage_2_threading(self.ui.stage_2[2].text()))
        #other
        self.ui.other[0].clicked.connect(lambda: self.other_threading(self.ui.other[0].text()))

           
        self.move(40, 40)
        self.show()
        
    def find_windows(self):
        try:
            #視窗名稱
            self.windows = Pymem("HoloCure.exe")
            #取得dll
            self.game_module = module_from_name(self.windows.process_handle, "HoloCure.exe").lpBaseOfDll
            #啟用功能
            for i in self.ui.stage_1:
                i.setEnabled(True)
            for i in self.ui.stage_2:
                i.setEnabled(True)
            for i in self.ui.other:
                i.setEnabled(True)
            QMessageBox.information(None, '掃描', '已掃描到遊戲')
        except:
            QMessageBox.critical(None, '錯誤', '請先開啟遊戲後再按偵測程式')
            
    def stage_1_threading(self, text):   
        t = threading.Thread(target = self.stage_1_enable,args = (text,))
        t.setDaemon(True)
        t.start()
    
    def stage_1_enable(self,text):
        #index, base address, offsets
        options_info = {
                     '鎖血無敵':[0,0x006FBD7C,[0x1900,0x140,0x24,0x10,0x144,0x4],1200470147],
                     '無限特殊技能':[1,0x006FBD7C, [0x1900,0x140,0x24,0x10,0x2DC,0x04],1100470147],
                     '全圖撿物':[2,0x006FBD7C,[0x18FC,0x144,0x140,0x140,0x140,0x24,0x10,0x798,0x04],1100470147],
                    }
        index, address, offsets, value = options_info[text]
        
        while(1):
            #判斷開關是否開啟
            if self.ui.stage_1[index].isChecked():
                try:
                    addr  = self.Hacking(self.game_module + address, offsets)
                    #防止重複覆蓋數據造成CPU的負擔
                    if self.windows.read_int(addr) != value:
                        self.windows.write_int(addr, value)
                except:
                    pass
            else:
                break
    
    def stage_2_threading(self, text):   
        t = threading.Thread(target = self.stage_2_enable,args = (text,))
        t.setDaemon(True)
        t.start()
    
    def stage_2_enable(self,text):
        #index, base address, offsets
        options_info = {
                     '鎖血無敵':[0,0x006FBD7C,[0x564,0x144,0x24,0x10,0x1E0,0x0,0x68,0x140,0x24,0x10,0x144,0x4],1200470147],
                     '無限特殊技能':[1,0x006FBD7C, [0x564,0x144,0x24,0x10,0x9CC,0x0,0x78,0x140,0x24,0x10,0x2DC,0x4],1100470147],
                     '全圖撿物':[2,0x006FBD7C,[0x564,0x144,0x24,0x10,0x33C,0x0,0x78,0x140,0x24,0x10,0x798,0x4],1100470147], 
                    }
        index, address, offsets,value = options_info[text]
        
        while(1):
            #判斷開關是否開啟
            if self.ui.stage_2[index].isChecked():
                try:
                    addr  = self.Hacking(self.game_module + address, offsets)
                    ##防止重複覆蓋數據造成CPU的負擔
                    if self.windows.read_int(addr) != value:
                        self.windows.write_int(addr, value)
                except:
                    pass
            else:
                break
                
    def other_threading(self, text):   
        t = threading.Thread(target = self.other_enable,args = (text,))
        #防止子線程未關閉
        t.setDaemon(True)
        t.start()
        #print(threading.active_count()) 
    
    def other_enable(self,text):
        #index, base address, offsets
        options_info = {'無限HoloCoin':[0,0x00448E48, [0x270,0xc,0x24,0x494],1100470147]}
        index, address, offsets,value = options_info[text]
        
       
        while(1):
            #判斷開關是否開啟
            if self.ui.other[index].isChecked():
                try:
                    addr  = self.Hacking(self.game_module + address, offsets)
                    ##防止重複覆蓋數據造成CPU的負擔
                    if self.windows.read_int(addr) != value:
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
