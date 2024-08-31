import tkinter.messagebox
from tkinter import *
import random
import time;
import datetime
from tkinter import Tk, StringVar, ttk

root=Tk()
root.geometry('1350x750+0+0')
root.title('RUGIPO Solar Farm Estimator')

Tops = Frame (root, width=1350, height=50, bd=12, relief='raise')
Tops.pack(side=TOP)
lblTitle = Label (Tops, font=('satoshi', 50, 'bold'), text='RUGIPO Solar Farm Estimator')
lblTitle.grid(row=0, column=0)

BottomMainFrame = Frame (root, width=1350, height=650, bd=12, relief='raise')
BottomMainFrame.pack(side=BOTTOM)

f1 = Frame (BottomMainFrame, width=450, height=650, bd=12, relief='raise')
f1.pack(side=LEFT)
f2 = Frame (BottomMainFrame, width=450, height=650, bd=12, relief='raise')
f2.pack(side=LEFT)
f2TOP = Frame (f2, width=450, height=350, bd=12, relief='raise')
f2TOP.pack(side=TOP)
f2BOTTOM = Frame (f2, width=450, height=300, bd=12, relief='raise')
f2BOTTOM.pack(side=BOTTOM)
f3 = Frame (BottomMainFrame, width=450, height=650, bd=12, relief='raise')
f3.pack(side=RIGHT)

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()


var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var22.set(0)
var23.set(0)
var24.set(0)
var25.set(0)


varCeiling= StringVar()
varTable= StringVar()
varACone= StringVar()
varACtwo= StringVar()
varACthree= StringVar()
varLaptop= StringVar()
varLED= StringVar()
varPlasma= StringVar()
varConsole= StringVar()
varSetup= StringVar()
varLightOne= StringVar()
varLightTwo= StringVar()
varLightThree= StringVar()
varLightFour= StringVar()
varWaterHeater= StringVar()
varWashingMachine= StringVar()
varMicrowave= StringVar()
varFridge= StringVar()
varGrinder= StringVar()
varPhotocopier= StringVar()
varPrinter= StringVar()
varCCTV= StringVar()
varWaterOne= StringVar()
varWaterTwo= StringVar()
varBattery= StringVar()
varBackup= StringVar()
varTotalLoad= StringVar()
varInverterSize= StringVar()
varBatterySize= StringVar()
varSolarPanel= StringVar()

varCeiling.set("0") 
varTable.set("0")
varACone.set("0")
varACtwo.set("0")
varACthree.set("0")
varLaptop.set("0")
varLED.set("0")
varPlasma.set("0")
varConsole.set("0")
varSetup.set("0")
varLightOne.set("0")
varLightTwo.set("0")
varLightThree.set("0")
varLightFour.set("0")
varWaterHeater.set("0")
varWashingMachine.set("0")
varMicrowave.set("0")
varFridge.set("0")
varGrinder.set("0")
varPhotocopier.set("0")
varPrinter.set("0")
varCCTV.set("0")
varWaterOne.set("0")
varWaterTwo.set("0")
varBattery.set("0")
varBackup.set("0")
varTotalLoad.set("0")
varInverterSize.set("0")
varBatterySize.set("0")
varSolarPanel.set("0")
varBackup.set("0")


def iExit():
    iExit= tkinter.messagebox.askyesno('Quit Systems', 'Do you want to leave Rugipo Solar Farm Estimator?')
    if iExit > 0:
        root.destroy()
        return
    
def iReset():
    varCeiling.set("0") 
    varTable.set("0")
    varACone.set("0")
    varACtwo.set("0")
    varACthree.set("0")
    varLaptop.set("0")
    varLED.set("0")
    varPlasma.set("0")
    varConsole.set("0")
    varSetup.set("0")
    varLightOne.set("0")
    varLightTwo.set("0")
    varLightThree.set("0")
    varLightFour.set("0")
    varWaterHeater.set("0")
    varWashingMachine.set("0")
    varMicrowave.set("0")
    varFridge.set("0")
    varGrinder.set("0")
    varPhotocopier.set("0")
    varPrinter.set("0")
    varCCTV.set("0")
    varWaterOne.set("0")
    varWaterTwo.set("0")
    varBattery.set("0")
    varBackup.set("0")
    varTotalLoad.set("0")
    varInverterSize.set("0")
    varBatterySize.set("0")
    varSolarPanel.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)


    txtCeiling.configure(state=DISABLED)
    txtTable.configure(state=DISABLED)
    txtACone.configure(state=DISABLED)
    txtACtwo.configure(state=DISABLED)
    txtACthree.configure(state=DISABLED)
    txtWaterHeater.configure(state=DISABLED)
    txtWashingMachine.configure(state=DISABLED)
    txtMicrowave.configure(state=DISABLED)
    txtFridge.configure(state=DISABLED)
    txtGrinder.configure(state=DISABLED)
    txtLaptop.configure(state=DISABLED)
    txtLED.configure(state=DISABLED)
    txtPlasma.configure(state=DISABLED)
    txtConsole.configure(state=DISABLED)
    txtSetup.configure(state=DISABLED)
    txtLightOne.configure(state=DISABLED)
    txtLightTwo.configure(state=DISABLED)
    txtLightThree.configure(state=DISABLED)
    txtLightFour.configure(state=DISABLED)
    txtPhotocopier.configure(state=DISABLED)
    txtPrinter.configure(state=DISABLED)
    txtCCTV.configure(state=DISABLED)
    txtWaterOne.configure(state=DISABLED)
    txtWaterTwo.configure(state=DISABLED)
    txtTotalLoad.configure(state=DISABLED)
    txtInverterSize.configure(state=DISABLED)
    txtBatterySize.configure(state=DISABLED)
    txtSolarPanel.configure(state=DISABLED)

def chkCeiling():
    if (var1.get() == 1):
        txtCeiling.configure(state = NORMAL)
        varCeiling.set('')
    elif (var1.get() == 0):
        txtCeiling.configure(state= DISABLED)
        varCeiling.set('0')

def chkTable():
    if (var2.get() == 1):
        txtTable.configure(state = NORMAL)
        varTable.set('')
    elif (var2.get() == 0):
        txtTable.configure(state= DISABLED)
        varTable.set('0')

def chkACone():
    if (var3.get() == 1):
        txtACone.configure(state = NORMAL)
        varACone.set('')
    elif (var2.get() == 0):
        txtACone.configure(state= DISABLED)
        varACone.set('0')

def chkACtwo():
    if (var4.get() == 1):
        txtACtwo.configure(state = NORMAL)
        varACtwo.set('')
    elif (var4.get() == 0):
        txtACtwo.configure(state= DISABLED)
        varACtwo.set('0')

def chkACthree():
    if (var5.get() == 1):
        txtACthree.configure(state = NORMAL)
        varACthree.set('')
    elif (var5.get() == 0):
        txtACthree.configure(state= DISABLED)
        varACthree.set('0')

def chkWaterHeater():
    if (var15.get() == 1):
        txtWaterHeater.configure(state = NORMAL)
        varWaterHeater.set('')
    elif (var15.get() == 0):
        txtWaterHeater.configure(state= DISABLED)
        varWaterHeater.set('0')

def chkWashingMachine():
    if (var16.get() == 1):
        txtWashingMachine.configure(state = NORMAL)
        varWashingMachine.set('')
    elif (var16.get() == 0):
        txtWashingMachine.configure(state= DISABLED)
        varWashingMachine.set('0')

def chkMicrowave():
    if (var17.get() == 1):
        txtMicrowave.configure(state = NORMAL)
        varMicrowave.set('')
    elif (var17.get() == 0):
        txtMicrowave.configure(state= DISABLED)
        varMicrowave.set('0')

def chkFridge():
    if (var18.get() == 1):
        txtFridge.configure(state = NORMAL)
        varFridge.set('')
    elif (var18.get() == 0):
        txtFridge.configure(state= DISABLED)
        varFridge.set('0')

def chkGrinder():
    if (var19.get() == 1):
        txtGrinder.configure(state = NORMAL)
        varGrinder.set('')
    elif (var19.get() == 0):
        txtGrinder.configure(state= DISABLED)
        varGrinder.set('0')

def chkLaptop():
    if (var6.get() == 1):
        txtLaptop.configure(state = NORMAL)
        varLaptop.set('')
    elif (var6.get() == 0):
        txtLaptop.configure(state= DISABLED)
        varLaptop.set('0')

def chkLED():
    if (var7.get() == 1):
        txtLED.configure(state = NORMAL)
        varLED.set('')
    elif (var7.get() == 0):
        txtLED.configure(state= DISABLED)
        varLED.set('0')

def chkPlasma():
    if (var8.get() == 1):
        txtPlasma.configure(state = NORMAL)
        varPlasma.set('')
    elif (var8.get() == 0):
        txtPlasma.configure(state= DISABLED)
        varPlasma.set('0')
   
def chkConsole():
    if (var9.get() == 1):
        txtConsole.configure(state = NORMAL)
        varConsole.set('')
    elif (var9.get() == 0):
        txtConsole.configure(state= DISABLED)
        varConsole.set('0')

def chkSetup():
    if (var10.get() == 1):
        txtSetup.configure(state = NORMAL)
        varSetup.set('')
    elif (var10.get() == 0):
        txtSetup.configure(state= DISABLED)
        varSetup.set('0')

def chkLightOne():
    if (var11.get() == 1):
        txtLightOne.configure(state = NORMAL)
        varLightOne.set('')
    elif (var11.get() == 0):
        txtLightOne.configure(state= DISABLED)
        varLightOne.set('0')

def chkLightTwo():
    if (var12.get() == 1):
        txtLightTwo.configure(state = NORMAL)
        varLightTwo.set('')
    elif (var12.get() == 0):
        txtLightTwo.configure(state= DISABLED)
        varLightTwo.set('0')

def chkLightThree():
    if (var13.get() == 1):
        txtLightThree.configure(state = NORMAL)
        varLightThree.set('')
    elif (var13.get() == 0):
        txtLightThree.configure(state= DISABLED)
        varLightThree.set('0')

def chkLightFour():
    if (var14.get() == 1):
        txtLightFour.configure(state = NORMAL)
        varLightFour.set('')
    elif (var14.get() == 0):
        txtLightFour.configure(state= DISABLED)
        varLightFour.set('0')

def chkPhotocopier():
    if (var20.get() == 1):
        txtPhotocopier.configure(state = NORMAL)
        varPhotocopier.set('')
    elif (var20.get() == 0):
        txtPhotocopier.configure(state= DISABLED)
        varPhotocopier.set('0')

def chkPrinter():
    if (var21.get() == 1):
        txtPrinter.configure(state = NORMAL)
        varPrinter.set('')
    elif (var21.get() == 0):
        txtPrinter.configure(state= DISABLED)
        varPrinter.set('0')

def chkCCTV():
    if (var22.get() == 1):
        txtCCTV.configure(state = NORMAL)
        varCCTV.set('')
    elif (var22.get() == 0):
        txtCCTV.configure(state= DISABLED)
        varCCTV.set('0')

def chkWaterOne():
    if (var23.get() == 1):
        txtWaterOne.configure(state = NORMAL)
        varWaterOne.set('')
    elif (var23.get() == 0):
        txtWaterOne.configure(state= DISABLED)
        varWaterOne.set('0')

def chkWaterTwo():
    if (var24.get() == 1):
        txtWaterTwo.configure(state = NORMAL)
        varWaterTwo.set('')
    elif (var24.get() == 0):
        txtWaterTwo.configure(state= DISABLED)
        varWaterTwo.set('0')


def HomeElectricalLoad():
    ans1= float(varCeiling.get())
    ans2= float(varTable.get())
    ans3= float(varACone.get())
    ans4= float(varACtwo.get())
    ans5= float(varACthree.get())
    ans6= float(varLaptop.get())
    ans7= float(varLED.get())
    ans8= float(varPlasma.get())
    ans9= float(varConsole.get())
    ans10= float(varSetup.get())
    ans11= float(varLightOne.get())
    ans12= float(varLightTwo.get())
    ans13= float(varLightThree.get())
    ans14= float(varLightFour.get())
    ans15= float(varWaterHeater.get())
    ans16= float(varWashingMachine.get())
    ans17= float(varMicrowave.get())
    ans18= float(varFridge.get())
    ans19= float(varGrinder.get())
    ans20= float(varPhotocopier.get())
    ans21= float(varPrinter.get())
    ans22= float(varCCTV.get())
    ans23= float(varWaterOne.get())
    ans24= float(varWaterTwo.get())
    ans25= float(varBackup.get())
    ans26= float(varBattery.get()) 

    iTotal1= ((ans1 * 75.0) + (ans2 * 50.0) + (ans3 * 1200.0) + (ans4 * 1700.0) + (ans5 * 2300.0))
    iTotal2= ((ans6 * 100.0) + (ans7 * 60.0) + (ans8 * 200.0) + (ans9 * 200.0) + (ans10 * 50.0))
    iTotal3= ((ans11 * 100.0) + (ans12 * 60.0) + (ans13 * 40.0) + (ans14 * 20.0))
    iTotal4= ((ans15 * 200.0) + (ans16 * 1000.0) + (ans17 * 1400.0) + (ans18 * 500.0) + (ans19 * 800.0))
    iTotal5= ((ans20 * 2000.0) + (ans21 * 2000.0) + (ans22 * 100.0) + (ans23 * 400.0) + (ans24 * 800.0))
    
    iTotalLoad= (iTotal1 + iTotal2 + iTotal3 + iTotal4 + iTotal5)
    iInverterSize= (iTotalLoad * 2)
    iBatterySize= ((iTotalLoad * ans25) / ans26)
    iSolarPanel= (ans26* ((iBatterySize / 10) + (iTotalLoad / ans26)))
    varTotalLoad.set(iTotalLoad)
    varInverterSize.set(iInverterSize)
    varBatterySize.set(iBatterySize)
    varSolarPanel.set(iSolarPanel)

#F1 UP
lblFansandAC = Label (f1, font=('satoshi', 18, 'bold'), text='Fans and AC')
lblFansandAC.grid(row=0, column=0)

Ceiling =Checkbutton(f1, text='Ceiling Fan (75W)', variable=var1, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkCeiling).grid (row=1, column=0, sticky=W)
txtCeiling = Entry(f1, font=('satoshi', 16, 'bold'), textvariable=varCeiling, width=6, state=DISABLED)
txtCeiling.grid(row=1, column=1)

Table =Checkbutton(f1, text='Table Fan (50W)', variable=var2, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkTable).grid (row=2, column=0, sticky=W)
txtTable = Entry(f1, font=('satoshi', 16, 'bold'), textvariable=varTable, width=6, state=DISABLED)
txtTable.grid(row=2, column=1)

ACone =Checkbutton(f1, text='Air Conditioner (1200W)', variable=var3, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkACone).grid (row=3, column=0, sticky=W)
txtACone = Entry(f1, font=('satoshi', 16, 'bold'), textvariable=varACone, width=6, state=DISABLED)
txtACone.grid(row=3, column=1)

ACtwo =Checkbutton(f1, text='Air Conditioner (1700W)', variable=var4, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkACtwo).grid (row=4, column=0, sticky=W)
txtACtwo = Entry(f1, font=('satoshi', 16, 'bold'), textvariable=varACtwo, width=6, state=DISABLED)
txtACtwo.grid(row=4, column=1)

ACthree =Checkbutton(f1, text='Air Conditioner (2300W)', variable=var5, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkACthree).grid (row=5, column=0, sticky=W)
txtACthree = Entry(f1, font=('satoshi', 16, 'bold'), textvariable=varACthree, width=6, state=DISABLED)
txtACthree.grid(row=5, column=1)

#F1 BOTTOM
lblAppliances = Label (f1, font=('satoshi', 18, 'bold'), text='Appliances')
lblAppliances.grid(row=7, column=0)

WaterHeater =Checkbutton(f1, text='Water Heater (200W)', variable=var15, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkWaterHeater).grid (row=8, column=0, sticky=W)
txtWaterHeater = Entry(f1, font=('satoshi', 16, 'bold'), textvariable=varWaterHeater, width=6, state=DISABLED)
txtWaterHeater.grid(row=8, column=1)

WashingMachine =Checkbutton(f1, text='Washing Machine (1000W)', variable=var16, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkWashingMachine).grid (row=9, column=0, sticky=W)
txtWashingMachine = Entry(f1, font=('satoshi', 16, 'bold'), textvariable=varWashingMachine, width=6, state=DISABLED)
txtWashingMachine.grid(row=9, column=1)

Microwave =Checkbutton(f1, text='Microwave (1400W)', variable=var17, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkMicrowave).grid (row=10, column=0, sticky=W)
txtMicrowave = Entry(f1, font=('satoshi', 16, 'bold'), textvariable=varMicrowave, width=6, state=DISABLED)
txtMicrowave.grid(row=10, column=1)

Fridge =Checkbutton(f1, text='Refridgerator (500W)', variable=var18, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkFridge).grid (row=11, column=0, sticky=W)
txtFridge = Entry(f1, font=('satoshi', 16, 'bold'), textvariable=varFridge, width=6, state=DISABLED)
txtFridge.grid(row=11, column=1)

Grinder =Checkbutton(f1, text='Grinder (800W)', variable=var19, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkGrinder).grid (row=12, column=0, sticky=W)
txtGrinder = Entry(f1, font=('satoshi', 16, 'bold'), textvariable=varGrinder, width=6, state=DISABLED)
txtGrinder.grid(row=12, column=1)

#F2TOP
lblEntertainment = Label (f2TOP, font=('satoshi', 18, 'bold'), text='Entertainment')
lblEntertainment.grid(row=0, column=0)

Laptop =Checkbutton(f2TOP, text='Laptop (100W)', variable=var6, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkLaptop).grid (row=1, column=0, sticky=W)
txtLaptop = Entry(f2TOP, font=('satoshi', 16, 'bold'), textvariable=varLaptop, width=6, state=DISABLED)
txtLaptop.grid(row=1, column=1)

LED =Checkbutton(f2TOP, text='LED TV (60W)', variable=var7, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkLED).grid (row=2, column=0, sticky=W)
txtLED = Entry(f2TOP, font=('satoshi', 16, 'bold'), textvariable=varLED, width=6, state=DISABLED)
txtLED.grid(row=2, column=1)

Plasma =Checkbutton(f2TOP, text='Plasma TV (250W)', variable=var8, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkPlasma).grid (row=3, column=0, sticky=W)
txtPlasma = Entry(f2TOP, font=('satoshi', 16, 'bold'), textvariable=varPlasma, width=6, state=DISABLED)
txtPlasma.grid(row=3, column=1)

Console =Checkbutton(f2TOP, text='Gaming Console (200W)', variable=var9, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkConsole).grid (row=4, column=0, sticky=W)
txtConsole = Entry(f2TOP, font=('satoshi', 16, 'bold'), textvariable=varConsole, width=6, state=DISABLED)
txtConsole.grid(row=4, column=1)

Setup =Checkbutton(f2TOP, text='TV Setup Box (50W)', variable=var10, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkSetup).grid (row=5, column=0, sticky=W)
txtSetup = Entry(f2TOP, font=('satoshi', 16, 'bold'), textvariable=varSetup, width=6, state=DISABLED)
txtSetup.grid(row=5, column=1)


#F2 BOTTOM
lblInput = Label (f2BOTTOM, font=('satoshi', 18, 'bold'), text='Input')
lblInput.grid(row=0, column=1)


lblBattery = Label(f2BOTTOM, font=('satoshi', 18), text='Battery')
lblBattery.grid(row=1, column=0, sticky=W)
txtBackup = Entry(f2BOTTOM, font=('satoshi', 16, 'bold'), textvariable=varBattery, width=4)
txtBackup.grid(row=1, column=1)

lblBackup = Label(f2BOTTOM, font=('satoshi', 18), text='Backup')
lblBackup.grid(row=2, column=0, sticky=W)
txtBackup = Entry(f2BOTTOM, font=('satoshi', 16, 'bold'), textvariable=varBackup, width=4)
txtBackup.grid(row=2, column=1)


lblOutput = Label (f2BOTTOM, font=('satoshi', 18, 'bold'), text='Output')
lblOutput.grid(row=0, column=2)

lblTotalLoad = Label(f2BOTTOM, font=('satoshi', 20), text='Total Load(W)')
lblTotalLoad.grid(row=1, column=2, sticky=W)
txtTotalLoad = Entry(f2BOTTOM, font=('satoshi', 20), width=7, textvariable=varTotalLoad, state=DISABLED)
txtTotalLoad.grid(row=1, column=3)

lblInverterSize = Label(f2BOTTOM, font=('satoshi', 20), text='Inverter Size(W)')
lblInverterSize.grid(row=2, column=2, sticky=W)
txtInverterSize = Entry(f2BOTTOM, font=('satoshi', 20), width=7, textvariable=varInverterSize, state=DISABLED)
txtInverterSize.grid(row=2, column=3)

lblBatterySize = Label(f2BOTTOM, font=('satoshi', 20), text='Battery Size(Ah)')
lblBatterySize.grid(row=3, column=2, sticky=W)
txtBatterySize = Entry(f2BOTTOM, font=('satoshi', 20), width=7, textvariable=varBatterySize, state=DISABLED)
txtBatterySize.grid(row=3, column=3)

lblSolarPanel = Label(f2BOTTOM, font=('satoshi', 20), text='Panels(W)')
lblSolarPanel.grid(row=4, column=2, sticky=W)
txtSolarPanel = Entry(f2BOTTOM, font=('satoshi', 20), width=7, textvariable=varSolarPanel, state=DISABLED)
txtSolarPanel.grid(row=4, column=3)
        

#F3
lblLights = Label (f3, font=('satoshi', 18, 'bold'), text='Lights')
lblLights.grid(row=0, column=0)

LightOne =Checkbutton(f3, text='Light bulb (100W)', variable=var11, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkLightOne).grid (row=1, column=0, sticky=W)
txtLightOne = Entry(f3, font=('satoshi', 16, 'bold'), textvariable=varLightOne, width=6, state=DISABLED)
txtLightOne.grid(row=1, column=1)

LightTwo =Checkbutton(f3, text='Light bulb (60W)', variable=var12, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkLightTwo).grid (row=2, column=0, sticky=W)
txtLightTwo = Entry(f3, font=('satoshi', 16, 'bold'), textvariable=varLightTwo, width=6, state=DISABLED)
txtLightTwo.grid(row=2, column=1)

LightThree =Checkbutton(f3, text='Light bulb (40W)', variable=var13, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkLightThree).grid (row=3, column=0, sticky=W)
txtLightThree = Entry(f3, font=('satoshi', 16, 'bold'), textvariable=varLightThree, width=6, state=DISABLED)
txtLightThree.grid(row=3, column=1)

LightFour =Checkbutton(f3, text='Tube Light (20W)', variable=var14, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkLightFour).grid (row=4, column=0, sticky=W)
txtLightFour = Entry(f3, font=('satoshi', 16, 'bold'), textvariable=varLightFour, width=6, state=DISABLED)
txtLightFour.grid(row=4, column=1)


#F3 BOTTOM
lblOthers = Label (f3, font=('satoshi', 18, 'bold'), text='Others')
lblOthers.grid(row=5, column=0)

Photocopier =Checkbutton(f3, text='Photocopier (2000W)', variable=var20, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkPhotocopier).grid (row=6, column=0, sticky=W)
txtPhotocopier = Entry(f3, font=('satoshi', 16, 'bold'), textvariable=varPhotocopier, width=6, state=DISABLED)
txtPhotocopier.grid(row=6, column=1)

Printer =Checkbutton(f3, text='Printer & Scanner (2000W)', variable=var21, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkPrinter).grid (row=7, column=0, sticky=W)
txtPrinter = Entry(f3, font=('satoshi', 16, 'bold'), textvariable=varPrinter, width=6, state=DISABLED)
txtPrinter.grid(row=7, column=1)

CCTV =Checkbutton(f3, text='CCTV (100W)', variable=var22, onvalue=1, offvalue=0, font=('satoshi', 18),command=chkCCTV ).grid (row=8, column=0, sticky=W)
txtCCTV = Entry(f3, font=('satoshi', 16, 'bold'), textvariable=varCCTV, width=6, state=DISABLED)
txtCCTV.grid(row=8, column=1)

WaterOne =Checkbutton(f3, text='Water Pump 0.5HP (400W)', variable=var23, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkWaterOne).grid (row=9, column=0, sticky=W)
txtWaterOne = Entry(f3, font=('satoshi', 16, 'bold'), textvariable=varWaterOne, width=6, state=DISABLED)
txtWaterOne.grid(row=9, column=1)

WaterTwo =Checkbutton(f3, text='Water Pump 1HP (800W)', variable=var24, onvalue=1, offvalue=0, font=('satoshi', 18), command=chkWaterTwo).grid (row=10, column=0, sticky=W)
txtWaterTwo = Entry(f3, font=('satoshi', 16, 'bold'), textvariable=varWaterTwo, width=6, state=DISABLED)
txtWaterTwo.grid(row=10, column=1)


btnCalculate=Button(f2BOTTOM, padx=16, pady=1, bd=4, fg='green', font=('satoshi', 16, 'bold'), width=4, text='Calculate', command=HomeElectricalLoad).grid(row=3, column=0)

btnReset=Button(f2BOTTOM, padx=16, pady=1, bd=4, fg='yellow', font=('satoshi', 16, 'bold'), width=4, command=iReset, text='Reset').grid(row=4, column=0)

btnExit=Button(f2BOTTOM, padx=16, pady=1, bd=4, fg='Red', font=('satoshi', 16, 'bold'), width=4, command=iExit, text='Exit').grid(row=5, column=0)

lblspace=Label(f2BOTTOM, text="\n\n\n\n\n\n\n")
lblspace.grid(row=6, column=0)

root.mainloop()