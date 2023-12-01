import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QFileDialog, QPushButton
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1113, 834)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1111, 781))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setObjectName("tabWidget")
        self.smoothingWindowTab = QtWidgets.QWidget()
        self.smoothingWindowTab.setObjectName("smoothingWindowTab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.smoothingWindowTab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1101, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.smoothingWindowLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.smoothingWindowLayout.setContentsMargins(0, 0, 0, 0)
        self.smoothingWindowLayout.setObjectName("smoothingWindowLayout")
        self.smothingComboBox = QtWidgets.QComboBox(self.smoothingWindowTab)
        self.smothingComboBox.setGeometry(QtCore.QRect(300, 520, 541, 31))
        self.smothingComboBox.setObjectName("smothingComboBox")
        self.smothingComboBox.addItem("")
        self.smothingComboBox.addItem("")
        self.smothingComboBox.addItem("")
        self.smothingComboBox.addItem("")
        self.label = QtWidgets.QLabel(self.smoothingWindowTab)
        self.label.setGeometry(QtCore.QRect(120, 520, 131, 31))
        self.label.setObjectName("label")
        self.smoothingAmplitudeSlider = QtWidgets.QSlider(self.smoothingWindowTab)
        self.smoothingAmplitudeSlider.setGeometry(QtCore.QRect(150, 610, 771, 22))
        self.smoothingAmplitudeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.smoothingAmplitudeSlider.setObjectName("smoothingAmplitudeSlider")
        self.smoothingFrequencySlider = QtWidgets.QSlider(self.smoothingWindowTab)
        self.smoothingFrequencySlider.setGeometry(QtCore.QRect(150, 690, 771, 22))
        self.smoothingFrequencySlider.setOrientation(QtCore.Qt.Horizontal)
        self.smoothingFrequencySlider.setObjectName("smoothingFrequencySlider")
        self.label_2 = QtWidgets.QLabel(self.smoothingWindowTab)
        self.label_2.setGeometry(QtCore.QRect(30, 610, 121, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.smoothingWindowTab)
        self.label_3.setGeometry(QtCore.QRect(30, 690, 121, 21))
        self.label_3.setObjectName("label_3")
        self.amplitudeDisp = QtWidgets.QLCDNumber(self.smoothingWindowTab)
        self.amplitudeDisp.setGeometry(QtCore.QRect(970, 602, 91, 31))
        self.amplitudeDisp.setObjectName("amplitudeDisp")
        self.frequencyDisp = QtWidgets.QLCDNumber(self.smoothingWindowTab)
        self.frequencyDisp.setGeometry(QtCore.QRect(970, 672, 91, 31))
        self.frequencyDisp.setObjectName("frequencyDisp")
        self.label_4 = QtWidgets.QLabel(self.smoothingWindowTab)
        self.label_4.setGeometry(QtCore.QRect(1070, 680, 31, 16))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.smoothingWindowTab, "")
        self.unifromRangeTab = QtWidgets.QWidget()
        self.unifromRangeTab.setObjectName("unifromRangeTab")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.unifromRangeTab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1111, 481))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.uniformRangeLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.uniformRangeLayout.setContentsMargins(0, 0, 0, 0)
        self.uniformRangeLayout.setObjectName("uniformRangeLayout")
        self.zoomInButton_1 = QtWidgets.QPushButton(self.unifromRangeTab)
        self.zoomInButton_1.setGeometry(QtCore.QRect(20, 500, 71, 28))
        self.zoomInButton_1.setObjectName("zoomInButton_1")
        self.zoomOutButton_1 = QtWidgets.QPushButton(self.unifromRangeTab)
        self.zoomOutButton_1.setGeometry(QtCore.QRect(100, 500, 71, 28))
        self.zoomOutButton_1.setObjectName("zoomOutButton_1")
        self.pausePlayButton_1 = QtWidgets.QPushButton(self.unifromRangeTab)
        self.pausePlayButton_1.setGeometry(QtCore.QRect(370, 500, 271, 28))
        self.pausePlayButton_1.setObjectName("pausePlayButton_1")
        self.rewindButton_1 = QtWidgets.QPushButton(self.unifromRangeTab)
        self.rewindButton_1.setGeometry(QtCore.QRect(660, 500, 71, 28))
        self.rewindButton_1.setObjectName("rewindButton_1")
        self.speedSlider_1 = QtWidgets.QSlider(self.unifromRangeTab)
        self.speedSlider_1.setGeometry(QtCore.QRect(839, 500, 251, 22))
        self.speedSlider_1.setOrientation(QtCore.Qt.Horizontal)
        self.speedSlider_1.setObjectName("speedSlider_1")
        self.label_5 = QtWidgets.QLabel(self.unifromRangeTab)
        self.label_5.setGeometry(QtCore.QRect(790, 500, 41, 16))
        self.label_5.setObjectName("label_5")
        self.checkBox_1 = QtWidgets.QCheckBox(self.unifromRangeTab)
        self.checkBox_1.setGeometry(QtCore.QRect(970, 730, 131, 20))
        self.checkBox_1.setObjectName("checkBox_1")
        self.widget = QtWidgets.QWidget(self.unifromRangeTab)
        self.widget.setGeometry(QtCore.QRect(10, 550, 1081, 151))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uniforRangeSlider_1 = QtWidgets.QSlider(self.widget)
        self.uniforRangeSlider_1.setOrientation(QtCore.Qt.Vertical)
        self.uniforRangeSlider_1.setObjectName("uniforRangeSlider_1")
        self.horizontalLayout.addWidget(self.uniforRangeSlider_1)
        self.uniforRangeSlider_2 = QtWidgets.QSlider(self.widget)
        self.uniforRangeSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.uniforRangeSlider_2.setObjectName("uniforRangeSlider_2")
        self.horizontalLayout.addWidget(self.uniforRangeSlider_2)
        self.uniforRangeSlider_3 = QtWidgets.QSlider(self.widget)
        self.uniforRangeSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.uniforRangeSlider_3.setObjectName("uniforRangeSlider_3")
        self.horizontalLayout.addWidget(self.uniforRangeSlider_3)
        self.uniforRangeSlider_4 = QtWidgets.QSlider(self.widget)
        self.uniforRangeSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.uniforRangeSlider_4.setObjectName("uniforRangeSlider_4")
        self.horizontalLayout.addWidget(self.uniforRangeSlider_4)
        self.uniforRangeSlider_5 = QtWidgets.QSlider(self.widget)
        self.uniforRangeSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.uniforRangeSlider_5.setObjectName("uniforRangeSlider_5")
        self.horizontalLayout.addWidget(self.uniforRangeSlider_5)
        self.uniforRangeSlider_6 = QtWidgets.QSlider(self.widget)
        self.uniforRangeSlider_6.setOrientation(QtCore.Qt.Vertical)
        self.uniforRangeSlider_6.setObjectName("uniforRangeSlider_6")
        self.horizontalLayout.addWidget(self.uniforRangeSlider_6)
        self.uniforRangeSlider_7 = QtWidgets.QSlider(self.widget)
        self.uniforRangeSlider_7.setOrientation(QtCore.Qt.Vertical)
        self.uniforRangeSlider_7.setObjectName("uniforRangeSlider_7")
        self.horizontalLayout.addWidget(self.uniforRangeSlider_7)
        self.uniforRangeSlider_8 = QtWidgets.QSlider(self.widget)
        self.uniforRangeSlider_8.setOrientation(QtCore.Qt.Vertical)
        self.uniforRangeSlider_8.setObjectName("uniforRangeSlider_8")
        self.horizontalLayout.addWidget(self.uniforRangeSlider_8)
        self.uniforRangeSlider_9 = QtWidgets.QSlider(self.widget)
        self.uniforRangeSlider_9.setOrientation(QtCore.Qt.Vertical)
        self.uniforRangeSlider_9.setObjectName("uniforRangeSlider_9")
        self.horizontalLayout.addWidget(self.uniforRangeSlider_9)
        self.uniforRangeSlider_10 = QtWidgets.QSlider(self.widget)
        self.uniforRangeSlider_10.setOrientation(QtCore.Qt.Vertical)
        self.uniforRangeSlider_10.setObjectName("uniforRangeSlider_10")
        self.horizontalLayout.addWidget(self.uniforRangeSlider_10)
        self.tabWidget.addTab(self.unifromRangeTab, "")
        self.animalTab = QtWidgets.QWidget()
        self.animalTab.setObjectName("animalTab")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.animalTab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 1111, 481))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.animalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.animalLayout.setContentsMargins(0, 0, 0, 0)
        self.animalLayout.setObjectName("animalLayout")
        self.zoomInButton_2 = QtWidgets.QPushButton(self.animalTab)
        self.zoomInButton_2.setGeometry(QtCore.QRect(20, 500, 71, 28))
        self.zoomInButton_2.setObjectName("zoomInButton_2")
        self.speedSlider_2 = QtWidgets.QSlider(self.animalTab)
        self.speedSlider_2.setGeometry(QtCore.QRect(839, 500, 251, 22))
        self.speedSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.speedSlider_2.setObjectName("speedSlider_2")
        self.rewindButton_2 = QtWidgets.QPushButton(self.animalTab)
        self.rewindButton_2.setGeometry(QtCore.QRect(660, 500, 71, 28))
        self.rewindButton_2.setObjectName("rewindButton_2")
        self.pausePlayButton_2 = QtWidgets.QPushButton(self.animalTab)
        self.pausePlayButton_2.setGeometry(QtCore.QRect(370, 500, 271, 28))
        self.pausePlayButton_2.setObjectName("pausePlayButton_2")
        self.zoomOutButton_2 = QtWidgets.QPushButton(self.animalTab)
        self.zoomOutButton_2.setGeometry(QtCore.QRect(100, 500, 71, 28))
        self.zoomOutButton_2.setObjectName("zoomOutButton_2")
        self.label_6 = QtWidgets.QLabel(self.animalTab)
        self.label_6.setGeometry(QtCore.QRect(790, 500, 41, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.animalTab)
        self.label_7.setGeometry(QtCore.QRect(190, 720, 55, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.animalTab)
        self.label_8.setGeometry(QtCore.QRect(410, 720, 55, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.animalTab)
        self.label_9.setGeometry(QtCore.QRect(640, 720, 55, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.animalTab)
        self.label_10.setGeometry(QtCore.QRect(870, 720, 55, 16))
        self.label_10.setObjectName("label_10")
        self.checkBox_2 = QtWidgets.QCheckBox(self.animalTab)
        self.checkBox_2.setGeometry(QtCore.QRect(970, 730, 131, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.widget1 = QtWidgets.QWidget(self.animalTab)
        self.widget1.setGeometry(QtCore.QRect(10, 540, 1091, 171))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.animalSlider_1 = QtWidgets.QSlider(self.widget1)
        self.animalSlider_1.setOrientation(QtCore.Qt.Vertical)
        self.animalSlider_1.setObjectName("animalSlider_1")
        self.horizontalLayout_2.addWidget(self.animalSlider_1)
        self.animalSlider_2 = QtWidgets.QSlider(self.widget1)
        self.animalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.animalSlider_2.setObjectName("animalSlider_2")
        self.horizontalLayout_2.addWidget(self.animalSlider_2)
        self.animalSlider_3 = QtWidgets.QSlider(self.widget1)
        self.animalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.animalSlider_3.setObjectName("animalSlider_3")
        self.horizontalLayout_2.addWidget(self.animalSlider_3)
        self.animalSlider_4 = QtWidgets.QSlider(self.widget1)
        self.animalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.animalSlider_4.setObjectName("animalSlider_4")
        self.horizontalLayout_2.addWidget(self.animalSlider_4)
        self.tabWidget.addTab(self.animalTab, "")
        self.musicTab = QtWidgets.QWidget()
        self.musicTab.setObjectName("musicTab")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.musicTab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 1111, 481))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.musicLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.musicLayout.setContentsMargins(0, 0, 0, 0)
        self.musicLayout.setObjectName("musicLayout")
        self.label_11 = QtWidgets.QLabel(self.musicTab)
        self.label_11.setGeometry(QtCore.QRect(640, 720, 55, 16))
        self.label_11.setObjectName("label_11")
        self.pausePlayButton_3 = QtWidgets.QPushButton(self.musicTab)
        self.pausePlayButton_3.setGeometry(QtCore.QRect(370, 500, 271, 28))
        self.pausePlayButton_3.setObjectName("pausePlayButton_3")
        self.rewindButton_3 = QtWidgets.QPushButton(self.musicTab)
        self.rewindButton_3.setGeometry(QtCore.QRect(660, 500, 71, 28))
        self.rewindButton_3.setObjectName("rewindButton_3")
        self.zoomInButton_3 = QtWidgets.QPushButton(self.musicTab)
        self.zoomInButton_3.setGeometry(QtCore.QRect(20, 500, 71, 28))
        self.zoomInButton_3.setObjectName("zoomInButton_3")
        self.layoutWidget = QtWidgets.QWidget(self.musicTab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 540, 1091, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.musicSlider_1 = QtWidgets.QSlider(self.layoutWidget)
        self.musicSlider_1.setOrientation(QtCore.Qt.Vertical)
        self.musicSlider_1.setObjectName("musicSlider_1")
        self.horizontalLayout_5.addWidget(self.musicSlider_1)
        self.musicSlider_2 = QtWidgets.QSlider(self.layoutWidget)
        self.musicSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.musicSlider_2.setObjectName("musicSlider_2")
        self.horizontalLayout_5.addWidget(self.musicSlider_2)
        self.musicSlider_3 = QtWidgets.QSlider(self.layoutWidget)
        self.musicSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.musicSlider_3.setObjectName("musicSlider_3")
        self.horizontalLayout_5.addWidget(self.musicSlider_3)
        self.musicSlider_4 = QtWidgets.QSlider(self.layoutWidget)
        self.musicSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.musicSlider_4.setObjectName("musicSlider_4")
        self.horizontalLayout_5.addWidget(self.musicSlider_4)
        self.label_15 = QtWidgets.QLabel(self.musicTab)
        self.label_15.setGeometry(QtCore.QRect(190, 720, 55, 16))
        self.label_15.setObjectName("label_15")
        self.speedSlider_3 = QtWidgets.QSlider(self.musicTab)
        self.speedSlider_3.setGeometry(QtCore.QRect(839, 500, 251, 22))
        self.speedSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.speedSlider_3.setObjectName("speedSlider_3")
        self.zoomOutButton_3 = QtWidgets.QPushButton(self.musicTab)
        self.zoomOutButton_3.setGeometry(QtCore.QRect(100, 500, 71, 28))
        self.zoomOutButton_3.setObjectName("zoomOutButton_3")
        self.label_12 = QtWidgets.QLabel(self.musicTab)
        self.label_12.setGeometry(QtCore.QRect(870, 720, 55, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.musicTab)
        self.label_13.setGeometry(QtCore.QRect(790, 500, 41, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.musicTab)
        self.label_14.setGeometry(QtCore.QRect(410, 720, 55, 16))
        self.label_14.setObjectName("label_14")
        self.checkBox_3 = QtWidgets.QCheckBox(self.musicTab)
        self.checkBox_3.setGeometry(QtCore.QRect(970, 730, 131, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.tabWidget.addTab(self.musicTab, "")
        self.ecgTab = QtWidgets.QWidget()
        self.ecgTab.setObjectName("ecgTab")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.ecgTab)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 1111, 481))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.ecgLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.ecgLayout.setContentsMargins(0, 0, 0, 0)
        self.ecgLayout.setObjectName("ecgLayout")
        self.pausePlayButton_4 = QtWidgets.QPushButton(self.ecgTab)
        self.pausePlayButton_4.setGeometry(QtCore.QRect(370, 500, 271, 28))
        self.pausePlayButton_4.setObjectName("pausePlayButton_4")
        self.rewindButton_4 = QtWidgets.QPushButton(self.ecgTab)
        self.rewindButton_4.setGeometry(QtCore.QRect(660, 500, 71, 28))
        self.rewindButton_4.setObjectName("rewindButton_4")
        self.label_16 = QtWidgets.QLabel(self.ecgTab)
        self.label_16.setGeometry(QtCore.QRect(790, 500, 41, 16))
        self.label_16.setObjectName("label_16")
        self.layoutWidget_2 = QtWidgets.QWidget(self.ecgTab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 540, 1091, 171))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ecgSlider_1 = QtWidgets.QSlider(self.layoutWidget_2)
        self.ecgSlider_1.setOrientation(QtCore.Qt.Vertical)
        self.ecgSlider_1.setObjectName("ecgSlider_1")
        self.horizontalLayout_8.addWidget(self.ecgSlider_1)
        self.ecgSlider_2 = QtWidgets.QSlider(self.layoutWidget_2)
        self.ecgSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.ecgSlider_2.setObjectName("ecgSlider_2")
        self.horizontalLayout_8.addWidget(self.ecgSlider_2)
        self.ecgSlider_3 = QtWidgets.QSlider(self.layoutWidget_2)
        self.ecgSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.ecgSlider_3.setObjectName("ecgSlider_3")
        self.horizontalLayout_8.addWidget(self.ecgSlider_3)
        self.ecgSlider_4 = QtWidgets.QSlider(self.layoutWidget_2)
        self.ecgSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.ecgSlider_4.setObjectName("ecgSlider_4")
        self.horizontalLayout_8.addWidget(self.ecgSlider_4)
        self.zoomOutButton_4 = QtWidgets.QPushButton(self.ecgTab)
        self.zoomOutButton_4.setGeometry(QtCore.QRect(100, 500, 71, 28))
        self.zoomOutButton_4.setObjectName("zoomOutButton_4")
        self.checkBox_4 = QtWidgets.QCheckBox(self.ecgTab)
        self.checkBox_4.setGeometry(QtCore.QRect(970, 730, 131, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.zoomInButton_4 = QtWidgets.QPushButton(self.ecgTab)
        self.zoomInButton_4.setGeometry(QtCore.QRect(20, 500, 71, 28))
        self.zoomInButton_4.setObjectName("zoomInButton_4")
        self.label_17 = QtWidgets.QLabel(self.ecgTab)
        self.label_17.setGeometry(QtCore.QRect(870, 720, 55, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.ecgTab)
        self.label_18.setGeometry(QtCore.QRect(190, 720, 55, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.ecgTab)
        self.label_19.setGeometry(QtCore.QRect(410, 720, 55, 16))
        self.label_19.setObjectName("label_19")
        self.speedSlider_4 = QtWidgets.QSlider(self.ecgTab)
        self.speedSlider_4.setGeometry(QtCore.QRect(839, 500, 251, 22))
        self.speedSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.speedSlider_4.setObjectName("speedSlider_4")
        self.label_20 = QtWidgets.QLabel(self.ecgTab)
        self.label_20.setGeometry(QtCore.QRect(640, 720, 55, 16))
        self.label_20.setObjectName("label_20")
        self.tabWidget.addTab(self.ecgTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1113, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.menuFile.addAction(self.actionLoad)
        self.menubar.addAction(self.menuFile.menuAction())
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        self.actionLoad.triggered.connect(self.loadWavFile)  # Connect to loadWavFile method

        self.pausePlayButton_3.clicked.connect(self.playPauseLoadedSound)  # Connect to playPauseLoadedSound method
        self.pausePlayButton_2.clicked.connect(self.playPauseLoadedSound)  # Connect to playPauseLoadedSound method

        self.rewindButton_3.clicked.connect(self.rewindLoadedSound)
        self.rewindButton_2.clicked.connect(self.rewindLoadedSound)

    def loadWavFile(self):
        # Open a file dialog and get the selected file name
        fileName, _ = QFileDialog.getOpenFileName(
            None, "Load WAV File", "", "WAV Files (*.wav);;All Files (*)"
        )

        if fileName:
            self.file_path = fileName  # Store the file path
            self.media_player = QMediaPlayer()

            # Create a QUrl from the file name
            url = QtCore.QUrl.fromLocalFile(fileName)

            # Create QMediaContent from the QUrl
            content = QMediaContent(url)

            # Set the media content for the media player
            self.media_player.setMedia(content)

    def playPauseLoadedSound(self):
        if hasattr(self, 'file_path') and self.file_path:
            if not hasattr(self, 'media_player'):
                media_content = QMediaContent(QtCore.QUrl.fromLocalFile(self.file_path))
                self.media_player = QMediaPlayer()
                self.media_player.setMedia(media_content)

            if self.media_player.state() == QMediaPlayer.PlayingState:
                self.media_player.pause()
            else:
                self.media_player.play()
        else:
            print("No file loaded.")


    def rewindLoadedSound(self):
        if hasattr(self, 'media_player'):
            self.media_player.setPosition(0)
        else:
            print("No file loaded.")



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.smothingComboBox.setItemText(0, _translate("MainWindow", "Rectangle"))
        self.smothingComboBox.setItemText(1, _translate("MainWindow", "Gaussian"))
        self.smothingComboBox.setItemText(2, _translate("MainWindow", "Hamming"))
        self.smothingComboBox.setItemText(3, _translate("MainWindow", "Hanning"))
        self.label.setText(_translate("MainWindow", "Smoothing Window"))
        self.label_2.setText(_translate("MainWindow", "Amplitude"))
        self.label_3.setText(_translate("MainWindow", "Frequency"))
        self.label_4.setText(_translate("MainWindow", "Hz"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.smoothingWindowTab), _translate("MainWindow", "Smoothing Window"))
        self.zoomInButton_1.setText(_translate("MainWindow", "Zoom In"))
        self.zoomOutButton_1.setText(_translate("MainWindow", "Zoom Out"))
        self.pausePlayButton_1.setText(_translate("MainWindow", "Pause/Play"))
        self.rewindButton_1.setText(_translate("MainWindow", "Rewind"))
        self.label_5.setText(_translate("MainWindow", "Speed"))
        self.checkBox_1.setText(_translate("MainWindow", "Hide Spectrogram"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.unifromRangeTab), _translate("MainWindow", "Uniform Range"))
        self.zoomInButton_2.setText(_translate("MainWindow", "Zoom In"))
        self.rewindButton_2.setText(_translate("MainWindow", "Rewind"))
        self.pausePlayButton_2.setText(_translate("MainWindow", "Pause/Play"))
        self.zoomOutButton_2.setText(_translate("MainWindow", "Zoom Out"))
        self.label_6.setText(_translate("MainWindow", "Speed"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.checkBox_2.setText(_translate("MainWindow", "Hide Spectrogram"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.animalTab), _translate("MainWindow", "Animal Sounds"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))
        self.pausePlayButton_3.setText(_translate("MainWindow", "Pause/Play"))
        self.rewindButton_3.setText(_translate("MainWindow", "Rewind"))
        self.zoomInButton_3.setText(_translate("MainWindow", "Zoom In"))
        self.label_15.setText(_translate("MainWindow", "TextLabel"))
        self.zoomOutButton_3.setText(_translate("MainWindow", "Zoom Out"))
        self.label_12.setText(_translate("MainWindow", "TextLabel"))
        self.label_13.setText(_translate("MainWindow", "Speed"))
        self.label_14.setText(_translate("MainWindow", "TextLabel"))
        self.checkBox_3.setText(_translate("MainWindow", "Hide Spectrogram"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.musicTab), _translate("MainWindow", "Musical Instruments"))
        self.pausePlayButton_4.setText(_translate("MainWindow", "Pause/Play"))
        self.rewindButton_4.setText(_translate("MainWindow", "Rewind"))
        self.label_16.setText(_translate("MainWindow", "Speed"))
        self.zoomOutButton_4.setText(_translate("MainWindow", "Zoom Out"))
        self.checkBox_4.setText(_translate("MainWindow", "Hide Spectrogram"))
        self.zoomInButton_4.setText(_translate("MainWindow", "Zoom In"))
        self.label_17.setText(_translate("MainWindow", "TextLabel"))
        self.label_18.setText(_translate("MainWindow", "TextLabel"))
        self.label_19.setText(_translate("MainWindow", "TextLabel"))
        self.label_20.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ecgTab), _translate("MainWindow", "ECG"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))

def main():
    app = QtWidgets.QApplication(sys.argv)  # Create the application instance
    MainWindow = QtWidgets.QMainWindow()  # Create the main window
    ui = Ui_MainWindow()  # Create an instance of the UI class
    ui.setupUi(MainWindow)  # Set up the UI for the main window
    MainWindow.show()  # Display the main window
    sys.exit(app.exec_())  # Run the application event loop


main()