from threading import Thread
from PySide6.QtWidgets import QMainWindow
from numpy import sum as npsum
import PySide6.QtCore as qtc
from interface_spectrometer.intspec_gui import Ui_intspecpan  # USER INTERFACE INTEGRATE SPECTRUM
from interface_spectrometer.wlanalyse_gui import Ui_wlanapan   # USER INTERFACE SINGLE WAVELENGTH ANALYSE


class pseudosensor():
    def __init__(self):
        self.name = "Devicename"    # give the device a name
        self.value = 0    # sensor values
        self.ready = 1     # 1 is ready, 0 is not (some devices are always ready)
        self.valueunit = ["bit"] # names for the values (sensor outputs or status etc.)
        self.scannable = False   # is there a scan function
        self.t0 = 0 # for time sensitive measurements we want some starting time

    def getvalue(self): # this is twat the sensor gives back
        return 0
    
    def scannervalue(self, pos):
        pass

    def update(self):
        pass

    def closeSW(self):
        pass


class Integratedspec(QMainWindow, pseudosensor):
    def __init__(self, parentwin, devid, *args, **kwargs):    # init when object is created
        QMainWindow.__init__(self, *args, **kwargs)    # get parent props of QMainWindow
        pseudosensor.__init__(self)                    # get parent props of pseudosensor
        
        # stuff for window
        self.ui =  Ui_intspecpan()
        self.ui.setupUi(self)
        self.parentwin = parentwin
        #self.ui.label.setStyleSheet("color: rgb(240,240,240); font-weight: bold; background-color: transparent; border-color: transparent; font-size: 14pt") ## to keep the format
        self.ui.label_devname.setText("Integrated intensity: Device " +  str(devid))
        self.setWindowFlags(self.windowFlags() | qtc.Qt.WindowStaysOnTopHint) #keep control panel on top
        self.setWindowFlag(qtc.Qt.FramelessWindowHint) ## we dont want to see the window frame
        self.setAttribute(qtc.Qt.WA_TranslucentBackground) ## we dont want to see the window frame
        self.show()

        # values and sensorstuff
        self.name = "Integrated intensity: Device " + str(devid)    # give the device a name
        self.value = 0            # this is the value at our pixel position
        self.spec = parentwin.speclive # we keep the spec axis
        self.wlaxis = parentwin.wlaxis # we keep the wavelength
        self.intmin = min(self.wlaxis) # here we start to integrate
        self.intmin = max(self.wlaxis) # here we start to integrate
        self.idmin = 0                      # lower id
        self.idmax = len(self.wlaxis)-1     # upper id


        # update window
        self.ui.lineEdit_wlmin.setText("{:.1f}".format(self.wlaxis[self.idmin]))
        self.ui.lineEdit_wlmax.setText("{:.1f}".format(self.wlaxis[self.idmax]))


        # buttons and slider
        self.ui.pushButton_getmin.clicked.connect(lambda: self.getmarkerid(1))
        self.ui.pushButton_getmax.clicked.connect(lambda: self.getmarkerid(2))
        self.ui.pushButton_fullrange.clicked.connect(lambda: self.getmarkerid(3))
        self.ui.horizontalSlider_mode.sliderReleased.connect(self.togglemode)


        ####################################### move frameless window ############################################


    def mousePressEvent(self, event):
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.oldPos = globalPos

    def mouseMoveEvent(self, event):
        p = event.globalPosition()
        globalPos = p.toPoint()
        delta = qtc.QPoint(globalPos - self.oldPos) 
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = globalPos


    #################################### window functions #########################################

    def togglemode(self):      # that we dont have to move the slider just clicking on it is enough
        if self.ui.horizontalSlider_mode.value() == 1:
            self.ui.horizontalSlider_mode.setValue(0)
        else: 
            self.ui.horizontalSlider_mode.setValue(1)


    #################################### update functions ##########################################

    def getvalue(self): # this is twat the sensor gives back
        return self.value

    def update(self, wlax, spec):   # this function is called by the devupdater in the interface object .. it simply updates
        self.wlaxis = wlax
        lenid = self.idmax - self.idmin # number of pixels that we average
        self.value = npsum(spec[self.idmin:self.idmax])/lenid # this is the average value
        self.ui.progressBar.setValue(self.value) # we plot the averaged value (prograssbar goes from 0 to 255)
        
        if self.ui.horizontalSlider_mode.value() == 0:    # in integration mode we simple sum up everything
            self.value = npsum(spec[self.idmin:self.idmax])             # we have to overwrite the value since we need the averaged for the progress bar
            self.ui.label_value.setText("{:.0f}".format(self.value))    # plot result
        else:                                             # in average mode we need to plot more digits
            self.ui.label_value.setText("{:.4f}".format(self.value))    # plot result
        

    def getmarkerid(self, id):  # here we set the limits for the integration and update the window

        if self.parentwin.specmode == True: # only if we have a marker available  
            if id == 1: # get lower lim from marker
                self.idmin = self.parentwin.specwindow.ui.MplWidget.xid
            elif id == 2: #get upper lim from marker
                self.idmax = self.parentwin.specwindow.ui.MplWidget.xid
            elif id == 3: # reset lower and upper lim
                self.idmin = 0                      # lower id
                self.idmax = len(self.wlaxis)-1     # upper id
            
            #check if idmin < idmax and flip if necessary
            if self.idmax < self.idmin:
                idmin = self.idmax
                self.idmmax = self.idmin
                self.idmin = idmin

            # update text
            self.ui.lineEdit_wlmin.setText("{:.1f}".format(self.wlaxis[self.idmin]))
            self.ui.lineEdit_wlmax.setText("{:.1f}".format(self.wlaxis[self.idmax]))

        else:
            self.parentwin.statusmessage("no point in spectrum selected")

    def closeSW(self):
        self.close()




############################################# analyse single wavelength ##############################################



class Wlanalyse(QMainWindow, pseudosensor):
    def __init__(self, parentwin, devid, *args, **kwargs):    # init when object is created
        QMainWindow.__init__(self, *args, **kwargs)    # get parent props of QMainWindow
        pseudosensor.__init__(self)                    # get parent props of pseudosensor

    # stuff for window
        self.ui =  Ui_wlanapan()
        self.ui.setupUi(self)
        self.parentwin = parentwin
        #self.ui.label.setStyleSheet("color: rgb(240,240,240); font-weight: bold; background-color: transparent; border-color: transparent; font-size: 14pt") ## to keep the format
        self.ui.label_devname.setText("Wavelength intensity: Device " +  str(devid))
        self.setWindowFlags(self.windowFlags() | qtc.Qt.WindowStaysOnTopHint) #keep control panel on top
        self.setWindowFlag(qtc.Qt.FramelessWindowHint) ## we dont want to see the window frame
        self.setAttribute(qtc.Qt.WA_TranslucentBackground) ## we dont want to see the window frame
        self.show()

        # values and sensorstuff
        self.name = "Wavelength intensity: Device " + str(devid)    # give the device a name
        self.value = 0            # this is the value at our pixel position
        self.spec = parentwin.speclive # we keep the spec axis
        self.wlaxis = parentwin.wlaxis # we keep the wavelength
        self.id = 0                      # id of marker

        # update wavelength position
        self.ui.lineEdit_wl.setText("{:.1f}".format(self.wlaxis[self.id]))

        # buttons
        self.ui.pushButton_getwl.clicked.connect(self.getmarkerid)


        ####################################### move frameless window ############################################

    def mousePressEvent(self, event):
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.oldPos = globalPos

    def mouseMoveEvent(self, event):
        p = event.globalPosition()
        globalPos = p.toPoint()
        delta = qtc.QPoint(globalPos - self.oldPos) 
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = globalPos

        ###################################### update and window functions ###############################################

    def getmarkerid(self):  # here we set the limits for the integration and update the window
        if self.parentwin.specmode == True: # only if we have a marker available  
            self.id = self.parentwin.specwindow.ui.MplWidget.xid
            self.ui.lineEdit_wl.setText("{:.1f}".format(self.wlaxis[self.id]))
        else:
            self.parentwin.statusmessage("no point in spectrum selected")

    def update(self, wlax, spec): 
        self.wlaxis = wlax
        self.value = spec[self.id]
        self.ui.progressBar.setValue(self.value) # we plot the averaged value (prograssbar goes from 0 to 255)
        self.ui.label_value.setText("{:.1f}".format(self.value))

    def closeSW(self):
            self.close()