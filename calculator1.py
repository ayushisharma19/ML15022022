import tkinter as tkr
from lib2to3.pgen2.literals import evalString


app=tkr.Tk(__name__)
app.title('Calculator')
app.geometry('600x350')

tkr.Label(app,text='Number 1',font=100).place(x=150,y=1)
tkr.Label(app,text='Number 2',font=100).place(x=150,y=24)


######## FUNCTIONS############

def show():
    print('Number 1: ',en1.get())
    print('Number 2: ',en2.get())
    print('radiobutton values:',rb1.get())
    
    exp()
def exp():
    a=en1.get()
    b=en2.get() 
    if rb1.get()=='+':
            exp=a+b
    elif rb1.get()=='-':
            exp=a-b
    elif rb1.get()=='%':
            exp=a%b
    elif rb1.get()=='/':
        exp=a/b
    else:
            exp=a*b
    tkr.Label(app,text=exp,font=(80)).pack()
    print('Calculation: ',exp)
    ##print('+'/'-'/'%'/'*')
######## ENTRY BOXES#############

en1=tkr.IntVar(app)
en2=tkr.IntVar(app)
tkr.Entry(app,textvariable=en1,font=(30),width=15).pack()
tkr.Entry(app,textvariable=en2,font=(30),width=15).pack()

######## RADIO BUTTON##########

rb1 =tkr.Variable(app,'0')
rb_values = {'+':'+','-':'-','%':'%','/':'/','*':'*'}
for k,v in rb_values.items():
    tkr.Radiobutton(app,text=k,variable=rb1,value=v).pack()
    
######## BUTTON##########

tkr.Button(app,text='Calculate',font=100,command=show).pack()
        

######## RESULT BUTTON#######

tkr.Label(app,text='**Result**',font=(100)).pack()


app.mainloop()
