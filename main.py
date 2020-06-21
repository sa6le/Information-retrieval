# ------------------------------------------------------
# ---------------------- main.py -----------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import numpy as np
import random
import matplotlib.pyplot as plt
N = 12
alfa1 = N/(N+10)
alfa2 = alfa1/2
alfa4 = -alfa1
A = 4+N
i = [x for x in range(1,A+1)]
j = [x for x in range(1,A+1)]
n = [x for x in range(0,A)]
l1 = list(range(1, 16)) + [15]
print(l1)

class MatplotlibWidget(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)


        loadUi("qt_designer.ui", self)

        self.setWindowTitle("l")

        self.pushButton_1.clicked.connect(self.update_graph)

        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))
        self.addToolBar(NavigationToolbar(self.MplWidget_2.canvas, self))

        self.comboBox.addItem("Распредленеие вероятностей P1")
        self.comboBox.addItem("Распредленеие вероятностей P2")
        self.comboBox.addItem("Распредленеие вероятностей P3")
        self.comboBox.addItem("Распредленеие вероятностей P4")

        self.comboBox.currentIndexChanged.connect(lambda i: i == 0 and self.update_graph())
        self.comboBox.currentIndexChanged.connect(lambda i: i == 1 and self.update_graph_2())
        self.comboBox.currentIndexChanged.connect(lambda i: i == 2 and self.update_graph_3())
        self.comboBox.currentIndexChanged.connect(lambda i: i == 3 and self.update_graph_4())





    def update_graph(self):
        rasp_ver_P1 = {}
        Sum1 = [np.exp((-alfa1 * k)) for k in range(1, A + 1)]
        P1 = np.exp(-alfa1 * np.array(i)) / (np.sum(Sum1))
        SumR1 = [(l1[i] * P1[i]) for i in range(0, A)]
        Rnumpy = np.round(np.sum(SumR1),3)
        Rfloat = float(Rnumpy)
        R1 = str(Rfloat)
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.bar(i,P1)
        self.MplWidget.canvas.axes.set_title('Распределение вероятностей P1')
        self.MplWidget.canvas.axes.set_ylim([0, 0.45])
        self.MplWidget.canvas.axes.grid()
        self.MplWidget.canvas.draw()
        self.lineEdit.setText("R1 = " + R1)

        for x in i:
            rasp_ver_P1[x] = np.round(P1[x - 1], 3)
        print("P1 = ",rasp_ver_P1, end='\n')

        P_Bayes = [[0 for j in range(0, A + 1)] for i in range(0, A + 1)]
        for c in range(1, A + 1):
            P_Bayes[0][c] = P1[c - 1]
            for d in range(1, A):
                sum = [P_Bayes[d - 1][k] for k in range(1, d + 1)]
                Py = 1 - np.sum(sum)
                for f in range(1, A + 1):
                    if f <= d:
                        P_Bayes[d][f] = 0
                    else:
                        P_Bayes[d][f] = (P_Bayes[d - 1][f]) / Py
        print(P_Bayes)
        Gn1 = [0 for q in range(0, len(n))]
        for l in n:
            q = [(-P_Bayes[l][i]) * np.log2(P_Bayes[l][i]) for i in range(l + 1, A + 1)]
            Gn1[l] = np.sum(q)
        print("Условные априорные энтропии", np.round(Gn1, 3))

        lj = list(P1)
        ans = []
        for j, e in enumerate(lj):
            acc = 1 - np.sum(lj[:j])
            ans.append(round(acc, 3))
        Hn1 = np.multiply(ans, Gn1)
        print('Значения КСН для последовательного поиска ', np.round(Hn1, 3))
        self.MplWidget_2.canvas.axes.clear()
        self.MplWidget_2.canvas.axes.plot(i, Hn1)
        self.MplWidget_2.canvas.axes.plot(i, Gn1, linestyle = '--')
        self.MplWidget_2.canvas.axes.legend(('H1', 'G1'), loc='upper right')
        self.MplWidget_2.canvas.axes.set_title('КСН H1 и УАЭ G1')
        self.MplWidget_2.canvas.axes.set_ylim([0, 2.5])
        self.MplWidget_2.canvas.axes.set_xlim([0, 16])
        self.MplWidget_2.canvas.axes.grid()
        self.MplWidget_2.canvas.draw()


    def update_graph_2(self):
        rasp_ver_P2 = {}
        Sum2 = [np.exp((-alfa2 * k)) for k in range(1, A + 1)]
        P2 = np.exp(-alfa2 * np.array(i)) / (np.sum(Sum2))
        SumR2 = [(l1[i] * P2[i]) for i in range(0, A)]
        Rnumpy2 = np.round(np.sum(SumR2),3)
        Rfloat2 = float(Rnumpy2)
        R2 = str(Rfloat2)
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.bar(i,P2)
        self.MplWidget.canvas.axes.set_title('Распределение вероятностей P2')
        self.MplWidget.canvas.axes.grid()
        self.MplWidget.canvas.draw()
        self.lineEdit.setText("R2 = " + R2)

        for x in i:
            rasp_ver_P2[x] = np.round(P2[x - 1], 3)
        print("P2 = ",rasp_ver_P2, end='\n')

        P_Bayes = [[0 for j in range(0, A + 1)] for i in range(0, A + 1)]
        for c in range(1, A + 1):
            P_Bayes[0][c] = P2[c - 1]
            for d in range(1, A):
                sum = [P_Bayes[d - 1][k] for k in range(1, d + 1)]
                Py = 1 - np.sum(sum)
                for f in range(1, A + 1):
                    if f <= d:
                        P_Bayes[d][f] = 0
                    else:
                        P_Bayes[d][f] = (P_Bayes[d - 1][f]) / Py
        print(P_Bayes)
        Gn2 = [0 for q in range(0, len(n))]
        for l in n:
            q = [(-P_Bayes[l][i]) * np.log2(P_Bayes[l][i]) for i in range(l + 1, A + 1)]
            Gn2[l] = np.sum(q)
        print("Условные априорные энтропии", np.round(Gn2, 3))

        lj = list(P2)
        ans = []
        for j, e in enumerate(lj):
            acc = 1 - np.sum(lj[:j])
            ans.append(round(acc, 3))
        Hn2 = np.multiply(ans, Gn2)
        print('Значения КСН для последовательного поиска ', np.round(Hn2, 3))
        self.MplWidget_2.canvas.axes.clear()
        self.MplWidget_2.canvas.axes.plot(i,Hn2)
        self.MplWidget_2.canvas.axes.plot(i, Gn2, linestyle = '--')
        self.MplWidget_2.canvas.axes.legend(('H2', 'G2'), loc='upper right')
        self.MplWidget_2.canvas.axes.set_title('КСН H2 и УАЭ G2')
        self.MplWidget_2.canvas.axes.set_xlim([0, 16])
        self.MplWidget_2.canvas.axes.set_ylim([0, 3.5])
        self.MplWidget_2.canvas.axes.grid()
        self.MplWidget_2.canvas.draw()

    def update_graph_3(self):
        rasp_ver_P3 = {}
        P3 = [np.around(1/A,4)  for k in range(1,A+1)]
        SumR3 = [(l1[i] * P3[i]) for i in range(0, A)]
        Rnumpy3 = np.round(np.sum(SumR3),3)
        Rfloat3 = float(Rnumpy3)
        R3= str(Rfloat3)
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.bar(i,P3)
        self.MplWidget.canvas.axes.set_title('Распределение вероятностей P3')
        self.MplWidget.canvas.axes.set_ylim([0, 0.07])
        self.MplWidget.canvas.axes.grid()
        self.MplWidget.canvas.draw()
        self.lineEdit.setText("R3 = " + R3)
        for x in i:
            rasp_ver_P3[x] = np.round(P3[x - 1], 3)
        print("P3 = ",rasp_ver_P3, end='\n')
        P_Bayes = [[0 for j in range(0, A + 1)] for i in range(0, A + 1)]
        for c in range(1, A + 1):
            P_Bayes[0][c] = P3[c - 1]
            for d in range(1, A):
                sum = [P_Bayes[d - 1][k] for k in range(1, d + 1)]
                Py = 1 - np.sum(sum)
                for f in range(1, A + 1):
                    if f <= d:
                        P_Bayes[d][f] = 0
                    else:
                        P_Bayes[d][f] = (P_Bayes[d - 1][f]) / Py
        print(P_Bayes)
        Gn3 = [0 for q in range(0, len(n))]
        for l in n:
            q = [(-P_Bayes[l][i]) * np.log2(P_Bayes[l][i]) for i in range(l + 1, A + 1)]
            Gn3[l] = np.sum(q)
        print("Условные априорные энтропии", np.round(Gn3, 3))

        lj = list(P3)
        ans = []
        for j, e in enumerate(lj):
            acc = 1 - np.sum(lj[:j])
            ans.append(round(acc, 3))
        Hn3 = np.multiply(ans, Gn3)
        print('Значения КСН для последовательного поиска ', np.round(Hn3, 3))
        self.MplWidget_2.canvas.axes.clear()
        self.MplWidget_2.canvas.axes.plot(i, Hn3)
        self.MplWidget_2.canvas.axes.plot(i, Gn3, linestyle = '--')
        self.MplWidget_2.canvas.axes.legend(('H3', 'G3'), loc='upper right')
        self.MplWidget_2.canvas.axes.set_title('КСН H3 и УАЭ G3')
        self.MplWidget_2.canvas.axes.set_ylim([0, 4])
        self.MplWidget_2.canvas.axes.set_xlim([0, 16])
        self.MplWidget_2.canvas.axes.grid()
        self.MplWidget_2.canvas.draw()

    def update_graph_4(self):
        rasp_ver_P4 = {}
        Sum4 = [np.exp((-alfa4 * k)) for k in range(1, A + 1)]
        P4 = np.exp(-alfa4 * np.array(i)) / (np.sum(Sum4))
        SumR4 = [(l1[i] * P4[i]) for i in range(0, A)]
        Rnumpy4 = np.round(np.sum(SumR4), 3)
        Rfloat4 = float(Rnumpy4)
        R4 = str(Rfloat4)
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.bar(i,P4)
        self.MplWidget.canvas.axes.set_title('Распределение вероятностей P4')
        self.MplWidget.canvas.axes.set_ylim([0, 0.5])
        self.MplWidget.canvas.axes.grid()
        self.MplWidget.canvas.draw()
        self.lineEdit.setText("R4 = " + R4)
        for x in i:
            rasp_ver_P4[x] = np.round(P4[x - 1], 3)
        print("P4 = ",rasp_ver_P4, end='\n')

        P_Bayes = [[0 for j in range(0, A + 1)] for i in range(0, A + 1)]
        for c in range(1, A + 1):
            P_Bayes[0][c] = P4[c - 1]
            for d in range(1, A):
                sum = [P_Bayes[d - 1][k] for k in range(1, d + 1)]
                Py = 1 - np.sum(sum)
                for f in range(1, A + 1):
                    if f <= d:
                        P_Bayes[d][f] = 0
                    else:
                        P_Bayes[d][f] = (P_Bayes[d - 1][f]) / Py
        print(P_Bayes)
        Gn4 = [0 for q in range(0, len(n))]
        for l in n:
            q = [(-P_Bayes[l][i]) * np.log2(P_Bayes[l][i]) for i in range(l + 1, A + 1)]
            Gn4[l] = np.sum(q)
        print("Условные априорные энтропии", np.round(Gn4, 3))

        lj = list(P4)
        ans = []
        for j, e in enumerate(lj):
            acc = 1 - np.sum(lj[:j])
            ans.append(round(acc, 3))
        Hn4 = np.multiply(ans, Gn4)
        print('Значения КСН для последовательного поиска ', np.round(Hn4, 3))
        self.MplWidget_2.canvas.axes.clear()
        self.MplWidget_2.canvas.axes.plot(i, Hn4)
        self.MplWidget_2.canvas.axes.set_title('КСН H4')
        self.MplWidget_2.canvas.axes.plot(i, Gn4, linestyle = '--')
        self.MplWidget_2.canvas.axes.legend(('H4', 'G4'), loc='upper right')
        self.MplWidget_2.canvas.axes.set_title('КСН H4 и УАЭ G4')
        self.MplWidget_2.canvas.axes.set_ylim([0, 2.5])
        self.MplWidget_2.canvas.axes.set_xlim([0, 16])
        self.MplWidget_2.canvas.axes.grid()
        self.MplWidget_2.canvas.draw()

app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()