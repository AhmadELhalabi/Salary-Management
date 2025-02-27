# Function of initsalary
def initsalary(yearlysalaries):
 name = input ("Enter your name: ")

 while True:
        month = input("Enter the month you want to manage: ")
        
        if month in yearlysalaries:
            break
        else:
            print("Invalid month name. Please enter a valid month (e.g., 'Jan', 'Feb').")
    
 details = {
    "user": name,
    "month" : month, 
    "salary" : yearlysalaries[month]
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
 # Additional calculations  
 rent = next(exp["amount"] for exp in expenses if exp["category"] == "Rent")  
 electricity = next(exp["amount"] for exp in expenses if exp["category"] == "Electricity")  
 yearlyrent = rent * 12  
 yearlyelectricity = electricity * 12  
 salarysquared = details["salary"] ** 2 

 # Assume additional savings boost
 additionalsavings = 50  
 savingsamount = next(exp["amount"] for exp in expenses if exp["category"] == "Savings")
    
 if savingsamount > 0:
        savingboost = additionalsavings / savingsamount  
        remainingaftersavingsboost = savingboost + savingsamount
 else:
        remainingaftersavingsboost = "N/A (No savings allocation)" 

 print("Additional Insights:")  
 print(f" - Yearly Rent: ${yearlyrent}")  
 print(f" - Yearly Electricity Cost: ${yearlyelectricity}")  
 print(f" - Salary squared (for fun): ${salarysquared }")  
 print(f" - Remaining after additional savings boost: ${remainingaftersavingsboost}")  
 print("------------------------------------------------------")

# Function to get salary for each of the 12 months
def getYearlySalaries():
    months = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
        "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"
    ]
    yearlysalaries = {}

    print("Enter your salary for each month:")
    for month in months:
        salary = float(input(f"{month}: "))
        yearlysalaries[month] = salary
    
    return yearlysalaries

# ---- MAIN PROGRAM LOOP ---- :
yearlysalaries = getYearlySalaries()
print("Yearly Salaries:", yearlysalaries)

listofsummaries = []
action = "yes"

while action.lower() != "no":
    salarydetails = initsalary(yearlysalaries)
    salarydetails["expenses"] = takeExpenses()
    salarydetails["expenses"] = calculateAmounts(salarydetails["salary"], salarydetails["expenses"])
    salarydetails["total_expenses"] = findTotal(salarydetails["expenses"])
    
    listofsummaries.append(salarydetails)
    
    displaysummary(salarydetails, salarydetails["expenses"], salarydetails["total_expenses"])
    
    action = input("\nWould you like to create another financial summary? (yes/no): ")

print("\nAll summaries:", listofsummaries)