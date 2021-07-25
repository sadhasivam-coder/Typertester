import time
from threading import Thread
import tkinter
wall=tkinter.Tk()
wall.geometry('550x180')
entry=tkinter.StringVar()
result=tkinter.StringVar()
def opo():
    x=entry.get()
    v=h
    v=0
    for xx in range(len(h)):
        try:
            if x[xx]==h[xx]:
                v+=1
        except:
            pass
    result.set('Your score is '+str(v*2)+'%')
    e1.destroy()
def timer():
    v=0
    while True:
        time.sleep(1)
        if v!=32:
            v+=1
        else:
            opo()
import random
h=''
for x in range(50):
    h+=str(chr(random.randrange(65,122)))
label1=tkinter.Label(wall,text='Typer Tester',font=38)
label1.pack()
label=tkinter.Label(wall,text=h,font=38,fg='green')
label.place(x=25,y=50)
e1=tkinter.Entry(wall,textvariable=entry,width=50,fg='red')
e1.place(x=40,y=80)
label11=tkinter.Label(wall,textvariable=result,font=38,fg='red')
label11.place(x=200,y=100)
thread = Thread(target = timer)
thread.start()
wall.mainloop()