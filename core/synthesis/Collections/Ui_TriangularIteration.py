# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/Desktop/Pyslvs-PyQt5/core/synthesis/Collections/TriangularIteration.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(361, 736)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/collection-triangular-iteration.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.load_4Bar = QtWidgets.QPushButton(Form)
        self.load_4Bar.setObjectName("load_4Bar")
        self.horizontalLayout_4.addWidget(self.load_4Bar)
        self.load_8Bar = QtWidgets.QPushButton(Form)
        self.load_8Bar.setObjectName("load_8Bar")
        self.horizontalLayout_4.addWidget(self.load_8Bar)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_4.addWidget(self.line_2)
        self.clear_button = QtWidgets.QPushButton(Form)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout_4.addWidget(self.clear_button)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_11.addWidget(self.line)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.main_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setObjectName("main_layout")
        self.joint_panel = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.joint_panel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.joint_panel.setObjectName("joint_panel")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.joint_panel)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.joint_name_label = QtWidgets.QLabel(self.joint_panel)
        self.joint_name_label.setObjectName("joint_name_label")
        self.verticalLayout_6.addWidget(self.joint_name_label)
        self.joint_name = QtWidgets.QLineEdit(self.joint_panel)
        self.joint_name.setReadOnly(True)
        self.joint_name.setObjectName("joint_name")
        self.verticalLayout_6.addWidget(self.joint_name)
        self.status_label = QtWidgets.QLabel(self.joint_panel)
        self.status_label.setObjectName("status_label")
        self.verticalLayout_6.addWidget(self.status_label)
        self.status = QtWidgets.QLabel(self.joint_panel)
        self.status.setObjectName("status")
        self.verticalLayout_6.addWidget(self.status)
        self.solution_label = QtWidgets.QLabel(self.joint_panel)
        self.solution_label.setObjectName("solution_label")
        self.verticalLayout_6.addWidget(self.solution_label)
        self.PLAP_solution = QtWidgets.QPushButton(self.joint_panel)
        self.PLAP_solution.setObjectName("PLAP_solution")
        self.verticalLayout_6.addWidget(self.PLAP_solution)
        self.PLLP_solution = QtWidgets.QPushButton(self.joint_panel)
        self.PLLP_solution.setObjectName("PLLP_solution")
        self.verticalLayout_6.addWidget(self.PLLP_solution)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.main_layout.addWidget(self.joint_panel)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_7.addWidget(self.line_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.Expression_list_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Expression_list_label.setObjectName("Expression_list_label")
        self.verticalLayout_9.addWidget(self.Expression_list_label)
        self.Expression_list = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.Expression_list.setObjectName("Expression_list")
        self.verticalLayout_9.addWidget(self.Expression_list)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.grounded_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.grounded_label.setObjectName("grounded_label")
        self.verticalLayout_10.addWidget(self.grounded_label)
        self.grounded_list = QtWidgets.QListView(self.verticalLayoutWidget_2)
        self.grounded_list.setObjectName("grounded_list")
        self.verticalLayout_10.addWidget(self.grounded_list)
        self.horizontalLayout_5.addLayout(self.verticalLayout_10)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Driver_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Driver_label.setObjectName("Driver_label")
        self.verticalLayout_2.addWidget(self.Driver_label)
        self.Driver_list = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.Driver_list.setObjectName("Driver_list")
        self.verticalLayout_2.addWidget(self.Driver_list)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Follower_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Follower_label.setObjectName("Follower_label")
        self.verticalLayout_4.addWidget(self.Follower_label)
        self.Follower_list = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.Follower_list.setObjectName("Follower_list")
        self.verticalLayout_4.addWidget(self.Follower_list)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Target_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Target_label.setObjectName("Target_label")
        self.verticalLayout_3.addWidget(self.Target_label)
        self.Target_list = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.Target_list.setObjectName("Target_list")
        self.verticalLayout_3.addWidget(self.Target_list)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.constraint_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.constraint_label.setObjectName("constraint_label")
        self.verticalLayout_5.addWidget(self.constraint_label)
        self.constraint_list = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.constraint_list.setObjectName("constraint_list")
        self.verticalLayout_5.addWidget(self.constraint_list)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Link_Expression_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Link_Expression_label.setObjectName("Link_Expression_label")
        self.verticalLayout.addWidget(self.Link_Expression_label)
        self.Link_Expression = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.Link_Expression.setReadOnly(True)
        self.Link_Expression.setObjectName("Link_Expression")
        self.verticalLayout.addWidget(self.Link_Expression)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Expression_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Expression_label.setObjectName("Expression_label")
        self.verticalLayout_8.addWidget(self.Expression_label)
        self.Expression = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.Expression.setReadOnly(True)
        self.Expression.setObjectName("Expression")
        self.verticalLayout_8.addWidget(self.Expression)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.verticalLayout_11.addWidget(self.splitter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Common:"))
        self.load_4Bar.setText(_translate("Form", "4 Bar"))
        self.load_8Bar.setText(_translate("Form", "8 Bar"))
        self.clear_button.setText(_translate("Form", "Clear"))
        self.joint_name_label.setText(_translate("Form", "Joint name:"))
        self.status_label.setText(_translate("Form", "Status:"))
        self.status.setText(_translate("Form", "No status"))
        self.solution_label.setText(_translate("Form", "Joint solutions:"))
        self.PLAP_solution.setText(_translate("Form", "PLAP"))
        self.PLLP_solution.setText(_translate("Form", "PLLP"))
        self.Expression_list_label.setText(_translate("Form", "Solutions:"))
        self.grounded_label.setText(_translate("Form", "Gounded:"))
        self.Driver_label.setText(_translate("Form", "Drivers:"))
        self.Follower_label.setText(_translate("Form", "Followers:"))
        self.Target_label.setText(_translate("Form", "Targets:"))
        self.constraint_label.setText(_translate("Form", "Gruebler\'s Equation:"))
        self.Link_Expression_label.setText(_translate("Form", "Link expression:"))
        self.Expression_label.setText(_translate("Form", "Expression:"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

