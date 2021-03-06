# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 20:52:11 2019

@author: satnam
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:35:52 2019

@author: satnam
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:26:47 2019

@author: satnam
"""

from tkinter import *
from tkinter.filedialog import askopenfilename
import csv
import os
from tkinter import ttk
import time
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from sklearn.model_selection import train_test_split
from matplotlib.figure import Figure
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor


def raise_frame(frame):
    frame.tkraise()
gui = Tk()

f1=Frame(gui,width=200,height=200)
f2=Frame(gui,width=600,height=600)
f3=Frame(gui,width=600,height=600)
f4=Frame(gui,width=600,height=600)
f5=Frame(gui,width=600,height=600)
for frame in (f1,f2,f3,f4,f5):
    frame.grid(row=0, column=0, sticky='news')
gui.title('Housing Prediction GUI')
#gui.geometry('600x600')
progress_bar = ttk.Progressbar(orient = 'horizontal', length=600, mode='determinate')
progress_bar.grid(row=23, columnspan=3, pady =10)


def data():
    global filename
    filename = askopenfilename(initialdir='C:\\',title = "Select file")
    e1.delete(0, END)
    e1.insert(0, filename)
    import pandas as pd
    global housing
    housing = pd.read_csv(filename)
    global col
    col = list(housing.head(0))
    #print(col)
    for i in range(len(col)):
        box1.insert(i+1, col[i])
def X_values():
    values = [box1.get(idx) for idx in box1.curselection()]
    for i in range(len(list(values))):
        box2.insert(i+1, values[i])
        box1.selection_clear(i+1, END)
    X_values.x1=[]
    for j in range(len(values)):X_values.x1.append(j)
    global x_size
    x_size = len(X_values.x1)
    print(x_size)
    print(X_values.x1)

def y_values():
    values= [box1.get(idx) for idx in box1.curselection()]
    for i in range(len(list(values))):
        box3.insert(i+1, values[i])
    y_values.y1=[]
    for j in range(len(values)):y_values.y1.append(j)
    print(y_values.y1)

def clear():
    
    python = sys.executable
    os.execl(python, python, * sys.argv)
    

def randomforest():
    progress()
    y_pred=0
    X = housing.iloc[:,X_values.x1].values
    y = housing.iloc[:,y_values.y1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7 ,test_size = 0.3, random_state=100)
    regressor = RandomForestRegressor(n_estimators = 125)
    regressor.fit(X_train,np.ravel(y_train))
    X_testy=[[area.get(),bedroom.get(),bathroom.get(),stories.get(),mainroad.get(),guestroom.get()]]
    y_pred = regressor.predict(X_testy)
    result= f'{y_pred[0]:,} Rs'
    t2.insert(END,result)
    y_pred = regressor.predict(X_test)

    c = [i for i in range(1,165,1)]
    fig = Figure(figsize=(6,6))
    ax1 = fig.add_subplot(311)
    ax1.plot(c,y_test, color="blue", linewidth=2.5, linestyle="-")  

    ax1.set_title ("Actual", fontsize=16)
    ax1.set_ylabel("Price", fontsize=14)    
    bar1 = FigureCanvasTkAgg(fig, f4)
    bar1.get_tk_widget().pack()
    bar1.draw()
    
    fig2=Figure(figsize=(6,6))
    ax2 = fig2.add_subplot(312)
    ax2.plot(c,y_pred, color="red",  linewidth=2.5, linestyle="-")  #Plotting predicted
    ax2.set_title ("Predicted", fontsize=16)
    ax2.set_ylabel("Price", fontsize=14)
    ax2.set_xlabel("Index", fontsize=14)
    bar2 = FigureCanvasTkAgg(fig2, f4)
    bar2.get_tk_widget().pack()
    bar2.draw()
    
    fig3=Figure(figsize=(10,10))     # Size of the figure
    ax3 = fig.add_subplot(313)
    sns.heatmap(housing.corr(),annot = True,ax=ax3)
    bar3 = FigureCanvasTkAgg(fig3, f4)
    bar3.get_tk_widget().pack() 
    bar3.draw()

def progress():
    progress_bar['maximum']=100

    for i in range(101):
        time.sleep(0.01)
        progress_bar['value'] = i
        progress_bar.update()

    progress_bar['value'] = 0
def register_user():
  username_info = username.get()
  password_info = password.get()
  file=open(username_info+".txt", "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()
  username_entry.delete(0, END)
  password_entry.delete(0, END)
  Label(f5, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()
def login_verify():
  username1 = username_verify.get()
  password1 = password_verify.get()
  list_of_files = os.listdir()  

  if username1+'.txt' in list_of_files:
      file1 = open(username1+'.txt', "r")
      verify = file1.read().splitlines()
      if password1 in verify:
          raise_frame(f2)
      else:
          Label(f1, text = "Wrong Password", fg = "green" ,font = ("calibri", 11)).pack()
  
  else:
      Label(f1, text = "Not Found", fg = "green" ,font = ("calibri", 11)).pack()
global username
global password
global username_entry
global password_entry
username = StringVar()
password = StringVar()
 
Label(f5, text = "Please enter details below").pack()
Label(f5, text = "").pack()
Label(f5, text = "Username * ").pack()

username_entry = Entry(f5, textvariable = username)
username_entry.pack()
Label(f5, text = "Password * ").pack()
password_entry =Entry(f5, textvariable = password)
password_entry.pack()
Label(f5, text = "").pack()
Button(f5, text = "Register", width = 10, height = 1, command = register_user).pack()   

im = PhotoImage(file='r.gif') # Create the PhotoImage widget
# Add the photo to a label:
Label(f1, image=im).pack() # Create a label with image
# Always keep a reference to avoid garbage collection
 
bedroom = IntVar()
bedroom.set(None)
bathroom = IntVar()
bathroom.set(None)
stories = IntVar()
stories.set(None)
mainroad = IntVar()
mainroad.set(None)
guestroom = IntVar()
guestroom.set(None)
l1=Label(f2, text='Select Data File')
l1.grid(row=0, column=0)
e1 = Entry(f2,text='')
e1.grid(row=0, column=1)
Button(f2,text='open', command=data).grid(row=0, column=2)
box1 = Listbox(f2,selectmode='multiple')
box1.grid(row=10, column=0)
Button(f2, text='Clear All/Log Out',command=clear).grid(row=12,column=0)
box2 = Listbox(f2)
box2.grid(row=10, column=1)
Button(f2, text='Select X', command=X_values).grid(row=12,column=1)
box3 = Listbox(f2)
box3.grid(row=10, column=2) 
Button(f2, text='Select y', command=y_values).grid(row=12,column=2)
Button(f2, text='Solution', command=randomforest).grid(row=20, column=1)
Button(f2, text='View Reports', command=lambda:raise_frame(f4)).grid(row=24, column=1)
areaLb = Label(f2, text="Area:",font=("Trebuchet MS", 12))
areaLb.grid(row=13, column=0, pady=10, sticky=W)
bedLb = Label(f2, text="Bedroom:",font=("Trebuchet MS", 12))
bedLb.grid(row=14, column=0, pady=10, sticky=W)
bathLb = Label(f2, text="Bathroom:",font=("Trebuchet MS", 12))
bathLb.grid(row=15, column=0, pady=10, sticky=W)
S4Lb = Label(f2, text="Stories:",font=("Trebuchet MS", 12))
S4Lb.grid(row=16, column=0, pady=10, sticky=W)
S5Lb = Label(f2, text="Mainroad:",font=("Trebuchet MS", 12))
S5Lb.grid(row=17, column=0, pady=10, sticky=W)
S6Lb = Label(f2, text="Guestroom:",font=("Trebuchet MS", 12))
S6Lb.grid(row=18, column=0, pady=10, sticky=W)

OPTIONS = [1,2,3,4,5]
OPTIONS1 = [0,1]

area=Entry(f2)
area.grid(row=13,column=1)

bedEn = OptionMenu(f2, bedroom,*OPTIONS)
bedEn.grid(row=14, column=1)

bathEn = OptionMenu(f2, bathroom,*OPTIONS)
bathEn.grid(row=15, column=1)

S3En = OptionMenu(f2, stories,*OPTIONS)
S3En.grid(row=16, column=1)

S4En = OptionMenu(f2, mainroad,*OPTIONS1)
S4En.grid(row=17, column=1)

S5En = OptionMenu(f2, guestroom,*OPTIONS1)
S5En.grid(row=18, column=1)

t2 = Text(f2, height=1, width=40)
t2.grid(row=22,column=1)

global username_verify
global password_verify
username_verify = StringVar()
password_verify = StringVar()
l=Label(f1, text="Username : ", font=("Trebuchet MS", 16)).pack()
eu = Entry(f1,textvariable=username_verify,width="20").pack()
l1=Label(f1, text="Password : ", font=("Trebuchet MS", 16)).pack()
ep = Entry(f1, textvariable=password_verify, show="*",width="20").pack()
c1 = Checkbutton(f1, text = "Keep me logged in").pack()

Button(f1,text='Login', command=login_verify,height = 3, width = 10).pack()
Button(f1,text='New User ?, Register', command=lambda:raise_frame(f5),height = 3).pack()
Button(f1,text='View Default Dataset/ Properties', command=lambda:raise_frame(f3),height = 3).pack()
'''
for r in range(5):
   for c in range(5):
      Label(f1, text='  ',
         borderwidth=1 ).grid(row=r,column=c)
      '''
with open("C:\\Users\\satnam\\Documents\\Housing2.csv", newline = "") as file:
   reader = csv.reader(file)

   # r and c tell us where to grid the labels
   r = 0
   for col in reader:
      c = 0
      for row in col:
         # i've added some styling
         label = Label(f3, width = 10, height = 2, \
                               text = row, relief =RIDGE)
         label.grid(row = r, column = c)
         c += 1
      r += 1
Button(f3,text='Go back', command=lambda:raise_frame(f1)).grid(row=70, column=3)
Button(f4,text='Go back', command=lambda:raise_frame(f2)).pack()
Button(f5,text='Go back', command=lambda:raise_frame(f1)).pack()


raise_frame(f1)
gui.mainloop()
