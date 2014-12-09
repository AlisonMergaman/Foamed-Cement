# -*- coding: utf-8 -*-
"""
GUI
Created August 2014

This prrogam is the GUI for the Bubble Cement Void Program. It is linked up
with program Comb_Plots. There, Comb_Plots is linked with many other programs
to make the algorithm work.

Run this program.

@author: Alison Mergaman
Alison.Mergaman@contr.netl.doe.gov
"""

import sys
from PyQt4 import QtGui, QtCore
import Comb_Plots
#import os


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
       


        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.form_widget = MainWidget()
        self.setCentralWidget(self.form_widget)

        self.resize(800, 300)
        self.center()
        self.setWindowTitle('CT Bubble Images')

        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def keyPressEvent(self, event):
        key = event.key()
        if (key == QtCore.Qt.Key_Return or key == QtCore.Qt.Key_Enter):
            self.form_widget.launchClicked()

    def outfileDialog(self):
        try:
            with open('outname.ini', 'r') as FI:
                textin = self, FI.readline().rstrip()
        except:
            pass
        text, ok = QtGui.QInputDialog.getText(self, 'Output File',
                                              'Output File Name:',
                                              text=textin[1])
        if ok:
            with open('outname.ini', 'w') as FO:
                FO.write(text)

    def HistoSpec(self):
        self.hs = HistWidget()



class MainWidget(QtGui.QWidget):

    def __init__(self):
        super(MainWidget, self).__init__()
        self.initUi()

    def initUi(self):
        #############################################
        # Directory Selection
        #############################################
        self.fflabel = QtGui.QLabel('Directory:')
        self.ffiletxt = QtGui.QLineEdit(self)
        self.ffiletxt.setSizePolicy(QtGui.QSizePolicy.Expanding,
                                    QtGui.QSizePolicy.Maximum)
        self.ffilebtn = QtGui.QPushButton('Browse', self)
        self.ffilebtn.clicked.connect(self.ffileDialog)

        ffilebox = QtGui.QHBoxLayout()
        ffilebox.addSpacing(50)
        ffilebox.addWidget(self.fflabel)
        ffilebox.addSpacing(5)
        ffilebox.addWidget(self.ffiletxt)
        ffilebox.addWidget(self.ffilebtn)
        ffilebox.addSpacing(50)

        #############################################
        # Output Directory Selection
        #############################################
        self.odlabel = QtGui.QLabel('Output Directory:')
        self.odtxt = QtGui.QLineEdit(self)
        self.odtxt.setSizePolicy(QtGui.QSizePolicy.Expanding,
                                 QtGui.QSizePolicy.Maximum)
        self.odbtn = QtGui.QPushButton('Browse', self)
        self.odbtn.clicked.connect(self.odDialog)

        odbox = QtGui.QHBoxLayout()
        odbox.addSpacing(50)
        odbox.addWidget(self.odlabel)
        odbox.addSpacing(5)
        odbox.addWidget(self.odtxt)
        odbox.addWidget(self.odbtn)
        odbox.addSpacing(50)

        #############################################
        # Skip, Start, Skip, Voxel Size
        #############################################
        sflabel = QtGui.QLabel('Skip File:')
        self.sftxt = QtGui.QLineEdit(self)
        self.sftxt.setFixedWidth(40)
        self.sftxt.setAlignment(QtCore.Qt.AlignRight)        
        
        stlabel = QtGui.QLabel('Start Row:')
        self.sttxt = QtGui.QLineEdit(self)
        self.sttxt.setFixedWidth(40)
        self.sttxt.setAlignment(QtCore.Qt.AlignRight)

        sklabel = QtGui.QLabel('Skip Row:')
        self.sktxt = QtGui.QLineEdit(self)
        self.sktxt.setFixedWidth(40)
        self.sktxt.setAlignment(QtCore.Qt.AlignRight)
        
        svlabel = QtGui.QLabel('Voxel Size:')
        self.svtxt = QtGui.QLineEdit(self)
        self.svtxt.setFixedWidth(60)
        self.svtxt.setAlignment(QtCore.Qt.AlignRight)
        
#        sinlabel = QtGui.QLabel('Voxel Size(in):')
#        self.sintxt = QtGui.QLineEdit(self)
#        self.sintxt.setFixedWidth(60)
#        self.sintxt.setAlignment(QtCore.Qt.AlignRight)
        

        

        sssbox = QtGui.QHBoxLayout()
        sssbox.addStretch(1)
        sssbox.addWidget(sflabel)
        sssbox.addWidget(self.sftxt)    
        sssbox.addStretch(1)
        sssbox.addWidget(stlabel)
        sssbox.addWidget(self.sttxt)
        sssbox.addStretch(1)
        sssbox.addWidget(sklabel)
        sssbox.addWidget(self.sktxt)
        sssbox.addStretch(1)
        sssbox.addWidget(svlabel)
        sssbox.addWidget(self.svtxt)
        sssbox.addStretch(1)
#        sssbox.addWidget(sinlabel)
#        sssbox.addWidget(self.sintxt)
#        sssbox.addStretch(1)



        #############################################
        # Name of Plot
        #############################################
        self.nplabel = QtGui.QLabel('Name of Plot:')
        self.nptxt = QtGui.QLineEdit(self)

        npbox = QtGui.QHBoxLayout()
        npbox.addSpacing(100)
        npbox.addWidget(self.nplabel)
        npbox.addSpacing(5)
        npbox.addWidget(self.nptxt)
        npbox.addSpacing(0)
        
        
                
        #############################################
        # Axes Names
        #############################################  
        air_conlabel = QtGui.QLabel('Air Content')
        
        acllabel = QtGui.QLabel('Average Chord Length')
        
        palabel = QtGui.QLabel('Paste Air Ratio')
        
        spacfaclabel = QtGui.QLabel('Spacing Factor')
        
        voidfreqlabel = QtGui.QLabel('Void Frequency')
        
        axesbox = QtGui.QHBoxLayout()
        axesbox.addSpacing(70)
        axesbox.addWidget(air_conlabel)
        axesbox.addSpacing(40)
        axesbox.addWidget(acllabel)
        axesbox.addSpacing(40)
        axesbox.addWidget(palabel)
        axesbox.addSpacing(40)
        axesbox.addWidget(spacfaclabel)
        axesbox.addSpacing(40)
        axesbox.addWidget(voidfreqlabel)
        axesbox.addSpacing(40)
                
        #############################################
        # X Axes
        #############################################  
   
        airxalabel = QtGui.QLabel('X Axis: 0, ')
        self.airxatxt = QtGui.QLineEdit(self)
        self.airxatxt.setFixedWidth(40)
        self.airxatxt.setAlignment(QtCore.Qt.AlignRight)
        
        aclxalabel = QtGui.QLabel('X Axis: 0, ')
        self.aclxatxt = QtGui.QLineEdit(self)
        self.aclxatxt.setFixedWidth(40)
        self.aclxatxt.setAlignment(QtCore.Qt.AlignRight)
        
        paxalabel = QtGui.QLabel('X Axis: 0, ')
        self.paxatxt = QtGui.QLineEdit(self)
        self.paxatxt.setFixedWidth(40)
        self.paxatxt.setAlignment(QtCore.Qt.AlignRight)
        
        spfxalabel = QtGui.QLabel('X Axis: 0, ')
        self.spfxatxt = QtGui.QLineEdit(self)
        self.spfxatxt.setFixedWidth(40)
        self.spfxatxt.setAlignment(QtCore.Qt.AlignRight)
        
        vfrxalabel = QtGui.QLabel('X Axis: 0, ')
        self.vfrxatxt = QtGui.QLineEdit(self)
        self.vfrxatxt.setFixedWidth(40)
        self.vfrxatxt.setAlignment(QtCore.Qt.AlignRight)

        xaxesbox = QtGui.QHBoxLayout()
        xaxesbox.addStretch(1)
        xaxesbox.addWidget(airxalabel)
        xaxesbox.addWidget(self.airxatxt)    
        xaxesbox.addStretch(1)
        xaxesbox.addWidget(aclxalabel)
        xaxesbox.addWidget(self.aclxatxt)    
        xaxesbox.addStretch(1)
        xaxesbox.addWidget(paxalabel)
        xaxesbox.addWidget(self.paxatxt)    
        xaxesbox.addStretch(1)
        xaxesbox.addWidget(spfxalabel)
        xaxesbox.addWidget(self.spfxatxt)    
        xaxesbox.addStretch(1)
        xaxesbox.addWidget(vfrxalabel)
        xaxesbox.addWidget(self.vfrxatxt)    
        xaxesbox.addStretch(1)
        
        #############################################
        # Y Axes
        #############################################
        airyalabel = QtGui.QLabel('Y Axis: 0, ')
        self.airyatxt = QtGui.QLineEdit(self)
        self.airyatxt.setFixedWidth(40)
        self.airyatxt.setAlignment(QtCore.Qt.AlignRight)
        
        aclyalabel = QtGui.QLabel('Y Axis: 0, ')
        self.aclyatxt = QtGui.QLineEdit(self)
        self.aclyatxt.setFixedWidth(40)
        self.aclyatxt.setAlignment(QtCore.Qt.AlignRight)
        
        payalabel = QtGui.QLabel('Y Axis: 0, ')
        self.payatxt = QtGui.QLineEdit(self)
        self.payatxt.setFixedWidth(40)
        self.payatxt.setAlignment(QtCore.Qt.AlignRight)
        
        spfyalabel = QtGui.QLabel('Y Axis: 0, ')
        self.spfyatxt = QtGui.QLineEdit(self)
        self.spfyatxt.setFixedWidth(40)
        self.spfyatxt.setAlignment(QtCore.Qt.AlignRight)
        
        vfryalabel = QtGui.QLabel('Y Axis: 0, ')
        self.vfryatxt = QtGui.QLineEdit(self)
        self.vfryatxt.setFixedWidth(40)
        self.vfryatxt.setAlignment(QtCore.Qt.AlignRight)
        

        yaxesbox = QtGui.QHBoxLayout()
        yaxesbox.addStretch(1)
        yaxesbox.addWidget(airyalabel)
        yaxesbox.addWidget(self.airyatxt)    
        yaxesbox.addStretch(1)
        yaxesbox.addWidget(aclyalabel)
        yaxesbox.addWidget(self.aclyatxt)    
        yaxesbox.addStretch(1)
        yaxesbox.addWidget(payalabel)
        yaxesbox.addWidget(self.payatxt)    
        yaxesbox.addStretch(1)
        yaxesbox.addWidget(spfyalabel)
        yaxesbox.addWidget(self.spfyatxt)    
        yaxesbox.addStretch(1)
        yaxesbox.addWidget(vfryalabel)
        yaxesbox.addWidget(self.vfryatxt)    
        yaxesbox.addStretch(1)


        #############################################
        # Launch Button
        #############################################
        self.lbtn = QtGui.QPushButton('Launch', self)
        self.lbtn.clicked.connect(self.launchClicked)
        #self.lbtn.setToolTip('Launch downsampler')
        #print 'Looky Looky'
        self.lbtn.resize(self.lbtn.sizeHint())
        self.thlabel = QtGui.QLabel('')

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.thlabel)
        hbox.addWidget(self.lbtn)

        #############################################
        # Over-all Layout
        #############################################
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(ffilebox)
        vbox.addLayout(odbox)
        vbox.addLayout(sssbox)
        vbox.addLayout(npbox)
        vbox.addLayout(axesbox)
        vbox.addLayout(xaxesbox)
        vbox.addLayout(yaxesbox)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.Que = []
        self.running = []
        self.Tmax = 1
        self.Trunning = 0

        self.readGUIini()


    def ffileDialog(self):
        fname = QtGui.QFileDialog.getExistingDirectory(self,
                                                       str(self.ffiletxt.text())
                                                       .rpartition('\\')[0])
        if (fname != ''):
            self.ffiletxt.setText(fname)

    def odDialog(self):
        dname = QtGui.QFileDialog.getExistingDirectory(self,
                                                       str(self.odtxt.text()))
        if (dname != ''):
            self.odtxt.setText(dname)



    def launchClicked(self):
        self.lbtn.setEnabled(False)
        self.lbtn.setText('Processing')
        self.repaint()
        with open('GUI.ini', 'w') as FO:
#                os.remove(dname)
                FO.write(str(self.ffiletxt.text()) + '\n')
                FO.write(str(self.odtxt.text()) + '\n')
                FO.write(str(self.nptxt.text()) + '\n')
                FO.write(str(self.sttxt.text()) + ' ' + 
                    str(self.sktxt.text()) + ' ' + 
                    str(self.sftxt.text()) + ' ' + 
                    str(self.svtxt.text()) + ' ' +
    #                str(self.sintxt.text()) + ' ' +
                    str(self.airxatxt.text()) + ' ' +
                    str(self.airyatxt.text()) + ' ' +
                    str(self.aclxatxt.text()) + ' ' +
                    str(self.aclyatxt.text()) + ' ' +
                    str(self.paxatxt.text()) + ' ' +
                    str(self.payatxt.text()) + ' ' +
                    str(self.spfxatxt.text()) + ' ' +
                    str(self.spfyatxt.text()) + ' ' +
                    str(self.vfrxatxt.text()) + ' ' +
                    str(self.vfryatxt.text()) + ' ' )
    #                str(self.yatxt.text()) + ' ')
        Comb_Plots.start_row = int(self.sttxt.text())
#        Comb_Plots.skip_file=int(self.sftxt.text())
        Comb_Plots.skip_row = int(self.sktxt.text())
        Comb_Plots.voxel = float(self.svtxt.text())
#        Comb_Plots.voxelin = float(self.sintxt.text())
        Comb_Plots.name_plot = str(self.nptxt.text())
        Comb_Plots.airxa = float(self.airxatxt.text())
        Comb_Plots.airya=float(self.airyatxt.text())
        Comb_Plots.aclxa=float(self.aclxatxt.text())
        Comb_Plots.paxa = float(self.paxatxt.text())
        Comb_Plots.spacxa=float(self.spfxatxt.text())
        Comb_Plots.voidxa=float(self.vfrxatxt.text())
        Comb_Plots.aclya=float(self.aclyatxt.text())
        Comb_Plots.paya=float(self.payatxt.text())
        Comb_Plots.spacya=float(self.spfyatxt.text())
        Comb_Plots.voidya=float(self.vfryatxt.text())
#        Comb_Plots.y_a = float(self.yatxt.text())
        Comb_Plots.comb_plots(str(self.ffiletxt.text()), str(self.odtxt.text()), int(self.sftxt.text()))
#        Comb_Plots.comb_plots(str(self.ffiletxt.text()), str(self.odtxt.text()))

        self.lbtn.setEnabled(True)
        self.lbtn.setText('Launch')
        self.repaint()


    def readGUIini(self):
        try:
            with open('GUI.ini', 'r') as FI:
                self.ffiletxt.setText(FI.readline()[:-1])
                self.odtxt.setText(FI.readline()[:-1])
                self.nptxt.setText(FI.readline()[:-1])
                line = (FI.readline()).split()
                self.sttxt.setText(line[0])
                self.sktxt.setText(line[1])

                self.sftxt.setText(line[2])
                self.svtxt.setText(line[3])
#                self.sintxt.setText(line[4])
                
                self.airxatxt.setText(line[4])
                self.airyatxt.setText(line[5])
                self.aclxatxt.setText(line[6])
                self.aclyatxt.setText(line[7])
                self.paxatxt.setText(line[8])
                self.payatxt.setText(line[9])
                self.spfxatxt.setText(line[10])
                self.spfyatxt.setText(line[11])
                self.vfrxatxt.setText(line[12])
                self.vfryatxt.setText(line[13])

                
                

        except:
            pass

 

class HistWidget(QtGui.QWidget):

    def __init__(self):
        super(HistWidget, self).__init__()
        self.initUi()
        self.readIni()

    def initUi(self):
        #############################################
        # File Spec
        #############################################
        self.flabel = QtGui.QLabel('File Specification:')
        self.ftxt = QtGui.QLineEdit(self)
        self.ftxt.setSizePolicy(QtGui.QSizePolicy.Expanding,
                                QtGui.QSizePolicy.Maximum)

        fbox = QtGui.QHBoxLayout()
        fbox.addSpacing(10)
        fbox.addWidget(self.flabel)
        fbox.addWidget(self.ftxt)
        fbox.addSpacing(10)

        #############################################
        # Bin Size Spc
        #############################################
        self.blabel = QtGui.QLabel('Number of Bins:')
        self.btxt = QtGui.QLineEdit(self)
        self.btxt.setFixedWidth(40)

        self.cblabel = QtGui.QLabel('Use Relative Values:')
        self.cb = QtGui.QCheckBox(self)

        self.minlabel = QtGui.QLabel('Min:')
        self.min = QtGui.QLineEdit(self)
        self.min.setFixedWidth(40)
        self.maxlabel = QtGui.QLabel('Max:')
        self.max = QtGui.QLineEdit(self)
        self.max.setFixedWidth(40)

        bbox = QtGui.QHBoxLayout()
        bbox.addStretch(1)
        bbox.addWidget(self.blabel)
        bbox.addWidget(self.btxt)
        bbox.addSpacing(10)
        bbox.addWidget(self.cblabel)
        bbox.addWidget(self.cb)
        bbox.addSpacing(10)
        bbox.addWidget(self.minlabel)
        bbox.addWidget(self.min)
        bbox.addWidget(self.maxlabel)
        bbox.addWidget(self.max)
        bbox.addStretch(1)

        #############################################
        # okay/cancel Buttons
        #############################################
        self.okbtn = QtGui.QPushButton('Okay', self)
        self.okbtn.clicked.connect(self.okc)
        self.okbtn.resize(self.okbtn.sizeHint())
        self.cbtn = QtGui.QPushButton('Cancel', self)
        self.cbtn.clicked.connect(self.close)
        self.cbtn.resize(self.cbtn.sizeHint())

        #############################################
        # Over-all Layout
        #############################################
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.okbtn)
        hbox.addWidget(self.cbtn)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(fbox)
        vbox.addLayout(bbox)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(100, 100, 450, 100)
        self.setWindowTitle('Histogram Specification')

        self.show()

    def readIni(self):
        try:
            with open('histo.ini', 'r') as FI:
                self.ftxt.setText(FI.readline().rstrip())
                self.btxt.setText(FI.readline().rstrip())
                self.cb.setChecked(int(FI.readline().rstrip()))
                (offsetl, offsetu) = FI.readline().rstrip().split()
                self.min.setText(offsetl)
                self.max.setText(offsetu)
        except:
            pass

    def okc(self):
        with open('histo.ini', 'w') as FO:
            FO.write(str(self.ftxt.text()) + '\n')
            FO.write(str(self.btxt.text()) + '\n')
            FO.write(str(self.cb.checkState()) + '\n')
            FO.write(str(self.min.text()) + ' ' +
                     str(self.max.text()))
        self.close()

    def can(self):
        self.close()




def main():
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
