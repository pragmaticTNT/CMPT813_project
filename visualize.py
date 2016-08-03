#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
(Modified) Zetcode Tkinter tutorial

This program --- used to --- draws three
rectangles filled with different colours.

Author: Jan Bodnar
Editor: Lilili
Last modified: July 2016
Website: www.zetcode.com
"""

from math import pi, sin, cos
from Tkinter import Tk, Canvas, Label, Frame, BOTH, X, Y


class Visual(Frame):
    def __init__(self, parent, scale, dim, theta, maxPrm, minPrm):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.scale = scale
        self.width = dim[0]
        self.height = dim[1]
        self.maxCenter = (self.width/4, self.height/2)
        self.minCenter = (3*self.width/4, self.height/2)
        # print "maxCenter:", self.maxCenter
        # print "minCenter:", self.minCenter
        self.initUI(len(theta), theta, maxPrm, minPrm)

    def initUI(self, n, theta, maxPrm, minPrm):
        self.parent.title("Umbrella")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self, bg="white")
        # ===> CANVAS CROSS MARKERS
        # canvas.create_line(0, 0, self.width, self.height)
        # canvas.create_line(self.width, 0, 0, self.height)
        # canvas.pack(fill=BOTH, expand=1)
        self.visualizeLines(canvas, n, self.maxCenter, theta, maxPrm)
        self.visualizeLines(canvas, n, self.minCenter, theta, minPrm)
        # ===> Horizontal Marker
        canvas.create_line(0, self.height/2, self.width, self.height/2)
        canvas.pack(fill=BOTH, expand=1)

    def visualizeLines(self, canvas, n, center, theta, lengths):
        newX = lambda i: center[0] + int(self.scale*lengths[i]*cos(theta[i]))
        # Canvas coordinates have (0,0) TOP-LEFT, +ve down and left
        newY = lambda i: center[1] - int(self.scale*lengths[i]*sin(theta[i]))
        points = [f(i) for i in range(n) for f in (newX, newY)]
        canvas.create_polygon(
                points, outline='red', fill="white", width=5
        )
        for i in range(0, 2*n, 2):
            canvas.create_line(
                    center[0], center[1], points[i], points[i+1]
            )


def main():
    scale = 30
    height = 400
    width = height*2
    theta = [ 0, pi/2, pi, pi*3/2 ]
    maxPrm = [ 1, 2, 3, 4 ]
    minPrm = [ 4, 3, 2, 1 ]
    root = Tk()
    bz = Visual(root, scale, width, height, theta, maxPrm, minPrm)
    root.geometry("800x400+0+0")
    root.mainloop()


if __name__ == '__main__':
    main()
