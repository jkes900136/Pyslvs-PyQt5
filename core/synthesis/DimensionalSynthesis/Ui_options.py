# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/桌面/Pyslvs-PyQt5/core/synthesis/DimensionalSynthesis/options.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(409, 492)
        Dialog.setMinimumSize(QtCore.QSize(409, 492))
        Dialog.setMaximumSize(QtCore.QSize(409, 492))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/DimensionalSynthesis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.planarlinkage = QtWidgets.QWidget()
        self.planarlinkage.setObjectName("planarlinkage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.planarlinkage)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.generation_label = QtWidgets.QLabel(self.planarlinkage)
        self.generation_label.setObjectName("generation_label")
        self.horizontalLayout_2.addWidget(self.generation_label)
        self.maxGen = QtWidgets.QSpinBox(self.planarlinkage)
        self.maxGen.setMinimum(0)
        self.maxGen.setMaximum(5000)
        self.maxGen.setSingleStep(100)
        self.maxGen.setProperty("value", 1000)
        self.maxGen.setObjectName("maxGen")
        self.horizontalLayout_2.addWidget(self.maxGen)
        self.report_label = QtWidgets.QLabel(self.planarlinkage)
        self.report_label.setObjectName("report_label")
        self.horizontalLayout_2.addWidget(self.report_label)
        self.report = QtWidgets.QSpinBox(self.planarlinkage)
        self.report.setMaximum(100)
        self.report.setObjectName("report")
        self.horizontalLayout_2.addWidget(self.report)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.PLTable = QtWidgets.QTableWidget(self.planarlinkage)
        self.PLTable.setObjectName("PLTable")
        self.PLTable.setColumnCount(2)
        self.PLTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.PLTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PLTable.setHorizontalHeaderItem(1, item)
        self.verticalLayout_2.addWidget(self.PLTable)
        self.tabWidget.addTab(self.planarlinkage, "")
        self.algorithm = QtWidgets.QWidget()
        self.algorithm.setObjectName("algorithm")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.algorithm)
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.algorithm)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.popSize = QtWidgets.QSpinBox(self.algorithm)
        self.popSize.setMinimum(10)
        self.popSize.setMaximum(10000)
        self.popSize.setSingleStep(10)
        self.popSize.setObjectName("popSize")
        self.horizontalLayout_3.addWidget(self.popSize)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.APTable = QtWidgets.QTableWidget(self.algorithm)
        self.APTable.setObjectName("APTable")
        self.APTable.setColumnCount(2)
        self.APTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.APTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.APTable.setHorizontalHeaderItem(1, item)
        self.APTable.horizontalHeader().setDefaultSectionSize(150)
        self.APTable.horizontalHeader().setMinimumSectionSize(150)
        self.verticalLayout_3.addWidget(self.APTable)
        self.tabWidget.addTab(self.algorithm, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.setDefault = QtWidgets.QPushButton(Dialog)
        self.setDefault.setObjectName("setDefault")
        self.horizontalLayout.addWidget(self.setDefault)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Options"))
        self.generation_label.setToolTip(_translate("Dialog", "<html><head/><body><p>This parameter determines the time of evolution.</p><p>If the value set to 0, algorithm will stop only when you clicked the interrupt button.</p></body></html>"))
        self.generation_label.setText(_translate("Dialog", "Max generation: (?)"))
        self.report_label.setToolTip(_translate("Dialog", "<html><head/><body><p>If the value set to 0, algorithm will report in every 10 generations.</p></body></html>"))
        self.report_label.setText(_translate("Dialog", "Report in every: (?)"))
        self.report.setSuffix(_translate("Dialog", "%"))
        item = self.PLTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Parameter"))
        item = self.PLTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.planarlinkage), _translate("Dialog", "Planar Linkage"))
        self.label.setToolTip(_translate("Dialog", "<html><head/><body><p>The greater the number will make possibilities more available, but will result in longer selection times.</p></body></html>"))
        self.label.setText(_translate("Dialog", "The first generation of the population: (?)"))
        item = self.APTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Parameter"))
        item = self.APTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.algorithm), _translate("Dialog", "Algorithm"))
        self.setDefault.setText(_translate("Dialog", "Reset to Default"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

