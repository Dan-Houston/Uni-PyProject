#!/usr/bin/env python3
# -For running on linux systems

#Program Developed by Daniel Houston
#Python 3.6.8
#Dependancies
import tkinter as tk #abbriviation of tkinter to speed up development
from tkinter import ttk
#import ttk #adds new tk features
import random #for password gen
import re

class BaseApp:
    def __init__(self,master):
        self.master=master
        self.MainApp=self.PassInput(self.master)
    class PassInput:
        def __init__(self,master):
            self.master=master
            self.frame=tk.Frame(self.master) #creating frame for widgets
            self.widgets={} #creating a widget dictionary for more efficient storage
            self.widgets['userPrompt']=tk.Label(self.frame,text='Enter a password,\n or generate one with the button below')
            self.widgets['userPrompt'].grid(row=0,column=0)
            self.widgets['userInput']=tk.Entry(self.frame)
            self.widgets['userInput'].grid(row=1,column=0)
            self.widgets['genPassword']=tk.Button(self.frame,text='Generate Password',command=lambda:self.genPass())
            self.widgets['genPassword'].grid(row=2,column=0)
            self.widgets['evalPassword']=tk.Button(self.frame,text='Evaluate',command=lambda:self.evaluate())
            self.widgets['evalPassword'].grid(row=1,column=1)
            self.frame.pack()
        def genPass(self):
            lines=open('wordList.txt').read().splitlines()
            word=random.choice(lines)
            word=word.capitalize()+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
            self.widgets['userInput'].delete(0, tk.END)
            self.widgets['userInput'].insert(0, word)           
        def evaluate(self):
            self.EvalMaster=tk.Toplevel(self.master)
            self.EvalWindow=self.PassEval(self.EvalMaster,self.widgets['userInput'].get())
        class PassEval:
            def __init__(self,master,password):
                self.master=master
                self.password=password
                self.widgets={}
                self.frame=tk.Frame(self.master)
                self.widgets['userPassword']=tk.Label(self.frame,text='Password : {}'.format(self.password))
                self.widgets['userPassword'].grid(row=0,column=0)
                self.widgets['userScore']=tk.Label(self.frame,text='Score : Evaluating...')
                self.widgets['userScore'].grid(row=1,column=0)
                self.widgets['seperator']=ttk.Separator(self.frame,orient=tk.VERTICAL)
                self.widgets['seperator'].grid(row=0,column=1,rowspan=2,sticky="ns")
                self.widgets['passAdvice']=tk.Frame(self.frame)
                self.widgets['passAdvice'].grid(row=0,rowspan=2,column=2)
                tk.Label(self.widgets['passAdvice'],text='test').pack()
                self.frame.pack()
            def evaluate(self):
                pass


def main():
    root=tk.Tk()
    app = BaseApp(root)
    root.mainloop()
    

if __name__=='__main__':
    main()

