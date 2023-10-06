##############################################################################################################################################
# 
# printedLABs - SpecControl
# 
# 
# Thorsten Schumacher 
# University of Bayreuth - Germany
# Thorsten.Schumacher@uni-bayreuth.de
# Version 0.9
#                                                                               
#
##############################################################################################################################################


# import relevant external modules
import cv2
import numpy as np 
import sys
import time
import nest_asyncio # get rid of async warnings (event loop issue)
from webbrowser import open as browseropen
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
from interface_spectrometer.spectrometersettings_gui import Ui_spectrometer_settingswin
from interface_spectrometer.specplotting_gui import Ui_specplottingwin
from interface_spectrometer.Workerclass import CamreadWorker, LivecamWorker, LivespecWorker, Devupdater
from interface_spectrometer.analyseclasses import Integratedspec, Wlanalyse


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
        self.helpweblink = 'https://printedlabs.uni-bayreuth.de/'   # here you will find some help using the software
        self.setWindowIcon(QIcon('confs/SWicon.png'))  # use this icon on the OS

        self.move(self.parentwin.intwinpos[0], self.parentwin.intwinpos[1]) # move the window to its position
        self.parentwin.intwinpos[1] += 286  #   store in parent window the position for the next interface window
        self.show()

        ## prepare device list and communication stuff
        self.interfacenr = interfacenum
        self.interfacename = "SystemClock - InterfaceNr. "+ str(interfacenum)
        self.sensors = []   # here we store the sensors as objects
        self.sensorid = 0   # we increase the sensorid with every added sensor
        self.devicelist = []    #for the experiment control panel we have here the avail. device list
        self.devnr = 0          # device number ... increases if we add devices ... for identification
        self.valuelist = []     #here we have the corresponding valuelist
        self.valueunit = []     #here is the unit
        self.ready = []         #here, if the device is ready (for synchronous measurements)
        self.analyselist = ["Integrated intensity", "Wavelength intensity"] # this are the tools we have
        self.ui.comboBox_devices.addItems(self.analyselist) # we put the tools in the toolslist
        

        # available sources (IDs) for cv2
        self.camindexfound = ["0"] #we start with one source
        self.ui.comboBox_camport.addItems(self.camindexfound)
        self.frameid = 0    # the frame number we got after connecting to the cam
        self.resolution = [1920, 1080] # this is the only resolution we are working with
        self.ROIymin = 200 # lower pixel of yROI
        self.ROIymax = 880 # lower pixel of yROI
        self.ROIsteps = 10 # discretization for ROI

        # empty frame and spec
        self.frameid = 0    # the frame number we got after connecting to the cam
        self.specid = 0     # the first number corresponding to the first frame
        self.averageID = 0  # keep at what frame for averaging we are
        self.framelive = np.zeros([self.resolution[1], self.resolution[0], 3], dtype=np.uint8)  # zero frame .. will be updated when cam is connected
        self.speclive = np.zeros([1, self.resolution[0]])                                       # zero spec .. will be updated when cam is connected
        self.speclive = self.speclive[0]                                                        # now we are done ... list in list is removed
        self.specreset = self.speclive                                                          # zero spec ... needed for spec averaging to reset growing spec
        self.currspec = self.specreset                                                          # growing spectrum when averaging is activated
        self.bayerspec = self.specreset + 1         # we start with a flat bayercorrection
        self.pxaxis = np.linspace(0, 1919, 1920)    # this is and will ever be the pixel axis of our sensor
        self.wlaxis = self.pxaxis                   # we start with wlaxis equal to pixel axis
        self.xid = 10       # random initial pixel id from marker


        # start an update thread for reading the camera if available and define Flags for the code
        self.threadpool = qtc.QThreadPool()
        self.runcam = False       # Flag for grabbing frames
        self.showlivecam = True   # Flag to check if live image is shown ... required to interrupt image loop
        self.specmode = False     # Flag if we are in specmode
        self.ROIon = False        # Flag if we are running ROI mode
        self.devupdating = True   # Flag if devupdate thread is running
        self.bayercorrmode = False # flag if bayercorrection is running
        self.devupdateworker = Devupdater(self) # create a worker object to update devices
        self.threadpool.start(self.devupdateworker) # start thread

        ## add settings window
        self.settingswin = spectrometersettingswin(self)  
        self.settingswin.ui.lineEdit_filepath.setText(getfolder()+"\savedata")  # write current folder into the folder linedit

        ## setup calibration and stuff
        self.getoldcalibration() # finally we load (if config file exists) the former calibration data
        self.setexposuretime() # to update slider and labels
        self.setbrightness() # to update slider and labels
        self.setgain() # ... what is now the averager ... to update slider and labels
    
    ########################################## UI buttons ####################################################
        
        # general stuff
        self.ui.pushButton_comrefresh.clicked.connect(self.scancam)
        self.ui.pushButton_comconnect.clicked.connect(self.connect2cam)
        self.ui.pushButton_settings.clicked.connect(self.opensettings)
        self.ui.pushButton_exit.clicked.connect(self.closeSW)
        self.ui.pushButton_help.clicked.connect(self.helplink)

        #camcontrol
        self.ui.horizontalSlider_exposure.valueChanged.connect(self.setexposuretime)
        self.ui.horizontalSlider_bright.valueChanged.connect(self.setbrightness)
        self.ui.horizontalSlider_gain.valueChanged.connect(self.setgain)

        #save buttons 
        self.ui.pushButton_savespec.clicked.connect(self.clicksavespec)
        self.ui.pushButton_saveimg.clicked.connect(self.clicksaveimg)
        
        #speccontrols
        self.ui.checkBox_spectrum.clicked.connect(self.spectrometermode)
        self.ui.checkBox_bayercorr.clicked.connect(self.bayercorr)

        # analyse
        self.ui.pushButton_adddev.clicked.connect(self.adddev)
        self.ui.pushButton_deldev.clicked.connect(self.deldev)


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
    def helplink(self):
        browseropen(self.helpweblink)


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

        # close all "connected" sensors
        if len(self.sensors) > 0: # if we have more than one sensor
            for dev in self.sensors: # all sensors
                dev.close() # close command
                del(dev)



        time.sleep(0.5)             # wait some time to stop the threads
        try:
            self.settingswin.close() # try to close the settings window
            self.specwindow.close()  # try to close the livespec window
            self.mycam.release()    # try to close the cam connection (if no cam is connected its also fine)
        except:
            pass
        self.close()                # close UI


    def opensettings(self):         # toggles between settings window is shown or not
        if self.ui.pushButton_settings.text() == "settings": 
            self.settingswin.show()
            self.ui.pushButton_settings.setText("close settings")
        else:
            self.settingswin.hide()
            self.ui.pushButton_settings.setText("settings")

    def getoldcalibration(self):
        if fileexists(getfolder()+"\confs\specconfig.npy"):           # check if config gile exists
            storeddata = np.load("confs\specconfig.npy")              # load it
            self.wlaxis = storeddata[0,:]                       # first col is the wavelength axis
            ymin = int(storeddata[1,2])                         # now start in second col with the parameters that we have to set again ... here yminROI
            ymax = int(storeddata[1,3])                         # ... here ymaxROI
            if storeddata[1,0] == 1:                            # ... flipx
                self.settingswin.ui.checkBox_flipx.setChecked(True) 
            if storeddata[1,1] == 1:                            # ... flipy
                self.settingswin.ui.checkBox_flipy.setChecked(True)
            if storeddata[1,4] == 1:                            # ... use ROI
                    self.settingswin.ui.checkBox_useROI.setChecked(True)
                    self.ROIon = True
                    self.settingswin.setROIalarm()
            self.settingswin.ui.lineEdit_ymin.setText(str(ymin))    # ... set ROImin in settingswin
            self.settingswin.ui.lineEdit_ymax.setText(str(ymax))    # ... set ROImax in settingswin
            self.ROIymin = ymin                                 # ... set ROImin
            self.ROIymax = ymax                                 # ... set ROIax
            self.statusmessage("calibration loaded")            # inform user that conf was loaded
        else:
            self.statusmessage("no calibration file")           # or inform user that no config file exists

    ###################################### camera readout and interface #########################################

    def returnCameraIndexes(self): # this function searches the first "ports" for an camera and stores the found ids
        
        # checks the first 10 indexes.
        index = 0                   # here we start searching
        camindexfound = []          # here is a cam
        imax = 10                   # here we stop searching
        while index < imax:
            cap = cv2.VideoCapture(index)           #connect to device
            if cap.isOpened():                      # if there is an open connection
                camindexfound.append(str(index))    # add this to the cam list
            
            cap.release()           # and close the connection again
            index += 1              # try next ID

        # finally we update the combobox and store the result in the object
        self.ui.comboBox_camport.clear()    
        self.ui.comboBox_camport.addItems(camindexfound)  
        self.camindexfound = camindexfound
        self.resetstatus() # we are done scanning what propably takes longer than 3 seconds

    def scancam(self):  # we start scanning available camera sources within a thread .. so that nothing freezes
        # scanning can take a long time .. so we keep the status on "scanning"
        self.ui.label_status.setText("scanning sources") 
        self.ui.label_status.repaint()
        # we start a thread doing the work and scanning
        scanthread = Thread(target = self.returnCameraIndexes, args=()) 
        scanthread.start()

    def connect2cam(self):
        if self.ui.pushButton_comconnect.text() == "connect":
            self.statusmessage("connecting")
            self.mycam = cv2.VideoCapture(int(self.ui.comboBox_camport.currentText()), cv2.CAP_DSHOW)  # , cv2.CAP_MSMF is suggested backend but also default, cv2.CAP_DSHOW comes from chatGPT
            #print(self.mycam.getBackendName())
            
            self.ui.pushButton_comconnect.setText("disconnect")
            if self.mycam.isOpened():
                self.runcam = True
                self.mycam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
                self.mycam.set(cv2.CAP_PROP_FRAME_WIDTH, self.resolution[0])
                self.mycam.set(cv2.CAP_PROP_FRAME_HEIGHT, self.resolution[1])
                #self.mycam.set(cv2.CAP_PROP_AUTO_WB, 0.75) # thies deactivates white balance
                #self.mycam.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25) # deactivates auto exposure
                #self.mycam.set(cv2.CAP_PROP_FPS, 30)
                self.setexposuretime() # to update slider and labels
                self.setbrightness() # to update slider and labels
                self.setgain() # ... what is now the averager ... to update slider and labels
                # now start reading the cam in a separate thread
                self.camreadworker = CamreadWorker(self)
                self.threadpool.start(self.camreadworker)
                if self.ui.checkBox_spectrum.isChecked() == False:  # if the spectrum screen is not shown then start it now
                    self.spectrometermode()  # we autostart the spectrometer mode
                    self.ui.checkBox_spectrum.setChecked(True)  #and check the checkbox that it is running ... simply as checking the specmode
            else:
                self.statusmessage('failed')
                self.ui.pushButton_comconnect.setText("connect")

        else:
            self.runcam = False
            self.mycam.release()
            
            self.ui.pushButton_comconnect.setText("connect")
            self.statusmessage("disconnected")

    
    def camreadupdate(self):
        self.frameid = 0    # after connecting to cam we start with frame nr 0
        self.currspec = self.speclive
        
        # weight of color channels
        R = 1
        B = 0.75
        G = 4
        N = R+B+G
        
        # now we start reading
        while self.runcam == True:
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
            if self.settingswin.ui.checkBox_useROI.isChecked():         # if we use ROI we have to cut the BWframe before we sum over the frame
                frameBW = frameBW[self.ROIymin : self.ROIymax, :]       # we cut the desired ROI
                xpixelnr = self.ROIymax-self.ROIymin                    # to normalize the integrated frame

            if self.ui.checkBox_average.isChecked():                    # we check if we have to average
                self.averageID += 1     # we increase the number of spectra that we have
                self.currspec = 1/self.ui.horizontalSlider_gain.value()*np.sum(frameBW, 0)/xpixelnr + self.currspec

                if self.averageID >= self.ui.horizontalSlider_gain.value():
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





    def imagemani(self, frame):             # this manipulates the frame and flips the x od/and y axis
        # flip x and y
        if self.settingswin.ui.checkBox_flipx.isChecked():      
            frame = cv2.flip(frame,1)
        if self.settingswin.ui.checkBox_flipy.isChecked():
            frame = cv2.flip(frame,0)


        return frame

    def setexposuretime(self):  # update exposure time
        self.ui.label_exposure.setText(str(self.ui.horizontalSlider_exposure.value()))
        if self.runcam == True:
            self.mycam.set(cv2.CAP_PROP_EXPOSURE, self.ui.horizontalSlider_exposure.value())

    def setbrightness(self):    # update brightness (not sure if that makes any sense)
        self.ui.label_bright.setText(str(self.ui.horizontalSlider_bright.value()))
        if self.runcam == True:
            #self.mycam.set(cv2.CAP_PROP_BRIGHTNESS, self.ui.horizontalSlider_bright.value())
            self.mycam.set(cv2.CAP_PROP_GAIN , self.ui.horizontalSlider_gain.value())

    def setgain(self):
        self.ui.label_aver.setText(str(self.ui.horizontalSlider_gain.value()))
        # reset averaging process
        self.currspec = self.specreset
        self.averageID = 0
        
        #### when it was gain
        #if self.runcam == True:
        #    self.mycam.set(cv2.CAP_PROP_GAIN , self.ui.horizontalSlider_gain.value())

    

    ########################################################## devices ########################################################################
    def adddev(self):
        id = self.ui.comboBox_devices.currentIndex()
        if id == 0: # we add integrated intensity
            self.sensors.append(Integratedspec(self, self.devnr))
            self.devicelist.append(self.sensors[-1].name)
            

        if id == 1: # we add integrated intensity
            self.sensors.append(Wlanalyse(self, self.devnr))
            self.devicelist.append(self.sensors[-1].name)

        
        self.devnr += 1 # prepare id for next device
        # update all ui components
        self.ui.listWidget_interf.clear() # clear all entries in the list widget
        self.ui.listWidget_interf.addItems(self.devicelist) # and rewrite all devices from the list
        

    def deldev(self):
        id = self.ui.listWidget_interf.currentRow()
        self.sensors[id].closeSW()
        self.ui.listWidget_interf.takeItem(id)
        del self.devicelist[id]
        del self.sensors[id]


    def devupdate(self):
        while self.devupdating == True:
            time.sleep(0.1)
            for dev in self.sensors:
                dev.update(self.wlaxis, self.speclive)
            
####################################################################### liveview ##############################################################
 
    def setupHW(self):
        self.LVwindow_name = "camera view"
        
        # we prepare the window for full frame image ... to adjust
        cv2.namedWindow(self.LVwindow_name, cv2.WINDOW_NORMAL)
        cv2.moveWindow(self.LVwindow_name, self.resolution[0] - 1, self.resolution[1] - 1)
        cv2.setWindowProperty(self.LVwindow_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        
        while self.showlivecam == True:    #  interrupt is set by settings live view button
            # option show image data
            frame = self.framelive  # we want the whole thing
            frmSat = np.amax(frame)
            
            if self.settingswin.ui.checkBox_useROI.isChecked():     # if we use ROI .. show ROI
                cv2.line(frame, (0, self.ROIymin), (1919, self.ROIymin), (0, 0, 160), 1)
                cv2.line(frame, (0, self.ROIymax), (1919, self.ROIymax), (0, 0, 160), 1)
        
            if self.settingswin.ui.checkBox_imginfo.isChecked() == True:    # if we want to see the additional infos
                
                if frmSat >= 240:
                    new_image = cv2.putText(
                    frame,
                    text = "Saturation: > 95 % warning!!!",
                    org = (30, 60),
                    fontFace = cv2.FONT_HERSHEY_DUPLEX,
                    fontScale = 1.0,
                    color = (0, 0, 0.6*255),
                    thickness = 1
                    )
                else:
                    new_image = cv2.putText(
                    frame,
                    text = "Saturation: "+"{:.2f}".format(100*frmSat/255)+" %",
                    org = (30, 60),
                    fontFace = cv2.FONT_HERSHEY_DUPLEX,
                    fontScale = 1.0,
                    color = (0, 0, 0.6*255),
                    thickness = 1
                    )
        
                # show integration time
                new_image = cv2.putText(
                frame,
                text = "Max. FPS: {:.2f}".format(self.mycam.get(cv2.CAP_PROP_FPS)),
                org = (30, 30),
                fontFace = cv2.FONT_HERSHEY_DUPLEX,
                fontScale = 1.0,
                color = (0, 0, 0.6*255),
                thickness = 1
                )

                # show camera parameter
                new_image = cv2.putText(
                frame,
                text = "Exposure val: {:.1f}".format(-1*self.ui.horizontalSlider_exposure.value()),
                org = (30, 90),
                fontFace = cv2.FONT_HERSHEY_DUPLEX,
                fontScale = 1.0,
                color = (0, 0, 0.6*255),
                thickness = 1
                )

                new_image = cv2.putText(
                frame,
                text = "Brightness: {:.1f} %".format(self.ui.horizontalSlider_bright.value()),
                org = (30, 120),
                fontFace = cv2.FONT_HERSHEY_DUPLEX,
                fontScale = 1.0,
                color = (0, 0, 0.6*255),
                thickness = 1
                )

                new_image = cv2.putText(
                frame,
                text = "Gain: {:.1f}".format(self.ui.horizontalSlider_gain.value()),
                org = (30, 150),
                fontFace = cv2.FONT_HERSHEY_DUPLEX,
                fontScale = 1.0,
                color = (0, 0, 0.6*255),
                thickness = 1
                )
        
            cv2.imshow(self.LVwindow_name, frame) # we update the plot    
            key = cv2.waitKey(10) # is needed otherwise the image is not updated ... it needs some time
        
            # ways out of that loop and to finish the software in camera mode
            if key == 27:  # ways to finish the loop
                break
            
        cv2.destroyWindow(self.LVwindow_name)   # finally we close the window 



    ###################################################### spectrometer mode #######################################################################
    
    def spectrometermode(self):
        if self.specmode == False:                      # if we are not running the specmode up to now ... we start it
            self.specwindow = Showlivespec()            # we create the plot window object                      
            self.specwindow.ui.MplWidget.wlaxis = self.wlaxis                           # we start with the old calibration file or the cam pixels
            time.sleep(0.25)                            # give it some time
            self.specmode = True                        # we started the spectrometer mode
            self.settingswin.setROIalarm()                                              # update marker on plotting window if ROI is active
            self.livespecworker = LivespecWorker(self)                                  # and define the worker to update the spec data to the plot
            self.threadpool.start(self.livespecworker)                                  # we start the thread

        elif self.specmode == True:     # the specmode is running -->
            self.specmode = False       # we stop the spectrometer mode (interrupts and ends the plot update thread)
            self.specwindow.close()     # and we close the window
            del self.specwindow         # we dele the spectrometer window

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


################################################################## save data ##############################################################
    def clicksavespec(self):            # save spectrum
        if self.specmode == True:   
            #combine filename
            fpath = self.settingswin.ui.lineEdit_filepath.text()
            fname = self.settingswin.ui.lineEdit_filename.text()
            fformat = self.settingswin.ui.lineEdit_specformat.text()
            imgnumber = self.settingswin.ui.lineEdit_imgnumber.text()
            
            #check if autoadd image number is checker
            if self.settingswin.ui.checkBox_autoaddimgnumber.isChecked() == False:
                fullpath = fpath+"\\"+fname+"."+fformat
                fullpathnpy = fpath+"\\"+fname+"."+"npy"

            elif self.settingswin.ui.checkBox_autoaddimgnumber.isChecked() == True:
                fullpath = fpath+"\\"+fname+imgnumber+"."+fformat
                fullpathnpy = fpath+"\\"+fname+imgnumber+"."+"npy"

                # increase image number
                numb = int(imgnumber)
                numb += 1
                self.settingswin.ui.lineEdit_imgnumber.setText(str(numb))
            
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
        fpath = self.settingswin.ui.lineEdit_filepath.text()
        fname = self.settingswin.ui.lineEdit_filename.text()
        fformat = self.settingswin.ui.lineEdit_imgformat.text()
        imgnumber = self.settingswin.ui.lineEdit_imgnumber.text()
        
        #check if autoadd image number is checker
        if self.settingswin.ui.checkBox_autoaddimgnumber.isChecked() == False:
            fullpath = fpath+"\\"+fname+"."+fformat
        elif self.settingswin.ui.checkBox_autoaddimgnumber.isChecked() == True:
            fullpath = fpath+"\\"+fname+imgnumber+"."+fformat
            # increase image number
            numb = int(imgnumber)
            numb += 1
            self.settingswin.ui.lineEdit_imgnumber.setText(str(numb))

        cv2.imwrite(fullpath, frame) # now save that thing


##############################################################################################################################################
#                                                          SETTINGS WINDOW
##############################################################################################################################################

class spectrometersettingswin(QMainWindow):
    
     ## initializing stuff when class is called ... all for/inside GUI
    def __init__(self, parentwin, *args, **kwargs):

        super().__init__(*args, **kwargs)
        # stuff for window
        self.ui =  Ui_spectrometer_settingswin()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() | qtc.Qt.WindowStaysOnTopHint) #keep control panel on top
        self.setWindowFlag(qtc.Qt.FramelessWindowHint) ## we dont want to see the window frame
        self.setAttribute(qtc.Qt.WA_TranslucentBackground) ## we dont want to see the window frame
        self.parentwin = parentwin

        self.calwllist = ["436.5", "546.3", "611.0"]    # this are the 3 best emission lines of an energy saving lamp (not LED but fluorescent tube)
        self.ui.lineEdit_wl1.setText(self.calwllist[0])
        self.ui.lineEdit_wl2.setText(self.calwllist[1])
        self.ui.lineEdit_wl3.setText(self.calwllist[2])

    ###################################### Buttons #################################################
        self.ui.pushButton_exit.clicked.connect(self.closesettings)
        self.ui.pushButton_liveview.clicked.connect(self.livecamview)
        self.ui.pushButton_getP1.clicked.connect(lambda: self.getP(1))
        self.ui.pushButton_getP2.clicked.connect(lambda: self.getP(2))
        self.ui.pushButton_getP3.clicked.connect(lambda: self.getP(3))
        self.ui.horizontalSlider_wlcalmode.valueChanged.connect(self.wlcalmode)
        self.ui.horizontalSlider_wlcalmode.sliderReleased.connect(self.togglecalmode)
        self.ui.pushButton_calwlaxis.clicked.connect(self.computewlaxis)
        self.ui.pushButton_browse.clicked.connect(self.browsefiles)
        self.ui.checkBox_useROI.clicked.connect(self.setROIalarm)

        #storage load and deleting calibration file
        self.ui.pushButton_savewlaxis.clicked.connect(self.saveconf)
        self.ui.pushButton_loadwlaxis.clicked.connect(self.parentwin.getoldcalibration)
        self.ui.pushButton_clearcal.clicked.connect(self.resetcal)


        # ROI buttons
        self.ui.pushButton_yminmin.clicked.connect(lambda: self.ROIylims(0))
        self.ui.pushButton_ymaxmin.clicked.connect(lambda: self.ROIylims(1))
        self.ui.pushButton_yminplu.clicked.connect(lambda: self.ROIylims(2))
        self.ui.pushButton_ymaxplu.clicked.connect(lambda: self.ROIylims(3))

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

    ##################################### functions ####################################################
    def helplink(self):
        browseropen(self.parentwin.helpweblink)

    def closesettings(self):
        self.parentwin.ui.pushButton_settings.setText("settings")
        self.hide()

    def livecamview(self):
        if self.parentwin.runcam == True:
            if self.ui.pushButton_liveview.text() == "live view":
                self.ui.pushButton_liveview.setText("stop")
                self.parentwin.showlivecam = True                          # we set the Flag and allow livecam view ... for the while loop in setupHW
                self.liveviewworker = LivecamWorker(self.parentwin)               # and start the worker
                self.parentwin.threadpool.start(self.liveviewworker)
            else:
                self.ui.pushButton_liveview.setText("live view")
                self.parentwin.showlivecam = False
        else:
            self.parentwin.statusmessage("no camera connected")

    def ROIylims(self,id):
        ROIstep = self.parentwin.ROIsteps

        if id == 0:
            self.parentwin.ROIymin -= ROIstep
            self.ui.lineEdit_ymin.setText(str(self.parentwin.ROIymin))
        if id == 1 and self.parentwin.ROIymin < self.parentwin.ROIymax - ROIstep:  # here we also have to check if reducing ymax by 10 will not go below ROIymin
            self.parentwin.ROIymax -= ROIstep
            self.ui.lineEdit_ymax.setText(str(self.parentwin.ROIymax))
        if id == 2 and self.parentwin.ROIymax > self.parentwin.ROIymin + ROIstep:  # same for the lower ylim when increasing
            self.parentwin.ROIymin += ROIstep
            self.ui.lineEdit_ymin.setText(str(self.parentwin.ROIymin))
        if id == 3:
            self.parentwin.ROIymax += ROIstep
            self.ui.lineEdit_ymax.setText(str(self.parentwin.ROIymax))

    def togglecalmode(self):      # that we dont have to move the slider just clicking on it is enough
        if self.ui.horizontalSlider_wlcalmode.value() == 3:
            self.ui.horizontalSlider_wlcalmode.setValue(2)
        else: 
            self.ui.horizontalSlider_wlcalmode.setValue(3)

    def setROIalarm(self):  # this handles the marker on the plot and shows if ROI mode is activated
        if self.parentwin.specmode == True:
            if self.ui.checkBox_useROI.isChecked():
                self.parentwin.specwindow.ui.alarmframe.setVisible(True)
                self.parentwin.specwindow.ui.label_22.setText("ROI activated!")
            else:
                self.parentwin.specwindow.ui.alarmframe.setVisible(False)
                self.parentwin.specwindow.ui.label_22.setText("ROI not activated")


    ## functions for save files tab
    def browsefiles(self):  # open browse window to define saving path
        path = QFileDialog.getExistingDirectory(self, "Open file")
        self.ui.lineEdit_filepath.setText(path)
    
    def saveconf(self):
        A = self.parentwin.wlaxis   #we get the current calibration axis/wavelength axis
        B = 0*A                     # make a zero vector of the same size as A to store additional confdata in it
        if self.ui.checkBox_flipx.isChecked():      # if x-axis is flipped set 0 adress to 1 = true
            B[0] = 1
        if self.ui.checkBox_flipy.isChecked():      # if y-axis is flipped set 1 adress to 1 = true
            B[1] = 1
        B[2] = self.parentwin.ROIymin       # in adress 2 and 3 strore the ROI parameters
        B[3] = self.parentwin.ROIymax
        if self.ui.checkBox_useROI.isChecked():
            B[4] = 1                        # use adress 4 if ROI is activated

        S = np.array([A, B])       # the matrix combining both 
        np.save("specconfig.npy", S) # also save it as numpy file
        self.parentwin.statusmessage("calibration saved")   #send message

    def resetcal(self):
        if fileexists(getfolder()+"\confs\specconfig.npy"):           # check if a configfile exists and then delete it
            removefile(getfolder()+"\confs\specconfig.npy")
        self.parentwin.wlaxis = self.parentwin.pxaxis           # overwrite the wlaxis with the pixelaxis
        if self.parentwin.specmode == True:                     #if we have the spectrumplot running, update its wlaxis
            self.parentwin.specwindow.ui.MplWidget.wlaxis = self.parentwin.pxaxis
        self.parentwin.statusmessage("calibration deleted")     # send message

    ################################### calibration ########################################################

    def getP(self, id):
        if self.parentwin.specmode:
            if id == 1:
                self.ui.lineEdit_px1.setText(str(self.parentwin.specwindow.ui.MplWidget.xid))
            elif id == 2:
                self.ui.lineEdit_px2.setText(str(self.parentwin.specwindow.ui.MplWidget.xid))
            elif id == 3:
                self.ui.lineEdit_px3.setText(str(self.parentwin.specwindow.ui.MplWidget.xid))
    
        else: # if there is no specmode running, we can not get ids from the marker
                self.parentwin.statusmessage("no point in spectrum selected")


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

    def computewlaxis(self):

        if self.ui.horizontalSlider_wlcalmode.value() == 2:     # calibration via 2 points
            # first we get the points and give them short variable names
            id1 = self.ui.lineEdit_px1.text()
            id2 = self.ui.lineEdit_px3.text()
            wl1 = self.ui.lineEdit_wl1.text()
            wl2 = self.ui.lineEdit_wl3.text()
            if id1 == id2:
                self.parentwin.statusmessage("bad calibration points")
            else:
                pixelx = self.parentwin.resolution[0]  # the amount of pixels along the wavelength (x) axis

                m = (float(wl2)-float(wl1)) / (int(id2) - int(id1))
                b = float(wl2) - m*int(id2)
                self.parentwin.wlaxis = np.linspace(0, pixelx-1, pixelx)*m  + b # store the wavelength axis in the main spectrometer object
                
                if self.parentwin.specmode: #if we have the spec liveview open (what can be assumed) we also have to update its wlaxis
                    self.parentwin.specwindow.ui.MplWidget.wlaxis = self.parentwin.wlaxis
        

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
                self.parentwin.statusmessage("bad calibration points")
            else:
                pixelx = self.parentwin.resolution[0]  # the amount of pixels along the wavelength (x) axis
                xax = np.linspace(0, pixelx-1, pixelx) # we create the x axis
        
                a = (x1*(w3-w2)+w1*(x2-x3)-x2*w3+w2*x3)/((x1-x2)*(x1-x3)*(x2-x3))
                b = (x1**2*(w2-w3)+w1*(x3**2-x2**2)+x2**2*w3-w2*x3**2)/((x1-x2)*(x1-x3)*(x2-x3))
                c = (x1*(x1*x2*w3-x1*w2*x3-x2**2*w3+w2*x3**2)+w1*x2*x3*(x2-x3))/((x1-x2)*(x1-x3)*(x2-x3))

                self.parentwin.wlaxis = a*xax**2 + xax*b  + c # store the wavelength axis in the main spectrometer object

                if self.parentwin.specmode: #if we have the spec liveview open (what can be assumed) we also have to update its wlaxis
                    self.parentwin.specwindow.ui.MplWidget.wlaxis = self.parentwin.wlaxis



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


class pseudosensor():
    def __init__(self, iface):
        self.name = "IntF" +str(iface) +".SystemClock"    # give the device a name
        self.value = 1    # sensor values
        self.ready = 1     # 1 is ready, 0 is not (analogin is always ready)
        self.valueunit = ["s"] # names for the values (sensor outputs or status etc.)
        self.scannable = True   # is there a scan function
        self.t0 = 0 # for time sensitive measurements we want some starting time

    def getvalue(self): # this is twat the sensor gives back
        #return time.time() - self.t0
        pass
    
    def scannervalue(self, pos):
        pass

    def update():
        pass

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