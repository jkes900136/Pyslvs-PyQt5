# -*- coding: utf-8 -*-
##Pyslvs - Open Source Planar Linkage Mechanism Simulation and Dimensional Synthesis System.
##Copyright (C) 2016-2018 Yuan Chang
##E-mail: pyslvs@gmail.com
##
##This program is free software; you can redistribute it and/or modify
##it under the terms of the GNU Affero General Public License as published by
##the Free Software Foundation; either version 3 of the License, or
##(at your option) any later version.
##
##This program is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU Affero General Public License for more details.
##
##You should have received a copy of the GNU Affero General Public License
##along with this program; if not, write to the Free Software
##Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

from core.QtModules import *
from .Ui_preview import Ui_Dialog
from core.graphics import BaseCanvas, colorQt
from core.io import get_from_parenthesis
from math import isnan
from typing import Tuple

class DynamicCanvas(BaseCanvas):
    def __init__(self, mechanism, Path, parent=None):
        super(DynamicCanvas, self).__init__(parent)
        self.mechanism = mechanism
        self.Path.path = Path
        self.slvsPath = self.mechanism['Target']
        self.index = 0
        #exp_symbol = ('A', 'B', 'C', 'D', 'E')
        self.exp_symbol = []
        self.links = []
        for exp in self.mechanism['Link_Expression'].split(';'):
            tags = get_from_parenthesis(exp, '[', ']').split(',')
            self.links.append(tags)
            for name in tags:
                if name not in self.exp_symbol:
                    self.exp_symbol.append(name)
        self.exp_symbol = sorted(self.exp_symbol)
        #Timer start.
        timer = QTimer(self)
        timer.setInterval(10)
        timer.timeout.connect(self.change_index)
        timer.start()
    
    def Comparator(self, fun, i):
        real_point = []
        for point in self.Path.path:
            if point:
                r = [path[i] for path in point if not isnan(path[i])]
                if r:
                    real_point.append(fun(r))
        fixed_point = fun(
            fun(self.mechanism[name][i] for name in self.mechanism['Driver']),
            fun(self.mechanism[name][i] for name in self.mechanism['Follower'])
        )
        if real_point:
            return fun(fun(real_point), fixed_point)
        else:
            return fixed_point
    
    def paintEvent(self, event):
        width = self.width()
        height = self.height()
        maxX = self.Comparator(max, 0)
        minX = self.Comparator(min, 0)
        maxY = self.Comparator(max, 1)
        minY = self.Comparator(min, 1)
        diffX = maxX - minX
        diffY = maxY - minY
        diff = diffX/diffY > width/height
        self.zoom = (width if diff else height)/(diffX if diff else diffY)*0.95
        self.ox = width/2 - (minX + maxX)/2*self.zoom
        self.oy = height/2 + (minY + maxY)/2*self.zoom
        super(DynamicCanvas, self).paintEvent(event)
        #Points that in the current angle section.
        self.Point = (self.mechanism['A'], self.mechanism['B']) + tuple(
            (c[self.index][0], c[self.index][1])
            if not isnan(c[self.index][0]) else False for c in self.Path.path[2:]
        )
        if False in self.Point:
            self.index += 1
            return
        #Draw links.
        for i, exp in enumerate(self.links):
            if i==0:
                continue
            name = "link_{}".format(i)
            self.drawLink(name, tuple(self.exp_symbol.index(tag) for tag in exp))
        #Draw path.
        self.drawPath()
        #Draw points.
        for i, name in enumerate(self.exp_symbol):
            coordinate = self.Point[i]
            if coordinate:
                color = colorQt('Green')
                fixed = False
                if name in self.slvsPath:
                    color = colorQt('Dark-Orange')
                elif name in self.mechanism['Driver']:
                    color = colorQt('Red')
                    fixed = True
                elif name in self.mechanism['Follower']:
                    color = colorQt('Blue')
                    fixed = True
                self.drawPoint(i, coordinate[0], coordinate[1], fixed, color)
        self.painter.end()
    
    def drawLink(self,
        name: str,
        points: Tuple[int]
    ):
        color = colorQt('Blue')
        pen = QPen(color)
        pen.setWidth(self.linkWidth)
        self.painter.setPen(pen)
        brush = QColor(226, 219, 190)
        brush.setAlphaF(0.75)
        self.painter.setBrush(brush)
        qpoints = tuple(
            QPointF(self.Point[i][0]*self.zoom, self.Point[i][1]*-self.zoom)
            for i in points if self.Point[i] and not isnan(self.Point[i][0])
        )
        if len(qpoints)==len(points):
            self.painter.drawPolygon(*qpoints)
        self.painter.setBrush(Qt.NoBrush)
        if self.showPointMark and name!='ground' and qpoints:
            pen.setColor(Qt.darkGray)
            self.painter.setPen(pen)
            self.painter.setFont(QFont('Arial', self.fontSize))
            text = "[{}]".format(name)
            cenX = sum(self.Point[i][0] for i in points if self.Point[i])/len(points)
            cenY = sum(self.Point[i][1] for i in points if self.Point[i])/len(points)
            self.painter.drawText(QPointF(cenX*self.zoom, cenY*-self.zoom), text)
    
    def drawPath(self):
        #Draw the path of mechanism.
        def drawPath(path):
            pointPath = QPainterPath()
            for i, coordinate in enumerate(path):
                if coordinate:
                    x = coordinate[0]*self.zoom
                    y = coordinate[1]*-self.zoom
                    if isnan(x):
                        continue
                    if i==0:
                        pointPath.moveTo(x, y)
                    else:
                        pointPath.lineTo(QPointF(x, y))
            self.painter.drawPath(pointPath)
        def drawDot(path):
            for coordinate in path:
                if isnan(coordinate[0]):
                    continue
                self.painter.drawPoint(QPointF(coordinate[0]*self.zoom, coordinate[1]*-self.zoom))
        draw = drawPath if self.Path.curve else drawDot
        Path = self.Path.path
        for i, path in enumerate(Path):
            color = colorQt('Green')
            if self.exp_symbol[i] in self.slvsPath:
                color = colorQt('Dark-Orange')
            pen = QPen(color)
            pen.setWidth(self.pathWidth)
            self.painter.setPen(pen)
            draw(path)
        #Draw the path that specified by user.
        pen = QPen(QColor(3, 163, 120))
        pen.setWidth(self.pathWidth)
        self.painter.setPen(pen)
        pointPath = QPainterPath()
        for name, path in self.slvsPath.items():
            for i, (x, y) in enumerate(path):
                x *= self.zoom
                y *= -self.zoom
                self.painter.drawEllipse(QPointF(x, y), 3, 3)
                if i==0:
                    pointPath.moveTo(x, y)
                else:
                    pointPath.lineTo(QPointF(x, y))
        pen.setColor(QColor(69, 247, 232))
        self.painter.setPen(pen)
        self.painter.drawPath(pointPath)
    
    @pyqtSlot()
    def change_index(self):
        self.index += 1
        self.index %= 360
        self.update()

class PreviewDialog(QDialog, Ui_Dialog):
    def __init__(self, mechanism, Path, parent=None):
        super(PreviewDialog, self).__init__(parent)
        self.setupUi(self)
        self.mechanism = mechanism
        self.setWindowTitle("Preview: {} (max {} generations)".format(self.mechanism['Algorithm'], self.mechanism['settings']['maxGen']))
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)
        self.splitter.setSizes([800, 100])
        previewWidget = DynamicCanvas(self.mechanism, Path, self)
        self.left_layout.insertWidget(0, previewWidget)
        #Basic information
        self.basic_label.setText("\n".join(["{}: {}".format(tag, self.mechanism[tag]) for tag in ['Algorithm', 'time']]+
            ["{}: {}".format(tag, self.mechanism[tag]) for tag in ['A', 'B']]+
            ["{}: {}".format(tag, self.mechanism[tag]) for tag in sorted(k for k in self.mechanism if 'L' in k)]))
        #Algorithm information
        interrupt = self.mechanism['interrupted']
        fitness = self.mechanism['TimeAndFitness'][-1]
        self.algorithm_label.setText("<html><head/><body><p>"+
            "<br/>".join(["Max generation: {}".format(self.mechanism['settings']['maxGen'])]+
            ["Fitness: {}".format(fitness if type(fitness)==float else fitness[1])]+
            ["<img src=\"{}\" width=\"15\"/>".format(":/icons/task-completed.png" if interrupt=='False' else
            ":/icons/question-mark.png" if interrupt=='N/A' else ":/icons/interrupted.png")+
            "Interrupted at: {}".format(interrupt)]+
            ["{}: {}".format(k, v) for k, v in self.mechanism['settings'].items()])+
            "</p></body></html>")
        #Hardware information
        self.hardware_label.setText("\n".join(["{}: {}".format(tag, self.mechanism['hardwareInfo'][tag]) for tag in
            ['os', 'memory', 'cpu', 'network']]))
