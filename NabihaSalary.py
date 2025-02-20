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

