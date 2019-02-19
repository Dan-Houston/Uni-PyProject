#!/usr/bin/env python3
# -For running on linux systems

#Program Developed by Daniel Houston
#Python 3.6.8
#Dependancies
import tkinter

class PasswordMaker:
    def __init__(self,master):
        self.frame=tkinter.Frame(master)
        self.frame.pack()

def main():
    root=tkinter.Tk()
    root.mainloop()
    

if __name__=='__main__':
    main()

