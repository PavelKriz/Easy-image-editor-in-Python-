# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3

# for unsharpMasking
import medianFilter
# tkinter for working with files
import tkinter as tk
from tkinter import filedialog
# load image
from PIL import Image
# for image save
import numpy as np
# UI desing
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
	# size is intern number for resizing image, image is resized with keeping same aspect ratio
	# numpy Image representation, and undo backup image
	size = 500
	NPundo = np.empty((2,2))
	NPimg = np.empty((2,2))
	#indicator if image is colorfull
	rgb = True
	
	# UI setup genereted by: PyQt5 UI code generator 5.11.3
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(636, 617)
		MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		MainWindow.setMouseTracking(False)
		MainWindow.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(135, 171, 255);\n"
"background-color: rgb(255, 255, 255);")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setText("")
		self.label.setObjectName("label")
		self.verticalLayout_2.addWidget(self.label)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 21))
		self.menubar.setObjectName("menubar")
		self.menuMenu = QtWidgets.QMenu(self.menubar)
		self.menuMenu.setObjectName("menuMenu")
		self.menuFilters = QtWidgets.QMenu(self.menubar)
		self.menuFilters.setObjectName("menuFilters")
		MainWindow.setMenuBar(self.menubar)
		self.toolBar = QtWidgets.QToolBar(MainWindow)
		self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.toolBar.setObjectName("toolBar")
		MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
		self.actionOpen = QtWidgets.QAction(MainWindow)
		self.actionOpen.setObjectName("actionOpen")
		self.actionUndo = QtWidgets.QAction(MainWindow)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("icons/undo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionUndo.setIcon(icon)
		self.actionUndo.setObjectName("actionUndo")
		self.actionSave = QtWidgets.QAction(MainWindow)
		self.actionSave.setObjectName("actionSave")
		self.actionRotLeft = QtWidgets.QAction(MainWindow)
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("icons/90doleva.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionRotLeft.setIcon(icon1)
		self.actionRotLeft.setObjectName("actionRotLeft")
		self.actionRotRight = QtWidgets.QAction(MainWindow)
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap("icons/90doprava.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionRotRight.setIcon(icon2)
		self.actionRotRight.setObjectName("actionRotRight")
		self.actionFlip = QtWidgets.QAction(MainWindow)
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap("icons/flip.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionFlip.setIcon(icon3)
		self.actionFlip.setObjectName("actionFlip")
		self.actionInvert = QtWidgets.QAction(MainWindow)
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap("icons/invert.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionInvert.setIcon(icon4)
		self.actionInvert.setObjectName("actionInvert")
		self.actionBrightUp = QtWidgets.QAction(MainWindow)
		icon5 = QtGui.QIcon()
		icon5.addPixmap(QtGui.QPixmap("icons/brightUP.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionBrightUp.setIcon(icon5)
		self.actionBrightUp.setObjectName("actionBrightUp")
		self.actionBrightDown = QtWidgets.QAction(MainWindow)
		icon6 = QtGui.QIcon()
		icon6.addPixmap(QtGui.QPixmap("icons/brightDOWN.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionBrightDown.setIcon(icon6)
		self.actionBrightDown.setObjectName("actionBrightDown")
		self.actionEdges = QtWidgets.QAction(MainWindow)
		icon7 = QtGui.QIcon()
		icon7.addPixmap(QtGui.QPixmap("icons/edges.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionEdges.setIcon(icon7)
		self.actionEdges.setObjectName("actionEdges")
		self.actionRGBtoRW = QtWidgets.QAction(MainWindow)
		icon8 = QtGui.QIcon()
		icon8.addPixmap(QtGui.QPixmap("icons/RGBtoBW.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionRGBtoRW.setIcon(icon8)
		self.actionRGBtoRW.setObjectName("actionRGBtoRW")
		self.actionCrazy_Rainbow = QtWidgets.QAction(MainWindow)
		self.actionCrazy_Rainbow.setObjectName("actionCrazy_Rainbow")
		self.actionBigger = QtWidgets.QAction(MainWindow)
		icon9 = QtGui.QIcon()
		icon9.addPixmap(QtGui.QPixmap("icons/bigger.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionBigger.setIcon(icon9)
		self.actionBigger.setObjectName("actionBigger")
		self.actionexitp = QtWidgets.QAction(MainWindow)
		self.actionexitp.setObjectName("actionexitp")
		self.actionSmaller = QtWidgets.QAction(MainWindow)
		icon10 = QtGui.QIcon()
		icon10.addPixmap(QtGui.QPixmap("icons/smaller.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionSmaller.setIcon(icon10)
		self.actionSmaller.setObjectName("actionSmaller")
		self.menuMenu.addAction(self.actionOpen)
		self.menuMenu.addAction(self.actionSave)
		self.menuMenu.addAction(self.actionexitp)
		self.menuFilters.addAction(self.actionCrazy_Rainbow)
		self.menubar.addAction(self.menuMenu.menuAction())
		self.menubar.addAction(self.menuFilters.menuAction())
		self.toolBar.addAction(self.actionUndo)
		self.toolBar.addAction(self.actionRotLeft)
		self.toolBar.addAction(self.actionRotRight)
		self.toolBar.addAction(self.actionFlip)
		self.toolBar.addAction(self.actionInvert)
		self.toolBar.addAction(self.actionBrightUp)
		self.toolBar.addAction(self.actionBrightDown)
		self.toolBar.addAction(self.actionRGBtoRW)
		self.toolBar.addAction(self.actionEdges)
		self.toolBar.addAction(self.actionBigger)
		self.toolBar.addAction(self.actionSmaller)
		
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		
# UI setup genereted by: PyQt5 UI code generator 5.11.3		
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "PK-Easy image editor"))
		self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
		self.menuFilters.setTitle(_translate("MainWindow", "Filters"))
		self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
		self.actionOpen.setText(_translate("MainWindow", "Open"))
		self.actionUndo.setText(_translate("MainWindow", "Undo"))
		self.actionUndo.setToolTip(_translate("MainWindow", "Vrati se o krok zpet"))
		self.actionSave.setText(_translate("MainWindow", "Save"))
		self.actionRotLeft.setText(_translate("MainWindow", "RotLeft"))
		self.actionRotLeft.setToolTip(_translate("MainWindow", "Rotace doleva o 90 stupňů."))
		self.actionRotRight.setText(_translate("MainWindow", "RotRight"))
		self.actionRotRight.setToolTip(_translate("MainWindow", "Rotace doprava o 90 stupňů."))
		self.actionFlip.setText(_translate("MainWindow", "Flip"))
		self.actionFlip.setToolTip(_translate("MainWindow", "Zrcadleni obrazku"))
		self.actionInvert.setText(_translate("MainWindow", "Invert"))
		self.actionInvert.setToolTip(_translate("MainWindow", "Invertuje obrázek."))
		self.actionBrightUp.setText(_translate("MainWindow", "BrightUp"))
		self.actionBrightUp.setToolTip(_translate("MainWindow", "Zvýší jas."))
		self.actionBrightDown.setText(_translate("MainWindow", "BrightDown"))
		self.actionBrightDown.setToolTip(_translate("MainWindow", "Sníží jas obrázku."))
		self.actionEdges.setText(_translate("MainWindow", "Edges"))
		self.actionEdges.setToolTip(_translate("MainWindow", "Zvýrazní hrany."))
		self.actionRGBtoRW.setText(_translate("MainWindow", "RGBtoRW"))
		self.actionRGBtoRW.setToolTip(_translate("MainWindow", "Převede barevný obrázek na černobílý."))
		self.actionCrazy_Rainbow.setText(_translate("MainWindow", "Crazy Rainbow"))
		self.actionBigger.setText(_translate("MainWindow", "Bigger"))
		self.actionBigger.setToolTip(_translate("MainWindow", "Zvětší náhled obrázku"))
		self.actionexitp.setText(_translate("MainWindow", "exit"))
		self.actionexitp.setToolTip(_translate("MainWindow", "Ukončí program."))
		self.actionSmaller.setText(_translate("MainWindow", "Smaller"))
		self.actionSmaller.setToolTip(_translate("MainWindow", "Zmenší náhled obrázku"))
		
# buttons relations

		self.actionOpen.triggered.connect(self.OpenImage)
		self.actionRotLeft.triggered.connect(self.rotLeft)
		self.actionRotRight.triggered.connect(self.rotRight)
		self.actionFlip.triggered.connect(self.flip)
		self.actionInvert.triggered.connect(self.invert)
		self.actionRGBtoRW.triggered.connect(self.RGBtoBW)
		self.actionBrightUp.triggered.connect(self.brighten)
		self.actionBrightDown.triggered.connect(self.darken)
		self.actionEdges.triggered.connect(self.unsharpMask)
		self.actionUndo.triggered.connect(self.undo)
		self.actionexitp.triggered.connect(self.exitp)
		self.actionCrazy_Rainbow.triggered.connect(self.rainBowFilt)
		self.actionSmaller.triggered.connect(self.smaller)
		self.actionBigger.triggered.connect(self.bigger)
		self.actionSave.triggered.connect(self.saveImage)
# not ended implemented bigger undo buffer
	'''
	def Undo(self):
		if self.BundoControl:
			self.NPimg = self.Lundo1[IundoControl - 1]
			self.Lundo1.remove(self.Lundo1[IundoControl])
			IundoControl += 1
			
	def backup(self):
		if self.Iundo = 1:
			self.Lundo.append(self.NPimg)
			IundoControl += 1
			return
			
		if self.BundoControl:
			self.Lundo1.append(self.NPimg)
		else:
			self.Lundo2.append(self.NPimg)
		IundoControl += 1
		
		if self.IundoControl >= 10:
			self.IundoControl = 0
			BundoControl = False
			self.Lundo2 = []
		else:
			self.IundoControl = 0
			BundoControl = True
			self.Lundo1 = []
	'''
# image operations functions or supporting functions
# ends program
	def exitp(self):
		exit()
# backup before previus operation
	def undo(self):
		self.NPimg = self.NPundo
		self.showImage( self.NPimg)
# save for undo before image operation		
	def backup(self):
		self.NPundo = self.NPimg
# enlarge image preview
	def bigger(self):
		self.size = int(self.size * 1.2)
		self.showImage(self.NPimg)
# reduce image preview	
	def smaller(self):
		self.size = int(self.size / 1.2)
		self.showImage(self.NPimg)
# rotate image to left		
	def rotLeft(self):
		self.backup()
		self.NPimg = np.rot90(self.NPimg, axes = (0, 1)).copy()
		self.showImage( self.NPimg)
# rotate image to right		
	def rotRight(self):
		self.backup()
		self.NPimg = np.rot90(self.NPimg, axes = (1, 0)).copy()
		self.showImage( self.NPimg)
# mirrors image
	def flip(self):
		self.backup()
		self.NPimg = np.flip(self.NPimg, 1).copy()
		self.showImage( self.NPimg)
#invert RGB values (modulo 256 values)
	def invert(self):
		self.backup()
		self.NPimg = 255 - self.NPimg
		self.showImage( self.NPimg)
# make image RGB wallues higher by 10 or set them to 255 if they are too big
	def brighten(self):
		self.backup()
		self.NPimg.setflags(write=1)
		self.NPimg[self.NPimg > 245] = 245
		self.NPimg = self.NPimg + 10
		self.showImage( self.NPimg)
# make image RGB wallues lower by 10 or set them to 0 if they are too small
	def darken(self):
		self.backup()
		self.NPimg.setflags(write=1)
		self.NPimg[self.NPimg < 10] = 10
		self.NPimg = self.NPimg - 10
		self.showImage( self.NPimg)
# convert colorfull image into black and white one
	def RGBtoBW (self):
		rgb = False
		self.backup()
		self.NPimg.setflags(write=1)
		self.NPimg[:] = np.max(self.NPimg,axis=-1,keepdims=1)/2+np.min(self.NPimg,axis=-1,keepdims=1)/2
		self.showImage(self.NPimg)
		
# most difficult operations, using medianfilter, its working as expacted in unsharpMasking
	def unsharpMask(self):
		self.backup()
		NPmed = np.asarray(self.NPimg)
		NPmed.setflags(write=1)
		height, width,rgb = self.NPimg.shape
		if self.rgb:
			NPmed = medianFilter.medianRGB(self.NPimg,NPmed,width,height)
		else:
			NPmed = medianFilter.medianBW(self.NPimg,NPmed,width,height)
		#Mask making
		NPimg2 = self.NPimg.astype('int32')
		NPmed2 = NPmed.astype('int32')
		Mask = NPimg2 - NPmed2
		# Some pixals may be negative
		Mask[Mask < 0 ] = 0
		# mask aplication
		NPresult = NPimg2 + Mask
		NPresult[NPresult > 255 ] = 255
	
		self.NPimg = NPresult.astype('uint8')
		self.showImage( self.NPimg)
		
# not working as expacted, it should had making rainbow in shape of stuff in image
	def rainBowFilt(self):
		self.backup()
		height, width,rgb = self.NPimg.shape
		if self.rgb:
			med = medianFilter.medianRGB(self.NPimg,np.asarray(self.NPimg),width,height)
		else:
			med = medianFilter.medianBW(self.NPimg,np.asarray(self.NPimg),width,height)
		origL = lambda x: x*1.5
		gaussL = lambda x: x*(-0.5)
		imOL = np.array([origL(x) for x in self.NPimg ])
		imGL = np.array([gaussL(x) for x in med])
		self.NPimg = imOL + imGL
		self.showImage( self.NPimg)

# open image with tkinter filedialog		
	def OpenImage(self):
		self.backup()
		root = tk.Tk()
		root.withdraw()
		root.filename = filedialog.askopenfilename(initialdir = "/",title = "Vyberte obrazek",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
		if  root.filename:
			img = Image.open(root.filename)
			self.NPimg = np.asarray(img)
			self.showImage( self.NPimg)
#save image with tkinter filedialog, // if no suffix is given, image is saved as png
	def saveImage(self):
		root = tk.Tk()
		root.withdraw()
		root.filename = filedialog.asksaveasfilename(initialdir = "/",title = "Uložte obrázek",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
		if root.filename:
			try:
				saveIMG = Image.fromarray(self.NPimg.astype('uint8'))
				saveIMG.save(root.filename)
			except ValueError:
				saveIMG = Image.fromarray(self.NPimg.astype('uint8'))
				saveIMG.save(root.filename + '.png')

# shows image in Qt label, size is derived from the self.size (it can be changed with bigger and smaller)
	def showImage(self, NPimgShow):
		image_profile = QtGui.QImage(NPimgShow, NPimgShow.shape[1], NPimgShow.shape[0], NPimgShow.shape[1] * 3,QtGui.QImage.Format_RGB888) #QImage object
		image_profile = image_profile.scaled(self.size,self.size, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation) # To scale image for example and keep its Aspect Ration    
		self.label.setPixmap(QtGui.QPixmap.fromImage(image_profile))
		

#Frame inicalization and run
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

