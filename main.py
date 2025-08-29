#Import modules that are used to work with
import json
from datetime import date
#declearing lists for latter use
FILENAME = "Expenses.json"

#Function Deffinations
def addExpense(records):   #Function to add new expense
    diction = {}  # A dictionary to temporarily store the input data
    diction["Date"] = str(date.today())
    diction["Category"] = input("Enter your Category of expense: ")
    try:
        diction["Amount"] = int(input("Enter your Amount of expense: ")) #accept integer data type otherwise return ValueError
    except ValueError:
        diction["Amount"] = None
        print("please Enter a valid value")
    if diction["Amount"] != None:
        records.append(diction)
    else:
        print("Add expense Faild!")
#Function to display all stored Expenses
def viewExpenses(records):
    print(44 * "_")
    print("| %-8s| %-14s| %-14s |" % ("Amount", "Catgory", "Date"))
    print("|" + 42*"_" + "|")
    for i in records:
        print("| %-8s| %-14s| %-14s |" % (i["Amount"], i["Category"], i["Date"]))
    print("|" + 42 * "_" + "|")

#Function which filter the catagory of the Expenses stored it takes one cathagory at a time
def CathagoryFilterer(key,records):
    filtCathagory = []
    for a in records:
        filtCathagory.append(a[key])
    for i in filtCathagory:
        n = filtCathagory.count(i)
        if n > 1:
            for a in range(n - 1):
                filtCathagory.remove(i)
    return filtCathagory
#Function which group all Expenses with the same cathagory
def FilterByCathagory(records):
    print(44 * "_")
    print("| %-8s| %-14s| %-14s |" % ("Amount", "Category", "Date"))
    for i in CathagoryFilterer("Category", records):
        print("|_______________ " + i + "__________")
        for a in records:
            if a["Category"] == i:
                print("| %-8s| %-14s| %-14s |" % (a["Amount"], a["Category"], a["Date"]))
    print("|" + 42 * "_" + "|")
#Function which group all Expenses with the same date
def FilterByDate(records):
    print(44 * "_")
    print("| %-8s| %-14s| %-14s |" % ("Amount", "Category", "Date"))
    for i in CathagoryFilterer("Date", records):
        print("|_____________" + i + "__________")
        for a in records:
            if a["Date"] == i:
                print("| %-8s| %-14s| %-14s |" % (a["Amount"], a["Category"], a["Date"]))
    print("|" + 42 * "_" + "|")
#Function to show summary report of Expenses
def SummaryReport(records):
    print("Summary report from day " + records[0]["Date"] + " to " + records[len(records) - 1]["Date"])
    for i in CathagoryFilterer("Category"):
        sum = 0
        for a in records:
            if a["Category"] == i:
                sum += a["Amount"]
        print("Your total Expenditure for " + i + " is " + str(sum))
    total = 0
    for a in records:
        total += a["Amount"]
    print(
        "Your overall Exprenditure is " + str(total) + " from " + records[0]["Date"] + " to " + records[len(records) - 1]["Date"])

try:
    file = open(FILENAME, 'r')
    records = json.load(file)
except FileNotFoundError:
    records = []
while True:
    print("__________________________________________")
    print("|======Welcome to Expense Tracker!=======|")
    print("|        Main menu                       |")
    print("| 1. Add Expense                         |")
    print("| 2. View Expenses                       |")
    print("| 3. Filter by Category                  |")
    print("| 4. Filter by Date                      |")
    print("| 5. Summary Report                      |")
    print("| 6. Save and Exit                       |")
    print("|________________________________________|")
    inp = (input("Enter your choice: "))
    if inp == '1':
        addExpense(records)
    elif inp == '2':
        viewExpenses(records)
    elif inp == '3':
        FilterByCathagory(records)
    elif inp == '4':
        FilterByDate(records)
    elif inp == '5':
        SummaryReport(records)
    elif inp == '6':
        with open(FILENAME,'w') as f:
            json.dump(records,f, indent=4)
        print("Good bye!")
        break
    else:
        print("You entered an invalid choice!")