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
                self.width=30
                #creating stringvars for evaluation
                self.nScore=tk.StringVar()
                self.nComplexity=tk.StringVar()
                self.nLengthBonus=tk.StringVar()
                self.nAlphaUCBonus=tk.StringVar()
                self.nAlphaLCBonus=tk.StringVar()
                self.nNumberBonus=tk.StringVar()
                self.nSymbolBonus=tk.StringVar()
                self.nMidCharBonus=tk.StringVar()
                self.nAlphasOnlyBonus=tk.StringVar()
                self.nNumbersOnlyBonus=tk.StringVar()
                self.nRepCharBonus=tk.StringVar()
                self.nConsecAlphaUCBonus=tk.StringVar()
                self.nConsecAlphaLCBonus=tk.StringVar()
                self.nConsecNumberBonus=tk.StringVar()
                self.nSeqAlphaBonus=tk.StringVar()
                self.nSeqNumberBonus=tk.StringVar()
                self.nSeqSymbolBonus=tk.StringVar()
                self.nRequirementsBonus=tk.StringVar()
                self.frame=tk.Frame(self.master)
                self.widgets['userPassword']=tk.Label(self.frame,text='Password : {}'.format(self.password))
                self.widgets['userPassword'].grid(row=0,column=0)
                self.widgets['userScore']=tk.Label(self.frame,textvariable=self.nScore)
                self.widgets['userScore'].grid(row=1,column=0)
                self.widgets['userComplexity']=tk.Label(self.frame,textvariable=self.nComplexity)
                self.widgets['userComplexity'].grid(row=2,column=0)
                self.widgets['seperator']=ttk.Separator(self.frame,orient=tk.VERTICAL)
                self.widgets['seperator'].grid(row=0,column=1,rowspan=3,sticky="ns")
                self.widgets['passAdvice']=tk.Frame(self.frame)
                self.widgets['passAdvice'].grid(row=0,rowspan=2,column=2)
                self.widgets['passAdditions']=tk.Label(self.widgets['passAdvice'],text='Additions:')
                self.widgets['passAdditions'].grid(row=0,column=0,columnspan=2)
                self.widgets['nLengthString']=tk.Label(self.widgets['passAdvice'],text='Numbers of Characters:',anchor='e',width=self.width)
                self.widgets['nLengthString'].grid(row=1,column=0)
                self.widgets['nLengthBonus']=tk.Label(self.widgets['passAdvice'],textvariable=self.nLengthBonus)
                self.widgets['nLengthBonus'].grid(row=1,column=1)
                self.widgets['nAlphaUCString']=tk.Label(self.widgets['passAdvice'],text='Uppercase Characters:',anchor='e',width=self.width)
                self.widgets['nAlphaUCString'].grid(row=2,column=0)
                self.widgets['nAlphaUCBonus']=tk.Label(self.widgets['passAdvice'],textvariable=self.nAlphaUCBonus)
                self.widgets['nAlphaUCBonus'].grid(row=2,column=1)
                self.widgets['nAlphaLCString']=tk.Label(self.widgets['passAdvice'],text='Lowercase Characters:',anchor='e',width=self.width)
                self.widgets['nAlphaLCString'].grid(row=3,column=0)
                self.widgets['nAlphaLCBonus']=tk.Label(self.widgets['passAdvice'],textvariable=self.nAlphaLCBonus)
                self.widgets['nAlphaLCBonus'].grid(row=3,column=1)
                self.widgets['nNumberString']=tk.Label(self.widgets['passAdvice'],text='Numbers:',anchor='e',width=self.width)
                self.widgets['nNumberString'].grid(row=4,column=0)
                self.widgets['nNumberBonus']=tk.Label(self.widgets['passAdvice'],textvariable=self.nNumberBonus)
                self.widgets['nNumberBonus'].grid(row=4,column=1)
                self.widgets['nSymbolString']=tk.Label(self.widgets['passAdvice'],text='Symbols:',anchor='e',width=self.width)
                self.widgets['nSymbolString'].grid(row=5,column=0)
                self.widgets['nSymbolBonus']=tk.Label(self.widgets['passAdvice'],textvariable=self.nSymbolBonus)
                self.widgets['nSymbolBonus'].grid(row=5,column=1)
                self.widgets['nMidCharString']=tk.Label(self.widgets['passAdvice'],text='Middle Numbers of Symbols:',anchor='e',width=self.width)
                self.widgets['nMidCharString'].grid(row=6,column=0)
                self.widgets['nMidCharBonus']=tk.Label(self.widgets['passAdvice'],textvariable=self.nMidCharBonus)
                self.widgets['nMidCharBonus'].grid(row=6,column=1)
                self.widgets['nRequirementsString']=tk.Label(self.widgets['passAdvice'],text='Requirements:',anchor='e',width=self.width)
                self.widgets['nRequirementsString'].grid(row=7,column=0)
                self.widgets['nRequirementsBonus']=tk.Label(self.widgets['passAdvice'],textvariable=self.nRequirementsBonus)
                self.widgets['nRequirementsBonus'].grid(row=7,column=1)
                self.widgets['passDeductions']=tk.Label(self.widgets['passAdvice'],text='Deductions:')
                self.widgets['passDeductions'].grid(row=8,column=0,columnspan=2)
                self.widgets['nAlphasOnlyString']=tk.Label(self.widgets['passAdvice'],text='Letters Only:',anchor='e',width=self.width)
                self.widgets['nAlphasOnlyString'].grid(row=9,column=0)
                self.widgets['nAlphasOnlyBonus']=tk.Label(self.widgets['passAdvice'],textvariable=self.nAlphasOnlyBonus)
                self.widgets['nAlphasOnlyBonus'].grid(row=9,column=1)
                self.widgets['nNumbersOnlyString']=tk.Label(self.widgets['passAdvice'],text='Numbers Only:',anchor='e',width=self.width)
                self.widgets['nNumbersOnlyString'].grid(row=10,column=0)
                self.widgets['nNumbersOnlyBonus']=tk.Label(self.widgets['passAdvice'],textvariable=self.nNumbersOnlyBonus)
                self.widgets['nNumbersOnlyBonus'].grid(row=10,column=1)
                self.widgets['nRepCharString']=tk.Label(self.widgets['passAdvice'],text='Repeated Characters:\n(Case Insensitive)',anchor='e',width=self.width)
                self.widgets['nRepCharString'].grid(row=11,column=0)
                self.widgets['nRepCharBonus']=tk.Label(self.widgets['passAdvice'],textvariable=self.nRepCharBonus)
                self.widgets['nRepCharBonus'].grid(row=11,column=1)
                self.widgets['nConsecAlphaUCString']=tk.Label(self.widgets['passAdvice'],text='Consecutive Uppercase Characters:',anchor='e',width=self.width)
                self.widgets['nConsecAlphaUCString'].grid(row=12,column=0)
                self.widgets['nConsecAlphaUCBonus']=tk.Label(self.widgets['passAdvice'],textvariable=self.nConsecAlphaUCBonus)
                self.widgets['nConsecAlphaUCBonus'].grid(row=12,column=1)
                self.widgets['nConsecAlphaLCString']=tk.Label(self.widgets['passAdvice'],text='Consecutive Lowercase Characters:',anchor='e',width=self.width)
                self.widgets['nConsecAlphaLCString'].grid(row=13,column=0)
                self.widgets['nConsecAlphaLCBonus']=tk.Label(self.widgets['passAdvice'],textvariable=self.nConsecAlphaLCBonus)
                self.widgets['nConsecAlphaLCBonus'].grid(row=13,column=1)
                self.widgets['nConsecNumberString']=tk.Label(self.widgets['passAdvice'],text='Consecutive Numbers:',anchor='e',width=self.width)
                self.widgets['nConsecNumberString'].grid(row=14,column=0)
                self.widgets['nConsecNumberBonus']=tk.Label(self.widgets['passAdvice'],textvariable=self.nConsecNumberBonus)
                self.widgets['nConsecNumberBonus'].grid(row=14,column=1)
                self.widgets['nSeqAlphaString']=tk.Label(self.widgets['passAdvice'],text='Sequential Letters (3+):',anchor='e',width=self.width)
                self.widgets['nSeqAlphaString'].grid(row=15,column=0)
                self.widgets['nSeqAlphaBonus']=tk.Label(self.widgets['passAdvice'],textvariable=self.nSeqAlphaBonus)
                self.widgets['nSeqAlphaBonus'].grid(row=15,column=1)
                self.widgets['nSeqNumberString']=tk.Label(self.widgets['passAdvice'],text='Sequential Numbers (3+):',anchor='e',width=self.width)
                self.widgets['nSeqNumberString'].grid(row=16,column=0)
                self.widgets['nSeqNumberBonus']=tk.Label(self.widgets['passAdvice'],textvariable=self.nSeqNumberBonus)
                self.widgets['nSeqNumberBonus'].grid(row=16,column=1)
                self.widgets['nSeqSymbolString']=tk.Label(self.widgets['passAdvice'],text='Sequential Symbols (3+):',anchor='e',width=self.width)
                self.widgets['nSeqSymbolString'].grid(row=17,column=0)
                self.widgets['nSeqSymbolBonus']=tk.Label(self.widgets['passAdvice'],textvariable=self.nSeqSymbolBonus)
                self.widgets['nSeqSymbolBonus'].grid(row=17,column=1)
                self.frame.pack()
                self.evaluate()
            def evaluate(self):
                password=self.password
                ##The following code was 'inspired' by pwdchecker.js @ www.passwordmeter.com
                #The variable names and evaluations are the same as the original code,
                #however the code has been adapted to work in python.
                #Consider this as an implementation of an algorithm in another language
                nScore=nLength=nAlphaUC=nAlphaLC=nNumber=nSymbol=nMidChar=nRequirements=nAlphasOnly=nNumbersOnly=nUnqChar=nRepChar=nRepInc=nConsecAlphaUC=nConsecAlphaLC=nConsecNumber=nConsecSymbol=nConsecCharType=nSeqAlpha=nSeqNumber=nSeqSymbol=nSeqChar=nReqChar=nMultConsecCharType=0
                nMultRepChar=nMultConsecSymbol=1
                nMultMidChar=nMultRequirements=nMultConsecAlphaUC=nMultConsecAlphaLC=nMultConsecNumber=2
                nReqCharType=nMultAlphaUC=nMultAlphaLC=nMultSeqAlpha=nMultSeqNumber=nMultSeqSymbol=3
                nMultLength=nMultNumber=4
                nMultSymbol=6
                sAlphaUC=sAlphaLC=sNumber=sSymbol=sMidChar=sRequirements="+ 0"
                sAlphasOnly=sNumbersOnly=sRepChar=sConsecAlphaUC=sConsecAlphaLC=sConsecNumber=sSeqAlpha=sSeqNumber=sSeqSymbol="- 0"
                sAlphas='abcdefghijklmnopqrstuvwxyz'
                sNumerics='01234567890'
                sSymbols = ')!"£$%^&*()'
                sComplexity='Too Short'
                sStandards='Below'
                nMinPwdLen=8
                nTmpAlphaUC=nTmpAlphaLC=nTmpNumber=nTmpSymbol=''
                nLength=len(password)
                nScore=nLength*nMultLength
                arrPwd=list(password)
                arrPwdLen=len(arrPwd)
                #Loop through pwd to check for symbols, numerics, lowercase/uppercase chars
                for a in range(len(arrPwd)):
                    if re.match('[A-Z]',arrPwd[a]):
                        if (nTmpAlphaUC!=''):
                            if (nTmpAlphaUC+1)==a:
                                nConsecAlphaUC+=1
                                nConsecCharType+=1
                        nTmpAlphaUC=a
                        nAlphaUC+=1
                    elif re.match('[a-z]',arrPwd[a]):
                        if (nTmpAlphaLC!=''):
                            if (nTmpAlphaLC+1)==a:
                                nConsecAlphaLC+=1
                                nConsecCharType+=1
                        nTmpAlphaLC=a
                        nAlphaLC+=1
                    elif re.match('[0-9]',arrPwd[a]):
                        if (a>0 and a<(arrPwdLen-1)):
                            nMidChar+=1
                        if (nTmpNumber!=''):
                            if (nTmpNumber+1==a):
                                nConsecNumber+=1
                                nConsecCharType+=1
                        nTmpNumber=a
                        nNumber+=1
                    elif re.match('[^a-zA-Z0-9_]',arrPwd[a]):
                        if (a>0 and a<(arrPwdLen-1)):
                            nMidChar+=1
                        if (nTmpSymbol!=''):
                            if (nTmpSymbol+1==a):
                                nConsecSymbol+=1
                                nConsecCharType+=1
                        nTmpSymbol=a
                        nSymbol+=1
                    #Nested loop to check for repeated chars
                    bCharExists=False
                    for b in range(len(arrPwd)):
                        if (arrPwd[a] == arrPwd[b] and a!=b):
                            bCharExists=True;
                            nRepInc+=abs(arrPwdLen/(b-a))
                    if bCharExists:
                        nRepChar+=1
                        nUnqChar=arrPwdLen-nRepChar
                        if nUnqChar:
                            nRepInc=math.ceil(nRepInc/nUnqChar)
                        else:
                            nRepInc=math.ceil(nRepInc)
                for s in range(0,23):
                    sFwd=sAlphas[s:s+3]
                    sRev=sFwd[::-1]
                    if (password.lower().find(sFwd) != -1 or password.lower().find(sRev) != -1):
                        nSeqAlpha+=1
                        nSeqChar+=1
                for s in range(0,8):
                    sFwd=sNumerics[s:s+3]
                    sRev=sFwd[::-1]
                    if (password.lower().find(sFwd) != -1 or password.lower().find(sRev) != -1):
                        nSeqNumber+=1
                        nSeqChar+=1
                for s in range(0,8):
                    sFwd=sSymbols[s:s+3]
                    sRev=sFwd[::-1]
                    if (password.lower().find(sFwd) != -1 or password.lower().find(sRev) != -1):
                        nSeqSymbol+=1
                        nSeqChar+=1
                #Point Additions
                self.nLengthBonus.set("+ "+str(nScore))
                if (nAlphaUC > 0 and nAlphaUC < nLength):
                    nScore+=((nLength-nAlphaUC)*2)
                    sAlphaUC="+ "+str((nLength - nAlphaUC) * 2)
                if (nAlphaLC > 0 and nAlphaLC < nLength):
                    nScore+=((nLength - nAlphaLC) * 2)
                    sAlphaLC="+ "+str((nLength - nAlphaLC) * 2)
                if (nNumber > 0 and nNumber < nLength):
                    nScore+=(nNumber*nMultNumber)
                    sNumber="+ "+str(nNumber*nMultNumber)
                if (nSymbol>0):
                    nScore+=(nSymbol*nMultSymbol)
                    sSymbol="+ "+str(nSymbol*nMultSymbol)
                if (nMidChar>0):
                    nScore+=(nMidChar*nMultMidChar)
                    sMidChar="+ "+str(nMidChar*nMultMidChar)
                self.nAlphaUCBonus.set(sAlphaUC)
                self.nAlphaLCBonus.set(sAlphaLC)
                self.nNumberBonus.set(sNumber)
                self.nSymbolBonus.set(sSymbol)
                self.nMidCharBonus.set(sMidChar)
                #Point Deductions
                if ((nAlphaLC>0 or nAlphaUC>0) and nSymbol==0 and nNumber==0):
                    nScore=nScore-nLength
                    nAlphasOnly=nLength
                    sAlphasOnly="- "+str(nLength)
                if (nAlphaLC==0 and nAlphaUC==0 and nSymbol==0 and nNumber >0):
                    nScore=nScore-nLength
                    nNumbersOnly=nLength
                    sNumbersOnly="- "+str(nLength)
                if (nRepChar>0):
                    nScore=nScore-nRepInc
                    sRedChar="- "+str(nRepInc)
                if (nConsecAlphaUC>0):
                    nScore=nScore-(nConsecAlphaUC*nMultConsecAlphaUC)
                    sConsecAlphaUC="- "+str(nConsecAlphaUC * nMultConsecAlphaUC)
                if (nConsecAlphaLC>0):
                    nScore=nScore-(nConsecAlphaLC*nMultConsecAlphaLC)
                    sConsecAlphaLC="- "+str(nConsecAlphaLC * nMultConsecAlphaLC)
                if (nConsecNumber>0):
                    nScore=nScore-(nConsecNumber * nMultConsecNumber)
                    sConsecNumber = "- "+str(nConsecNumber * nMultConsecNumber)
                if (nSeqAlpha>0):
                    nScore = nScore - (nSeqAlpha * nMultSeqAlpha)
                    sSeqAlpha = "- " + str(nSeqAlpha * nMultSeqAlpha)
                if (nSeqNumber>0):
                    nScore = nScore - (nSeqNumber * nMultSeqNumber)
                    sSeqNumber = "- " + str(nSeqNumber * nMultSeqNumber)
                if (nSeqSymbol>0):
                    nScore = nScore - (nSeqSymbol * nMultSeqSymbol)
                    sSeqSymbol = "- " + str(nSeqSymbol * nMultSeqSymbol)
                self.nAlphasOnlyBonus.set(sAlphasOnly)
                self.nNumbersOnlyBonus.set(sNumbersOnly)
                self.nRepCharBonus.set(sRepChar)
                self.nConsecAlphaUCBonus.set(sConsecAlphaUC)
                self.nConsecAlphaLCBonus.set(sConsecAlphaLC)
                self.nConsecNumberBonus.set(sConsecNumber)
                self.nSeqAlphaBonus.set(sSeqAlpha)
                self.nSeqNumberBonus.set(sSeqNumber)
                self.nSeqSymbolBonus.set(sSeqSymbol)
                arrChars=[nLength,nAlphaUC,nAlphaLC,nNumber,nSymbol]
                arrCharsIds=["nLength","nAlphaUC","nAlphaLC","nNumber","nSymbol"]
                arrCharsLen=len(arrChars)
                for c in range(0,arrCharsLen):
                    if (arrCharsIds[c]=="nLength"):
                        minVal=nMinPwdLen-1
                    else:
                        minVal=0
                    if (arrChars[c]==minVal+1):
                        nReqChar+=1
                    elif (arrChars[c]>minVal+1):
                        nReqChar+=1
                nRequirements=nReqChar
                if (len(password)>nMinPwdLen):
                    nMinReqChars=3
                else:
                    nMinReqChars=4
                if (nRequirements>nMinReqChars):
                    nScore+=(nRequirements*2)
                    sRequirements="+ "+str(nRequirements*2)
                self.nRequirementsBonus.set(sRequirements)
                #Sets any >100 to 100 and <0 to 0, for % format
                if (nScore>100):
                    nScore=100
                elif (nScore<0):
                    nScore=0
                if (nScore>=0 and nScore<20):
                    sComplexity="Very Weak"
                elif (nScore>=20 and nScore<40):
                    sComplexity="Weak"
                elif (nScore>=40 and nScore<60):
                    sComplexity="Good"
                elif (nScore>=60 and nScore<80):
                    sComplexity="Strong"
                elif (nScore>=80 and nScore<=100):
                    sComplexity="Very Strong"
                self.nScore.set("Score:"+str(nScore)+"%")
                self.nComplexity.set("Complexity:"+sComplexity)







                    
                


def main():
    root=tk.Tk()
    app = BaseApp(root)
    root.mainloop()
    

if __name__=='__main__':
    main()

