import PySide6.QtCore as qtc
from time import sleep as sleep

class CamreadWorker(qtc.QRunnable):
    
    def __init__(self, *args, **kwargs):
        super(CamreadWorker, self).__init__()
        self.parentwin = args[0]
    
    def run(self):
        self.parentwin.camreadupdate()
        

class LivecamWorker(qtc.QRunnable):
    
    def __init__(self, *args, **kwargs):
        super(LivecamWorker, self).__init__()
        self.parentwin = args[0]
    
    def run(self):
        self.parentwin.setupHW()

class LivespecWorker(qtc.QRunnable):
    
    def __init__(self, *args, **kwargs):
        super(LivespecWorker, self).__init__()
        self.parentwin = args[0]
    
    def run(self):
        self.parentwin.specplotupdate()


class Camconnect(qtc.QRunnable):
    def __init__(self, *args, **kwargs):
        super(Camconnect, self).__init__()
        self.parentwin = args[0]
    
    def run(self):
        self.parentwin.connect2cam()


