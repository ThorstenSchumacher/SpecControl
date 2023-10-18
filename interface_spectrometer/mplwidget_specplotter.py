from PySide6.QtWidgets import*
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from threading import Thread
import numpy as np
   
class MplWidget(QWidget):
    
    def __init__(self, parent):

        QWidget.__init__(self, parent)
        # this is just to start with empty data
        self.xres = 1920
        self.setaxisresolution()
 
        # maker
        self.xid = 550           # xcoordinate in px axis
        self.xidP = 550          # xcoordinate this is what will be printed
        self.yid = 0.5            # ycoordinate in px axis
        self.xmarkwl = 0        # xcoordinate in wl axis so actually the wavelength
        self.ymark = 0        # ycoordinate of cursor

        # preparing the figure
        plt.ion()
        plt.style.use('dark_background')
        plt.rcParams.update({"figure.facecolor":  (32/255, 31/255, 34/255), "axes.facecolor":    (32/255, 31/255, 34/255)})
  

        #### prepare plot
        self.canvas = FigureCanvas(Figure())
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.canvas.axes = self.canvas.figure.add_subplot(111)  
        self.line1, = self.canvas.axes.plot(self.xax, self.yax, color =(100/255, 150/255, 200/255), animated=False)
        self.line2, = self.canvas.axes.plot([self.xid, self.xid], [0, 3e3], color =(200/255, 200/255, 200/255))
        self.line3, = self.canvas.axes.plot([0, 4e3], [self.yid, self.yid], color =(200/255, 200/255, 200/255))
        self.setLayout(vertical_layout)
        self.canvas.axes.set_xlabel("wavelength (nm)" ,fontsize=14)
        self.canvas.axes.set_ylabel("intensity (arb.u.)"  ,fontsize=14)
        self.canvas.axes.grid(linestyle="--", color='gray')
        self.canvas.toolbar_visible = True
        self.canvas.axes.set_ylim(0, 100)
        # zoombox
        self.rectangle = patches.Rectangle((self.wlaxis[self.zoomboxX[0]], self.zoomboxY[0]), 100, self.wlaxis[self.zoomboxX[1]] - self.wlaxis[self.zoomboxX[0]], linewidth=1, edgecolor='r', facecolor= (200/255, 0, 0, 0.3))
        self.rectangle.set_visible(False)
        self.canvas.axes.add_patch(self.rectangle)
        self.zoommode = False

        # ... start animation function to update graph!
        self.showlivedata() # with this we start the animation and the Ui .. that means the Ui itself takes of the animation 


        #Flags
        self.wlmode = True    # = True ... we use the wavelength axis, = False ... we use the pixel axis
        self.specmode = 0     # 0 = Intensity Plot, 1 = Trasmission, 2 = Absorption
        self.zoommode = False # we are in the zoom mode
        self.zoomed = False   # if we are zoomed we dont want autoscale yaxis


########################################## figure and axis update functions #########################################

    def setaxisresolution(self):
        self.xax = np.linspace(0, self.xres-1, self.xres)    # this is and will ever be the pixel axis of our sensor
        self.yax = np.zeros((self.xres, 1))            # this is our intensity spectrum from the sensor
        self.wlaxis = self.xax                   # we start with a pixel wavelength axis
        self.xaxP = self.xax                     # this is the function that will be printed (for first run .. will continously be overwritten)
        self.yaxP = self.yax                     # this is the function that will be printed (for first run .. will continously be overwritten)

        self.ylamp = np.ones((1,self.xres))           # we start with a flat equal 1 lamp spectrum
        self.yback = np.zeros((1,self.xres))          # we start with a flat equal 0 background spectrum

        # plot x range (ids)
        self.plotxrange = [0, self.xres-1]  # min value and max value
        self.plotyrange = [0, 1]

        # zoombox ranges
        self.zoomboxX = [0, self.xres-1]
        self.zoomboxY = [0, 1]



    def saveimg(self, filepathname):
        self.canvas.figure.savefig(filepathname, bbox_inches='tight')

    def updatexax(self):
        if self.wlmode == True:     # we are in wavelength mode
            self.canvas.axes.set_xlabel("wavelength (nm)" ,fontsize=14)
        else:                       # we are in pixel mode
            self.canvas.axes.set_xlabel("pixel" ,fontsize=14)

    def updateyax(self):
        if self.specmode == 0:      # we are in intensity mode
            self.canvas.axes.set_ylabel("intensity (arb. u.)" ,fontsize=14)
        elif self.specmode == 1:    # we are in transmission mode
            self.canvas.axes.set_ylabel("transmission (%)" ,fontsize=14)
        elif self.specmode == 2:    # we are in extinction mode
            self.canvas.axes.set_ylabel("extinction ()" ,fontsize=14)

########################################### spectrum update functions #################################################
    
    def getlamp(self):          #overwrite the lamp spectrum
        self.ylamp = self.yax

    def getback(self):          #overwrite the background spectrum
        self.yback = [self.yax]
        

    def data_update(self, i):
        ## now get the frame and prepare data
        # wavelength axis modes (pixel vs wavelength)
        if self.wlmode == True :            # wavelength
            self.xaxP = self.wlaxis
            self.xidP = self.wlaxis[self.xid]
        else:                               # pixel
            self.xaxP = self.xax
            self.xidP = self.xid

        # y-axis mode Intensity, Transmission, Absorption
        if self.specmode == 0:    # Intensity mode .... y axis is simply the current livespec
            self.yaxP = self.yax
        elif self.specmode == 1:    # Transmission mode .... y axis is the background corrected intensity / lamp intensity 
            lampcorr = (self.ylamp - self.yback)
            lampcorr[lampcorr <= 0] = 1e8
            self.yaxP = 100*(self.yax - self.yback)/lampcorr
            self.yaxP = self.yaxP[0]
            
        elif self.specmode == 2:     # Extinxtion mode is -log(T) ... see above
            lampcorr = (self.ylamp - self.yback)
            T = (self.yax - self.yback)/lampcorr # as above
            T[T==0]=1/(2**8)  # replace all zeros by a really small number that is the limit of our bit depth
            T[np.isinf(T)] = 3000
            T[np.isnan(T)] = 3000
            self.yaxP = -np.log10(T)
            self.yaxP = self.yaxP[0]


        #plot spectrum
        self.line1.set_xdata(self.xaxP[self.plotxrange[0] : self.plotxrange[1]])
        self.line1.set_ydata(self.yaxP[self.plotxrange[0] : self.plotxrange[1]])
        #plot marker
        self.line3.set_ydata([self.yid, self.yid])
        self.line2.set_xdata([self.xidP, self.xidP])
        #show saturation alarm

        # show zoombox
        if self.zoommode == True:
            self.rectangle.remove()
            if self.wlmode == True:
                self.rectangle = patches.Rectangle((self.wlaxis[self.zoomboxX[0]], self.zoomboxY[0]), self.wlaxis[self.zoomboxX[1]] - self.wlaxis[self.zoomboxX[0]] , self.zoomboxY[1] - self.zoomboxY[0], linewidth=1, edgecolor='r', facecolor= (200/255, 0, 0, 0.3))
            else:
                self.rectangle = patches.Rectangle((self.xax[self.zoomboxX[0]], self.zoomboxY[0]), self.xax[self.zoomboxX[1]] - self.xax[self.zoomboxX[0]] , self.zoomboxY[1] - self.zoomboxY[0], linewidth=1, edgecolor='r', facecolor= (200/255, 0, 0, 0.3))
            self.canvas.axes.add_patch(self.rectangle)


        # set limits
        self.canvas.axes.set_xlim(np.min(self.xaxP[self.plotxrange[0] : self.plotxrange[1]]), np.max(self.xaxP[self.plotxrange[0] : self.plotxrange[1]])) # xaxis is simple
        
        # yaxis we have to autoscale of use values of zoombox if we are in zoomed mode
        if self.zoomed == False:        # autpscale
            if np.max(self.yaxP) == 0:
                myylim = 1
            else:
                myylim = 1.08*np.max(self.yaxP[self.plotxrange[0] : self.plotxrange[1]])
                if np.isnan(myylim):
                    myylim = -np.log10(1/(2**8))
                self.canvas.axes.set_ylim(0, myylim)
        elif self.zoomed == True:    # zoombox
            self.canvas.axes.set_ylim(np.min(self.zoomboxY), np.max(self.zoomboxY)) # from min to max

        return self

    def ani_init(self):
        self.line1.set_data(self.xaxP[self.plotxrange[0] : self.plotxrange[1]], self.yaxP[self.plotxrange[0] : self.plotxrange[1]])
        return self

    def showlivedata(self):
        self.anim = animation.FuncAnimation(self.canvas.figure, self.data_update, init_func=self.ani_init, interval=200, blit=False, repeat=False)
        self.canvas.draw_idle()  # Zeichenfläche neu zeichnen, um Blitting zu aktivieren

    def updateframedata(self, data):
        self.yax = data

    def resetlampandback(self):
        self.ylamp = np.ones((1,self.xres))           # we start with a flat equal 1 lamp spectrum
        self.yback = np.zeros((1,self.xres))          # we start with a flat equal 0 background spectrum
    

    
