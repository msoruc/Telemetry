from tkinter import *
from tkinter import ttk
import time
from random import randint

#Set some Globabl Limits

MinMainVolt=46
WarnMainVolt=47
MaxMainVolt=49

MinAuxVolt=11
WarnAuxVolt=12
MaxAuxVolt=15



class App():

    def recorddata(self):

        #import the gobal
        global MinMainVolt
        global WarnMainVolt
        global MaxMainVolt
        global MinAuxVolt
        global WarnAuxVolt
        global MaxAuxVolt

        defaultbg = root.cget('bg')



    #Set the back ground color depending on the voltage

        self.mainvolt.set(randint(0,100))
        if self.mainvolt.get() < MinMainVolt or self.mainvolt.get() > MaxMainVolt:
            self.mainvoltlabel.config(bg='red')
        elif self.mainvolt.get() < WarnMainVolt:
            self.mainvoltlabel.config(bg='yellow')
        else:
            self.mainvoltlabel.config(bg=defaultbg)


        self.auxvolt.set(randint(0,100))
        if self.auxvolt.get() < MinMainVolt or self.auxvolt.get() > MaxAuxVolt:
            self.auxvoltlabel.config(bg='red')
        elif self.auxvolt.get() < WarnMainVolt:
            self.auxvoltlabel.config(bg='yellow')
        else:
            self.auxvoltlabel.config(bg=defaultbg)




        #causes the program to recall the record segment every 100 ms
        root.after(1000,lambda: self.recorddata())

    def __init__(self, master):
        frame=Frame(master)
        frame.pack()
        master.title("Solar Car Telemetry")
        labels=["Driver:", "Day:, ""Main Battery Voltage:","Aux Battery Voltage","Current"]


        #declare some variables
        self.drivername=StringVar()
        self.drivedate=StringVar()
        self.mainvolt=DoubleVar()
        self.auxvolt=DoubleVar()
        self.current=DoubleVar()
        self.amphour=DoubleVar()

        #set some defaults
        self.main=48.3
        self.aux=12.3
        self.cur=50.0
        self.amphr=100


        #set some variables
        self.mainvolt.set(self.main)
        self.auxvolt.set(self.aux)
        self.current.set(self.cur)
        self.amphour.set(self.amphr)


        #define the labels
        self.drivernamelabel=Label(frame, text="Driver:")
        self.drivedatelabel=Label(frame, text="Date:")
        self.mainvoltlabel=Label(frame, text="Main Voltage:")
        self.auxvoltlabel=Label(frame, text="Aux Voltage:")
        self.currentlabel=Label(frame, text="Current:")
        self.amphourlabel=Label(frame, text="AmpHour:")

        self.drivername = Entry(frame)
        self.drivedate = Entry(frame)
        self.mainvoltvalue=Label(frame, textvariable=self.mainvolt)
        self.auxvoltlvalue=Label(frame, textvariable=self.auxvolt)
        self.currentvalue=Label(frame, textvariable=self.current)
        self.amphourvalue = Label(frame, textvariable=self.amphour)

        #place labels in grid
        self.drivernamelabel.grid(row=0, column=0)
        self.drivedatelabel.grid(row=1, column=0)
        self.mainvoltlabel.grid(row=2, column=0)
        self.auxvoltlabel.grid(row=3, column=0)
        self.currentlabel.grid(row=4, column=0)
        self.amphourlabel.grid(row=5, column=0)

        self.drivername.grid(row=0, column=1)
        self.drivedate.grid(row=1, column=1)
        self.mainvoltvalue.grid(row=2, column=1)
        self.auxvoltlvalue.grid(row=3, column=1)
        self.currentvalue.grid(row=4, column=1)
        self.amphourvalue.grid(row=5, column=1)

        #define the buttons
        self.button = Button(frame,
                             text="Quit", width=15,
                             command=frame.quit)
        self.record = Button(frame,
                             text="Record", width=15, command=lambda: self.recorddata())


        self.record.grid(row=6, column=0, sticky='e')
        self.button.grid(row=6, column=1, sticky='e')








root= Tk()


app=App(root)
root.mainloop()
