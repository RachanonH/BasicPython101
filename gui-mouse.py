from tkinter import * #Lib Tk interface
from tkinter import ttk
import pyautogui as pg
import webbrowser

GUI = Tk()
GUI.title('Calender program')
GUI.geometry('500x300')

def Calender(): #คลิกที่ตรง bar calender 
    pg.click(1860,1053)

B1 = Button(GUI,text='Calender1',command = Calender)
B1.pack(ipadx = 20, ipady = 10, pady = 20)

B2 = ttk.Button(GUI,text='Calender2',command = Calender)
B2.pack(ipadx = 20, ipady = 10, pady =20)


def Google(): #เปิด GG เข้ามา
    webbrowser.open('https://www.google.com/')

B3 = ttk.Button(GUI,text='Google',command = Google)
B3.pack(ipadx = 20, ipady= 10, pady = 20)


GUI.mainloop()