from tkinter import *


def about_window():
    aboutwindow = Tk()
    aboutwindow.title("About")
    aboutwindow.geometry("{}x{}".format(200, 150))
    aboutwindow.resizable(width=False, height=False)
    about_label = Label(aboutwindow,
                        text="\n \nRPN Calculator \n \n Copyright \n "
                             "Tomasz 'lilinho' Pawelec (2017) \n \n Version 1.0")
    about_label.pack()
    aboutwindow.mainloop()


def how_to():
    howto = Tk()
    howto.title("About")
    howto.geometry("{}x{}".format(300, 250))
    howto.resizable(width=False, height=False)
    how_label = Label(howto, text="\n RPN stands for Reverse Polish Notation"
                                  "\n For more information about it visit"
                                  "\n https://en.wikipedia.org/wiki/Reverse_Polish_notation"
                                  "\n\n Example: If you want to add 5+5 press:"
                                  "\n 5 -> ENTER -> 5 -> ENTER -> \'+\'"
                                  "\n POW - calculates x raised to the power y"
                                  "\n SQRT - calculates square root of x"
                                  "\n C - clears entry field"
                                  "\n AC - clears all"
                                  "\n POP - delete last entry"
                                  "\n +/- - changes sign of last inputed number"
                                  "\n (*number* -> ENTER -> +/-)")
    how_label.pack()
    howto.mainloop()