# Function of initsalary
def initsalary():
 name = input ("Enter your name: ")
 month = input ("Enter the month: ")

 details = {
    "user": name,
    "month" : month, 
    "salary" : float (input("Enter your salary for the month: "))
}
 return details 

# Function to take expense and percentages
def takeExpenses():
 expenses= []
 categories = ["Savings", "Rent" , "Electricity"]

 for category in categories:
   percent = float (input(f"Enter the percentage allocated to {category}: "))

   expense = {
    "category": category ,
    "percentage": percent 
   }

   expenses.append(expense)

 return expenses


#Function to calculate the allocated amounts
def calculateAmounts(salary,expenses):
 for expense in expenses:
  expense["amount"] =( expense["percentage"]/100)*salary
  
 return expenses

# Function to find total expenses 
def findTotal(expenses):
 total = 0

 for expense in expenses:
   total = total + expense ["amount"] 

 return total

# Function to display the financial summary 
def displaysummary (details, expenses,totalexpenses):
 print("------------------ Financial Summary ------------------")
 print(f"User: {details['user']}")
 print(f"Month: {details['month']}")
 print(f"Salary: ${details['salary']}")
    
 print("Allocations:")
 for expense in expenses:
        print(f" - {expense['category']}: ${expense['amount']} ({expense['percentage']}%)")
    
 remainingsalary = details["salary"] - totalexpenses
 print(f"Total Expenses: ${totalexpenses}")
 print(f"Remaining Salary: ${remainingsalary}")
 print("------------------------------------------------------")
