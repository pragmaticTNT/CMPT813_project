#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

This script shows a simple window
on the screen.

Author: Jan Bodnar
Last modified: November 2015
Website: www.zetcode.com
"""

from Tkinter import Tk, Canvas, RAISED, TOP, RIGHT, BOTH, X, Y, LEFT
from ttk import Frame, Label, Button, Style

class Example(Frame):
    def __init__(self, parent):
        # Frame.__init__(self, parent, background="white")  #Tkinter Frame
        Frame.__init__(self, parent)    # ttk Frame
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Drawing Window")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=True)

        frameL = Frame(self, relief=RAISED, borderwidth=2)
        frameL.pack(fill=BOTH, expand=True)
        lbMax = Label(frameL, text="Maximum Arrangment", width=25)
        lbMax.pack(side=TOP, padx=5, pady=5)
        canvas = Canvas(frameL)
        canvas.create_rectangle(30, 10, 120, 80, outline="#fff", fill="#fff")

        frameR = Frame(self, relief=RAISED, borderwidth=2)
        frameR.pack(fill=BOTH, expand=True)
        lbMin = Label(frameR, text="Minimum Arrangment", width=25)
        lbMin.pack(side=TOP, padx=5, pady=5)

        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.pack(side=RIGHT, padx=10, pady=10)


def main():
    root = Tk()
    root.geometry("500x750+0+0")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
