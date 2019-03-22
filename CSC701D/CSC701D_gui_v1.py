#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')


# 
# # CSC 701D Project 1
# 
# 
# Submitted by: Gara, Pacot, Santillan
# 
# 

# In[ ]:


import matpylib as mp #Defined Library by the Authors

import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.backends.backend_tkagg
import matplotlib.backends.tkagg as tkagg
import matplotlib.transforms as transforms
from matplotlib.backends.backend_agg import FigureCanvasAgg
import tkinter as tk
from tkinter import *
import numpy as np
import sys
import math
import traceback

master = tk.Tk()
transform_op,options,gen_points= [],[],[]
counter = -1
CheckVar1, CheckVar2, CheckVar3, CheckVar4, CheckVar5, CheckVar6, CheckVar7, CheckVar8 = IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()

#-----------------------FINAL FUNCTIONS--------------------------------#
def collect_number(p):
    op = [int(s) for s in re.findall(r'-?\d+\.?\d*', p)]
    return op

def collect_string(p):
    op = ''.join([str(s) for s in re.findall(r'[A-Z]*[a-z]*', p)])
    return op

def prompt1():
     messagebox.showinfo("Ga_Pa_Sa Project", "A program that shows the use of matrices in Computer Graphics.\nAllow the user to input a 2D object which can be one or more points, line segments, \nvectors, polygons such as rectangle, square, and etc., \ntogether with samples of conics like circle, ellipse, parabola, hyperbola.\nAllow the user to choose what operation to do with the object which are the following: translate or change in position, rotate or change in orientation, shear or change in shape, \nuniform or non-uniform scale or change size, dilate, contract, reflect, projection")

def save_points():
    global gen_points
    global options

    try:
        val = input1.get() 
        
        if len(val) > 0:
            
            if Points.get() == 1:
                t1 = splitter(val,',')
                for i in range(0,len(t1)):
                    t2 = splitter(t1[i],' ')
                    x = int(t2[0].strip())
                    y = int(t2[1].strip())
                    t3 = [x,y]
                    gen_points.append(t3)
                options = 1
                messagebox.showinfo("Ga_Pa_Sa Project", "Success!")

            if Circle1.get() == 1:
                temp = splitter(val,',')
                points = mp.circle(int(temp[0]),int(temp[1]),int(temp[2]))
                gen_points=points
                options = 2
                messagebox.showinfo("Ga_Pa_Sa Project", "Success!")

            if Polygon1.get() == 1:
                t1 = splitter(val,',')
                for i in range(0,len(t1)):
                    t2 = splitter(t1[i],' ')
                    x = int(t2[0].strip())
                    y = int(t2[1].strip())
                    t3 = [x,y]
                    gen_points.append(t3)
                options = 3
                messagebox.showinfo("Ga_Pa_Sa Project", "Success!")
                
            if Parabola1.get() == 1:
                temp = splitter(val,',')
                points = mp.parabola(float(temp[0]),float(temp[1]),int(temp[2]),int(temp[3]))
                gen_points=points
                options = 4
                messagebox.showinfo("Ga_Pa_Sa Project", "Success!")
                
            if Ellipse1.get() == 1:
                temp = splitter(val,',')
                points = mp.ellipse(int(temp[0]),int(temp[1]),int(temp[2]),int(temp[3]))
                gen_points=points
                options = 5
                messagebox.showinfo("Ga_Pa_Sa Project", "Success!")
                
            if Hyperbola1.get() == 1:
                temp = splitter(val,',')
                points = mp.hyperbola(int(temp[0]),int(temp[1]),int(temp[2]),int(temp[3]),str(temp[4]))
                gen_points=points
                options = 6
                messagebox.showinfo("Ga_Pa_Sa Project", "Success!")
                
        else:
            messagebox.showinfo("Ga_Pa_Sa Project", "Error!")
            
    except Exception as e:
        print('Oops! something went wrong while trying saving the generated points.')
        
def Record_Transformations():
    
    if CheckVar1.get() == 1:
        answer = simpledialog.askstring("Translation Entry!", "\n\nSample Input: T(?,?) or t(1,2)\n                   \n",
                            parent=master)
        try:
            if (answer[0] == 'T' or answer[0] == 't'):
                transform_op.append(answer)
                var4.set(transform_op)
            else:
                messagebox.showinfo("", "Error!!!")
        except Exception as e:
            print('NOP!')
            
    if CheckVar2.get() == 1:
        answer = simpledialog.askstring("Rotation Entry!", "Inputs are angle in degrees and \noptional x and y if rotation is with respect to point (x, y)\n\nSample Entry: R(90,cw) or r(90,cc)\ncc=counter clockwise\ncw=clockwise",
                            parent=master)
        try:
            if (answer[0] == 'R' or answer[0] == 'r'):
                transform_op.append(answer)
                var4.set(transform_op)
            else:
                messagebox.showinfo("", "Error!!!")
        except Exception as e:
            print('NOP!')
            
    if CheckVar3.get() == 1:
        answer = simpledialog.askstring("Shear Entry!", "Shear - creates a shear transformation matrix\nInputs are shear value along x and y,\n if 0 then no shear along that axis. default is 0\n\nSample Entry: SH(4,x) or sh(4,y)",
                            parent=master)
        try:
            if (answer[0] == 'S' and answer[1] == 'H') or (answer[0] == 's' and answer[1] == 'h'):
                transform_op.append(answer)
                var4.set(transform_op)
            else:
                messagebox.showinfo("", "Error!!!")
        except Exception as e:
            print('NOP!')
            
    if CheckVar4.get() == 1:
        answer = simpledialog.askstring("Scale Entry!", "Scale(x, y) - creates a scale transformation matrix\nInput is scale in x and y\n\nSample Entry: S(4,4) or s(5,5)",
                            parent=master)
        try:
            if (answer[0] == 'S' or answer[0] == 's'):
                transform_op.append(answer)
                var4.set(transform_op)
            else:
                messagebox.showinfo("", "Error!!!")
        except Exception as e:
            print('NOP!')
            
    if CheckVar5.get() == 1:
        answer = simpledialog.askstring("Dilate Entry!", "Dilate(x) - creates a dilation transformation matrix\nInput is dilation value\nDilation value must be more than 1 or \nelse will be set to 1 and 1 = no dilation\n\nSample Entry: D(4) or d(5)",
                            parent=master)
        try:
            if (answer[0] == 'D' or answer[0] == 'd'):
                transform_op.append(answer)
                var4.set(transform_op)
            else:
                messagebox.showinfo("", "Error!!!")
        except Exception as e:
            print('NOP!')
            
    if CheckVar6.get() == 1:
        answer = simpledialog.askstring("Contract Entry!", "\n\nContract(x) - creates a contraction transformation matrix\nInput is contraction value\ncontraction value must be less than 1 or else will be set to 1 and means no contraction\n\nSample Entry: C(4) or c(5)",
                            parent=master)
        try:
            if (answer[0] == 'C' or answer[0] == 'c'):
                transform_op.append(answer)
                var4.set(transform_op)
            else:
                messagebox.showinfo("", "Error!!!")
        except Exception as e:
            print('NOP!')
            
    if CheckVar7.get() == 1:
        answer = simpledialog.askstring("Reflect Entry!", "\n\nReflect axis = 2 - creates a reflection transformation matrix\nInput is axis value 0=x axis reflection; 1=y axis reflection; \n2=reflection along origin; 3=reflection along y=x line\n\nSample Entry: RF(x) or rf(y) or rf(z)",
                            parent=master)
        try:
            if (answer[0] == 'R' and answer[1] == 'F') or (answer[0] == 'r' and answer[1] == 'f'):
                transform_op.append(answer)
                var4.set(transform_op)
            else:
                messagebox.showinfo("", "Error!!!")
        except Exception as e:
            print('NOP!')
            
    if CheckVar8.get() == 1:
        answer = simpledialog.askstring("Projection Entry!", "\n\nSample Entry: P(4,4) or p(5,5)",
                            parent=master)
        try:
            if (answer[0] == 'P' or answer[0] == 'p'):
                transform_op.append(answer)
                var4.set(transform_op)
            else:
                messagebox.showinfo("", "Error!!!")
        except Exception as e:
            print('NOP!')
    rem_trans.set(str(len(transform_op)))
    
def Make_Transformations():
    global counter,gen_points,var4,transform_op
    points = []
    
    if len(gen_points) > 0:
        try:
            counter +=1
            collection = collect_number(transform_op[counter])
            collection1 = collect_string(transform_op[counter])

            if transform_op[counter][0].upper() == 'C':
                temp = mp.contract(gen_points, collection[0])
            if transform_op[counter][0].upper() == 'D':
                temp = mp.dilate(gen_points, collection[0])
            if transform_op[counter][0].upper() == 'P':
                temp = mp.project(gen_points, collection[0],collection[1])
            if (transform_op[counter][0].upper() == 'R' and transform_op[counter][1].upper() == 'F'):
                temp = mp.reflect(gen_points, collection1[2])
            if (transform_op[counter][0].upper() == 'R' and transform_op[counter][1].upper() != 'F'):
                merge = collection1[1] + collection1[2]
                temp = mp.rotate(gen_points, collection[0],str(merge))
            if (transform_op[counter][0].upper() == 'S' and transform_op[counter][1].upper() != 'H'):
                temp = mp.scale(gen_points, collection[0],collection[1])
            if (transform_op[counter][0].upper() == 'S' and transform_op[counter][1].upper() == 'H'):
                temp = mp.shear(gen_points, collection[0],str(collection1[2]))
            if transform_op[counter][0].upper() == 'T':
                temp = mp.translate(gen_points, collection[0],collection[1])

            gen_points = []
            gen_points = temp

            p = rem_trans.get()
            m = int(p) - 1
            rem_trans.set(str(m))

            #Display Coordinates before any transformations
            listbox.delete(0, END)
            listbox.insert(END, "Scroll transformed point/s here:")
            for items in gen_points:
                listbox.insert(END, [items])
            display_transformation()

        except Exception as e:
            print('No Operation for Transformations!!')
    else :
        messagebox.showinfo("Ga_Pa_Sa Project", "Oops! Something went wrong.")
        
def draw_figure(canvas, figure, loc=(0, 0)):
    
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)
    
    return photo

def display_shape():
   
    if len(gen_points) > 0:
        
        # Dedicated line for conics
        if options == 2 or options == 4 or options == 5 or options == 6:
            x, y = [], []
            for i in gen_points:
                x.append(i[0])
                y.append(i[1])
        
        X1,Y1 = [],[]
        fig1 = mpl.figure.Figure(figsize=(10, 5)) #-------------Figure 1---------------#
        ax1 = fig1.add_axes([0, 0, 1, 1],facecolor='#CCCCCC')
        plt.style.use('bmh')
        ax1 = fig1.add_subplot(111)
        
        #Points
        if options == 1: 
            for i in range(0,len(gen_points)):
                X1.append(int(gen_points[i][0]))
                Y1.append(int(gen_points[i][1]))
            ax1.scatter(X1, Y1, lw=2, color='blue')
            
        #Conics  
        if options == 2 or options == 5 or options == 6: 
            x1, x2 = [], []
            y1, y2 = [], []
            for i,j in zip(x[0:len(x)//2], y[0:len(y)//2]):
                x1.append(i)
                y1.append(j)
            ax1.plot(x1, y1,lw=2, color='blue')
            for i,j in zip(x[len(x)//2:len(x)], y[len(y)//2:len(y)]):
                x2.append(i)
                y2.append(j)
            ax1.plot(x2, y2,lw=2, color='blue')

        if options == 4: 
            ax1.plot(x, y, lw=2, color='blue')
            
        #Polygon  
        if options == 3: 
            for i in range(0,len(gen_points)):
                X1.append(int(gen_points[i][0]))
                Y1.append(int(gen_points[i][1]))
            ax1.plot(X1,Y1, lw=2, color='blue')

        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        ax1.set_aspect('equal', adjustable='box')
        ax1.set_title('Input',size=20)
        ax1.set_ylim(-1000,1000)
        ax1.set_xlim(-1000,1000)
        ax1.plot(list(range(-1000,1000)), mp.zeros(2000), color='black', linestyle='-')
        ax1.plot(mp.zeros(2000), list(range(-1000,1000)), color='black', linestyle='-')

        fig_x1, fig_y1 = 30,6
        fig_photo1 = draw_figure(canvas, fig1, loc=(fig_x1, fig_y1))
        fig_w, fig_h = fig_photo1.width(), fig_photo1.height()
        
        #Display Coordinates before any transformations
        listbox.delete(0, END)
        listbox.insert(END, "Scroll transformed point/s here:")
        for items in gen_points:
            listbox.insert(END, [items])
        
        mainloop()
    else:
        messagebox.showinfo("Ga_Pa_Sa Project", "Error while displaying Shape!")
        
def display_transformation():
    X1,Y1 = [],[]
    if len(gen_points) > 0:
        
        # Dedicated line for conics
        if options == 2 or options == 4 or options == 5 or options == 6:
            x, y = [], []
            for i in gen_points:
                x.append(i[0])
                y.append(i[1])

        fig = mpl.figure.Figure(figsize=(9.8, 5)) #-------------Figure 2----------------#
        ax = fig.add_axes([0, 0, 1, 1],facecolor='#CCCCCC')
        ax = fig.add_subplot(111)
        
        #Points
        if options == 1: 
            for i in range(0,len(gen_points)):
                X1.append(int(gen_points[i][0]))
                Y1.append(int(gen_points[i][1]))
            ax.scatter(X1, Y1, lw=2, color='blue')
            
        #Conics  
        if options == 2 or options == 5 or options == 6: 
            x1, x2 = [], []
            y1, y2 = [], []
            for i,j in zip(x[0:len(x)//2], y[0:len(y)//2]):
                x1.append(i)
                y1.append(j)
            ax.plot(x1, y1,lw=2, color='blue')
            for i,j in zip(x[len(x)//2:len(x)], y[len(y)//2:len(y)]):
                x2.append(i)
                y2.append(j)
            ax.plot(x2, y2,lw=2, color='blue')

        if options == 4: 
            ax.plot(x, y, lw=2, color='blue')
            
        #Polygon    
        if options == 3: 
            for i in range(0,len(gen_points)):
                X1.append(int(gen_points[i][0]))
                Y1.append(int(gen_points[i][1]))
            ax.plot(X1,Y1, lw=2, color='blue')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_aspect('equal', adjustable='box')
        ax.set_title('Output',size=20)
        ax.set_ylim(-1000,1000)
        ax.set_xlim(-1000,1000)
        ax.plot(list(range(-1000,1000)), mp.zeros(2000), color='black', linestyle='-')
        ax.plot(mp.zeros(2000), list(range(-1000,1000)), color='black', linestyle='-')
        
        fig_x, fig_y = 799,6
        fig_photo = draw_figure(canvas, fig, loc=(fig_x, fig_y))
        
        mainloop()
    else:
        messagebox.showinfo("Ga_Pa_Sa Project", "Error while displaying Transformation/s!!")

def _quit():
    master.quit()     
    master.destroy() 

def splitter(value,sym):
    new_val = []
    a = value.split(sym)
    for i in range(0,len(a)):
        new_val.append(a[i].strip(' '))
    return new_val
       
def clear():
    global gen_points,counter,transform_op,options,canvas,Matrix_val,C1,C2,C3,C4,C5,C6,C7,C8
    
    canvas = canvas
    gen_points,options,transform_op = [],[],[]
    var4.set("")
    input1.set("")
    Matrix_val.set("") 
    rem_trans.set("0")
    listbox.delete(0, END)
    counter = -1
    C1.deselect()
    C2.deselect()
    C3.deselect()
    C4.deselect()
    C5.deselect()
    C6.deselect()
    C7.deselect()
    C8.deselect()
    Point_var.deselect()
    Circle1_var.deselect()
    Polygon1_var.deselect()
    Parabola1_var.deselect()
    Ellipse1_var.deselect()
    Hyperbola1_var.deselect()
    
    canvas.update()
    screen_blocker()
    
def screen_blocker():
    global canvas
    canvas = canvas
    x,y1,y2=[],[],[] 
    
    fig1 = mpl.figure.Figure(figsize=(10, 5)) #-------------Figure 1---------------#
    ax1 = fig1.add_axes([0, 0, 1, 1],facecolor='#CCCCCC')
    plt.style.use('bmh')
    ax1 = fig1.add_subplot(111)
    ax1.plot(x, y1, lw=2, color='red')
    ax1.plot(x, y2, lw=2, color='red')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_aspect('equal', adjustable='box')
    ax1.set_title('Input',size=20)
    ax1.set_ylim(-1000,1000)
    ax1.set_xlim(-1000,1000)
    ax1.plot(list(range(-1000,1000)), mp.zeros(2000), color='black', linestyle='-')
    ax1.plot(mp.zeros(2000), list(range(-1000,1000)), color='black', linestyle='-')
    fig_x1, fig_y1 = 30,6
    fig_photo1 = draw_figure(canvas, fig1, loc=(fig_x1, fig_y1))
    fig_w, fig_h = fig_photo1.width(), fig_photo1.height()

    fig = mpl.figure.Figure(figsize=(9.8, 5)) #-------------Figure 2----------------#
    ax = fig.add_axes([0, 0, 1, 1],facecolor='#CCCCCC')
    ax = fig.add_subplot(111)
    ax.plot(x, y1, lw=2, color='red')
    ax.plot(x, y2, lw=2, color='red')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_aspect('equal', adjustable='box')
    ax.set_title('Output',size=20)
    ax.set_ylim(-1000,1000)
    ax.set_xlim(-1000,1000)
    ax.plot(list(range(-1000,1000)), mp.zeros(2000), color='black', linestyle='-')
    ax.plot(mp.zeros(2000), list(range(-1000,1000)), color='black', linestyle='-')
    fig_x, fig_y = 799,6
    fig_photo = draw_figure(canvas, fig, loc=(fig_x, fig_y))
    
    mainloop()

############################# MAIN OF THE PROGRAM #################################
   
w, h = 1532, 680 #----------------------------CANVAS--------------------------#
canvas = tk.Canvas(master, width=w, height=h)
canvas.grid(row=0, column=0)
canvas.pack()

master.geometry("+{}+{}".format(0, 0)) #-------------USER MENU----------------#
master.title("CSC701D Project")
menu = Menu(master)
master.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Tutorial", command="")
filemenu.add_separator()
aboutmenu = Menu(menu)
menu.add_cascade(label="About", command=prompt1)
exitmenu = Menu(menu)
menu.add_cascade(label="Exit", menu="",command=_quit)

x,y1,y2=[],[],[]
fig1 = mpl.figure.Figure(figsize=(10, 5)) #-------------Figure 1---------------#
ax1 = fig1.add_axes([0, 0, 1, 1],facecolor='#CCCCCC')
plt.style.use('bmh')
ax1 = fig1.add_subplot(111)
ax1.plot(x, y1, lw=2, color='red')
ax1.plot(x, y2, lw=2, color='red')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_aspect('equal', adjustable='box')
ax1.set_title('Input',size=20)
ax1.set_ylim(-1000,1000)
ax1.set_xlim(-1000,1000)
ax1.plot(list(range(-1000,1000)), mp.zeros(2000), color='black', linestyle='-')
ax1.plot(mp.zeros(2000), list(range(-1000,1000)), color='black', linestyle='-')
fig_x1, fig_y1 = 30,6
fig_photo1 = draw_figure(canvas, fig1, loc=(fig_x1, fig_y1))
fig_w, fig_h = fig_photo1.width(), fig_photo1.height()

fig = mpl.figure.Figure(figsize=(9.8, 5)) #-------------Figure 2----------------#
ax = fig.add_axes([0, 0, 1, 1],facecolor='#CCCCCC')
ax = fig.add_subplot(111)
ax.plot(x, y1, lw=2, color='red')
ax.plot(x, y2, lw=2, color='red')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_aspect('equal', adjustable='box')
ax.set_title('Output',size=20)
ax.set_ylim(-1000,1000)
ax.set_xlim(-1000,1000)
ax.plot(list(range(-1000,1000)), mp.zeros(2000), color='black', linestyle='-')
ax.plot(mp.zeros(2000), list(range(-1000,1000)), color='black', linestyle='-')
fig_x, fig_y = 799,6
fig_photo = draw_figure(canvas, fig, loc=(fig_x, fig_y))

#-------------Other Options in Canvas----------------#
var = StringVar() 
label = Label( master, textvariable=var, relief=RAISED )
var.set("Transformation Options:")
label.pack()   
label.place(relx=.1, rely=.53, anchor="c")
label.config(font=("Courier", 14),bg='black',fg='white')

C1 = Checkbutton(master, text = "Translate", variable = CheckVar1,                height=2,                width = 10)
C1.pack()
C1.place(relx=.04, rely=.58, anchor="c")

C2 = Checkbutton(master, text = "Rotate", variable = CheckVar2,         height=2,         width = 10)
C2.pack()
C2.place(relx=.10, rely=.58, anchor="c")

C3 = Checkbutton(master, text = "Shear", variable = CheckVar3,          height=2,          width = 10)
C3.pack()
C3.place(relx=.16, rely=.58, anchor="c")

C4 = Checkbutton(master, text = "Scale", variable = CheckVar4,          height=2,          width = 10)
C4.pack()
C4.place(relx=.21, rely=.58, anchor="c")

C5 = Checkbutton(master, text = "Dilate", variable = CheckVar5,       height=2,       width = 10)
C5.pack()
C5.place(relx=.26, rely=.58, anchor="c")

C6 = Checkbutton(master, text = "Contract", variable = CheckVar6,          height=2,          width = 10)
C6.pack()
C6.place(relx=.32, rely=.58, anchor="c")

C7 = Checkbutton(master, text = "Reflect", variable = CheckVar7,          height=2,          width = 10)
C7.pack()
C7.place(relx=.39, rely=.58, anchor="c")

C8 = Checkbutton(master, text = "Projection", variable = CheckVar8,          height=2,          width = 10)
C8.pack()
C8.place(relx=.46, rely=.58, anchor="c")

var3 = StringVar()
label3 = Label( master, textvariable=var3 )
var3.set("List of Transformation Operation/s:")
label3.pack()   
label3.place(relx=.14, rely=.67, anchor="c")
label3.config(font=("Courier", 14))

scrollbar = Scrollbar(master)
scrollbar.pack( side = RIGHT)

var4 = StringVar()
label4 = Entry( master, textvariable=var4, width=76, state=DISABLED, xscrollcommand = scrollbar.set )
var4.set("_")
label4.pack()   
label4.place(relx=.26, rely=.71, anchor="c")
label4.config(font=("Courier", 12))

var1 = StringVar() #---------------Shape Options---------------#
label2 = Label( master, textvariable=var1, relief=RAISED )
var1.set("Shape Options:")
label2.pack()   
label2.place(relx=.06, rely=.76, anchor="c")
label2.config(font=("Courier", 14),bg='black',fg='white')

var1 = StringVar()
label2 = Label( master, textvariable=var1 )
var1.set("Enter Points Here:")
label2.pack()   
label2.place(relx=.07, rely=.81, anchor="c")
label2.config(font=("Courier", 12))

input1 = StringVar() #-----------------User Input Textbox---------------------#
user_entry = Entry( master, textvariable=input1, width=51 )
user_entry.pack()   
user_entry.place(relx=.30, rely=.81, anchor="c")
user_entry.config(font=("Courier", 12))

Points = IntVar()  #-----------------Point Shape---------------------#
Point_var = Checkbutton(master, text = "Points", variable = Points,                height=2,                width = 10)
Point_var.pack()
Point_var.place(relx=.03, rely=.85, anchor="c")

Circle1 = IntVar()  #-----------------Circle Shape---------------------#
Circle1_var = Checkbutton(master, text = "Circle", variable = Circle1,                height=2,                width = 10,
               command="")
Circle1_var.pack()
Circle1_var.place(relx=.08, rely=.85, anchor="c")

Polygon1 = IntVar()  #-----------------Polygon Shape---------------------#
Polygon1_var= Checkbutton(master, text = "Polygon", variable = Polygon1,                height=2,                width = 10,
               command="")
Polygon1_var.pack()
Polygon1_var.place(relx=.13, rely=.85, anchor="c")

Parabola1 = IntVar()  #-----------------Parabola Shape---------------------#
Parabola1_var= Checkbutton(master, text = "Parabola", variable = Parabola1,                height=2,                width = 10,
               command="")
Parabola1_var.pack()
Parabola1_var.place(relx=.19, rely=.85, anchor="c")

Ellipse1 = IntVar()  #-----------------Ellipse Shape---------------------#
Ellipse1_var= Checkbutton(master, text = "Ellipse", variable = Ellipse1,                height=2,                width = 10,
               command="")
Ellipse1_var.pack()
Ellipse1_var.place(relx=.25, rely=.85, anchor="c")

Hyperbola1 = IntVar()  #-----------------Hyperbola Shape---------------------#
Hyperbola1_var= Checkbutton(master, text = "Hyperbola", variable = Hyperbola1,                height=2,                width = 10,
               command="")
Hyperbola1_var.pack()
Hyperbola1_var.place(relx=.31, rely=.85, anchor="c")

var = StringVar() #-----------------Matrix Display---------------------#
label = Label( master, textvariable=var, relief=RAISED )
var.set("Resulting Matrix:")
label.pack()   
label.place(relx=.58, rely=.53, anchor="c")
label.config(font=("Courier", 14),bg='black',fg='white')

Matrix_val = StringVar()     
Matrix_label = Label( master, textvariable=Matrix_val, width=20,relief=RAISED)
Matrix_val.set("[ ]")
Matrix_label.pack()   
Matrix_label.place(relx=.75, rely=.62, anchor="c")
Matrix_label.config(font=("Courier", 15))

listbox = Listbox(master,width=70, height=7)
listbox.pack()
listbox.place(relx=.52, rely=.56)
listbox.config(font=("Courier", 12))

rem1_var = StringVar() #-----------Reminders------------#
rem1 = Label( master, textvariable=rem1_var, relief=RAISED ) 
rem1_var.set('User Input Reminders:')
rem1.pack()   
rem1.place(relx=.59, rely=.78, anchor="c")
rem1.config(font=("Courier", 12),bg='black',fg='white')

rem2_var = StringVar()
rem2 = Label( master, textvariable=rem2_var ) 
rem2_var.set('Points/Polygons: Sample Entry ===> 0 500,500 500,500 100,0 100,0 500')
rem2.pack()   
rem2.place(relx=.74, rely=.83, anchor="c")
rem2.config(font=("Courier", 12))

uni_var = StringVar()
uni = Label( master, textvariable=uni_var ) 
uni_var.set('Circle: Sample Entry ===> 0,0,100 (x,y,radius)')
uni.pack()   
uni.place(relx=.67, rely=.86, anchor="c")
uni.config(font=("Courier", 12))

uni_var = StringVar()
uni = Label( master, textvariable=uni_var ) 
uni_var.set('Parabola: Sample Entry ===> -0.02,-0.002,700,200 (ax^2+bx+c=0)')
uni.pack()   
uni.place(relx=.72, rely=.89, anchor="c")
uni.config(font=("Courier", 12))

uni_var = StringVar()
uni = Label( master, textvariable=uni_var ) 
uni_var.set('Ellipse: Sample Entry ===> 200,200,0,0  ')
uni.pack()   
uni.place(relx=.65, rely=.92, anchor="c")
uni.config(font=("Courier", 12))

uni_var = StringVar()
uni = Label( master, textvariable=uni_var ) 
uni_var.set('Hyperbola: Sample Entry ===> 200,200,0,0,dir where dir = (v,h)      ')
uni.pack()   
uni.place(relx=.74, rely=.95, anchor="c")
uni.config(font=("Courier", 12))

uni_var = StringVar()
uni = Label( master, textvariable=uni_var ) 
uni_var.set('*vertical,horizontal         ')
uni.pack()   
uni.place(relx=.61, rely=.98, anchor="c")
uni.config(font=("Courier", 12))

button0 = tk.Button(master,text="Go",  #--------------Buttons----------------#
                   fg="white", # transformation operations
                   bg="green",
                   width = 9,
                   command=Record_Transformations)
button0.config(font=("Courier",14))
button0.place(relx=.05, rely=.62, anchor="c")

button1 = tk.Button(master,text="Draw Shape",
                   fg="white",
                   command=display_shape,
                   bg="green")
button1.config(font=("Courier",14))
button1.pack()
button1.place(relx=.01, rely=.94)

rem_trans1 = StringVar()
label2 = Label( master, textvariable=rem_trans1 )
rem_trans1.set("Remaining Transformations: ")
label2.pack()   
label2.place(relx=.19, rely=.92, anchor="c")
label2.config(font=("Courier", 12))

rem_trans = StringVar()
label2 = Label( master, textvariable=rem_trans )
rem_trans.set("0")
label2.pack()   
label2.place(relx=.28, rely=.92, anchor="c")
label2.config(font=("Courier",16),fg='red')

button2 = tk.Button(master,text="Transform Shape (By Step)", 
                   fg="white",
                   bg="green",
                   command=Make_Transformations)
button2.config(font=("Courier",14))
button2.pack()
button2.place(relx=.10, rely=.94)


button3 = tk.Button(master,text="Clear All", 
                   fg="white",
                   bg="red",
                   command=clear)
button3.config(font=("Courier",14))
button3.pack()
button3.place(relx=.30, rely=.94)

button4 = tk.Button(master,text="Go", #---shape operations---#
                   fg="white",
                   bg="green",
                   width = 9,
                   command=save_points)
button4.config(font=("Courier",14))
button4.place(relx=.01, rely=.87)

mainloop()


# In[ ]:




