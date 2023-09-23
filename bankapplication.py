from pickle import load, dump
from tkinter import *
import tkinter.messagebox as mb
from re import match, compile

screen = Tk()
screen.minsize(500, 500)
screen.maxsize(500, 500)
screen.title('Bank Application')
screen.configure(bg='white')


def isNumber(s: str) -> bool:
    if s.isnumeric():
        return True
    return True if match(compile(r'^[-+]?(?:\d+(\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?$'), s) else False


username = StringVar()
fullName = StringVar()
ageData = StringVar()
genderData = IntVar()
balanceData = StringVar()
password = StringVar()
amount = StringVar()


def afterLogin():
    screen.withdraw()
    screen3 = Toplevel(screen)
    screen3.minsize(500, 500)
    screen3.maxsize(500, 500)
    screen3.title('Home Page')
    screen3.configure(bg='white')

    def logout():
        screen3.destroy()
        screen.deiconify()
        username.set('')
        ageData.set('')
        genderData.set('')
        balanceData.set('')
        password.set('')

    def personalinfo():
        screen3.withdraw()
        screen4 = Toplevel(screen)
        screen4.minsize(500, 500)
        screen4.maxsize(500, 500)
        screen4.title('Personal Information')
        screen4.configure(bg='white')

        def toggleWindow2():
            screen3.deiconify()
            screen4.destroy()

        Label(screen4, text='Welcome '+username.get(), font=('arial', 20),
              bg='white').place(anchor=CENTER, relx=.5, rely=.1)
        Label(screen4, text='Name: '+fullName.get(), font=('arial', 15),
              bg='white').place(anchor=CENTER, relx=.5, rely=.3)
        tempGen = 'Female'
        if +genderData.get() == 1:
            tempGen = 'Male'
        Label(screen4, text='Gender: '+tempGen, font=('arial', 15),
              bg='white').place(anchor=CENTER, relx=.5, rely=.4)
        Label(screen4, text='Age: '+ageData.get(), font=('arial', 15),
              bg='white').place(anchor=CENTER, relx=.5, rely=.5)
        Label(screen4, text='Balance: '+balanceData.get(), font=('arial', 15),
              bg='white').place(anchor=CENTER, relx=.5, rely=.6)

        Button(screen4, text='Back', font=('arial', 12), height=1, width=11,
               command=toggleWindow2).place(anchor=CENTER, relx=.5, rely=.8)

        screen4.mainloop()

    def deposit():
        screen3.withdraw()
        screen5 = Toplevel(screen)
        screen5.minsize(500, 500)
        screen5.maxsize(500, 500)
        screen5.title('Deposit')
        screen5.configure(bg='white')
        depositBalLb = Label(screen5, text='Balance: '+balanceData.get(), font=('arial', 14),
                             bg='white')
        depositBalLb.place(anchor=CENTER, relx=.8, rely=.3)

        def depositProcess():
            if not isNumber(amount.get()):
                mb.askokcancel('Alert', 'Please Enter the Number')
            elif int(amount.get()) <= 0:
                mb.askokcancel('Alert', 'Please Enter Approprite Amount')
            else:
                file1 = open('app.dat', 'rb+')
                listData = load(file1)
                file1.seek(0)
                for i in range(len(listData)):
                    if listData[i]['uname'] == username.get():

                        balanceData.set(
                            str(int(listData[i]['balance'])+int(amount.get())))
                        listData[i]['balance'] = balanceData.get()
                        dump(file=file1, obj=listData)
                        depositBalLb.config(text='Balance: '+balanceData.get())
                        mb.askokcancel(
                            'Success', 'Rs.'+amount.get()+' Deposited Successfully')
                        break
                    else:
                        mb.askokcancel(
                            'Invalid Data', 'Invalid Username or Password')

            amount.set('')

        def toggleWindow3():
            screen3.deiconify()
            screen5.destroy()

        Label(screen5, text='Deposit', font=('arial', 20),
              bg='white').place(anchor=CENTER, relx=.5, rely=.1)

        Label(screen5, text='Username: '+username.get(), font=('arial', 14),
              bg='white').place(anchor=CENTER, relx=.23, rely=.3)

        Label(screen5, text='Amount:', font=('arial', 12),
              bg='white').place(anchor=CENTER, relx=.2, rely=.5)
        Entry(screen5, font=('arial', 12), width=20, textvariable=amount).place(
            anchor=CENTER, relx=.48, rely=.5)

        Button(screen5, text='Deposit', font=('arial', 12), height=1, width=11,
               command=depositProcess).place(anchor=CENTER, relx=.35, rely=.7)

        Button(screen5, text='Back', font=('arial', 12), height=1, width=11,
               command=toggleWindow3).place(anchor=CENTER, relx=.68, rely=.7)

        screen5.mainloop()

    def withdraw():
        screen3.withdraw()
        screen6 = Toplevel(screen)
        screen6.minsize(500, 500)
        screen6.maxsize(500, 500)
        screen6.title('Withdraw')
        screen6.configure(bg='white')
        withdrawBalLb = Label(screen6, text='Balance:'+balanceData.get(), font=('arial', 14),
                              bg='white')
        withdrawBalLb.place(anchor=CENTER, relx=.8, rely=.3)

        def withdrawProcess():
            if not isNumber(amount.get()):
                mb.askokcancel('Alert', 'Please Enter the Number')
            elif int(amount.get()) <= 0 or (int(balanceData.get())-int(amount.get())) < 0:
                mb.askokcancel('Alert', 'Please Enter Approprite Amount')
            else:
                file1 = open('app.dat', 'rb+')
                listData = load(file1)
                file1.seek(0)
                for i in range(len(listData)):
                    if listData[i]['uname'] == username.get():

                        balanceData.set(
                            str(int(listData[i]['balance'])-int(amount.get())))
                        listData[i]['balance'] = balanceData.get()
                        dump(file=file1, obj=listData)
                        withdrawBalLb.config(
                            text='Balance: '+balanceData.get())
                        mb.askokcancel(
                            'Success', 'Withdrawal of Rs.'+amount.get()+' Successfully')
                        break
                    else:
                        mb.askokcancel(
                            'Invalid Data', 'Invalid Username or Password')

            amount.set('')

        def toggleWindow4():
            screen3.deiconify()
            screen6.destroy()

        Label(screen6, text='Withdraw', font=('arial', 20),
              bg='white').place(anchor=CENTER, relx=.5, rely=.1)

        Label(screen6, text='Username:'+username.get(), font=('arial', 14),
              bg='white').place(anchor=CENTER, relx=.23, rely=.3)

        Label(screen6, text='Amount:', font=('arial', 12),
              bg='white').place(anchor=CENTER, relx=.2, rely=.5)
        Entry(screen6, font=('arial', 12), width=20, textvariable=amount).place(
            anchor=CENTER, relx=.48, rely=.5)

        Button(screen6, text='Withdraw', font=('arial', 12), height=1, width=11,
               command=withdrawProcess).place(anchor=CENTER, relx=.35, rely=.7)

        Button(screen6, text='Back', font=('arial', 12), height=1, width=11,
               command=toggleWindow4).place(anchor=CENTER, relx=.68, rely=.7)

        screen6.mainloop()

    Label(screen3, text='Welcome '+username.get(), font=('arial', 20),
          bg='white').place(anchor=CENTER, relx=.5, rely=.1)
    Button(screen3, text='Personal Information', font=('arial', 13), height=1,
           width=21, command=personalinfo).place(anchor=CENTER, relx=.5, rely=.3)
    Button(screen3, text='Deposit', font=('arial', 13), height=1,
           width=11, command=deposit).place(anchor=CENTER, relx=.5, rely=.5)
    Button(screen3, text='Withdraw', font=('arial', 13), height=1,
           width=11, command=withdraw).place(anchor=CENTER, relx=.5, rely=.7)

    Label(screen3, text='Logout Your Account...', font=('arial', 13),
          bg='white').place(anchor=CENTER, relx=.5, rely=.9)
    Button(screen3, text='Logout', font=('arial', 13), height=1,
           width=10, command=logout).place(anchor=CENTER, relx=.8, rely=.9)

    screen3.mainloop()


def doLoginProcess():
    listData = []
    file1 = None
    try:
        file1 = open('app.dat', 'rb')
        listData = load(file1)
        for dic in listData:
            print('data: ', dic)
            if dic['uname'] == username.get() and dic['pass'] == password.get():
                fullName.set(dic['fname'])
                ageData.set(dic['age'])
                balanceData.set(dic['balance'])
                genderData.set(dic['gender'])
                mb.askokcancel(
                    'Success', 'Login Successfully')
                afterLogin()
                return

        mb.askokcancel(
            'Invalid Data', 'Invalid Username or Password')
        return

    except:
        mb.askokcancel('Not Valid', 'No user data exist')
        return


def registerProcess():
    screen.withdraw()
    screen2 = Toplevel(screen)
    screen2.minsize(500, 500)
    screen2.maxsize(500, 500)
    screen2.title('Register')
    screen2.configure(bg='white')

    def toggleWindow():
        screen.deiconify()
        screen2.destroy()

    fname = StringVar()
    age = StringVar()
    gender = IntVar()
    bal = StringVar()
    username = StringVar()
    password = StringVar()

    def doRegister():
        if (not age.get().isnumeric()) or not bal.get().isnumeric():
            mb.askokcancel('Invalid Data', 'Please provide valid data')
        else:
            listData = []
            file1 = None
            try:
                file1 = open('app.dat', 'rb+')
                listData = load(file1)
                for dic in listData:
                    print('data: ', dic)
                    if dic['uname'] == username.get():
                        mb.askokcancel(
                            'Invalid Data', 'Username is already present...')
                        return
                file1.seek(0)
            except:
                file1 = open('app.dat', 'wb+')

            listData.append({
                'fname': fname.get(),
                'uname': username.get(),
                'pass': password.get(),
                'balance': bal.get(),
                'age': age.get(),
                'gender': gender.get(),
            })
            dump(file=file1, obj=listData)

            mb.askokcancel('Success', 'User Registered Successfully')
            toggleWindow()

    Label(screen2, text='Register', font=('arial', 20),
          bg='white').place(anchor=CENTER, relx=.5, rely=.1)

    Label(screen2, text='Full Name:', font=('arial', 11),
          bg='white').place(anchor=CENTER, relx=.1, rely=.2)
    Entry(screen2, textvariable=fname, font=('arial', 11),
          width=30).place(anchor=CENTER, relx=.45, rely=.2)

    Label(screen2, text='Age:', font=('arial', 11),
          bg='white').place(anchor=CENTER, relx=.1, rely=.3)
    Entry(screen2, font=('arial', 11), width=30, textvariable=age).place(
        anchor=CENTER, relx=.45, rely=.3)

    Label(screen2, text='Gender:', font=('arial', 11),
          bg='white').place(anchor=CENTER, relx=.1, rely=.4)
    Radiobutton(screen2, text="Male", variable=gender, value=1,).place(
        anchor=CENTER, relx=.25, rely=.4)
    Radiobutton(screen2, text="Female", variable=gender, value=0,).place(
        anchor=CENTER, relx=.45, rely=.4)

    Label(screen2, text='Balance:', font=('arial', 11),
          bg='white').place(anchor=CENTER, relx=.1, rely=.5)
    Entry(screen2, font=('arial', 11), width=30, textvariable=bal).place(
        anchor=CENTER, relx=.45, rely=.5)

    Label(screen2, text='Username:', font=('arial', 11),
          bg='white').place(anchor=CENTER, relx=.1, rely=.6)
    Entry(screen2, font=('arial', 11), width=30, textvariable=username).place(
        anchor=CENTER, relx=.45, rely=.6)

    Label(screen2, text='Password:', font=('arial', 11),
          bg='white').place(anchor=CENTER, relx=.1, rely=.7)
    Entry(screen2, font=('arial', 11), width=30, textvariable=password).place(
        anchor=CENTER, relx=.45, rely=.7)

    Button(screen2, text='Register', font=('arial', 12), height=1,
           width=11, command=doRegister).place(anchor=CENTER, relx=.35, rely=.85)
    Button(screen2, text='Cancel', command=toggleWindow, font=(
        'arial', 12), height=1, width=11).place(anchor=CENTER, relx=.73, rely=.85)

    screen2.mainloop()


Label(screen, text='Login', font=('arial', 25),
      bg='white').place(anchor=CENTER, relx=.5, rely=.1)

Label(screen, text='Username:', font=('arial', 12),
      bg='white').place(anchor=CENTER, relx=.12, rely=.3)
Entry(screen, font=('arial', 12), width=30, textvariable=username).place(
    anchor=CENTER, relx=.5, rely=.3)

Label(screen, text='Password:', font=('arial', 12),
      bg='white').place(anchor=CENTER, relx=.12, rely=.45)
Entry(screen, font=('arial', 12), width=30, textvariable=password, show='*').place(
    anchor=CENTER, relx=.5, rely=.45)

Button(screen, text='Login', font=('arial', 12), height=1, width=11,
       command=doLoginProcess).place(anchor=CENTER, relx=.35, rely=.6)
Button(screen, text='Cancel', font=('arial', 12), height=1, width=11,
       command=screen.destroy).place(anchor=CENTER, relx=.65, rely=.6)

Label(screen, text='New User/Register...?', font=('arial', 12),
      bg='white').place(anchor=CENTER, relx=.52, rely=.8)
Button(screen, text='Register', command=registerProcess, font=(
    'arial', 10), height=1, width=11).place(anchor=CENTER, relx=.8, rely=.8)

screen.mainloop()
