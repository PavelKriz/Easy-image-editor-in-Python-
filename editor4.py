# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

# docasne pro vyvoj usnharp mask
import cv2


# pro praci se soubory
import tkinter as tk
from tkinter import filedialog
# nacteni obrazku
from PIL import Image
# prace s obrazky
import numpy as np
# UI
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(550, 453)
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
		self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 21))
		self.menubar.setObjectName("menubar")
		self.menuMenu = QtWidgets.QMenu(self.menubar)
		self.menuMenu.setObjectName("menuMenu")
		MainWindow.setMenuBar(self.menubar)
		self.toolBar = QtWidgets.QToolBar(MainWindow)
		self.toolBar.setObjectName("toolBar")
		MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
		self.statusBar = QtWidgets.QStatusBar(MainWindow)
		self.statusBar.setObjectName("statusBar")
		MainWindow.setStatusBar(self.statusBar)
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
		self.menuMenu.addAction(self.actionOpen)
		self.menuMenu.addAction(self.actionSave)
		self.menubar.addAction(self.menuMenu.menuAction())
		self.toolBar.addAction(self.actionUndo)
		self.toolBar.addAction(self.actionRotLeft)
		self.toolBar.addAction(self.actionRotRight)
		self.toolBar.addAction(self.actionFlip)
		self.toolBar.addAction(self.actionInvert)
		self.toolBar.addAction(self.actionBrightUp)
		self.toolBar.addAction(self.actionBrightDown)
		self.toolBar.addAction(self.actionRGBtoRW)
		self.toolBar.addAction(self.actionEdges)
		
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
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
	
	def rotLeft(self):
		self.NPimg = np.rot90(self.NPimg, axes = (0, 1)).copy()
		self.showImage( self.NPimg)
		
	def rotRight(self):
		self.NPimg = np.rot90(self.NPimg, axes = (1, 0)).copy()
		self.showImage( self.NPimg)
	
	def flip(self):
		self.NPimg = np.flip(self.NPimg, 1).copy()
		self.showImage( self.NPimg)
		
	def invert(self):
		self.NPimg = 255 - self.NPimg
		self.showImage( self.NPimg)
		
	def brighten(self):
		self.NPimg.setflags(write=1)
		self.NPimg[self.NPimg > 245] = 245
		self.NPimg = self.NPimg + 10
		self.showImage( self.NPimg)

	def darken(self):
		self.NPimg.setflags(write=1)
		self.NPimg[self.NPimg < 10] = 10
		self.NPimg = self.NPimg - 10
		self.showImage( self.NPimg)
	
	def RGBtoBW (self):
		self.NPimg.setflags(write=1)
		self.NPimg[:] = np.max(self.NPimg,axis=-1,keepdims=1)/2+np.min(self.NPimg,axis=-1,keepdims=1)/2
		self.showImage( self.NPimg)
	
	def unsharpMask(self):
		# vyroba pouze hran
		
		for x in range(1, self.NPimg.shape()[0]):  # ignore the edge pixels for simplicity (1 to width-1)
			for y in range(1, height-1): # ignore edge pixels for simplicity (1 to height-1)

				# initialise Gx to 0 and Gy to 0 for every pixel
				Gx = 0
				Gy = 0
		
				# top left pixel
				p = img.getpixel((x-1, y-1))
				r = p[0]
				g = p[1]
				b = p[2]
		
				# intensity ranges from 0 to 765 (255 * 3)
				intensity = r + g + b
		
				# accumulate the value into Gx, and Gy
				Gx += -intensity
				Gy += -intensity
		
				# remaining left column
				p = img.getpixel((x-1, y))
				r = p[0]
				g = p[1]
				b = p[2]
		
				Gx += -2 * (r + g + b)
		
				p = img.getpixel((x-1, y+1))
				r = p[0]
				g = p[1]
				b = p[2]
		
				Gx += -(r + g + b)
				Gy += (r + g + b)
		
				# middle pixels
				p = img.getpixel((x, y-1))
				r = p[0]
				g = p[1]
				b = p[2]
		
				Gy += -2 * (r + g + b)
		
				p = img.getpixel((x, y+1))
				r = p[0]
				g = p[1]
				b = p[2]
		
				Gy += 2 * (r + g + b)
		
				# right column
				p = img.getpixel((x+1, y-1))
				r = p[0]
				g = p[1]
				b = p[2]
		
				Gx += (r + g + b)
				Gy += -(r + g + b)
		
				p = img.getpixel((x+1, y))
				r = p[0]
				g = p[1]
				b = p[2]
		
				Gx += 2 * (r + g + b)
		
				p = img.getpixel((x+1, y+1))
				r = p[0]
				g = p[1]
				b = p[2]
		
				Gx += (r + g + b)
				Gy += (r + g + b)
		
				# calculate the length of the gradient (Pythagorean theorem)
				length = math.sqrt((Gx * Gx) + (Gy * Gy))
		
				# normalise the length of gradient to the range 0 to 255
				length = length / 4328 * 255
		
				length = int(length)
		
				# draw the length in the edge image
				#newpixel = img.putpixel((length,length,length))
				newimg.putpixel((x,y),(length,length,length))
		gaussian_3 = cv2.GaussianBlur(self.NPimg, (9,9), 10.0)
		#self.NPimg = cv2.addWeighted(self.NPimg, 1.5, gaussian_3, -0.5, 0, self.NPimg)
		origL = lambda x: x*1.5
		gaussL = lambda x: x*(-0.5)
		imOL = np.array([origL(x) for x in self.NPimg ])
		imGL = np.array([gaussL(x) for x in gaussian_3])
		self.NPimg = self.NPimg + gaussian_3# + gamma
		self.showImage( self.NPimg)
		
	def rainBowFilt(self):
		gaussian_3 = cv2.GaussianBlur(self.NPimg, (9,9), 10.0)
		#self.NPimg = cv2.addWeighted(self.NPimg, 1.5, gaussian_3, -0.5, 0, self.NPimg)
		origL = lambda x: x*1.5
		gaussL = lambda x: x*(-0.5)
		imOL = np.array([origL(x) for x in self.NPimg ])
		imGL = np.array([gaussL(x) for x in gaussian_3])
		self.NPimg = imOL + imGL# + gamma
		self.showImage( self.NPimg)
		
	def OpenImage(self):
		root = tk.Tk()
		root.withdraw()
		root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
		img = Image.open(root.filename)
		self.NPimg = np.asarray(img)
		self.showImage( self.NPimg)
		
	def showImage(self, NPimgShow):
		image_profile = QtGui.QImage(NPimgShow, NPimgShow.shape[1], NPimgShow.shape[0], NPimgShow.shape[1] * 3,QtGui.QImage.Format_RGB888) #QImage object
		image_profile = image_profile.scaled(500,500, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation) # To scale image for example and keep its Aspect Ration    
		self.label.setPixmap(QtGui.QPixmap.fromImage(image_profile))

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

