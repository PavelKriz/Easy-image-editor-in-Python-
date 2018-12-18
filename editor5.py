# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

# pro praci se soubory
import medianFilter
import tkinter as tk
from tkinter import filedialog
# nacteni obrazku
from PIL import Image
# prace s obrazky
import numpy as np
# UI
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
	size = 500
	NPundo = np.empty((2,2))
	NPimg = np.empty((2,2))
	rgb = True
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(636, 569)
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
		MainWindow.insertToolBarBreak(self.toolBar)
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
		self.actionrecalc = QtWidgets.QAction(MainWindow)
		icon9 = QtGui.QIcon()
		icon9.addPixmap(QtGui.QPixmap("icons/recalc.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionrecalc.setIcon(icon9)
		self.actionrecalc.setObjectName("actionrecalc")
		self.actionexitp = QtWidgets.QAction(MainWindow)
		self.actionexitp.setObjectName("actionexitp")
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
		self.toolBar.addAction(self.actionrecalc)
		
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		
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
		self.actionCrazy_Rainbow.setToolTip(_translate("MainWindow", "Vytvoří na obrázku bláznivé barvy"))
		self.actionrecalc.setText(_translate("MainWindow", "Recalc"))
		self.actionrecalc.setToolTip(_translate("MainWindow", "Přepočítá velikost obrázku podle velikosti okna"))
		self.actionexitp.setText(_translate("MainWindow", "exitp"))
		self.actionexitp.setToolTip(_translate("MainWindow", "Ukončí program."))

				#vazby
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
		self.actionrecalc.triggered.connect(self.recalc)
		
	def exitp(self):
		exit()
	
	def undo(self):
		self.NPimg = self.NPundo
		self.showImage( self.NPimg)
	def backup(self):
		self.NPundo = self.NPimg
		
	def recalc(self):
		self.size = self.size * 1.2
		self.showImage(self.NPimg)
		
		
	# rozpracovane Undo s vetsim bufferem nez jedna	
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
	def rotLeft(self):
		self.backup()
		self.NPimg = np.rot90(self.NPimg, axes = (0, 1)).copy()
		self.showImage( self.NPimg)
		
	def rotRight(self):
		self.backup()
		self.NPimg = np.rot90(self.NPimg, axes = (1, 0)).copy()
		self.showImage( self.NPimg)
	
	def flip(self):
		self.backup()
		self.NPimg = np.flip(self.NPimg, 1).copy()
		self.showImage( self.NPimg)
		
	def invert(self):
		self.backup()
		self.NPimg = 255 - self.NPimg
		self.showImage( self.NPimg)
		
	def brighten(self):
		self.backup()
		self.NPimg.setflags(write=1)
		self.NPimg[self.NPimg > 245] = 245
		self.NPimg = self.NPimg + 10
		self.showImage( self.NPimg)

	def darken(self):
		self.backup()
		self.NPimg.setflags(write=1)
		self.NPimg[self.NPimg < 10] = 10
		self.NPimg = self.NPimg - 10
		self.showImage( self.NPimg)
	
	def RGBtoBW (self):
		rgb = False
		self.backup()
		self.NPimg.setflags(write=1)
		self.NPimg[:] = np.max(self.NPimg,axis=-1,keepdims=1)/2+np.min(self.NPimg,axis=-1,keepdims=1)/2
		self.showImage(self.NPimg)
	
	def unsharpMask(self):
		self.backup()
		NPmed = np.asarray(self.NPimg)
		NPmed.setflags(write=1)
		height, width,rgb = self.NPimg.shape
		if self.rgb:
			NPmed = medianFilter.medianRGB(self.NPimg,NPmed,width,height)
		else:
			NPmed = medianFilter.medianBW(self.NPimg,NPmed,width,height)
		#vyroba masky	
		NPimg2 = self.NPimg.astype('int32')
		NPmed2 = NPmed.astype('int32')
		Mask = NPimg2 - NPmed2
		#nektere body se mohou dostat i pod nulu!
		Mask[Mask < 0 ] = 0
		# aplikace masky
		NPresult = NPimg2 + Mask
		NPresult[NPresult > 255 ] = 255
	
		self.NPimg = NPresult.astype('uint8')
		self.showImage( self.NPimg)
	#	test = Image.fromarray(NPresult.astype('uint8'))
	#	medianIMG.save('obrazek2.jpg')
		
		
		
	def rainBowFilt(self):
		self.backup()
		height, width,rgb = self.NPimg.shape
		if self.rgb:
			med = medianFilter.medianRGB(self.NPimg,np.asarray(self.NPimg),width,height)
		else:
			med = medianFilter.medianBW(self.NPimg,np.asarray(self.NPimg),width,height)
		#self.NPimg = cv2.addWeighted(self.NPimg, 1.5, gaussian_3, -0.5, 0, self.NPimg)
		origL = lambda x: x*1.5
		gaussL = lambda x: x*(-0.5)
		imOL = np.array([origL(x) for x in self.NPimg ])
		imGL = np.array([gaussL(x) for x in med])
		self.NPimg = imOL + imGL# + gamma
		self.showImage( self.NPimg)
		
	def OpenImage(self):
		self.backup()
		root = tk.Tk()
		root.withdraw()
		root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
		if  root.filename:
			img = Image.open(root.filename)
			self.NPimg = np.asarray(img)
			self.showImage( self.NPimg)
		
	def showImage(self, NPimgShow):
		image_profile = QtGui.QImage(NPimgShow, NPimgShow.shape[1], NPimgShow.shape[0], NPimgShow.shape[1] * 3,QtGui.QImage.Format_RGB888) #QImage object
		image_profile = image_profile.scaled(self.size,self.size, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation) # To scale image for example and keep its Aspect Ration    
		self.label.setPixmap(QtGui.QPixmap.fromImage(image_profile))
		
		
		
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

