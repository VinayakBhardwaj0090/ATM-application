class User: # class for user

    def __init__(self, u_id, password, balance=5000): # Function for crating new account 
        self.user_id = u_id
        self.user_passowrd = password
        self.balance = balance
    
    def deposit(self,amount): # Function for deposit
        if amount % 100 == 0 and amount <= 100000:
            notes={2000:0, 1000:0, 500:0, 200:0, 100:0}
            d_amnt=0
            print("\nDenomination")  # Denomination on deposit
            for i in notes.keys():
                notes[i]=int(input(f"Enter no. of {i}'s notes : "))
                d_amnt+=i*notes[i]
            if amount==d_amnt:
                self.balance += amount
                return f"Deposited {amount} successfully."
            else:
                return "Invalid Denomination."
        else: 
            return "Invalid Deposit amount or denomination"

    def withdraw(self,amount): # Function for withdraw
        if amount % 100 == 0 and amount <= 50000:
            if self.balance >= amount:
                self.balance -= amount
                denom_list=denomination(amount)        # denomination on withdrawal
                d_amnt=0
                for i in denom_list.keys():
	                d_amnt+= i*(denom_list[i]) 
	                print(f"{i} * {denom_list[i]} = {i*denom_list[i]}")	
                print("Total Amount: ",d_amnt)
                print("Withdrew successfully.")
            
                if self.balance<5000:               # Notification if minimum balance reached
                    print("\t*** Notification: Maintain Minimum Balance of 5000 ***")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount or denomination.")

    def check_balance(self): # Function for Checking balance
        return f"Balance: {self.balance}"
    
    def update(self, new_password): # Function for Change password
        self.user_passowrd=new_password

def denomination(amount):      # denomination function
	notes={2000:0, 1000:0, 500:0, 200:0, 100:0}
	for i in notes.keys():
		if amount>0:
			Note = amount//i
			if Note>0:
				amount-=i*Note 
				notes[i]=Note
		else:
			break
	return notes

users={} # dictionary that maintains or stores users 

def user_main():  # user main function
    while True:
        print("\n\t\t***** User Main Menu ****")
        print("1. Create New Accont\n2. Login to Existing Account\n3. Back to Main Menu\n0. Exit")
        choice=input("Enter Your Choice : ")
        
        if choice=='1':   # Create new account
            u_id=input("Enter new id: ")
            if u_id in users.keys():
                print("User already exist.")
            else:
                n_password = input("Enter new password: ")
                u_bal = int(input("Enter Balance in account: "))
                new_user = User(u_id,n_password,u_bal)
                users.update({u_id : new_user})
                print("**** Congrulation! New Account is created *****")

        elif choice=='2':  # Existing account
            u_id=input("Enter ID: ")
            if u_id in users.keys():
                user = users[u_id]
                count=3
                while count>0:
                    password = input("Enter Passowrd: ")
                    if password == user.user_passowrd:
                                       # users function
                        while True:
                            print("\nUser Menu:")
                            print("1. Deposit")
                            print("2. Withdraw")
                            print("3. Check Balance")
                            print("4. Change Password")
                            print("5. Logout")
                            user_choice = input("Enter your choice: ")
                            if user_choice == '1':
                                amount = int(input("Enter the deposit amount: "))
                                print(user.deposit(amount))
                            elif user_choice == '2':
                                amount = int(input("Enter the withdrawal amount: "))
                                user.withdraw(amount)
                            elif user_choice == '3':
                                print(user.check_balance())
                            elif user_choice == '4':
                                new_password = input("Enter new password: ")
                                user.update(new_password)
                                print("Password changed successfully.")
                            elif user_choice == '5':
                                print("\n\t<---> User loged Out <--->")
                                count=-1
                                break
                            else:
                                print("Invalid choice. Please try again.")
                    else:
                        count-=1
                        if count==0:
                            print("!!!! To Many worng attemps. Account Locked !!!! ")
                        else:
                            print("Wrong password. Attempt remain ",count)    
            else:
                print("!!!!! User Not found. !!!!")
        
        elif choice=='3': # Back to main file
            return -1
        
        elif choice=='0':   # Exit the program
            print("\n\t**** Thanks for using our services ****\n\t**** Exit ATM Program ****")
            return 0
        else:
            print("\n<----> Invalid choice! <---->\n<--> Enter from given options <-->")


class Admin:  # Admin class

    def __init__(self, admin_id, password, balance): # Create admin account
        self.admin_id = admin_id
        self.password = password
        self.balance = balance

    def total_balance(self): # Check total balance
        return f"Total Balance: {self.balance}"

    def deposit_cash(self, amount): # Deposite in admin account
        if amount % 100 == 0 and amount <= 300000:
            
            notes={2000:0, 1000:0, 500:0, 200:0, 100:0}
            d_amnt=0
            print("\nDenomination")  # Denomination on deposit
            for i in notes.keys():
                notes[i]=int(input(f"Enter no. of {i}'s notes : "))
                d_amnt+=i*notes[i]
            if amount==d_amnt:
                self.balance += amount
                print(f"Deposited {amount} successfully.")
            else:
                print("Invalid Denomination.")
            if self.balance < 75000:
                print("\t*** Notification: Balance is less than 75,000. ***")
        else:
            print("Invalid deposit amount or denomination.")

    def withdraw(self,amount): # Function for withdraw
        if amount % 100 == 0 and amount <= 500000:
            if self.balance >= amount:
                self.balance -= amount
                denom_list=denomination(amount)        # denomination on withdrawal
                d_amnt=0
                for i in denom_list.keys():
	                d_amnt+= i*(denom_list[i]) 
	                print(f"{i} * {denom_list[i]} = {i*denom_list[i]}")	
                print("Total Amount: ",d_amnt)
                print("Withdrew successfully.")
                if self.balance<75000:      # Notification if minimum balance reached
                    print("\t*** Notification: Maintain Minimum Balance of 75000 ***")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount or denomination.")

admins ={}   # dictionary to maintain admin details 

def admin_main(): # Admin functions 
    admin_id = input("Enter Admin ID: ")
    if admin_id in admins: # check valid admin id
        count=3
        while count>0:    # if password is wrong three times
            password = input("Enter Password: ")
            if admins[admin_id] == password: # Admin functions
                while True:                                
                    print("\n\t\t**** Admin Menu ****")
                    print("1. Total Balance")
                    print("2. Deposit Cash")
                    print("3. Withdraw Cash")
                    print("4. Logout")
                    admin_choice = input("Enter your choice: ")
                    if admin_choice == '1':
                        print(admin.total_balance())
                    elif admin_choice == '2':
                        amount = int(input("Enter the deposit amount: "))
                        admin.deposit_cash(amount)
                    elif admin_choice == '3':
                        amount=int(input("Enter the Withdraw amount: "))
                        admin.withdraw(amount)
                    elif admin_choice == '4':
                        print("\n\t<----> Admin Loged Out <---->\n")
                        count=-1
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                count-=1
                if count==0:
                    print("!!!! To Many worng attemps. Account Locked !!!! ")
                else:
                    print("Wrong password. Attempt remain: ",count)
    else:
        print("!!!! Wrong Admin Id !!!!")

''' Main program '''
if __name__=='__main__':
    print('\n\t\t*** Welcome To The ATM ***')
    print(" New Admin Account ")
    admin_id = input("Enter Admin ID: ")
    admin_pass = input("Enter Admin Password: ")
    admin_ammount = int(input("Enter Balance for Admin (Rs100-5L): "))
    admins.update({admin_id : admin_pass})
    admin = Admin(admin_id,admin_pass,admin_ammount)
    while True:
        print("\t**** Main Menu ****")
        print("1. User\n2. Admin\n3.Exit")
        choice = input("Enter your choice: ")

        if choice=='1': # Open user functions/file
                        
            val=user_main()
            if val==0:
                break       
        elif choice=='2': # Open admin functions/file
                        
            val=admin_main()
            if val==0:
                break
        elif choice=='3':    # Exit the program
            print("\n\t**** Thanks for using our services ****\n\t**** Exit ATM Program ****")
            break
        else:          # Wrong input/choice
            print("\n\t<----> Invalid choice! <---->\n\t<--> Enter from given options <-->")