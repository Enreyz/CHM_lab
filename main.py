import sys
import math
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, QHeaderView
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib.pylab as pyl
import numpy as np
import untitled
import RK_methods as rk
import pickle


class MainWindow(QtWidgets.QMainWindow, untitled.Ui_MainWindow):
    def __init__(self):
        global ax
        global axx
        super().__init__()
        self.setupUi(self)

        self.start_value_y1.setDisabled(True)
        self.start_value_y2.setDisabled(True)
        self.param_a.setDisabled(True)

        # инициализация фигуры и тулбара для графика
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        # обработка нажатия кнопок
        self.button_go.clicked.connect(self.AddPlot)
        self.button_clear.clicked.connect(self.ClearPlot)
        self.tabs.activated.connect(self.LoadTab)
        self.comboBox.currentTextChanged.connect(self.switcher)

        # установка графика
        self.verticalLayout_2.addWidget(self.toolbar)
        self.verticalLayout_2.addWidget(self.canvas)
        axx = self.figure.add_subplot(122)
        plot = plt.xlabel(r'$u1$')
        plot = plt.ylabel(r'$u2$')
        plot = plt.title('StreamPlot')
        plot = plt.grid(True)
        plt.tight_layout()
        ax = self.figure.add_subplot(121)
        plot = plt.xlabel(r'$x$')
        plot = plt.ylabel(r'$u$')
        plot = plt.title('Graph')
        plot = plt.grid(True)
        plt.tight_layout()


    def LoadTab(self):
        if (self.tabs.currentText()[0]) == 'm' and (self.tabs.currentText()[2]) != 'a':
            self.label_14.setPixmap(QtGui.QPixmap("render.png"))
            table = self.load_obj("mtable_" + self.tabs.currentText())
            info = self.load_obj("minfo_" + self.tabs.currentText())
            self.tableWidget.setRowCount(0)
            self.tableWidget.setRowCount(len(table['X']))
            self.tableWidget.verticalHeader().hide()
            if self.tableWidget.columnCount() == 13:
                self.tableWidget.removeColumn(12)
                self.tableWidget.removeColumn(11)
            self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("v(i)"))
            self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("v(i) удв."))
            for i in range(len(table['X'])):
                if i == 0:
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(str(i)))
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(str(table['H'][i])))
                    self.tableWidget.setItem(i, 2, QTableWidgetItem(str(table['X'][i])))
                    self.tableWidget.setItem(i, 3, QTableWidgetItem(str(table['Y'][i])))
                else:
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(str(i)))
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(str(table['H'][i])))
                    self.tableWidget.setItem(i, 2, QTableWidgetItem(str(table['X'][i])))
                    self.tableWidget.setItem(i, 3, QTableWidgetItem(str(table['Y'][i])))
                    self.tableWidget.setItem(i, 4, QTableWidgetItem(str(table['W'][i])))
                    self.tableWidget.setItem(i, 5, QTableWidgetItem(str(table['W-V'][i])))
                    self.tableWidget.setItem(i, 6, QTableWidgetItem(str(table['S'][i])))
                    self.tableWidget.setItem(i, 7, QTableWidgetItem(str(table['local'][i]+table['Y'][i])))
                    self.tableWidget.setItem(i, 8, QTableWidgetItem(str(table['W'][i])))
                    self.tableWidget.setItem(i, 9, QTableWidgetItem(str(table['deg_count'][i])))
                    self.tableWidget.setItem(i, 10, QTableWidgetItem(str(table['inc_count'][i])))
                    header = self.tableWidget.horizontalHeader()
                    for i in range(0, 11, 1):
                        header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
            self.label_8.setText("Задача основная №1, вариант №6, метод = РК* (4 порядка)")
            self.label_7.setText(
                "x0 = " + str(table['X'][0]) + ", y0 = " + str(table['Y'][0]) + ", T = " + str(info['x1']) + ", h0 = " + str(table['H'][0]) + ", ε = " + str(info['eps']) + ", ε гр = " + str(info['eps_bord']))
            self.label_9.setText(
                "Nmax = " + str(info['n']) + ", ε min = " + str(info['eps'] / 32) + ", n = " + str(info['n'] - 1) + ", b-xn = " + str(info['x1'] - table['X'][info['n'] - 1]))
            self.label_10.setText("max|S| = " + str(info['max err est']) + " при х = " + str(info['X on max err est']))
            self.label_20.setText("min|S| = " + str(info['min err est']) + " при х = " + str(info['X on min err est']))
            self.label_11.setText("ум. шага = " + str(info['deg']) + ", ув. шага = " + str(info['inc']))
            self.label_12.setText(
                "max h = " + str(max(table['H'])) + " при х = " + str(table['X'][table['H'].index(max(table['H'])) + 1]))
            if table['H'].index(min(table['H'])) == (info['n'] - 1):
                self.label_21.setText(
                    "min h = " + str(min(table['H'])) + " при х = " + str(table['X'][table['H'].index(min(table['H']))]))
            else:
                self.label_21.setText("min h = " + str(min(table['H'])) + " при х = " + str(
                    table['X'][table['H'].index(min(table['H'])) + 1]))
            self.label_13.setText("")
        #####
        elif (self.tabs.currentText()[0]) == 'm' and (self.tabs.currentText()[2]) == 'a':
            self.label_14.setPixmap(QtGui.QPixmap("render3.png"))
            table = self.load_obj("amtable_" + self.tabs.currentText())
            info = self.load_obj("aminfo_" + self.tabs.currentText())
            self.tableWidget.setRowCount(0)
            self.tableWidget.setRowCount(len(table['X']))
            self.tableWidget.verticalHeader().hide()
            if self.tableWidget.columnCount() == 11:
                self.tableWidget.insertColumn(11)
                self.tableWidget.insertColumn(12)
            self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("v(i)1"))
            self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("v(i)1 удв."))
            self.tableWidget.setHorizontalHeaderItem(11, QTableWidgetItem("v(i)2"))
            self.tableWidget.setHorizontalHeaderItem(12, QTableWidgetItem("v(i)2 удв."))
            for i in range(len(table['X'])):
                if i == 0:
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(str(i)))
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(str(table['H'][i])))
                    self.tableWidget.setItem(i, 2, QTableWidgetItem(str(table['X'][i])))
                    self.tableWidget.setItem(i, 3, QTableWidgetItem(str(table['Y1'][i])))
                    self.tableWidget.setItem(i, 11, QTableWidgetItem(str(table['Y2'][i])))
                else:
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(str(i)))
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(str(table['H'][i])))
                    self.tableWidget.setItem(i, 2, QTableWidgetItem(str(table['X'][i])))
                    self.tableWidget.setItem(i, 3, QTableWidgetItem(str(table['Y1'][i])))
                    self.tableWidget.setItem(i, 4, QTableWidgetItem(str(table['W1'][i])))
                    self.tableWidget.setItem(i, 5, QTableWidgetItem(str(table['W-V'][i])))
                    self.tableWidget.setItem(i, 6, QTableWidgetItem(str(table['S'][i])))
                    self.tableWidget.setItem(i, 8, QTableWidgetItem(str(table['W1'][i])))
                    self.tableWidget.setItem(i, 9, QTableWidgetItem(str(table['deg_count'][i])))
                    self.tableWidget.setItem(i, 10, QTableWidgetItem(str(table['inc_count'][i])))
                    self.tableWidget.setItem(i, 11, QTableWidgetItem(str(table['Y2'][i])))
                    self.tableWidget.setItem(i, 12, QTableWidgetItem(str(table['W2'][i])))
                    header = self.tableWidget.horizontalHeader()
                    for i in range(0, 13, 1):
                        header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
            self.label_8.setText("Задача основная №2, вариант №6, метод = РК* (4 порядка)")
            self.label_7.setText(
                "x0 = " + str(table['X'][0]) + ", y0 = " + str(table['Y'][0]) + ", T = " + str(info['x1']) + ", h0 = " + str(table['H'][0]) + ", ε = " + str(info['eps']) + ", ε гр = " + str(info['eps_bord']))
            self.label_9.setText(
                "Nmax = " + str(info['n']) + ", ε min = " + str(info['eps'] / 32) + ", n = " + str(info['n'] - 1) + ", b-xn = " + str(info['x1'] - table['X'][info['n'] - 1]))
            self.label_10.setText("max|S| = " + str(info['max err est']) + " при х = " + str(info['X on max err est']))
            self.label_20.setText("min|S| = " + str(info['min err est']) + " при х = " + str(info['X on min err est']))
            self.label_11.setText("ум. шага = " + str(info['deg']) + ", ув. шага = " + str(info['inc']))
            self.label_12.setText(
                "max h = " + str(max(table['H'])) + " при х = " + str(table['X'][table['H'].index(max(table['H'])) + 1]))
            if table['H'].index(min(table['H'])) == (info['n'] - 1):
                self.label_21.setText(
                    "min h = " + str(min(table['H'])) + " при х = " + str(table['X'][table['H'].index(min(table['H']))]))
            else:
                self.label_21.setText("min h = " + str(min(table['H'])) + " при х = " + str(
                    table['X'][table['H'].index(min(table['H'])) + 1]))
            self.label_13.setText("")
        #####
        elif (self.tabs.currentText()[0]) == 't':
            self.label_14.setPixmap(QtGui.QPixmap("render2.png"))
            table = self.load_obj("ttable_" + self.tabs.currentText())
            info = self.load_obj("tinfo_" + self.tabs.currentText())
            Y_ch=[]
            for i in range(len(table['X'])):
                Y_ch.append(self.check(table['X'][i], table['Y'][0]))
            glob = [0] * (len(table['Y']))
            for i in range(len(table['Y'])):
                glob[i] = abs(Y_ch[i] - table['Y'][i])
            self.tableWidget.setRowCount(0)
            self.tableWidget.setRowCount(len(table['X']))
            self.tableWidget.verticalHeader().hide()
            if self.tableWidget.columnCount() == 11:
                self.tableWidget.insertColumn(11)
                self.tableWidget.insertColumn(12)
            self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("v(i)"))
            self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("v(i) удв."))
            self.tableWidget.setHorizontalHeaderItem(11, QTableWidgetItem("V(i)"))
            self.tableWidget.setHorizontalHeaderItem(12, QTableWidgetItem("V(i) - u(i)"))
            for i in range(len(table['X'])):
                if i == 0:
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(str(i)))
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(str(table['H'][0])))
                    self.tableWidget.setItem(i, 2, QTableWidgetItem(str(table['X'][i])))
                    self.tableWidget.setItem(i, 3, QTableWidgetItem(str(table['Y'][i])))
                    self.tableWidget.setItem(i, 11, QTableWidgetItem(str(Y_ch[i])))
                else:
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(str(i)))
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(str(table['H'][i])))
                    self.tableWidget.setItem(i, 2, QTableWidgetItem(str(table['X'][i])))
                    self.tableWidget.setItem(i, 3, QTableWidgetItem(str(table['Y'][i])))
                    self.tableWidget.setItem(i, 4, QTableWidgetItem(str(table['W'][i])))
                    self.tableWidget.setItem(i, 5, QTableWidgetItem(str(table['W-V'][i])))
                    self.tableWidget.setItem(i, 6, QTableWidgetItem(str(table['S'][i])))
                    self.tableWidget.setItem(i, 7, QTableWidgetItem(str(table['local'][i] + table['Y'][i])))
                    self.tableWidget.setItem(i, 8, QTableWidgetItem(str(table['W'][i])))
                    self.tableWidget.setItem(i, 9, QTableWidgetItem(str(table['deg_count'][i])))
                    self.tableWidget.setItem(i, 10, QTableWidgetItem(str(table['inc_count'][i])))
                    self.tableWidget.setItem(i, 11, QTableWidgetItem(str(Y_ch[i])))
                    self.tableWidget.setItem(i, 12, QTableWidgetItem(str(abs(Y_ch[i] - table['Y'][i]))))
                    header = self.tableWidget.horizontalHeader()
                    for i in range(0, 13, 1):
                        header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
            self.label_8.setText("Задача тестовая, вариант №6, метод = РК* (4 порядка)")
            self.label_7.setText(
                "x0 = " + str(table['X'][0]) + ", y0 = " + str(table['Y'][0]) + ", T = " + str(info['x1']) + ", h0 = " + str(table['H'][0]) + ", ε = " + str(
                    info['eps']) + ", ε гр = " + str(info['eps_bord']))
            self.label_9.setText(
                "Nmax = " + str(info['n']) + ", ε min = " + str(info['eps'] / 32) + ", n = " + str(info['n'] - 1) + ", b-xn = " + str(
                    info['x1'] - table['X'][info['n'] - 1]))
            self.label_10.setText("min|S| = " + str(info['min err est']) + " при х = " + str(info['X on min err est']))
            self.label_20.setText("max|S| = " + str(info['max err est']) + " при х = " + str(info['X on max err est']))
            self.label_11.setText("ум. шага = " + str(info['deg']) + ", ув. шага = " + str(info['inc']))
            self.label_12.setText("max h = " + str(max(table['H'])) + " при х = " + str(
                table['X'][table['H'].index(max(table['H'])) + 1]))
            if table['H'].index(min(table['H'])) == (info['n'] - 1):
                self.label_21.setText("min h = " + str(min(table['H'])) + " при х = " + str(
                    table['X'][table['H'].index(min(table['H']))]))
            else:
                self.label_21.setText("min h = " + str(min(table['H'])) + " при х = " + str(
                    table['X'][table['H'].index(min(table['H'])) + 1]))
            self.label_13.setText(
                "max|ui-vi| = " + str(max(glob)) + " при х = " + str(table['X'][glob.index(max(glob))]))

    def ClearPlot(self): # функция очистки графика
        global ax
        global axx
        ax.clear()
        axx.clear()
        plt.sca(ax)
        plot = plt.xlabel(r'$x$')
        plot = plt.ylabel(r'$u$')
        plot = plt.title('Graph')
        plot = plt.grid(True)
        plt.sca(axx)
        plot = plt.xlabel(r'$u1$')
        plot = plt.ylabel(r'$u2$')
        plot = plt.title('StreamPlot')
        plot = plt.grid(True)
        self.canvas.draw()
        self.tableWidget.setRowCount(0)
        self.tabs.clear()

    def AddPlot(self): # функция добавления графика
        global ax
        global axx
        Y_ch = []  # Значение y для тестовой задачи

        # получение флагов увеличения/уменьшения
        if self.check_not_inc.isChecked():
            check_not_inc = 0
        else:
            check_not_inc = 1

        if self.check_not_deg.isChecked():
            check_not_deg = 0
        else:
            check_not_deg = 1

        # получение параметров диффура
        param_a = np.float64(self.param_a.text())

        # получение начальных условий
        x0 = np.float64(self.start_value_x.text())
        y0 = np.float64(self.start_value_y.text())

        # получение начального шага
        h = np.float64(self.start_step.text())

        # получение точности выхода за границу
        eps_bord = np.float64(self.eps_border.text())

        # получение контроля локальной погрешности
        eps = np.float64(self.control_error.text())

        # получение y10,y20
        y10 = np.float64(self.start_value_y1.text())
        y20 = np.float64(self.start_value_y2.text())

        # получение макс. числа шагов
        n = np.int(self.max_step.text())

        # получение конечного значения отрезка Х
        x1 = np.float64(self.finish_value.text())

        if self.GetItem() == "Основная №1":
            table, info = rk.rk4_v2(self.f1, x0, y0, x1, h, n, eps_bord, check_not_inc, check_not_deg, eps, 1)
            ax.plot(table['X'], table['Y'], '*-', label='x0=' + str(x0) + ', y0 = ' + str(y0) + ", осн. №1")
            ax.legend()
            self.tabs.addItem("m_x0=" + str(x0) + "y0=" + str(y0) + "eps=" + str(eps) + "eps_bord=" + str(eps_bord) + "h=" + str(h) + "n=" + str(n))
            self.save_obj(table, "mtable_m_x0=" + str(x0) + "y0=" + str(y0) + "eps=" + str(eps) + "eps_bord=" + str(eps_bord) + "h=" + str(h) + "n=" + str(n))
            self.save_obj(info, "minfo_m_x0=" + str(x0) + "y0=" + str(y0) + "eps=" + str(eps) + "eps_bord=" + str(eps_bord) + "h=" + str(h) + "n=" + str(n))
            self.tableWidget.setRowCount(0)
            self.tableWidget.setRowCount(len(table['X']))
            self.tableWidget.verticalHeader().hide()
            if self.tableWidget.columnCount() == 13:
                self.tableWidget.removeColumn(12)
                self.tableWidget.removeColumn(11)
            self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("v(i)"))
            self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("v(i) удв."))
            for i in range(len(table['X'])):
                if i == 0:
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(str(i)))
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(str(h)))
                    self.tableWidget.setItem(i, 2, QTableWidgetItem(str(table['X'][i])))
                    self.tableWidget.setItem(i, 3, QTableWidgetItem(str(table['Y'][i])))
                else:
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(str(i)))
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(str(table['H'][i])))
                    self.tableWidget.setItem(i, 2, QTableWidgetItem(str(table['X'][i])))
                    self.tableWidget.setItem(i, 3, QTableWidgetItem(str(table['Y'][i])))
                    self.tableWidget.setItem(i, 4, QTableWidgetItem(str(table['W'][i])))
                    self.tableWidget.setItem(i, 5, QTableWidgetItem(str(table['W-V'][i])))
                    self.tableWidget.setItem(i, 6, QTableWidgetItem(str(table['S'][i])))
                    self.tableWidget.setItem(i, 7, QTableWidgetItem(str(table['local'][i] + table['Y'][i])))
                    self.tableWidget.setItem(i, 8, QTableWidgetItem(str(table['W'][i])))
                    self.tableWidget.setItem(i, 9, QTableWidgetItem(str(table['deg_count'][i])))
                    self.tableWidget.setItem(i, 10, QTableWidgetItem(str(table['inc_count'][i])))
                    header = self.tableWidget.horizontalHeader()
                    for i in range(0, 11, 1):
                        header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
            self.label_8.setText("Задача основная №1, вариант №6, метод = РК* (4 порядка)")
            self.label_7.setText("x0 = " + str(x0) + ", y0 = " + str(y0) + ", T = " + str(x1) + ", h0 = " + str(h) + ", ε = " + str(eps) + ", ε гр = " + str(eps_bord))
            self.label_9.setText("Nmax = " + str(n) + ", ε min = " + str(eps/32) + ", n = " + str(info['n']-1) + ", b-xn = " + str(x1-table['X'][info['n']-1]))
            self.label_10.setText("max|S| = " + str(info['max err est']) + " при х = " + str(info['X on max err est']))
            self.label_20.setText("min|S| = " + str(info['min err est']) + " при х = " + str(info['X on min err est']))
            self.label_11.setText("ум. шага = " + str(info['deg']) + ", ув. шага = " + str(info['inc']))
            self.label_12.setText("max h = " + str(max(table['H'])) + " при х = " + str(table['X'][table['H'].index(max(table['H']))+1]))
            if table['H'].index(min(table['H'])) == (info['n']-1):
                self.label_21.setText("min h = " + str(min(table['H'])) + " при х = " + str(table['X'][table['H'].index(min(table['H']))]))
            else:
                self.label_21.setText("min h = " + str(min(table['H'])) + " при х = " + str(table['X'][table['H'].index(min(table['H']))+1]))
            self.label_13.setText("")
    ######################################
        if self.GetItem() == "Основная №2":
            table, info = rk.rk4_for_system(self.f2, self.f3, x0, y10, y20, x1, h, n, param_a, eps_bord, check_not_inc, check_not_deg, eps)
            ax.plot(table['X'], table['Y1'], '*-', label='(1)a=' + str(param_a) + ', x0=' + str(x0) + ', y0 = ' + str(y10) + ", осн. №2")
            ax.plot(table['X'], table['Y2'], '*-',
                    label='(2)a=' + str(param_a) + ', x0=' + str(x0) + ', y0 = ' + str(y20) + ", осн. №2")
            ax.legend()
            axx.clear()
            plt.sca(axx)
            plot = plt.xlabel(r'$u1$')
            plot = plt.ylabel(r'$u2$')
            plot = plt.title('StreamPlot')
            plot = plt.grid(True)
            dy1 = np.arange(y10 - 1, y10 + 1, 0.5)
            dy2 = np.arange(y20 - 2, y20 + 2, 0.5)
            for i in range(len(dy1)):
                for j in range(len(dy2)):
                    if i==0 and j == 0:
                        table1, info1 = rk.rk4_for_system(self.f2, self.f3, x0, dy1[i], dy2[j], x1, h, n, param_a, eps_bord,
                                                    check_not_inc, check_not_deg, eps)
                        axx.plot(table1['Y1'], table1['Y2'], color="b", label='a=' + str(param_a) + ', x0=' + str(x0) + ', y0 = ' + str(y0) + ", осн. №2")
                    else:
                        table1, info1 = rk.rk4_for_system(self.f2, self.f3, x0, dy1[i], dy2[j], x1, h, n, param_a,
                                                          eps_bord,
                                                          check_not_inc, check_not_deg, eps)
                        axx.plot(table1['Y1'], table1['Y2'], color="b")
            axx.legend()
            self.tabs.addItem("m_a=" + str(param_a) + "x0=" + str(x0) + "y0=" + str(y0) + "eps=" + str(eps) + "eps_bord=" + str(eps_bord) + "h=" + str(h) + "n=" + str(n))
            self.save_obj(table, "amtable_m_a=" + str(param_a) + "x0=" + str(x0) + "y0=" + str(y0) + "eps=" + str(eps) + "eps_bord=" + str(eps_bord) + "h=" + str(h) + "n=" + str(n))
            self.save_obj(info, "aminfo_m_a=" + str(param_a) + "x0=" + str(x0) + "y0=" + str(y0) + "eps=" + str(eps) + "eps_bord=" + str(eps_bord) + "h=" + str(h) + "n=" + str(n))
            self.tableWidget.setRowCount(0)
            self.tableWidget.setRowCount(len(table['X']))
            self.tableWidget.verticalHeader().hide()
            if self.tableWidget.columnCount() == 11:
                self.tableWidget.insertColumn(11)
                self.tableWidget.insertColumn(12)
            self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("v(i)1"))
            self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("v(i)1 удв."))
            self.tableWidget.setHorizontalHeaderItem(11, QTableWidgetItem("v(i)2"))
            self.tableWidget.setHorizontalHeaderItem(12, QTableWidgetItem("v(i)2 удв."))
            for i in range(len(table['X'])):
                if i == 0:
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(str(i)))
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(str(h)))
                    self.tableWidget.setItem(i, 2, QTableWidgetItem(str(table['X'][i])))
                    self.tableWidget.setItem(i, 3, QTableWidgetItem(str(table['Y1'][i])))
                    self.tableWidget.setItem(i, 11, QTableWidgetItem(str(table['Y2'][i])))
                else:
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(str(i)))
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(str(table['H'][i])))
                    self.tableWidget.setItem(i, 2, QTableWidgetItem(str(table['X'][i])))
                    self.tableWidget.setItem(i, 3, QTableWidgetItem(str(table['Y1'][i])))
                    self.tableWidget.setItem(i, 4, QTableWidgetItem(str(table['W1'][i])))
                    self.tableWidget.setItem(i, 5, QTableWidgetItem(str(table['W-V'][i])))
                    self.tableWidget.setItem(i, 6, QTableWidgetItem(str(table['S'][i])))
                    self.tableWidget.setItem(i, 8, QTableWidgetItem(str(table['W1'][i])))
                    self.tableWidget.setItem(i, 9, QTableWidgetItem(str(table['deg_count'][i])))
                    self.tableWidget.setItem(i, 10, QTableWidgetItem(str(table['inc_count'][i])))
                    self.tableWidget.setItem(i, 11, QTableWidgetItem(str(table['Y2'][i])))
                    self.tableWidget.setItem(i, 12, QTableWidgetItem(str(table['W2'][i])))
                    header = self.tableWidget.horizontalHeader()
                    for i in range(0, 13, 1):
                        header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
            self.label_8.setText("Задача основная №2, вариант №6, метод = РК* (4 порядка)")
            self.label_7.setText("x0 = " + str(x0) + ", y10 = " + str(y10) + ", y20=" + str(y20) + ", T = " + str(x1) + ", h0 = " + str(h) + ", ε = " + str(eps) + ", ε гр = " + str(eps_bord))
            self.label_9.setText("Nmax = " + str(n) + ", ε min = " + str(eps/32) + ", n = " + str(info['n']-1) + ", b-xn = " + str(x1-table['X'][info['n']-1]))
            self.label_10.setText("max|S| = " + str(info['max err est']) + " при х = " + str(info['X on max err est']))
            self.label_20.setText("min|S| = " + str(info['min err est']) + " при х = " + str(info['X on min err est']))
            self.label_11.setText("ум. шага = " + str(info['deg']) + ", ув. шага = " + str(info['inc']))
            self.label_12.setText("max h = " + str(max(table['H'])) + " при х = " + str(table['X'][table['H'].index(max(table['H']))+1]))
            if table['H'].index(min(table['H'])) == (info['n']-1):
                self.label_21.setText("min h = " + str(min(table['H'])) + " при х = " + str(table['X'][table['H'].index(min(table['H']))]))
            else:
                self.label_21.setText("min h = " + str(min(table['H'])) + " при х = " + str(table['X'][table['H'].index(min(table['H']))+1]))
            self.label_13.setText("")
    ##################################################
        elif self.GetItem() == "Тестовая":
            table, info = rk.rk4_v2(self.f, x0, y0, x1, h, n, eps_bord, check_not_inc, check_not_deg, eps, 1)

            for i in range(len(table['X'])):
                Y_ch.append(self.check(table['X'][i], y0))

            glob = [0] * (len(table['Y']))

            for i in range(len(table['Y'])):
                glob[i] = abs(Y_ch[i] - table['Y'][i])

            self.ClearPlot
            xx = np.arange(x0, x1, 0.001)
            yy = [0]*(len(xx))
            for i in range(len(xx)):
                yy[i] = self.check(xx[i], y0)
            ax.plot(xx, yy, '--', label='x0=' + str(x0) + ', y0 = ' + str(y0) + ", тест.")
            ax.plot(table['X'], table['Y'], '*-', label='x0=' + str(x0) + ', y0 = ' + str(y0) + ", осн.")
            ax.legend()
            self.tabs.addItem(
                "t_x0=" + str(x0) + "y0=" + str(y0) + "eps=" + str(
                    eps) + "eps_bord=" + str(eps_bord) + "h=" + str(h) + "n=" + str(n))
            self.save_obj(table, "ttable_t_x0=" + str(x0) + "y0=" + str(
                y0) + "eps=" + str(eps) + "eps_bord=" + str(eps_bord) + "h=" + str(h) + "n=" + str(n))
            self.save_obj(info, "tinfo_t_x0=" + str(x0) + "y0=" + str(
                y0) + "eps=" + str(eps) + "eps_bord=" + str(eps_bord) + "h=" + str(h) + "n=" + str(n))
            self.tableWidget.setRowCount(0)
            self.tableWidget.setRowCount(len(table['X']))
            self.tableWidget.verticalHeader().hide()
            if self.tableWidget.columnCount() == 11:
                self.tableWidget.insertColumn(11)
                self.tableWidget.insertColumn(12)
            self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("v(i)"))
            self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("v(i) удв."))
            self.tableWidget.setHorizontalHeaderItem(11, QTableWidgetItem("V(i)"))
            self.tableWidget.setHorizontalHeaderItem(12, QTableWidgetItem("V(i) - u(i)"))
            for i in range(len(table['X'])):
                if i == 0:
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(str(i)))
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(str(h)))
                    self.tableWidget.setItem(i, 2, QTableWidgetItem(str(table['X'][i])))
                    self.tableWidget.setItem(i, 3, QTableWidgetItem(str(table['Y'][i])))
                    self.tableWidget.setItem(i, 11, QTableWidgetItem(str(Y_ch[i])))
                else:
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(str(i)))
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(str(table['H'][i])))
                    self.tableWidget.setItem(i, 2, QTableWidgetItem(str(table['X'][i])))
                    self.tableWidget.setItem(i, 3, QTableWidgetItem(str(table['Y'][i])))
                    self.tableWidget.setItem(i, 4, QTableWidgetItem(str(table['W'][i])))
                    self.tableWidget.setItem(i, 5, QTableWidgetItem(str(table['W-V'][i])))
                    self.tableWidget.setItem(i, 6, QTableWidgetItem(str(table['S'][i])))
                    self.tableWidget.setItem(i, 7, QTableWidgetItem(str(table['local'][i] + table['Y'][i])))
                    self.tableWidget.setItem(i, 8, QTableWidgetItem(str(table['W'][i])))
                    self.tableWidget.setItem(i, 9, QTableWidgetItem(str(table['deg_count'][i])))
                    self.tableWidget.setItem(i, 10, QTableWidgetItem(str(table['inc_count'][i])))
                    self.tableWidget.setItem(i, 11, QTableWidgetItem(str(Y_ch[i])))
                    self.tableWidget.setItem(i, 12, QTableWidgetItem(str(abs(Y_ch[i] - table['Y'][i]))))
                    header = self.tableWidget.horizontalHeader()
                    for i in range(0, 13, 1):
                        header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
            self.label_8.setText("Задача тестовая, вариант №6, метод = РК* (4 порядка)")
            self.label_7.setText(
                "x0 = " + str(x0) + ", y0 = " + str(y0) + ", T = " + str(x1) + ", h0 = " + str(h) + ", ε = " + str(
                    eps) + ", ε гр = " + str(eps_bord))
            self.label_9.setText(
                "Nmax = " + str(n) + ", ε min = " + str(eps / 32) + ", n = " + str(info['n'] - 1) + ", b-xn = " + str(
                    x1 - table['X'][info['n'] - 1]))
            self.label_10.setText("max|S| = " + str(info['min err est']) + " при х = " + str(info['X on min err est']))
            self.label_20.setText("min|S| = " + str(info['max err est']) + " при х = " + str(info['X on max err est']))
            self.label_11.setText("ум. шага = " + str(info['deg']) + ", ув. шага = " + str(info['inc']))
            self.label_12.setText("max h = " + str(max(table['H'])) + " при х = " + str(
                table['X'][table['H'].index(max(table['H'])) + 1]))
            if table['H'].index(min(table['H'])) == (info['n'] - 1):
                self.label_21.setText("min h = " + str(min(table['H'])) + " при х = " + str(
                    table['X'][table['H'].index(min(table['H']))]))
            else:
                self.label_21.setText("min h = " + str(min(table['H'])) + " при х = " + str(
                    table['X'][table['H'].index(min(table['H'])) + 1]))
            self.label_13.setText("max|ui-vi| = " + str(max(glob)) + " при х = " + str(table['X'][glob.index(max(glob))]))
        self.canvas.draw()

    def GetItem(self): # функция получения информации из ComboBox
        item = self.comboBox.currentText()
        return item

    def GetTab(self): # функция получения информации из tabs
        item = self.tabs.currentText()
        return item

    def f(self, x, y, param_a):  # Правая часть диффура
        return 3 * y

    def f1(self, x, y, param_a):  # Правая часть диффура
        return (1/(2*x+x**2))*(y**2)+y-(y**3)*math.sin(10*x)

    def check(self, x, y0):  # Точное решение
        res = y0 * math.exp(3 * x)
        return res

    def save_obj(self, obj, name):
        with open('obj/' + name + '.pkl', 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

    def load_obj(self, name):
        with open('obj/' + name + '.pkl', 'rb') as f:
            return pickle.load(f)

    def switcher(self, value):
        if value == "Основная №1":
            self.label_14.setPixmap(QtGui.QPixmap("render2.png"))
            self.start_value_y.setEnabled(True)
            self.start_value_y1.setDisabled(True)
            self.start_value_y2.setDisabled(True)
            self.param_a.setDisabled(True)
        elif value == "Тестовая":
            self.label_14.setPixmap(QtGui.QPixmap("render.png"))
            self.start_value_y.setEnabled(True)
            self.start_value_y1.setDisabled(True)
            self.start_value_y2.setDisabled(True)
            self.param_a.setDisabled(True)
        elif value == "Основная №2":
            self.label_14.setPixmap(QtGui.QPixmap("render3.png"))
            self.start_value_y.setDisabled(True)
            self.start_value_y1.setEnabled(True)
            self.start_value_y2.setEnabled(True)
            self.param_a.setEnabled(True)

    def f2(self, x, y1, y2, param_a):
        return y2

    def f3(self, x, y1, y2, param_a):
        return -param_a * math.sqrt(y2 ** 2 + 1)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main = MainWindow()
    main.show()

    sys.exit(app.exec_())