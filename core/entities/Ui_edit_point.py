# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ahshoe\Desktop\Pyslvs-PyQt5\core\entities\edit_point.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(314, 474)
        Dialog.setMinimumSize(QtCore.QSize(314, 474))
        Dialog.setMaximumSize(QtCore.QSize(314, 474))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/bearing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_label = QtWidgets.QLabel(Dialog)
        self.name_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.name_label.setObjectName("name_label")
        self.verticalLayout.addWidget(self.name_label)
        self.Point = QtWidgets.QComboBox(Dialog)
        self.Point.setObjectName("Point")
        self.verticalLayout.addWidget(self.Point)
        self.color_label = QtWidgets.QLabel(Dialog)
        self.color_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.color_label.setObjectName("color_label")
        self.verticalLayout.addWidget(self.color_label)
        self.Color = QtWidgets.QComboBox(Dialog)
        self.Color.setObjectName("Color")
        self.verticalLayout.addWidget(self.Color)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.X_coordinate = QtWidgets.QDoubleSpinBox(Dialog)
        self.X_coordinate.setMinimum(-999999.0)
        self.X_coordinate.setMaximum(999999.0)
        self.X_coordinate.setObjectName("X_coordinate")
        self.gridLayout.addWidget(self.X_coordinate, 1, 0, 1, 1)
        self.Y_coordinate = QtWidgets.QDoubleSpinBox(Dialog)
        self.Y_coordinate.setMinimum(-999999.0)
        self.Y_coordinate.setMaximum(999999.0)
        self.Y_coordinate.setObjectName("Y_coordinate")
        self.gridLayout.addWidget(self.Y_coordinate, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.type_label = QtWidgets.QLabel(Dialog)
        self.type_label.setObjectName("type_label")
        self.verticalLayout.addWidget(self.type_label)
        self.Type = QtWidgets.QComboBox(Dialog)
        self.Type.setObjectName("Type")
        self.Type.addItem("")
        self.Type.addItem("")
        self.Type.addItem("")
        self.verticalLayout.addWidget(self.Type)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.Angle = QtWidgets.QDoubleSpinBox(Dialog)
        self.Angle.setEnabled(False)
        self.Angle.setMaximum(180.0)
        self.Angle.setObjectName("Angle")
        self.verticalLayout.addWidget(self.Angle)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.noSelected = QtWidgets.QListWidget(Dialog)
        self.noSelected.setDragEnabled(True)
        self.noSelected.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.noSelected.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.noSelected.setObjectName("noSelected")
        self.horizontalLayout.addWidget(self.noSelected)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.selected = QtWidgets.QListWidget(Dialog)
        self.selected.setDragEnabled(True)
        self.selected.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.selected.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.selected.setObjectName("selected")
        self.horizontalLayout.addWidget(self.selected)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Point"))
        self.name_label.setText(_translate("Dialog", "Point Number"))
        self.color_label.setText(_translate("Dialog", "Color"))
        self.label.setText(_translate("Dialog", "x coordinate"))
        self.label_2.setText(_translate("Dialog", "y coordinate"))
        self.type_label.setText(_translate("Dialog", "Type:"))
        self.Type.setItemText(0, _translate("Dialog", "R (pin)"))
        self.Type.setItemText(1, _translate("Dialog", "P (slider block)"))
        self.Type.setItemText(2, _translate("Dialog", "RP (pin in slot)"))
        self.label_5.setText(_translate("Dialog", "Angle (Slider):"))
        self.label_3.setText(_translate("Dialog", "Links:"))
        self.label_4.setText(_translate("Dialog", ">>"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

