# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EPANET\frmTableDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmTable(object):
    def setupUi(self, frmTable):
        frmTable.setObjectName("frmTable")
        frmTable.resize(465, 415)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmTable.setFont(font)
        self.centralWidget = QtWidgets.QWidget(frmTable)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.fraTop = QtWidgets.QFrame(self.centralWidget)
        self.fraTop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraTop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraTop.setObjectName("fraTop")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.fraTop)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.fraTop)
        self.tabWidget.setObjectName("tabWidget")
        self.tabType = QtWidgets.QWidget()
        self.tabType.setObjectName("tabType")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabType)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lblSelect = QtWidgets.QLabel(self.tabType)
        self.lblSelect.setObjectName("lblSelect")
        self.verticalLayout_4.addWidget(self.lblSelect)
        self.fraType1 = QtWidgets.QFrame(self.tabType)
        self.fraType1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraType1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraType1.setObjectName("fraType1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.fraType1)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.rbnTimeseriesNode = QtWidgets.QRadioButton(self.fraType1)
        self.rbnTimeseriesNode.setObjectName("rbnTimeseriesNode")
        self.gridLayout_2.addWidget(self.rbnTimeseriesNode, 4, 0, 1, 1)
        self.rbnTimeseriesLink = QtWidgets.QRadioButton(self.fraType1)
        self.rbnTimeseriesLink.setObjectName("rbnTimeseriesLink")
        self.gridLayout_2.addWidget(self.rbnTimeseriesLink, 6, 0, 1, 1)
        self.txtNodeLink = QtWidgets.QLineEdit(self.fraType1)
        self.txtNodeLink.setObjectName("txtNodeLink")
        self.gridLayout_2.addWidget(self.txtNodeLink, 5, 1, 1, 1)
        self.rbnNodes = QtWidgets.QRadioButton(self.fraType1)
        self.rbnNodes.setObjectName("rbnNodes")
        self.gridLayout_2.addWidget(self.rbnNodes, 0, 0, 1, 1)
        self.cboTime = QtWidgets.QComboBox(self.fraType1)
        self.cboTime.setObjectName("cboTime")
        self.gridLayout_2.addWidget(self.cboTime, 1, 1, 1, 1)
        self.rbnLinks = QtWidgets.QRadioButton(self.fraType1)
        self.rbnLinks.setObjectName("rbnLinks")
        self.gridLayout_2.addWidget(self.rbnLinks, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.fraType1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 3, 0, 1, 2)
        self.verticalLayout_4.addWidget(self.fraType1)
        self.tabWidget.addTab(self.tabType, "")
        self.tabColumns = QtWidgets.QWidget()
        self.tabColumns.setObjectName("tabColumns")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabColumns)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblSelectColumn = QtWidgets.QLabel(self.tabColumns)
        self.lblSelectColumn.setObjectName("lblSelectColumn")
        self.verticalLayout_3.addWidget(self.lblSelectColumn)
        self.lstColumns = QtWidgets.QListWidget(self.tabColumns)
        self.lstColumns.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lstColumns.setObjectName("lstColumns")
        self.verticalLayout_3.addWidget(self.lstColumns)
        self.cbxSort = QtWidgets.QCheckBox(self.tabColumns)
        self.cbxSort.setObjectName("cbxSort")
        self.verticalLayout_3.addWidget(self.cbxSort)
        self.tabWidget.addTab(self.tabColumns, "")
        self.tabFilters = QtWidgets.QWidget()
        self.tabFilters.setObjectName("tabFilters")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabFilters)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblDefine = QtWidgets.QLabel(self.tabFilters)
        self.lblDefine.setObjectName("lblDefine")
        self.verticalLayout_2.addWidget(self.lblDefine)
        self.fraFilter1 = QtWidgets.QFrame(self.tabFilters)
        self.fraFilter1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraFilter1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraFilter1.setObjectName("fraFilter1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fraFilter1)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cboFilter = QtWidgets.QComboBox(self.fraFilter1)
        self.cboFilter.setObjectName("cboFilter")
        self.horizontalLayout_2.addWidget(self.cboFilter)
        self.cboCompare = QtWidgets.QComboBox(self.fraFilter1)
        self.cboCompare.setObjectName("cboCompare")
        self.horizontalLayout_2.addWidget(self.cboCompare)
        self.txtValue = QtWidgets.QLineEdit(self.fraFilter1)
        self.txtValue.setObjectName("txtValue")
        self.horizontalLayout_2.addWidget(self.txtValue)
        self.verticalLayout_2.addWidget(self.fraFilter1)
        self.lstFilter = QtWidgets.QListWidget(self.tabFilters)
        self.lstFilter.setObjectName("lstFilter")
        self.verticalLayout_2.addWidget(self.lstFilter)
        self.fraFilter3 = QtWidgets.QFrame(self.tabFilters)
        self.fraFilter3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraFilter3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraFilter3.setObjectName("fraFilter3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.fraFilter3)
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cmdAdd = QtWidgets.QPushButton(self.fraFilter3)
        self.cmdAdd.setObjectName("cmdAdd")
        self.horizontalLayout_4.addWidget(self.cmdAdd)
        self.cmdDelete = QtWidgets.QPushButton(self.fraFilter3)
        self.cmdDelete.setObjectName("cmdDelete")
        self.horizontalLayout_4.addWidget(self.cmdDelete)
        self.verticalLayout_2.addWidget(self.fraFilter3)
        self.tabWidget.addTab(self.tabFilters, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout_8.addWidget(self.fraTop)
        self.fraOKCancel = QtWidgets.QFrame(self.centralWidget)
        self.fraOKCancel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraOKCancel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraOKCancel.setObjectName("fraOKCancel")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fraOKCancel)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(338, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cmdOK = QtWidgets.QPushButton(self.fraOKCancel)
        self.cmdOK.setObjectName("cmdOK")
        self.horizontalLayout.addWidget(self.cmdOK)
        self.cmdCancel = QtWidgets.QPushButton(self.fraOKCancel)
        self.cmdCancel.setObjectName("cmdCancel")
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.verticalLayout_8.addWidget(self.fraOKCancel)
        frmTable.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmTable)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmTable)

    def retranslateUi(self, frmTable):
        _translate = QtCore.QCoreApplication.translate
        frmTable.setWindowTitle(_translate("frmTable", "EPANET Table Selection"))
        self.lblSelect.setText(_translate("frmTable", "Select the type of table to create:"))
        self.rbnTimeseriesNode.setText(_translate("frmTable", "Time series for node"))
        self.rbnTimeseriesLink.setText(_translate("frmTable", "Time series for link"))
        self.rbnNodes.setText(_translate("frmTable", "Network Nodes at"))
        self.rbnLinks.setText(_translate("frmTable", "Network Links at"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabType), _translate("frmTable", "Type"))
        self.lblSelectColumn.setText(_translate("frmTable", "Select which columns to include in the table:"))
        self.cbxSort.setText(_translate("frmTable", "Sort by"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabColumns), _translate("frmTable", "Columns"))
        self.lblDefine.setText(_translate("frmTable", "Define conditions for selecting table entries: "))
        self.cmdAdd.setText(_translate("frmTable", "Add"))
        self.cmdDelete.setText(_translate("frmTable", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFilters), _translate("frmTable", "Filters"))
        self.cmdOK.setText(_translate("frmTable", "OK"))
        self.cmdCancel.setText(_translate("frmTable", "Cancel"))

