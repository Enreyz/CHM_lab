# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1766, 954)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(260, 10, 592, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 0, 5, 5)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.eps_border = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.eps_border.setObjectName("eps_border")
        self.gridLayout.addWidget(self.eps_border, 1, 1, 1, 1)
        self.start_value_x = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.start_value_x.setObjectName("start_value_x")
        self.gridLayout.addWidget(self.start_value_x, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.start_step = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.start_step.setObjectName("start_step")
        self.gridLayout.addWidget(self.start_step, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.control_error = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.control_error.setObjectName("control_error")
        self.gridLayout.addWidget(self.control_error, 3, 1, 1, 1)
        self.start_value_y = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.start_value_y.setObjectName("start_value_y")
        self.gridLayout.addWidget(self.start_value_y, 5, 0, 1, 1)
        self.max_step = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.max_step.setObjectName("max_step")
        self.gridLayout.addWidget(self.max_step, 3, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 4, 0, 1, 1)
        self.check_not_inc = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_not_inc.setObjectName("check_not_inc")
        self.gridLayout.addWidget(self.check_not_inc, 4, 1, 1, 1)
        self.check_not_deg = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_not_deg.setObjectName("check_not_deg")
        self.gridLayout.addWidget(self.check_not_deg, 4, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 6, 0, 1, 1)
        self.finish_value = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.finish_value.setObjectName("finish_value")
        self.gridLayout.addWidget(self.finish_value, 7, 0, 1, 1)
        self.button_clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_clear.setObjectName("button_clear")
        self.gridLayout.addWidget(self.button_clear, 7, 2, 1, 1)
        self.button_go = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_go.setObjectName("button_go")
        self.gridLayout.addWidget(self.button_go, 7, 1, 1, 1)
        self.start_value_y1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.start_value_y1.setObjectName("start_value_y1")
        self.gridLayout.addWidget(self.start_value_y1, 6, 1, 1, 1)
        self.start_value_y2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.start_value_y2.setObjectName("start_value_y2")
        self.gridLayout.addWidget(self.start_value_y2, 6, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 5, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 5, 2, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(860, 10, 461, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 0, 0, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.verticalLayout.addWidget(self.label_20)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.verticalLayout.addWidget(self.label_21)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 310, 511, 581))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(70)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(38)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(10)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(580, 310, 1171, 581))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget_2)
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 241, 191))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(5, 0, 5, 5)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 3, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("render.png"))
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 1, 0, 1, 1)
        self.param_a = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.param_a.setObjectName("param_a")
        self.gridLayout_2.addWidget(self.param_a, 4, 0, 1, 1)
        self.tabs = QtWidgets.QComboBox(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(10, 270, 511, 22))
        self.tabs.setObjectName("tabs")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1766, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Контроль лок. погрешности(ε):"))
        self.eps_border.setText(_translate("MainWindow", "0.000001"))
        self.start_value_x.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "Задача:"))
        self.label_6.setText(_translate("MainWindow", "Начальный шаг (h0):"))
        self.start_step.setText(_translate("MainWindow", "0.01"))
        self.label_5.setText(_translate("MainWindow", "Макс. число шагов(n):"))
        self.label_2.setText(_translate("MainWindow", "Начальное значение Х(х0):"))
        self.control_error.setText(_translate("MainWindow", "0.00001"))
        self.start_value_y.setText(_translate("MainWindow", "10"))
        self.max_step.setText(_translate("MainWindow", "10000"))
        self.start_value_y1.setText(_translate("MainWindow", "1"))
        self.start_value_y2.setText(_translate("MainWindow", "1"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Тестовая"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Основная №1"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Основная №2"))
        self.label_3.setText(_translate("MainWindow", "Точность выхода на границу(ε гр):"))
        self.label_18.setText(_translate("MainWindow", "Начальное значение Y(у0):"))
        self.check_not_inc.setText(_translate("MainWindow", "Не увеличивать шаг"))
        self.check_not_deg.setText(_translate("MainWindow", "Не уменьшать шаг"))
        self.label_19.setText(_translate("MainWindow", "x∈[х0;T], где T:"))
        self.finish_value.setText(_translate("MainWindow", "1"))
        self.button_clear.setText(_translate("MainWindow", "Очистить график и таблицу"))
        self.button_go.setText(_translate("MainWindow", "Вычислить"))
        self.label_17.setText(_translate("MainWindow", "Начальное значение Y(y10):"))
        self.label_22.setText(_translate("MainWindow", "Начальное значение Y(y20):"))
        self.label_8.setText(_translate("MainWindow", "№ и тип задачи, № варианта, метод"))
        self.label_7.setText(_translate("MainWindow", "х0, у0, Т, h0, ε, ε гр"))
        self.label_9.setText(_translate("MainWindow", "Nmax, ε min, n, b-xn"))
        self.label_10.setText(_translate("MainWindow", "max|S| при x"))
        self.label_20.setText(_translate("MainWindow", "min|S| при х"))
        self.label_11.setText(_translate("MainWindow", "ум. шага, ув. шага"))
        self.label_12.setText(_translate("MainWindow", "max h при x"))
        self.label_21.setText(_translate("MainWindow", "min x при х"))
        self.label_13.setText(_translate("MainWindow", "Для тестовых: max|ui-vi| при х"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "i"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "h(i-1)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "x(i)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "v(i)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "v(i) удв."))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "v(i) - v(i) удв."))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "S"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "v(i) уточ."))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "v(i) итог."))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Ум. шага"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Ув. шага"))
        self.label_16.setText(_translate("MainWindow", "Параметр а:"))
        self.label_15.setText(_translate("MainWindow", "Задача Коши:"))
        self.param_a.setText(_translate("MainWindow", "1"))

