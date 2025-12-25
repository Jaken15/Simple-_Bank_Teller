from tkinter import*
from tkinter import messagebox
from Process import bank_teller as Bank
from tkinter import ttk

class BankTellerUI:
    def __init__(self,root,Pin):
        self.transaction_op = ""
        self.curr_amount = 0
        self.Pin = Pin
        self.app = Bank()
        self.Bank = Toplevel(root)
        self.Bank.geometry("900x500")
        self.Bank.title("Bank Teller System")

        self.sidebar = Frame(self.Bank,bg="#1e1e1e",width=200)
        self.sidebar.pack(side=LEFT,fill='y')

        Home_button = Button(self.sidebar,text="Home",
                             font=("arial",10),
                             relief='flat',bg="#333",
                             fg="white",command=self.Home)
        Home_button.pack(fill='x',padx=10,pady=10)

        Deposit_button = Button(self.sidebar,text="Deposit",
                         font=("arial",10),
                         relief="flat",bg="#333",
                         fg="white",command=self.Deposit)
        Deposit_button.pack(fill='x',padx=10,pady=10)

        Withdraw_button = Button(self.sidebar,text="Withdraw",
                                 font=("arial",10),
                                 relief="flat",bg="#333",
                                 fg="white",command=self.withdraw)
        Withdraw_button.pack(padx=10,pady=10,fill="x")

        Transaction_button = Button(self.sidebar,text="Transaction",
                                    font=("arial",10),
                                    relief="flat",bg="#333",
                                    fg="white",command=self.transaction)
        Transaction_button.pack(fill="x",padx=10,pady=10)

        # Main Content

        self.mainframe = Frame(self.Bank,bg="white")
        self.mainframe.pack(side="left",fill="both",expand=True)
        self.Home()

    def Home(self):
        self.Clear()
        welcome = Label(self.mainframe,text="Welcome to bank teller system",
                        font=("arial",20),bg="white")
        welcome.pack(pady=50)
    
    def Deposit(self):
        self.Clear()
        Deposit_page = Label(self.mainframe,text="Deposit page",
                             font=("arial",20),bg="white")
        Deposit_page.pack(pady=20)

        deposit_entry = Entry(self.mainframe,font=("arial",12),width=10)
        deposit_entry.pack(pady=10)

        deposit_button = Button(self.mainframe,text="Deposit",bg="#1e90ff",
                                fg='white',width=10,command=lambda:self.Deposit_Func(deposit_entry))
        deposit_button.pack(pady=10)

        exit_button = Button(self.mainframe,text=("Logout"),bg="#1e1e1e",
                             fg="white",width=10,command=self.Close)
        exit_button.pack(pady=10)

    def withdraw(self):
        self.Clear()
        Witdraw_page = Label(self.mainframe,text="Witdraw page"
                             ,font=("arial",20),bg="white")
        Witdraw_page.pack(pady=20)

        withdraw_entry = Entry(self.mainframe,font=("arial",12),width=10)
        withdraw_entry.pack(pady=10)

        withdraw_button = Button(self.mainframe,text="Witdraw",bg="#e63946",width=10,
                                 fg="white",command=lambda:self.withdraw_func(withdraw_entry))
        withdraw_button.pack(pady=10)

        exit_button = Button(self.mainframe,text=("Logout"),bg="#1e1e1e",
                             fg="white",width=10,command=self.Close)
        exit_button.pack(pady=10)

    def transaction(self):
        self.Clear()
        Transaction_page = Label(self.mainframe,text="Trasaction page",bg='white',
                                 font=("arial",20))
        Transaction_page.pack(pady=10)

        Mytree = ttk.Treeview(self.mainframe,columns=("Pinumber","Amount","transaction",
                                                 "time","date"),show="headings")

        Mytree.column("Pinumber",width=120,stretch=False,anchor="w")
        Mytree.column("Amount",width=120,stretch=False,anchor="w")
        Mytree.column("transaction",width=120,stretch=False,anchor="w")
        Mytree.column("time",width=120,stretch=False,anchor="w")
        Mytree.column("date",width=120,stretch=False,anchor="w")

        Mytree.heading("Pinumber",text="Pin number",anchor="w")
        Mytree.heading("Amount",text="Amount",anchor="w")
        Mytree.heading("transaction",text="Transaction",anchor="w")
        Mytree.heading("time",text="Date",anchor="w")
        Mytree.heading("date",text="Time",anchor="w")

        transac = self.app.view_transaction(self.Pin)
        balance = self.app.balance(self.Pin)

        total_balance = Label(self.mainframe,text=f"Total Balance :${balance}",
                              font=("arial",15))
        
        for index,info in enumerate(transac):
            Mytree.insert(parent="",index="end",iid=index,
                          values=info)
            
        total_balance.pack(pady=5,padx=20)
        Mytree.pack(fill='both',expand=True,side='left')
    
    def Clear(self):
        for widget in self.mainframe.winfo_children():
            widget.destroy()

    def Close(self):
        self.Bank.withdraw()
        root.deiconify()

    def Deposit_Func(self,entry):
        amount = entry.get()
        entry.delete(0,END)
        self.transaction_op = "deposit"
        cash = int(amount)
        try:
            if amount.isdigit():
              self.app.deposit(self.Pin,cash)
              self.app.insert_transaction(self.transaction_op,self.Pin)
              messagebox.showinfo("Sucessfully","Successfully deposit")
            else:
              messagebox.showwarning("Invalid","Lagyan mo ng number wag kang bobo\nsapakin kita dyan eh")
        except Exception as e:
            print(e)

    def withdraw_func(self,entry):
        amount = entry.get()
        entry.delete(0,END)
        self.transaction_op = "Withdraw"
        try:
            if amount.isdigit():
                cash = int(amount)
                self.curr_amount = cash
                self.app.withdraw(self.Pin,cash)
                self.app.insert_transaction(self.transaction_op,self.Pin)
                messagebox.showinfo("Accress Granted","Successfully Withdraw")
            else:
                messagebox.showwarning("Invalid","Lagyan mo ng number wag kang bobo\nsapakin kita dyan eh")
        except Exception as e:
            print(e)

# login window

def login_form(root):
    root.geometry("520x250")
    root.title("Login Form")

    Login_frame = Frame(root,bg="white")
    Login_frame.pack(pady=20,padx=20,expand=True,fill='both')

    login_label = Label(Login_frame,text="Bank Teller",
                        font=("arial",26),bg="white",fg="black")
    login_label.pack(pady=(0,15))

    login_pin = Label(Login_frame,text="Enter Pin",
                    font=("arial",12),bg="white",fg='black')
    login_pin.pack(pady=(0,5))

    login_entry = Entry(Login_frame,font=("arial",12),
                        width=10,justify='center',show="*")
    login_entry.pack(pady=(0,15))

    button_frame = Frame(root,bg="white")
    button_frame.pack(pady=10)

    enter_button = Button(button_frame,text="Enter",bg="green",
                          fg="white",width=10,command=lambda:Login(login_entry))
    enter_button.pack(side=LEFT,padx=10)

    exit_button = Button(button_frame,text="Exit",bg="red",
                         fg="white",width=10,command=root.destroy)
    exit_button.pack(side=LEFT,pady=(5,10))

# for login pin code

def Login(Pincode):
    pin_number = Pincode.get()
    app = Bank()
    Pincode.delete(0,END)
    if len(pin_number) != 0:
        con = app.Login(int(pin_number))
        if con == True:
           root.withdraw()
           BankUI = BankTellerUI(root,int(pin_number))
        else:
            messagebox.showwarning("Invalid","Invalid Pin Number")
root = Tk()
login_form(root)
root.mainloop()