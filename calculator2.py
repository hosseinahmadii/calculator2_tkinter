from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator =""
    text_input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator=""

root = Tk()
root.title("Calculator:")
root.resizable(width=False , height=False)
root.configure(bg='gray')

operator = ""
text_input = StringVar()

txtDisplay = Entry(root, font=('arial', 20, 'bold'),width=24, textvariable=text_input, bd=30,
                   insertwidth=4, bg='light grey', justify='right').grid(columnspan=4)

##================================= First Row ========================================================
remain = Button(root,width=5,height=1, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='%', command=lambda:btnClick('%')).grid(row=1, column=0)
power_of_two = Button(root, width=5,height=1 ,bd=8, fg='black', font=('arial', 20, 'bold'),
               text='x^2', command=lambda:btnClick('**2')).grid(row=1, column=1)
radical = Button(root,width=5,height=1, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='√x', command=lambda:btnClick('**(1/2)')).grid(row=1, column=2)
division = Button(root,width=5,height=1, bd=8, fg='black', font=('arial', 20, 'bold'),
                  text='/', command=lambda:btnClick('/')).grid(row=1, column=3)
##================================= Second Row ========================================================
btn7 = Button(root,width=5,height=1, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='7', command=lambda:btnClick(7)).grid(row=2, column=0)
btn8 = Button(root,width=5,height=1, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='8', command=lambda:btnClick(8)).grid(row=2, column=1)
btn9 = Button(root,width=5,height=1, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='9', command=lambda:btnClick(9)).grid(row=2, column=2)
multiplication = Button(root,width=5,height=1, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='*', command=lambda:btnClick('*')).grid(row=2, column=3)
##================================= Third Row ========================================================
btn4 = Button(root,width=5,height=1, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='4', command=lambda:btnClick(4)).grid(row=3, column=0)
btn5 = Button(root,width=5,height=1, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='5', command=lambda:btnClick(5)).grid(row=3, column=1)
btn6 = Button(root,width=5,height=1, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='6', command=lambda:btnClick(6)).grid(row=3, column=2)
subtraction = Button(root,width=5,height=1, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='-', command=lambda:btnClick('-')).grid(row=3, column=3)
##================================= Fourth Row ========================================================
btn1 = Button(root,width=5,height=1, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='1', command=lambda:btnClick(1)).grid(row=4, column=0)
btn2 = Button(root,width=5,height=1, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='2', command=lambda:btnClick(2)).grid(row=4, column=1)
btn3 = Button(root,width=5,height=1, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='3', command=lambda:btnClick(3)).grid(row=4, column=2)
sum = Button(root,width=5,height=1, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='+', command=lambda:btnClick('+')).grid(row=4, column=3)
##================================= The fifth Row ========================================================
btn_clean= Button(root,width=5,height=1, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='C', command= btnClearDisplay).grid(row=5, column=0)
btn0  = Button(root,width=5,height=1, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='0', command=lambda:btnClick(0)).grid(row=5, column=1)
point = Button(root,width=5,height=1, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='.', command=lambda:btnClick('.')).grid(row=5, column=2)
btnEquals = Button(root,width=5,height=1, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='=', command=btnEqualsInput).grid(row=5, column=3)

##================================= Functions ========================================================



root.mainloop()