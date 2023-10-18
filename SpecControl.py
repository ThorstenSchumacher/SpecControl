##############################################################################################################################################
# 
# printedLABs - SpecControl
# 
# 
# Thorsten Schumacher 
# University of Bayreuth - Germany
# Thorsten.Schumacher@uni-bayreuth.de
# Version 1.0
#                                                                               
#
##############################################################################################################################################


# import relevant external modules
import cv2
import numpy as np 
import sys
import time
import nest_asyncio # get rid of async warnings (event loop issue)
nest_asyncio.apply() 
from os import getcwd as getfolder
from os import remove as removefile
from os.path import exists as fileexists

from threading import Thread
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
import PySide6.QtCore as qtc
from PySide6.QtGui import QIcon

# import own modules and gui
from interface_spectrometer.spectrometercom_gui import Ui_speccom_mainwin
from interface_spectrometer.specplotting_gui import Ui_specplottingwin
from interface_spectrometer.Workerclass import CamreadWorker, LivecamWorker, LivespecWorker, Camconnect


################## class for status messages #####################
class Statusemitter(qtc.QObject):
    messagesignal = qtc.Signal(str)

    def sendmessage(self, mymessage)    :
        self.messagesignal.emit(mymessage)

##############################################################################################################################################
#                                                          MAIN WINDOW                                                                       #
##############################################################################################################################################
# to create single exe incl. icon (e.g. TaskManager ...) use in pyintaller ....  "pyinstaller --onefile --noconsole --icon=confs/SWicon.png SpecControl.py"


class spectrometerwin(QMainWindow):
    
     ## initializing stuff when class is called ... all for/inside GUI
    def __init__(self, interfacenum, parentwin, *args, **kwargs):

        super().__init__(*args, **kwargs)
        # stuff for window
        self.ui =  Ui_speccom_mainwin()
        self.ui.setupUi(self)
        self.interfacennr = interfacenum
        self.setWindowFlags(self.windowFlags() | qtc.Qt.WindowStaysOnTopHint) #keep control panel on top
        self.setWindowFlag(qtc.Qt.FramelessWindowHint) ## we dont want to see the window frame
        self.setAttribute(qtc.Qt.WA_TranslucentBackground) ## we dont want to see the window frame
        self.ui.label_status.setStyleSheet("color:#ff0000; background-color: transparent; border-color: transparent; font-size: 12pt") ## to keep the format
        self.ui.label.setStyleSheet("color: rgb(240,240,240); font-weight: bold; background-color: transparent; border-color: transparent; font-size: 14pt") ## to keep the format
        self.parentwin = parentwin # here we have the parent window (experimental control)
        self.setWindowIcon(QIcon('confs/SWicon.png'))  # use this icon on the OS
        self.setWindowTitle("SpecControl - PrintedLabs")  # this is the Frame Title (shown as WindowName in OS)
        self.ui.frame.setFixedHeight(291)
        self.move(self.parentwin.intwinpos[0], self.parentwin.intwinpos[1]) # move the window to its position
        self.parentwin.intwinpos[1] += 286  #   store in parent window the position for the next interface window
        self.ui.lineEdit_filepath.setText(getfolder()+"\savedata")  # write current folder into the folder linedit
        self.show()

        # available sources (IDs) for cv2
        self.camindexfound = ["0"] #we start with one source
        self.ui.comboBox_camport.addItems(self.camindexfound)
        self.frameid = 0    # the frame number we got after connecting to the cam
        self.resolutiondesired = [2*1920, 2*1080] # this is the desired resolution we are working with ... 
        self.resolution = [2*1920, 2*1080] # self.resolution will be overwritten when cam is connected and readout
        self.ROIymin = 200 # lower pixel of yROI
        self.ROIymax = 880 # lower pixel of yROI
        self.ROIsteps = 10 # discretization for ROI

        # empty frame and spec
        self.generateemptydata() # all 


        # start an update thread for reading the camera if available and define Flags for the code
        self.threadpool = qtc.QThreadPool()
        self.runcam = False       # Flag for grabbing frames
        self.showlivecam = False   # Flag to check if live image is shown ... required to interrupt image loop
        self.specmode = False     # Flag if we are in specmode
        self.ROIon = False        # Flag if we are running ROI mode
        self.bayercorrmode = False # Flag if bayercorrection is running
        self.settingsopen = False # Flag if Settings are open
        self.infoopen = False # Flag if infobox is shown
        self.calibrationopen = False # Flag if calibrationwindow is shown
        self.averagemode = False # Flag if averaging is activated
        self.freezemode = False # Flag if we want to freeze the spectrum (no new image will be recorded)
        self.calibrated = False # flag if there is a calibration .. we start with false

       # prepare statusmessage signal - connection 
        self.messageemitter = Statusemitter()           # create an Object for signal emission containing the signal send function
        self.messageemitter.messagesignal.connect(self.statusmessage) # this will be the target function of our signal

        ## create liveview window
        self.specwindow = Showlivespec()            # we create the plot window object                 
        self.specwindow.ui.MplWidget.wlaxis = self.wlaxis    # we start with the old calibration file or the cam pixels
        
        
        ## setup calibration and stuff
        self.getoldcalibration() # finally we load (if config file exists) the former calibration data
        self.setexposuretime() # to update slider and labels
        self.setbrightness() # to update slider and labels
        self.setgain() # ... what is now the averager ... to update slider and labels
    

        # calibration values
        self.calwllist = ["436.5", "546.3", "611.0"]    # this are the 3 best emission lines of an energy saving lamp (not LED but fluorescent tube)
        self.ui.lineEdit_wl1.setText(self.calwllist[0])
        self.ui.lineEdit_wl2.setText(self.calwllist[1])
        self.ui.lineEdit_wl3.setText(self.calwllist[2])


    ########################################## UI buttons ####################################################
        
        # general stuff
        self.ui.pushButton_comrefresh.clicked.connect(self.scancam)
        self.ui.pushButton_comconnect.clicked.connect(self.launchcamconnect) # later we open worker thread launch.....
        self.ui.pushButton_settings.clicked.connect(self.showsettings)
        self.ui.pushButton_exit.clicked.connect(self.closeSW)
        self.ui.pushButton_infobox.clicked.connect(self.showinfobox)
        self.ui.pushButton_cali.clicked.connect(self.showcali)
        self.ui.pushButton_mini.clicked.connect(self.minimizeSC)

        #camcontrol
        self.ui.horizontalSlider_exposure.valueChanged.connect(self.setexposuretime)
        self.ui.horizontalSlider_bright.valueChanged.connect(self.setbrightness)
        self.ui.horizontalSlider_gain.valueChanged.connect(self.setgain)
        self.ui.horizontalSlider_average.valueChanged.connect(self.setaverage)

        #save button
        self.ui.pushButton_savespec.clicked.connect(self.clicksavespec)
        
        #speccontrols
        self.ui.checkBox_bayercorr.clicked.connect(self.bayercorr)
        self.ui.pushButton_average.clicked.connect(self.averagetoggle)
        self.ui.pushButton_freeze.clicked.connect(self.freezetoggle)

        #settings
        self.ui.pushButton_liveview.clicked.connect(self.livecamview)
        self.ui.pushButton_browse.clicked.connect(self.browsefiles)
        self.ui.checkBox_useROI.clicked.connect(self.setROIalarm)
        
        # ROI buttons
        self.ui.pushButton_yminmin.clicked.connect(lambda: self.ROIylims(0))
        self.ui.pushButton_ymaxmin.clicked.connect(lambda: self.ROIylims(1))
        self.ui.pushButton_yminplu.clicked.connect(lambda: self.ROIylims(2))
        self.ui.pushButton_ymaxplu.clicked.connect(lambda: self.ROIylims(3))
        self.ui.lineEdit_ymin.setText(str(self.ROIymin))
        self.ui.lineEdit_ymax.setText(str(self.ROIymax))

        #calibration
        self.ui.horizontalSlider_wlcalmode.sliderReleased.connect(self.togglecalmode)
        self.ui.pushButton_getP1.clicked.connect(lambda: self.getP(1))
        self.ui.pushButton_getP2.clicked.connect(lambda: self.getP(2))
        self.ui.pushButton_getP3.clicked.connect(lambda: self.getP(3))
        self.ui.horizontalSlider_wlcalmode.valueChanged.connect(self.wlcalmode)
        self.ui.pushButton_calwlaxis.clicked.connect(self.computewlaxis)
       
        #storage load and deleting calibration file
        self.ui.pushButton_savewlaxis.clicked.connect(self.saveconf)
        self.ui.pushButton_loadwlaxis.clicked.connect(self.getoldcalibration)
        self.ui.pushButton_clearcal.clicked.connect(self.resetcal)


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

    ###################################### general functions ##################################################

    def minimizeSC(self):
        self.showMinimized() # minimize control panel
        if self.showlivecam == True:
            self.livecamview() # we click the button and liveview ends



    def statusmessage(self, text):          # writes a message to the status label and resets it after 3000ms
        self.ui.label_status.setText(text)  # the message is set
        self.ui.label_status.repaint()      # label updated
        qtc.QTimer.singleShot(3000, self.resetstatus)   #after 3000ms we call the resetstatus function that writes "waiting" again

    def resetstatus(self):  # resets the status label to waiting
        self.ui.label_status.setText("waiting")
    
    def closeSW(self):
        self.devupdating = False    # set flag that updating the devices shall stop
        self.runcam = False         # set flag to interrupt frame grabbing
        self.specmode = False         # set flag to interrupt frame grabbing
        self.showlivecam = False    # set flag to interrubt liveview

        time.sleep(0.5)             # wait some time to stop the threads
        try:
            self.specwindow.close()  # try to close the livespec window
            self.mycam.release()    # try to close the cam connection (if no cam is connected its also fine)
        except:
            pass
        self.close()                # close UI


    def getoldcalibration(self):
        if fileexists(getfolder()+"\confs\specconfig.npy"):           # check if config gile exists
            storeddata = np.load("confs\specconfig.npy")              # load it
            self.wlaxis =  storeddata[0,:]                          # first col is the wavelength axis 
            self.wlaxiscal =  storeddata[0,:]                          # first col is the wavelength axis we store as calibration wlaxis
            self.specwindow.ui.MplWidget.wlaxis = self.wlaxis   # and we also write it to the plotwidget
            self.calibrated = True
            ymin = int(storeddata[1,2])                         # now start in second col with the parameters that we have to set again ... here yminROI
            ymax = int(storeddata[1,3])                         # ... here ymaxROI
            if storeddata[1,0] == 1:                            # ... flipx
                self.ui.checkBox_flipx.setChecked(True) 
            if storeddata[1,1] == 1:                            # ... flipy
                self.ui.checkBox_flipy.setChecked(True)
            if storeddata[1,4] == 1:                            # ... use ROI
                    self.ui.checkBox_useROI.setChecked(True)
                    self.ROIon = True
                    self.setROIalarm()
            self.ui.lineEdit_ymin.setText(str(ymin))    # ... set ROImin in settings
            self.ui.lineEdit_ymax.setText(str(ymax))    # ... set ROImax in settings
            self.ROIymin = ymin                                 # ... set ROImin
            self.ROIymax = ymax                                 # ... set ROIax
            self.statusmessage("calibration loaded")            # inform user that conf was loaded
        else:
            self.statusmessage("no calibration file")           # or inform user that no config file exists

    def averagetoggle(self):
        self.averagemode = not(self.averagemode)    # toggle averagemode Flag
        if self.averagemode == False:
            self.ui.pushButton_average.setStyleSheet(u""+ self.buttonstyle("summe.png", "summeb.png", 0)) # set to unactivated mode
        else:
            self.ui.pushButton_average.setStyleSheet(u""+ self.buttonstyle("summe.png", "summeb.png", 1)) # set to activated mode 

    def freezetoggle(self):
        if self.runcam == True:
            self.freezemode = not(self.freezemode)    # toggle freemode Flag  
            if self.freezemode:
                 self.ui.pushButton_freeze.setStyleSheet(u""+ self.buttonstyle("play.png", "playb.png", 1)) # set to activated mode
            else:
                self.ui.pushButton_freeze.setStyleSheet(u""+ self.buttonstyle("pause.png", "pauseb.png", 0)) # set to unactivated mode
        else:
            self.statusmessage("no camera connected")


    def showinfobox(self):
        self.ui.pushButton_cali.setStyleSheet(u""+ self.calibuttonstyle(0))
        self.calibrationopen = self.settingsopen = False # no other menu is open
        self.ui.pushButton_settings.setStyleSheet(u""+ self.buttonstyle("settings.png", "settingsb.png", 0)) # set to activated mode

        if self.infoopen:
            self.ui.frame.setFixedHeight(291)
            self.infoopen = False
            self.ui.pushButton_infobox.setStyleSheet(u""+ self.buttonstyle("info.png", "infob.png", 0)) # set to unactivated mode
        else:
            self.ui.stackedWidgetsettings.setCurrentIndex(1)
            self.ui.frame.setFixedHeight(421)
            self.infoopen = True
            self.ui.pushButton_infobox.setStyleSheet(u""+ self.buttonstyle("info.png", "infob.png", 1)) # set to activated mode

    def showsettings(self):
        self.ui.pushButton_cali.setStyleSheet(u""+ self.calibuttonstyle(0))
        self.ui.pushButton_infobox.setStyleSheet(u""+ self.buttonstyle("info.png", "infob.png", 0)) # set to unactivated mode
        self.calibrationopen = self.infoopen = False # no other menu is open

        if self.settingsopen:
            self.ui.frame.setFixedHeight(291)
            self.settingsopen = False
            self.ui.pushButton_settings.setStyleSheet(u""+ self.buttonstyle("settings.png", "settingsb.png", 0)) # set to activated mode
        else:
            self.ui.stackedWidgetsettings.setCurrentIndex(0)
            self.ui.frame.setFixedHeight(621)
            self.settingsopen = True
            self.ui.pushButton_settings.setStyleSheet(u""+ self.buttonstyle("settings.png", "settingsb.png", 1)) # set to activated mode

    def showcali(self):
        self.settingsopen = self.infoopen = False # no other menu is open
        self.ui.pushButton_infobox.setStyleSheet(u""+ self.buttonstyle("info.png", "infob.png", 0)) # set to unactivated mode
        self.ui.pushButton_settings.setStyleSheet(u""+ self.buttonstyle("settings.png", "settingsb.png", 0)) # set to activated mode


        if self.calibrationopen:
            self.ui.pushButton_cali.setStyleSheet(u""+ self.calibuttonstyle(0))
            self.ui.frame.setFixedHeight(291)
            self.calibrationopen = False
        else:
            self.ui.stackedWidgetsettings.setCurrentIndex(2)
            self.ui.pushButton_cali.setStyleSheet(u""+ self.calibuttonstyle(1))
            self.ui.frame.setFixedHeight(621)
            self.calibrationopen = True

    ## functions for save files tab
    def browsefiles(self):  # open browse window to define saving path
        path = QFileDialog.getExistingDirectory(self, "Open file")
        self.ui.lineEdit_filepath.setText(path)


    def setROIalarm(self):  # this handles the marker on the plot and shows if ROI mode is activated
        if self.specmode == True:
            if self.ui.checkBox_useROI.isChecked():
                self.specwindow.ui.alarmframe.setVisible(True)
                self.specwindow.ui.label_22.setText("ROI activated!")
            else:
                self.specwindow.ui.alarmframe.setVisible(False)
                self.specwindow.ui.label_22.setText("ROI not activated")


    def buttonstyle(self, image, imagehover, pressmode): # image is the image button of the style, pressmode: 0 = set to unactivated, 1 = set to activated mode
        if pressmode == 1:
            stylecode = "QPushButton {\n border: none;\n border-radius: 0px;\n	background-color: rgb(100, 150, 200);\n	background-image: url(:/icons/"+ image +");\n	color: white;\n}\n \n QPushButton:hover {\n	background-image: url(:/icons/"+ imagehover +");\n	color: white;\n}\n \n QPushButton:pressed {\n background-color: rgb(130, 180, 230);\n color: white;\n}"
        if pressmode == 0:
            stylecode = "QPushButton {\n border: none;\n border-radius: 0px;\n	background-color: rgb(90, 90, 90);\n	background-image: url(:/icons/"+ image +");\n	color: white;\n}\n \n QPushButton:hover {\n	background-image: url(:/icons/"+ imagehover +");\n	color: white;\n}\n \n QPushButton:pressed {\n background-color: rgb(130, 180, 230);\n color: white;\n}"
        return stylecode
    
    def calibuttonstyle(self, pressmode): # image is the image button of the style, pressmode: 0 = set to unactivated, 1 = set to activated mode
        if pressmode == 0:
            stylecode = "QPushButton {\n border: none;\n	border-radius: 0px;\n	background-color: rgb(90, 90, 90);\n	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 65), stop:0.166 rgba(255, 255, 0,65), stop:0.333 rgba(0, 255, 0, 65), stop:0.5 rgba(0, 255, 255,65), stop:0.666 rgba(0, 0, 255, 65), stop:0.833 rgba(255, 0, 255,65), stop:1 rgba(255, 0, 0, 65));\n	font: 75 12pt " + "Futura Md BT" + ";\n	color:  rgb(230, 230, 230);\n} QPushButton:hover {\n	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 150), stop:0.166 rgba(255, 255, 0,150), stop:0.333 rgba(0, 255, 0, 150), stop:0.5 rgba(0, 255, 255, 150), stop:0.666 rgba(0, 0, 255, 150), stop:0.833 rgba(255, 0, 255, 150), stop:1 rgba(255, 0, 0, 150));\n	color: white;\n}\n QPushButton:pressed {\n	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n	color: white;\n}\n "
        if pressmode == 1:
            stylecode = "QPushButton {\n border: none;\n	border-radius: 0px;\n	background-color: rgb(90, 90, 90);\n	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 180), stop:0.166 rgba(255, 255, 0,180), stop:0.333 rgba(0, 255, 0, 180), stop:0.5 rgba(0, 255, 255,180), stop:0.666 rgba(0, 0, 255, 180), stop:0.833 rgba(255, 0, 255,180), stop:1 rgba(255, 0, 0, 180));\n	font: 75 12pt " + "Futura Md BT" + ";\n	color:  rgb(230, 230, 230);\n} QPushButton:hover {\n	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 220), stop:0.166 rgba(255, 255, 0,220), stop:0.333 rgba(0, 255, 0, 220), stop:0.5 rgba(0, 255, 255, 220), stop:0.666 rgba(0, 0, 255, 220), stop:0.833 rgba(255, 0, 255, 220), stop:1 rgba(255, 0, 0, 220));\n	color: white;\n}\n QPushButton:pressed {\n	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n	color: white;\n}\n "
        return stylecode


    
###################################### camera readout and interface #########################################

    def returnCameraIndexes(self): # this function searches the first "ports" for an camera and stores the found ids
        
                # checks the first 10 indexes.
        index = 0
        camindexfound = []

        while True:
            cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)  # Use cv2.CAP_DSHOW for Windows

            if not cap.isOpened(): # we are done if no furter camera is found
                break

            _, frame = cap.read()  # Read a frame to check if the camera is working

            if frame is not None: # we find out if there is a frame
                camindexfound.append(str(index)) # the we add the camera as camera
            
            cap.release() # release the cam
            index += 1 # and go to next index

        # finally we update the combobox and store the result in the object
        self.ui.comboBox_camport.clear()    
        self.ui.comboBox_camport.addItems(camindexfound)  
        self.camindexfound = camindexfound
        self.ui.comboBox_camport.setEnabled(True) # we disable the combobox so that nobody can press it while scanning
        self.ui.pushButton_comconnect.setEnabled(True) # enable connect and refresh buttons again
        self.ui.pushButton_comrefresh.setEnabled(True) # enable connect and refresh buttons again

        self.resetstatus() # we are done scanning what propably takes longer than 3 seconds

    def scancam(self):  # we start scanning available camera sources within a thread .. so that nothing freezes
        # scanning can take a long time .. so we keep the status on "scanning"
        self.ui.comboBox_camport.setDisabled(True) # we disable the combobox so that nobody can press it while scanning
        self.ui.pushButton_comconnect.setDisabled(True) # dont push the button before cameras are scanned .. will be enabled after scan again
        self.ui.pushButton_comrefresh.setDisabled(True) # dont push the button before cameras are scanned .. will be enabled after scan again
        self.ui.label_status.setText("scanning camera sources") # set text to scanning
        self.ui.label_status.repaint()
        # we start a thread doing the work and scanning
        scanthread = Thread(target = self.returnCameraIndexes, args=()) 
        scanthread.start()

    def connect2cam(self):
        if self.ui.pushButton_comconnect.text() == "connect": # in case we are not connected but want to
            self.ui.pushButton_comconnect.setDisabled(True) # set buttons and menu disabled to avoid starting a second process
            self.ui.pushButton_comrefresh.setDisabled(True)
            self.ui.comboBox_camport.setDisabled(True)
            self.messageemitter.sendmessage("connecting to camera")
            
            # open camera
            self.mycam = cv2.VideoCapture(int(self.ui.comboBox_camport.currentText()), cv2.CAP_DSHOW)  # , cv2.CAP_MSMF is suggested backend but also default, cv2.CAP_DSHOW comes from chatGPT
            
            self.ui.pushButton_comconnect.setText("disconnect")
            if self.mycam.isOpened():
                self.mycam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
                self.mycam.set(cv2.CAP_PROP_FRAME_WIDTH, self.resolutiondesired[0])
                self.mycam.set(cv2.CAP_PROP_FRAME_HEIGHT, self.resolutiondesired[1])
                self.mycam.set(cv2.CAP_PROP_AUTO_WB, 0.75) # thies deactivates white balance
                self.mycam.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25) # deactivates auto exposure
                self.mycam.set(cv2.CAP_PROP_FPS, 30)

                #  since we can only wish a resultion but that depends on the hardware lets see what we got and store it
                self.resolution[1] = int(self.mycam.get(cv2.CAP_PROP_FRAME_HEIGHT))
                self.resolution[0] = int(self.mycam.get(cv2.CAP_PROP_FRAME_WIDTH))
                self.generateemptydata(); # reset all data variables like image, wavelength axis etc.
                self.specwindow.ui.MplWidget.xres = self.resolution[0]   # we start with the old calibration file or the cam pixels
                self.specwindow.ui.MplWidget.setaxisresolution() # compute new, empty data with correct dimensions
                
                # if we have a calibration loaded of generated, we use the calibration wlaxis
                if self.calibrated and self.wlaxiscal.size == self.specwindow.ui.MplWidget.xres:
                    self.specwindow.ui.MplWidget.wlaxis = self.wlaxiscal
                else:
                    self.calibrated = False
                    self.statusmessage("calibration does not match!")

                # now we set the camera parameter for the first time
                self.runcam = True  # we set the flag! and afterwards we update the set cam parameter
                self.setexposuretime() # to update slider and labels
                self.setbrightness() # to update slider and labels
                self.setgain() # to update slider and labels
                self.setaverage() # to update slider and labels

                # now start reading the cam in a separate thread
                self.camreadworker = CamreadWorker(self)
                self.ui.pushButton_comconnect.setEnabled(True)
                self.threadpool.start(self.camreadworker)   # run camera thread
                self.messageemitter.sendmessage("camera connected") # and send status
            else:
                self.messageemitter.sendmessage('failed')
                # and set all buttons enabled
                self.ui.pushButton_comconnect.setEnabled(True)
                self.ui.pushButton_comrefresh.setEnabled(True)
                self.ui.comboBox_camport.setEnabled(True)
                self.ui.pushButton_comconnect.setText("connect")

        else: # in case we want to disconnect
            if self.freezemode: # if we are in freeze mode we change that
                self.freezetoggle()
            
            self.runcam = False # stop loop 
            time.sleep(0.25) # and give it some time before we release the camera
            
            # reset UI buttons      
            self.ui.pushButton_comconnect.setText("connect")
            self.ui.pushButton_comconnect.setEnabled(True)
            self.ui.pushButton_comrefresh.setEnabled(True)
            self.ui.comboBox_camport.setEnabled(True)
            self.messageemitter.sendmessage("disconnected from camera")
            
            # release camera after everything else is done
            self.mycam.release()


    def launchcamconnect(self):
        # if there is a camera in the list
        if self.ui.comboBox_camport.currentIndex() >= 0:
            self.camlaunchworker = Camconnect(self)
            self.threadpool.start(self.camlaunchworker)
            self.spectrometermode()  # we autostart the spectrometer mode
           
        else:
            self.statusmessage("no camera port")

    
    def camreadupdate(self):
        self.frameid = 0    # after connecting to cam we start with frame nr 0
        self.currspec = self.speclive
        
        # now we start reading
        while self.runcam == True:
   
            if self.freezemode == False:
                self.rval, frame = self.mycam.read()
                framelive = self.imagemani(frame)
            
            # in any case, we need grayscale for the spectrometer mode
            frameBW = cv2.cvtColor(framelive, cv2.COLOR_BGR2GRAY)   #convert it into grayscale (Y←0.299⋅R+0.587⋅G+0.114⋅B)
            #frameBW = np.mean(framelive, axis=2) # this a simple channel average
            #frameBW = B/N*framelive[:,:,0] + G/N*framelive[:,:,1] + R/N*framelive[:,:,2]
            
            # saturation alert ... must be analysed before BW transorm is performed
            if self.specmode == True: # we must be in specmode and have the window to show saturation alert
                if np.max(framelive) > 254:  # if there is any pixel in any channel > 254
                    try:
                        self.specwindow.ui.label_32.setVisible(True)
                    except:
                        pass
                else:
                    try:
                        self.specwindow.ui.label_32.setVisible(False)
                    except:
                        pass

            # liveview BW
            if self.ui.checkBox_grayscale.isChecked() == True:  # if it is checked we overwrite the liveframe with its BW version
                self.framelive = frameBW
            else: 
                self.framelive = framelive
            self.frameid += 1

            # prepare the live spectrum
            xpixelnr = self.resolution[1]                               # to normalize the integrated frame
            if self.ui.checkBox_useROI.isChecked():         # if we use ROI we have to cut the BWframe before we sum over the frame
                frameBW = frameBW[self.ROIymin : self.ROIymax, :]       # we cut the desired ROI
                xpixelnr = self.ROIymax-self.ROIymin                    # to normalize the integrated frame

            if self.averagemode == True:                    # we check if we have to average
                self.averageID += 1     # we increase the number of spectra that we have
                self.currspec = 1/self.ui.horizontalSlider_average.value()*np.sum(frameBW, 0)/xpixelnr + self.currspec

                if self.averageID >= self.ui.horizontalSlider_average.value() and self.freezemode == False:
                    self.speclive =   self.currspec #
                    self.currspec = self.specreset
                    self.averageID = 0      # we start from new with a new frame
                    self.specid += 1

                    # finaly we perform the bayer correction if checked
                    if self.bayercorrmode == True: # if bayercorrmode is running!
                        self.speclive = self.speclive/self.bayerspec # we devide our spec by the bayerspec   


            else:    # if not, the averaging mode is off so we directly have the live, single frame spectrum
                self.speclive = np.sum(frameBW, 0)/xpixelnr                 # we integrate over the frame
                self.specid += 1
                
                # finaly we perform the bayer correction if checked
                if self.bayercorrmode == True: # if bayercorrmode is running!
                    self.speclive = self.speclive/self.bayerspec # we devide our spec by the bayerspec   


    def generateemptydata(self):
        self.frameid = 0    # the frame number we got after connecting to the cam
        self.specid = 0     # the first number corresponding to the first frame
        self.averageID = 0  # keep at what frame for averaging we are
        self.framelive = np.zeros([self.resolution[1], self.resolution[0], 3], dtype=np.uint8)  # zero frame .. will be updated when cam is connected
        self.speclive = np.zeros([1, self.resolution[0]])                                       # zero spec .. will be updated when cam is connected
        self.speclive = self.speclive[0]                                                        # now we are done ... list in list is removed
        self.specreset = self.speclive                                                          # zero spec ... needed for spec averaging to reset growing spec
        self.currspec = self.specreset                                                          # growing spectrum when averaging is activated
        self.bayerspec = self.specreset + 1         # we start with a flat bayercorrection
        self.pxaxis = np.linspace(0, self.resolution[0]-1, self.resolution[0])    # this is and will ever be the pixel axis of our sensor
        self.wlaxis = self.pxaxis                   # we start with wlaxis equal to pixel axis
        self.xid = 10       # random initial pixel id from marker

    def imagemani(self, frame):             # this manipulates the frame and flips the x od/and y axis
        # flip x and y
        if self.ui.checkBox_flipx.isChecked():      
            frame = cv2.flip(frame,1)
        if self.ui.checkBox_flipy.isChecked():
            frame = cv2.flip(frame,0)
        return frame


    def setexposuretime(self):  # update exposure time
        self.ui.label_exposure.setText(str(self.ui.horizontalSlider_exposure.value()))
        if self.runcam == True:
            self.mycam.set(cv2.CAP_PROP_EXPOSURE, self.ui.horizontalSlider_exposure.value())

    def setbrightness(self):    # update brightness (not sure if that makes any sense)
        self.ui.label_bright.setText(str(self.ui.horizontalSlider_bright.value()))
        if self.runcam == True:
            self.mycam.set(cv2.CAP_PROP_BRIGHTNESS, self.ui.horizontalSlider_bright.value())

    def setgain(self):
        self.ui.label_gain.setText(str(self.ui.horizontalSlider_gain.value()))
        if self.runcam == True:
            self.mycam.set(cv2.CAP_PROP_GAIN , self.ui.horizontalSlider_gain.value())
        
    def setaverage(self):
        self.ui.label_aver.setText(str(self.ui.horizontalSlider_average.value()))
        # reset averaging process
        self.currspec = self.specreset
        self.averageID = 0
        
    
    
       
####################################################################### liveview ##############################################################
 
    def livecamview(self):
        if self.runcam == True:
            if self.ui.pushButton_liveview.text() == "live view":
                self.ui.pushButton_liveview.setText("stop")
                self.showlivecam = True                          # we set the Flag and allow livecam view ... for the while loop in setupHW
                self.liveviewworker = LivecamWorker(self)               # and start the worker
                self.threadpool.start(self.liveviewworker)
            else:
                self.ui.pushButton_liveview.setText("live view")
                self.showlivecam = False
        else:
            self.statusmessage("no camera connected")


    def ROIylims(self,id):
        ROIstep = self.ROIsteps

        if id == 0:
            self.ROIymin -= ROIstep
            self.ui.lineEdit_ymin.setText(str(self.ROIymin))
        if id == 1 and self.ROIymin < self.ROIymax - ROIstep:  # here we also have to check if reducing ymax by 10 will not go below ROIymin
            self.ROIymax -= ROIstep
            self.ui.lineEdit_ymax.setText(str(self.ROIymax))
        if id == 2 and self.ROIymax > self.ROIymin + ROIstep:  # same for the lower ylim when increasing
            self.ROIymin += ROIstep
            self.ui.lineEdit_ymin.setText(str(self.ROIymin))
        if id == 3:
            self.ROIymax += ROIstep
            self.ui.lineEdit_ymax.setText(str(self.ROIymax))

    def setupHW(self):
        self.LVwindow_name = "camera view"
        
        # we prepare the window for full frame image ... to adjust
        cv2.namedWindow(self.LVwindow_name, cv2.WINDOW_NORMAL)
        cv2.moveWindow(self.LVwindow_name, self.resolution[0] - 1, self.resolution[1] - 1)
        cv2.setWindowProperty(self.LVwindow_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        
        while self.showlivecam == True:    #  interrupt is set by settings live view button
            # option show image data
            frame = self.framelive  # we want the whole thing
            
            if self.ui.checkBox_useROI.isChecked():     # if we use ROI .. show ROI
                cv2.line(frame, (0, self.ROIymin), (self.resolution[0]-1, self.ROIymin), (0, 0, 160), 1)
                cv2.line(frame, (0, self.ROIymax), (self.resolution[0]-1, self.ROIymax), (0, 0, 160), 1)


            cv2.imshow(self.LVwindow_name, frame) # we update the plot    
            key = cv2.waitKey(10) # is needed otherwise the image is not updated ... it needs some time
        
            # ways out of that loop and to finish the software in camera mode
            if key == 27:  # ways to finish the loop
                break
            
        cv2.destroyWindow(self.LVwindow_name)   # finally we close the window 


    ###################################################### Calibration ############################################################################
    
    def togglecalmode(self):      # that we dont have to move the slider just clicking on it is enough
        if self.ui.horizontalSlider_wlcalmode.value() == 3:
            self.ui.horizontalSlider_wlcalmode.setValue(2)
        else: 
            self.ui.horizontalSlider_wlcalmode.setValue(3)


    def computewlaxis(self):
    
        if self.ui.horizontalSlider_wlcalmode.value() == 2:     # calibration via 2 points
            # first we get the points and give them short variable names
            id1 = self.ui.lineEdit_px1.text()
            id2 = self.ui.lineEdit_px3.text()
            wl1 = self.ui.lineEdit_wl1.text()
            wl2 = self.ui.lineEdit_wl3.text()
            if id1 == id2:
                self.statusmessage("bad calibration points")
            else:
                pixelx = self.resolution[0]  # the amount of pixels along the wavelength (x) axis

                m = (float(wl2)-float(wl1)) / (int(id2) - int(id1))
                b = float(wl2) - m*int(id2)
                self.wlaxis = np.linspace(0, pixelx-1, pixelx)*m  + b # store the wavelength axis in the main spectrometer object
                self.wlaxiscal = np.linspace(0, pixelx-1, pixelx)*m  + b # store the wavelength axis in the main spectrometer object
                self.calibrated = True # we have calibrated the spectrometer
                
                if self.specmode: #if we have the spec liveview open (what can be assumed) we also have to update its wlaxis
                    self.specwindow.ui.MplWidget.wlaxis = self.wlaxis
        

        elif self.ui.horizontalSlider_wlcalmode.value() == 3:     # calibration via 3 points
            print("here comes the 3 point calibration")
            # first we get the points and give them short variable names
            x1 = float( self.ui.lineEdit_px1.text() )
            x2 = float( self.ui.lineEdit_px2.text() )
            x3 = float( self.ui.lineEdit_px3.text() )
            w1 = float( self.ui.lineEdit_wl1.text() )
            w2 = float( self.ui.lineEdit_wl2.text() )
            w3 = float( self.ui.lineEdit_wl3.text() )

            if x1 == x2 or x1 == x3 or x2 == x3:
                self.statusmessage("bad calibration points")
            else:
                pixelx = self.resolution[0]  # the amount of pixels along the wavelength (x) axis
                xax = np.linspace(0, pixelx-1, pixelx) # we create the x axis
        
                a = (x1*(w3-w2)+w1*(x2-x3)-x2*w3+w2*x3)/((x1-x2)*(x1-x3)*(x2-x3))
                b = (x1**2*(w2-w3)+w1*(x3**2-x2**2)+x2**2*w3-w2*x3**2)/((x1-x2)*(x1-x3)*(x2-x3))
                c = (x1*(x1*x2*w3-x1*w2*x3-x2**2*w3+w2*x3**2)+w1*x2*x3*(x2-x3))/((x1-x2)*(x1-x3)*(x2-x3))

                self.wlaxis = a*xax**2 + xax*b  + c # store the wavelength axis in the main spectrometer object

                if self.specmode: #if we have the spec liveview open (what can be assumed) we also have to update its wlaxis
                    self.specwindow.ui.MplWidget.wlaxis = self.wlaxis

    def wlcalmode(self):
        if self.ui.horizontalSlider_wlcalmode.value() == 2:
            self.ui.pushButton_getP2.setVisible(False)
            self.ui.lineEdit_wl2.setVisible(False)
            self.ui.lineEdit_px2.setVisible(False)
            self.ui.label_20.setVisible(False)

        elif self.ui.horizontalSlider_wlcalmode.value() == 3:
            self.ui.pushButton_getP2.setVisible(True)
            self.ui.lineEdit_wl2.setVisible(True)
            self.ui.lineEdit_px2.setVisible(True)
            self.ui.label_20.setVisible(True)



    def saveconf(self):
        A = self.wlaxis   #we get the current calibration axis/wavelength axis
        B = 0*A                     # make a zero vector of the same size as A to store additional confdata in it
        if self.ui.checkBox_flipx.isChecked():      # if x-axis is flipped set 0 adress to 1 = true
            B[0] = 1
        if self.ui.checkBox_flipy.isChecked():      # if y-axis is flipped set 1 adress to 1 = true
            B[1] = 1
        B[2] = self.ROIymin       # in adress 2 and 3 strore the ROI parameters
        B[3] = self.ROIymax
        if self.ui.checkBox_useROI.isChecked():
            B[4] = 1                        # use adress 4 if ROI is activated

        S = np.array([A, B])       # the matrix combining both 
        np.save("confs\specconfig.npy", S) # also save it as numpy file
        self.statusmessage("calibration saved")   #send message

    def resetcal(self):
        if fileexists(getfolder()+"\confs\specconfig.npy"):           # check if a configfile exists and then delete it
            removefile(getfolder()+"\confs\specconfig.npy")
        self.wlaxis = self.pxaxis           # overwrite the wlaxis with the pixelaxis
        if self.specmode == True:                     #if we have the spectrumplot running, update its wlaxis
            self.specwindow.ui.MplWidget.wlaxis = self.pxaxis
        self.statusmessage("calibration deleted")     # send message



    ###################################################### spectrometer mode #######################################################################
    
    def spectrometermode(self):
        if self.specmode == False:                      # if we are not running the specmode up to now ... we start it
            self.specmode = True                        # we started the spectrometer mode
            self.setROIalarm()                                              # update marker on plotting window if ROI is active
            self.livespecworker = LivespecWorker(self)                                  # and define the worker to update the spec data to the plot
            self.threadpool.start(self.livespecworker)                                  # we start the thread
           
        elif self.specmode == True:     # the specmode is running -->
            self.specmode = False       # we stop the spectrometer mode (interrupts and ends the plot update thread)


    def specplotupdate(self):
        self.specwindow.ui.MplWidget.xax = self.pxaxis # we write the pixelaxis into the MplQidget
        plotwincom = WindowCom()               # we create a comchannel
        plotwincom.signal.connect(self.specwindow.ui.MplWidget.updateframedata)
        while self.specmode == True:
            plotwincom.signal.emit(self.speclive)
            time.sleep(0.01)

    def bayercorr(self):
        if fileexists(getfolder()+"\confs\\bayercorrection.csv"):           # check if bayer correction file exists
            if self.bayercorrmode == False:
                A = np.loadtxt("confs\\bayercorrection.csv")
                wl = A[:,0]     # wavelength of correction
                bayI = A[:,1]   # corresponding intensity
                self.bayerspec = np.interp(self.wlaxis, wl, bayI)       # compute interpolation ... extrapolation is constant the first/last value of bayercorr file
                self.bayerspec = self.bayerspec/np.max(self.bayerspec)  # normalize correction function
                self.bayercorrmode = True   # set Flag to True
            else:
                self.bayercorrmode = False  # we finish bayermode
        else:                                                        # if the bayercorr file does not exist
            self.statusmessage("no bayer-correction file found")


    def getP(self, id):
        if self.specmode:
            if id == 1:
                self.ui.lineEdit_px1.setText(str(self.specwindow.ui.MplWidget.xid))
            elif id == 2:
                self.ui.lineEdit_px2.setText(str(self.specwindow.ui.MplWidget.xid))
            elif id == 3:
                self.ui.lineEdit_px3.setText(str(self.specwindow.ui.MplWidget.xid))
    
        else: # if there is no specmode running, we can not get ids from the marker
                self.statusmessage("no point in spectrum selected")



################################################################## save data ##############################################################
    def clicksavespec(self):            # save spectrum
        if self.specmode == True:
            self.clicksaveimg() # first, save the image, so we know what was on the sensor

            # now continue and write the spectrum
            #combine filename
            fpath = self.ui.lineEdit_filepath.text()
            fname = self.ui.lineEdit_filename.text()
            fformat = self.ui.lineEdit_specformat.text()
            imgnumber = self.ui.lineEdit_imgnumber.text()
            
            #check if autoadd image number is checker
            if self.ui.checkBox_autoaddimgnumber.isChecked() == False:
                fullpath = fpath+"\\"+fname+"."+fformat
                fullpathnpy = fpath+"\\"+fname+"."+"npy"

            elif self.ui.checkBox_autoaddimgnumber.isChecked() == True:
                fullpath = fpath+"\\"+fname+imgnumber+"."+fformat
                fullpathnpy = fpath+"\\"+fname+imgnumber+"."+"npy"

                # increase image number
                numb = int(imgnumber)
                numb += 1
                self.ui.lineEdit_imgnumber.setText(str(numb))
            
            # generate matrix that we want to save as spectrum
            x = self.specwindow.ui.MplWidget.xaxP    # wavelength
            y = self.specwindow.ui.MplWidget.yaxP    # intensity or Transmission or Extinction
            if np.shape(y) == (1,1920):
                y = np.reshape(np.transpose(y), -1)
            S = np.transpose(np.array([x, y]))       # the mattrix combining both        
            np.savetxt(fullpath, S, delimiter='\t') # now save that thing
            np.save(fullpathnpy, S) # also save it as numpy file

            # save spectrum as image
            self.specwindow.ui.MplWidget.saveimg(fpath+"\\"+fname+imgnumber+"."+"png")

        else:
            self.statusmessage("no spectrum to save")

    def clicksaveimg(self):         # save image
        frame = self.framelive
        #combine filename
        fpath = self.ui.lineEdit_filepath.text()
        fname = self.ui.lineEdit_filename.text()
        fformat = self.ui.lineEdit_imgformat.text()
        imgnumber = self.ui.lineEdit_imgnumber.text()
        
        #check if autoadd image number is checker
        if self.ui.checkBox_autoaddimgnumber.isChecked() == False:
            fullpath = fpath+"\\"+fname+"."+fformat
        elif self.ui.checkBox_autoaddimgnumber.isChecked() == True:
            fullpath = fpath+"\\"+fname+imgnumber+"."+fformat
            self.ui.lineEdit_imgnumber.setText(imgnumber)

        cv2.imwrite(fullpath, frame) # now save that thing


##############################################################################################################################################
#                                                          SPECTRUM LIVE VIEW WINDOW
##############################################################################################################################################

class Showlivespec(QMainWindow):
    
    ## initializing stuff when class is called ... all for/inside GUI
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # stuff for window
        self.ui = Ui_specplottingwin()
        self.ui.setupUi(self)
        #self.setWindowFlags(self.windowFlags() | qtc.Qt.WindowStaysOnTopHint) #keep control panel on top
        self.setWindowFlag(qtc.Qt.FramelessWindowHint) ## we dont want to see the window frame
        self.setAttribute(qtc.Qt.WA_TranslucentBackground) ## we dont want to see the window frame
        self.ui.label_22.setStyleSheet("color:#bebebe; background-color: transparent; border-color: transparent; font-size: 10pt; font-weight:600") ## to keep the format
        self.ui.label_25.setStyleSheet("color:#bebebe; background-color: transparent; border-color: transparent; font-size: 10pt; font-weight:600") ## to keep the format
        self.ui.label_26.setStyleSheet("color:#bebebe; background-color: transparent; border-color: transparent; font-size: 10pt; font-weight:600") ## to keep the format
        self.ui.label_30.setStyleSheet("color:#bebebe; background-color: transparent; border-color: transparent; font-size: 10pt; font-weight:600") ## to keep the format
        self.ui.label_31.setStyleSheet("color:#bebebe; background-color: transparent; border-color: transparent; font-size: 10pt; font-weight:600") ## to keep the format
        self.ui.label_32.setVisible(False) # saturation alert label
        self.setWindowIcon(QIcon('confs/SWicon.png'))  # use this icon on the OS
        self.setWindowTitle("live-spectrum")  # this is the Frame Title (shown as WindowName in OS)
        self.show()
        self.move(120, 1080-790)
        self.ui.MplWidget.canvas.mpl_connect('button_press_event', self.waitonwindowclick)      # if clicked on mpl then start function that writes coordinates into MplWidget
        self.ui.MplWidget.canvas.mpl_connect('motion_notify_event', self.mousemove)      # if clicked on mpl then start function that writes coordinates into MplWidget
        self.specmodelist = ["Intensity", "Transmission", "Extinction"]
        self.ui.comboBox_analysismode.addItems(self.specmodelist)
        self.specmodes()    # to start with default conditions
        self.togglecalmode() # we automatically switch from px to nm (also setups labels and everything in consequence)
    
        #### zoom parameter ####
        self.zoomxrange = [0, 1920] # range that will be plotted
        self.zoomyrange = [0, 1] # range that will be plotted
        self.zoomstep = 0           # zooming has 2 steps (set first lim, then second lim)
        self.zoommode = False        # Flag if we are in the zoom process

        ######## buttons #######
        self.ui.comboBox_analysismode.currentIndexChanged.connect(self.specmodes)
        self.ui.pushButton_source.clicked.connect(self.ui.MplWidget.getlamp)
        self.ui.pushButton_background.clicked.connect(self.ui.MplWidget.getback)
        self.ui.pushButton_reset.clicked.connect(self.ui.MplWidget.resetlampandback)
        self.ui.horizontalSlider_axisswitch.sliderReleased.connect(self.togglecalmode)
        self.ui.pushButton_zoom.clicked.connect(self.zooming)
        self.ui.pushButton_home.clicked.connect(self.zoomout)
        self.ui.pushButton_mini.clicked.connect(self.minimizespecwindow)


######################### general functions #####################################
    def minimizespecwindow(self):
        self.showMinimized() # minimize control panel




######################### Specmodeswitching ######################################

    def specmodes(self):   # this functions sets the y-axis mode (I,T,A) in the MplWidget and shows/hides buttons for lamp and backgroudn spec, respectively
        # intensity
        if self.ui.comboBox_analysismode.currentIndex() == 0:   
            self.ui.MplWidget.specmode = 0  
            self.ui.MplWidget.zoomed = False
            self.ui.label_31.setText("arb. u.") # marker unit for the y axis

        # transmission
        if self.ui.comboBox_analysismode.currentIndex() == 1:
            self.ui.MplWidget.specmode = 1
            self.ui.label_31.setText("%") # marker unit for the y axis
            self.ui.MplWidget.zoomed = True
            self.ui.MplWidget.zoomboxY = [0, 110]

        #extinction
        if self.ui.comboBox_analysismode.currentIndex() == 2:
            self.ui.MplWidget.specmode = 2
            self.ui.label_31.setText("") # marker unit for the y axis
            self.ui.MplWidget.zoomed = False

        #finally we update the y axis label
        self.ui.MplWidget.updateyax()



########################## graph/MplWidget control functions ####################################

    def xaxswitching(self):
        if self.ui.horizontalSlider_axisswitch.value() == 0:
            self.ui.MplWidget.wlmode = False
            self.ui.label_30.setText("px")  # unit for cursor/marker
        elif self.ui.horizontalSlider_axisswitch.value() == 1:
            self.ui.MplWidget.wlmode = True
            self.ui.label_30.setText("nm") # unit for cursor/marker


    def togglecalmode(self):      # that we dont have to move the slider just clicking on it is enough
        if self.ui.horizontalSlider_axisswitch.value() == 1:
            self.ui.horizontalSlider_axisswitch.setValue(0)
        else: 
            self.ui.horizontalSlider_axisswitch.setValue(1)
        self.xaxswitching()

########################## marker from Mpl - functions ######################################

    # save pixed ids if we click on the spectrum figure/graph .... needed for calibration
    def waitonwindowclick(self, event):
        if event.xdata is not None:
            xwl = float(event.xdata)   # xid of mouse marker
            self.ui.MplWidget.xmarkwl = round(event.xdata, 2)      # xid to show not rounded wavelength (2 digits)
            self.ui.label_25.setText(str(self.ui.MplWidget.xmarkwl))    # write markerpos x to graph
            self.ui.MplWidget.yid = round(event.ydata,2)             # yid of mouse marker
            self.ui.MplWidget.ymark = round(event.ydata,2)       # yid of mouse marker (2 digits)
            self.ui.label_26.setText(str(self.ui.MplWidget.ymark))    # write markerpos x to graph
            if self.ui.MplWidget.wlmode == True:
                self.ui.MplWidget.xid = self.findnearesid(self.ui.MplWidget.wlaxis, xwl)
            else:
                self.ui.MplWidget.xid = self.findnearesid(self.ui.MplWidget.xax, xwl)

            
            # now check if we are in zoommode
            if self.zoommode == True:
                if self.zoomstep == 0:  # we gave the first limit
                    self.zoomxrange[0] = self.ui.MplWidget.xid
                    self.zoomyrange[0] = self.ui.MplWidget.yid
                    self.ui.MplWidget.zoommode = True
                    self.ui.MplWidget.zoomboxX[0] = self.ui.MplWidget.xid
                    self.ui.MplWidget.zoomboxY[0] = self.ui.MplWidget.yid
                    
                elif self.zoomstep == 1:  # we gave the first limit
                    self.zoomxrange[1] = self.ui.MplWidget.xid
                    self.zoomyrange[1] = self.ui.MplWidget.yid
                    self.zoommode = False
                    self.ui.MplWidget.zoommode = False
                    self.ui.MplWidget.rectangle.set_visible(False)
                    self.ui.MplWidget.zoomed = True         # we have to points so the Mplwidget can use the zoomed window y axis

                    # now we have both marks and we can write them to the MplWidget
                    if self.zoomxrange[0] < self.zoomxrange[1]:      # we check that the lower limit is lower, how it should be
                        self.ui.MplWidget.plotxrange[0] = self.zoomxrange[0]
                        self.ui.MplWidget.plotxrange[1] = self.zoomxrange[1]
                    else:   # if its the other way round we make it how it should be
                        self.ui.MplWidget.plotxrange[0] = self.zoomxrange[1]
                        self.ui.MplWidget.plotxrange[1] = self.zoomxrange[0]
                self.zoomstep = 1 # we are one step further

            return self

    def mousemove(self, event):
        if self.zoommode == True:
            if event.xdata is not None:
                xwl = float(event.xdata)   # xid of mouse marker
                self.ui.MplWidget.zoomboxY[1] = round(event.ydata,2)
                
                if self.ui.MplWidget.wlmode == True:
                    self.ui.MplWidget.zoomboxX[1] = self.findnearesid(self.ui.MplWidget.wlaxis, xwl)
                else:
                    self.ui.MplWidget.zoomboxX[1] = self.findnearesid(self.ui.MplWidget.xax, xwl)


    def findnearesid(self, arr, val):
        diff = np.abs(arr - val) # absolut value of difference
        ids = np.where(diff == np.min(diff))
        pixid = ids[0]
        return pixid[0]

    def zooming(self):
        self.zoomout() # first, we unzoom
        self.zoomstep = 0
        self.zoommode = True
        
    def zoomout(self):
            self.ui.MplWidget.zoomed = False    # we use the autoscaling of the Mplwidget
            self.ui.MplWidget.plotxrange[0] = 0 # and reset the ranges
            self.ui.MplWidget.plotxrange[1] = 1920



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
        

class WindowCom(qtc.QObject):   # we use this to transfer data between windows
    signal = qtc.Signal(object)


class Fakeparentwin():
    def __init__(self):
        self.intwinpos = [100, 10]


##  start gui
if __name__ == "__main__":
    app = QApplication(sys.argv)              # define Qapplication Object
    fakeparentwin = Fakeparentwin()           # that everything is fine for printedLAB Labcontrol  
    experimentUI = spectrometerwin(0,fakeparentwin)       # define User interface
    app.exec()                                      # execute
    sys.exit(print("code finished"))                # exit code