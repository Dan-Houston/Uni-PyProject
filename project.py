#!/usr/bin/env python3
# -For running on linux systems

#Program Developed by Daniel Houston
#Python 3.6.8
#Dependancies
import tkinter as tk #abbriviation of tkinter to speed up development
from tkinter import ttk #ttk adds new tk features
from tkinter import messagebox #allows pop-up messages
import random #for password gen
import re #regular expressions
import math #for math ops in passEval


chars= {'alphas':'abcdefghijklmnopqrstuvwxyz',
        'numerics':'1234567890',
        'symbols':'!"£$%^&*()_+-=[]{};:\'@\\#~|<>,.?/'
        }

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
            if self.widgets['userInput'].get()=='':
                    tk.messagebox.showerror("Error","No input Detected")
                    return None
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
                self.widgets['userScore']=tk.Label(self.frame,text='Score : 0')
                self.widgets['userScore'].grid(row=1,column=0)
                self.widgets['userComplexity']=tk.Label(self.frame,text='Complexity: Too Short')
                self.widgets['userComplexity'].grid(row=2,column=0)
                self.widgets['seperator']=ttk.Separator(self.frame,orient=tk.VERTICAL)
                self.widgets['seperator'].grid(row=0,column=1,rowspan=2,sticky="ns")
                self.widgets['passAdvice']=tk.Frame(self.frame)
                self.widgets['passAdvice'].grid(row=0,rowspan=2,column=2)
                tk.Label(self.widgets['passAdvice'],text='test').pack()
                self.frame.pack()
                self.evaluate()
            def evaluate(self):
                password=self.password
                ##The following code was 'inspired' by pwdchecker.js @ www.passwordmeter.com
                #The variable names and evaluations are the same as the original code,
                #however the code has been adapted to work in python.
                #Consider this as an implementation of an algorithm in another language
                nScore=nLength=nAlphaUC=nAlphaLC=nNumber=nSymbol=nMidChar=nRequirements=nAlphdasOnly=nNumbersOnly=nUnqChar=nRepChar=nRepInc=nConsecAlphaUC=nConsecAlphaLC=nConsecNumber=nConsecSymbol=nConsecCharType=nSeqAlpha=nSeqNumber=nSeqSymbol=nSeqChar=nReqChar=nMultConsecCharType=0
                nMultRepChar=nMultConsecSymbol=1
                nMultMidChar=nMultRequirements=nMultConsecAlphaUC=nMultConsecAlphaLC=nMultConsecNumer=2
                nReqCharType=nMultAlphaUC=nMultAlphdaLC=nMultSeqAlpha=nMultSeqNumber=nMultSeqSymbol=3
                nMultLength=nMultNumber=4
                nMultSymbol=6
                sAlphas='abcdefghijklmnopqrstuvwxyz'
                sNumerics='01234567890'
                sSymbols = ')!@#$%^&*()'
                sComplexity='Too Short'
                sStandards='Below'
                nTmpAlphaUC=nTmpAlphaLC=nTmpNumber=nTmpSymbol=''
                nLength=len(password)
                nScore=nLength*nMultLength
                arrPwd=list(password)
                arrPwdLen=len(arrPwd)
                print(arrPwdLen,nLength)
                #Loop through pwd to check for symbols, numerics, lowercase/uppercase chars
                for a in range(len(arrPwd)):
                    if re.match('[A-Z]',arrPwd[a]):
                        if (nTmpAlphaUC!=''):
                            if (nTmpAlphaUC+1)==a:
                                nConsecAlphaUC+=1
                                nConsecCharType+=1
                                print('ya')
                        nTmpAlphaUC=a
                        nAlphaUC+=1
                    elif re.match('[a-z]',arrPwd[a]):
                        if (nTmpAlphaLC!=''):
                            if (nTmpAlphaLC+1)==a:
                                nConsecAlphaLC+=1
                                nConsecCharType+=1
                                print('yi')
                        nTmpAlphaLC=a
                        nAlphaLC+=1
                    elif re.match('[0-9]',arrPwd[a]):
                        if (a>0 and a<(arrPwdLen-1)):
                            nMidChar+=1
                        if (nTmpNumber!=''):
                            if (nTmpNumber+1==a):
                                nConsecNumber+=1
                                nConsecCharType+=1
                                print('yu')
                        nTmpNumber=a
                        nNumber+=1
                    elif re.match('[^a-zA-Z0-9_]',arrPwd[a]):
                        if (a>0 and a<(arrPwdLen-1)):
                            nMidChar+=1
                        if (nTmpSymbol!=''):
                            if (nTmpSymbol+1==a):
                                nConsecSymbol+=1
                                nConsecCharType+=1
                                print('ye')
                        nTmpSymbol=a
                        nSymbol+=1
                    #Nested loop to check for repeated chars
                    bCharExists=False
                    for b in range(len(arrPwd)):
                        if (arrPwd[a] == arrPwd[b] and a!=b):
                            bCharExists=true;
                            nRepInc+=abs(arrPwdLen/(b-a))
                    if bCharExists:
                        nRepChar+=1
                        nUnqChar=arrPwdLen-nRepChar
                        nRecInc=
                
                


def main():
    root=tk.Tk()
    app = BaseApp(root)
    root.mainloop()
    

if __name__=='__main__':
    main()

