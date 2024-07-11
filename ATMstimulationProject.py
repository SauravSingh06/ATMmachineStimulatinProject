from tkinter import *
from tkinter import simpledialog, messagebox

# Initial account details
account_balance = 100000
transaction_history = []
account_pin = "1234"

# Function to handle cash withdrawal
def cash_withdrawal():
    global account_balance, transaction_history
    entered_pin = simpledialog.askstring("PIN Verification", "Enter your PIN:", show='*')
    if entered_pin == account_pin:
        amount = simpledialog.askinteger("Cash Withdrawal", "Enter amount to withdraw:")
        if amount is not None:
            if amount > account_balance:
                messagebox.showwarning("Warning", "Insufficient balance!")
            else:
                account_balance -= amount
                transaction_history.append(f"Withdrawn: {amount}")
                atm_label.config(text="Transaction successful!")
    else:
        messagebox.showerror("Error", "Incorrect PIN!")

# Function to handle cash deposit
def cash_deposit():
    global account_balance, transaction_history
    entered_pin = simpledialog.askstring("PIN Verification", "Enter your PIN:", show='*')
    if entered_pin == account_pin:
        amount = simpledialog.askinteger("Cash Deposit", "Enter amount to deposit:")
        if amount is not None:
            account_balance += amount
            transaction_history.append(f"Deposited: {amount}")
            atm_label.config(text="Transaction successful!")
    else:
        messagebox.showerror("Error", "Incorrect PIN!")

# Function to show last transaction details
def last_transaction_details():
    entered_pin = simpledialog.askstring("PIN Verification", "Enter your PIN:", show='*')
    if entered_pin == account_pin:
        if transaction_history:
            atm_label.config(text=f"Last transaction: {transaction_history[-1]}")
        else:
            atm_label.config(text="No transactions yet.")
    else:
        messagebox.showerror("Error", "Incorrect PIN!")

# Function to show transaction history
def show_transaction_history():
    entered_pin = simpledialog.askstring("PIN Verification", "Enter your PIN:", show='*')
    if entered_pin == account_pin:
        if transaction_history:
            history = "\n".join(transaction_history[-5:])  # Show last 5 transactions
            messagebox.showinfo("Transaction History", history)
        else:
            messagebox.showinfo("Transaction History", "No transactions yet.")
    else:
        messagebox.showerror("Error", "Incorrect PIN!")

# Function to show current balance
def show_balance():
    entered_pin = simpledialog.askstring("PIN Verification", "Enter your PIN:", show='*')
    if entered_pin == account_pin:
        atm_label.config(text=f"Current balance: {account_balance}")
    else:
        messagebox.showerror("Error", "Incorrect PIN!")

# Function to change PIN
def change_pin():
    global account_pin
    old_pin = simpledialog.askstring("Change PIN", "Enter current PIN:", show='*')
    if old_pin == account_pin:
        new_pin = simpledialog.askstring("Change PIN", "Enter new PIN:", show='*')
        confirm_new_pin = simpledialog.askstring("Change PIN", "Confirm new PIN:", show='*')
        if new_pin == confirm_new_pin:
            account_pin = new_pin
            atm_label.config(text="PIN changed successfully!")
        else:
            messagebox.showerror("Error", "PINs do not match!")
    else:
        messagebox.showerror("Error", "Incorrect current PIN!")

# Function to verify PIN
def verify_pin():
    entered_pin = simpledialog.askstring("Login", "Enter your PIN:", show='*')
    if entered_pin == account_pin:
        show_atm_interface()
    else:
        messagebox.showerror("Error", "Incorrect PIN!")

# Function to show ATM interface after successful login
def show_atm_interface():
    login_label.pack_forget()
    btn_login.pack_forget()
    
    # Welcome message
    atm_label0 = Label(atm, text="WELCOME", font="bold")
    atm_label0.pack()

    # Initial message
    global atm_label
    atm_label = Label(atm, text="Please select an option", bg="yellow", font="bold")
    atm_label.pack()

    # Instructions
    atm_label2 = Label(atm, text="Press 1 - For Cash Withdrawal \nPress 2 - For Cash Deposit \nPress 3 - For Last Transaction Details \nPress 4 - To Change your PIN\nPress 5 - To View Transaction History\nPress 6 - To View Current Balance")
    atm_label2.pack()

    # Frame for buttons
    f1 = Frame(atm)
    f1.pack()

    # Adding buttons for each action
    btn_withdrawal = Button(f1, text="1", command=cash_withdrawal)
    btn_withdrawal.grid(row=0, column=0, padx=10, pady=10)

    btn_deposit = Button(f1, text="2", command=cash_deposit)
    btn_deposit.grid(row=0, column=1, padx=10, pady=10)

    btn_last_transaction = Button(f1, text="3", command=last_transaction_details)
    btn_last_transaction.grid(row=0, column=2, padx=10, pady=10)

    btn_change_pin = Button(f1, text="4", command=change_pin)
    btn_change_pin.grid(row=0, column=3, padx=10, pady=10)

    btn_transaction_history = Button(f1, text="5", command=show_transaction_history)
    btn_transaction_history.grid(row=0, column=4, padx=10, pady=10)

    btn_balance = Button(f1, text="6", command=show_balance)
    btn_balance.grid(row=0, column=5, padx=10, pady=10)

# Setting up the main window
atm = Tk()
atm.title("ATM Machine Simulation")
atm.geometry("600x400")
atm.maxsize(600,400)

# Initial login prompt
login_label = Label(atm, text="Please log in to access the ATM", font="bold")
login_label.pack()

btn_login = Button(atm, text="Login", command=verify_pin)
btn_login.pack()

# Running the main loop
atm.mainloop()

