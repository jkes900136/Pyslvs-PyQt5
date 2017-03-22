# -*- coding: utf-8 -*-
from ..QtModules import *
from .Ui_run_Triangle_Solver import Ui_Form as Triangle_Solver_Form
from .run_Triangle_Solver_edit import Triangle_Solver_edit_show
from ..io.undoRedo import (TSinitCommand, TSeditCommand, TSdeleteCommand)
from ..kernel.pyslvs_triangle_solver.TS import solver

class Triangle_Solver_show(QWidget, Triangle_Solver_Form):
    startMerge = pyqtSignal()
    def __init__(self, FileState, Point, Directions=list(), parent=None):
        super(Triangle_Solver_show, self).__init__(parent)
        self.setupUi(self)
        self.answers = list()
        self.Point = Point
        self.FileState = FileState
        self.ReloadTable(Directions)
    
    def ReloadTable(self, Directions):
        self.directions = Directions
        for condition in self.directions:
            row = self.directionsTable.rowCount()
            self.directionsTable.insertRow(row)
            self.directionsTable.setItem(row, 0, QTableWidgetItem(condition['Type']))
            e = condition['p1']
            p1Item = QTableWidgetItem('Result{}'.format(e) if type(e)==int else str(e))
            if type(e)==tuple: p1Item.setToolTip("x = {}\ny = {}".format(e[0], e[1]))
            self.directionsTable.setItem(row, 2, p1Item)
            e = condition['p2']
            p2Item = QTableWidgetItem('Result{}'.format(e) if type(e)==int else str(e))
            if type(e)==tuple: p1Item.setToolTip("x = {}\ny = {}".format(e[0], e[1]))
            self.directionsTable.setItem(row, 3, p2Item)
            condition = {k:v for k, v in condition.items() if k!='Type'}
            conditionItem = QTableWidgetItem(str(condition))
            conditionItem.setToolTip('\n'.join(["{}: {}".format(k, v) for k, v in condition.items()]))
            self.directionsTable.setItem(row, 4, conditionItem)
    
    def editDirection(self, name, edit=False):
        if edit is False: dlg = Triangle_Solver_edit_show(self.Point, self.directionsTable.rowCount(), name)
        else: dlg = Triangle_Solver_edit_show(self.Point, edit, **self.directions[edit])
        dlg.show()
        if dlg.exec_():
            direction = dlg.condition
            self.FileState.beginMacro("{} {{TS Direction}}".format('Add' if edit is False else 'Edit'))
            self.FileState.push(TSeditCommand(self.directions, self.directionsTable, direction, edit))
            self.FileState.endMacro()
    
    @pyqtSlot()
    def on_pluse_PLAP_clicked(self): self.editDirection('PLAP')
    @pyqtSlot()
    def on_pluse_PLLP_clicked(self): self.editDirection('PLLP')
    @pyqtSlot()
    def on_pluse_PLPP_clicked(self): self.editDirection('PLPP')
    
    @pyqtSlot(int, int)
    def on_directionsTable_cellDoubleClicked(self, row, column):
        if row>-1: self.editDirection(self.directions[row]['Type'], row)
    
    @pyqtSlot()
    def on_remove_botton_clicked(self):
        n = self.directionsTable.rowCount()
        if n>0:
            self.FileState.beginMacro("Delete {TS Direction}")
            self.FileState.push(TSdeleteCommand(self.directions, self.directionsTable))
            self.FileState.endMacro()
    
    @pyqtSlot()
    def on_clear_botton_clicked(self):
        for i in range(self.directionsTable.rowCount()): self.on_remove_botton_clicked()
    
    @pyqtSlot(QTableWidgetItem)
    def on_directionsTable_itemChanged(self, item):
        self.Solve.setEnabled(len(self.directions)>0)
        self.Merge.setEnabled(len(self.answers)>0)
    
    @pyqtSlot()
    def on_Solve_clicked(self):
        if self.directions:
            directions = [{k:v for k, v in e.items() if k!='Type'} for e in self.directions]
            directions = [{k:(v if type(v)!=str else
                (self.Point[int(v.replace('Point', ''))]['x'], self.Point[int(v.replace('Point', ''))]['y']))
                for k, v in e.items()} for e in directions]
            s = solver(directions)
            self.answers = s.answer()
            for e in self.answers:
                result = QTableWidgetItem("({:.02f}, {:.02f})".format(e[0], e[1]))
                result.setToolTip("x = {}\ny = {}".format(e[0], e[1]))
                self.directionsTable.setItem(self.answers.index(e), 1, result)
    
    @pyqtSlot()
    def on_Merge_clicked(self): self.startMerge.emit()
