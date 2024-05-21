import tkinter as tk
from tkinter.ttk import Combobox
from PIL import ImageTk,Image
from datetime import datetime
from pygame import mixer 
from threading import Thread
from time import sleep
#colors
bg_color = '#ffffff'
co1 = "#566FC6"#BLUE
co2 = "#000000"#black

#window 
window = tk.Tk()
window.title("My_alarm")
window.geometry('350x150')
window.configure(bg=bg_color)

#frames up
frame_line = tk.Frame (window ,width=400,height=5,bg=co1)
frame_line.grid(row=0,column=0)

frame_body = tk.Frame (window ,width=400,height=290,bg = bg_color)
frame_body.grid(row=1,column=0)

img =Image.open('icons8-alarm-100.png')
img.resize((100,100))
img = ImageTk.PhotoImage(img)

app_image = tk.Label(frame_body,height=100,image=img,bg=bg_color)
app_image.place(x=10,y=10)

name = tk.Label(frame_body, text = "Alarm", height=1 , font=('Ivy 18 bold'), bg=bg_color)
name.place(x=125,y=10)

hour = tk.Label(frame_body, text = "hour", height=1 , font=('Ivy 10 bold'), bg=bg_color,fg=co1)
hour.place(x=127,y=40)
c_hour = Combobox(frame_body,width=2,font=('arial 15'))
c_hour['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12")
c_hour.current(0)
c_hour.place(x=130,y=58)

min = tk.Label(frame_body, text = "Min", height=1 , font=('Ivy 10 bold'), bg=bg_color,fg=co1)
min.place(x=180,y=40)
c_min = Combobox(frame_body,width=2,font=('arial 15'))
c_min['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_min.current(0)
c_min.place(x=180,y=58)

sec = tk.Label(frame_body,text = "Sec",height=1 , font=('Ivy 10 bold'), bg=bg_color,fg=co1)
sec.place(x=230,y=40)
c_sec = Combobox(frame_body,width=2,font=('arial 15'))
c_sec['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_sec.current(0)
c_sec.place(x=230,y=58)

period = tk.Label(frame_body,text = "Period",height=1 , font=('Ivy 10 bold'), bg=bg_color,fg=co1)
period.place(x=280,y=40)
c_period = Combobox(frame_body,width=3,font=('arial 15'))
c_period['values'] = ("AM","PM")
c_period.current(0)
c_period.place(x=280,y=58)

def activate_alarm():
    t=Thread(target=alarm)
    t.start()
def deactivate_alarm():
    print('Deactivate Alarm: ',select.get())
    mixer.music.stop()

select = tk.IntVar()

rad1 = tk.Radiobutton(frame_body,font=('arial 10 bold'),value = 1 , text = "Activate" , bg = bg_color,command=activate_alarm,variable=select)
rad1.place(x=125,y=95)

def sound_alarm():
    mixer.music.load('best_alarm.mp3')
    mixer.music.play()
    select.set(0)
    rad2 = tk.Radiobutton(frame_body,font=('arial 10 bold'),value = 2 , text = "Deactivate" , bg = bg_color,command=deactivate_alarm,variable=select)
    rad2.place(x=187,y=95)

def alarm():
    while True:
        control = select.get()
        print(control)
        alarm_hour = c_hour.get()
        alarm_min = c_min.get()
        alarm_sec = c_sec.get()
        alarm_period = c_period.get()
        alarm_period = str(alarm_period.upper)

        now = datetime.now()

        hour=now.strftime("%I")
        min=now.strftime("%M")
        sec =now.strftime("%S")
        period=now.strftime("%p")

        if control == 1:
            if alarm_hour==hour:
                if alarm_min==min:
                    if alarm_sec==sec:
                        print("Time to take a break !")
                        sound_alarm()
        sleep(1)


mixer.init()
window.mainloop() 