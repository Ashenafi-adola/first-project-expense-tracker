#Import modules that are used to work with
import json
from datetime import date
#declearing lists for latter use

records = []
#Function Deffinations
def addExpense():   #Function to add new expense
    diction = {}  # A dictionary to temporarily store the input data
    diction["Date"] = str(date.today())
    diction["Cathagory"] = input("Enter your Cathagory of expense: ")
    try:
        diction["Amount"] = int(input("Enter your Amount of expense: ")) #accept integer data type otherwise return ValueError
    except ValueError:
        diction["Amount"] = None
        print("please Enter a valid value")
    try: #check weather the file to which the data is stored exist or not
        with open("Expenses.json", "x") as file:
            records.append(diction)
            json.dump(records, file, indent=2)
    except FileExistsError:
        with open("Expenses.json") as file:
            records = json.load(file)
            if diction["Amount"] != None:
                records.append(diction)
        with open("Expenses.json", "w") as file:
            json.dump(records, file, indent=2)
#Function to display all stored Expenses
def viewExpenses():
    with open("Expenses.json") as file:
        records = json.load(file)
        print(44 * "_")
        print("| %-8s| %-14s| %-14s |" % ("Amount", "Cathagory", "Date"))
        print("|" + 42*"_" + "|")
        for i in records:
            print("| %-8s| %-14s| %-14s |" % (i["Amount"], i["Cathagory"], i["Date"]))
        print("|" + 42 * "_" + "|")
#Function which returns the Expenses stored in the file as list
def fileLoader():
    with open("Expenses.json") as file:
        records = json.load(file)
    return records
#Function which filter the catagory of the Expenses stored it takes one cathagory at a time
def CathagoryFilterer(key):
    filtCathagory = []
    for a in fileLoader():
        filtCathagory.append(a[key])
    for i in filtCathagory:
        n = filtCathagory.count(i)
        if n > 1:
            for a in range(n - 1):
                filtCathagory.remove(i)
    return filtCathagory
#Function which group all Expenses with the same cathagory
def FilterByCathagory():
    print(44 * "_")
    print("| %-8s| %-14s| %-14s |" % ("Amount", "Cathagory", "Date"))
    for i in CathagoryFilterer("Cathagory"):
        print("|_______________ " + i + "__________")
        for a in fileLoader():
            if a["Cathagory"] == i:
                print("| %-8s| %-14s| %-14s |" % (a["Amount"], a["Cathagory"], a["Date"]))
    print("|" + 42 * "_" + "|")
#Function which group all Expenses with the same date
def FilterByDate():
    print(44 * "_")
    print("| %-8s| %-14s| %-14s |" % ("Amount", "Cathagory", "Date"))
    for i in CathagoryFilterer("Date"):
        print("|_____________" + i + "__________")
        for a in fileLoader():
            if a["Date"] == i:
                print("| %-8s| %-14s| %-14s |" % (a["Amount"], a["Cathagory"], a["Date"]))
    print("|" + 42 * "_" + "|")
#Function to show summary report of Expenses
def SummaryReport():
    print("Summary report from day " + fileLoader()[0]["Date"] + " to " + fileLoader()[len(fileLoader()) - 1]["Date"])
    for i in CathagoryFilterer("Cathagory"):
        sum = 0
        for a in fileLoader():
            if a["Cathagory"] == i:
                sum += a["Amount"]
        print("Your total Expenditure for " + i + " is " + str(sum))
    total = 0
    for a in fileLoader():
        total += a["Amount"]
    print(
        "Your overall Exprenditure is " + str(total) + " from " + fileLoader()[0]["Date"] + " to " + fileLoader()[len(fileLoader()) - 1]["Date"])
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
        addExpense()
    elif inp == '2':
        viewExpenses()
    elif inp == '3':
        FilterByCathagory()
    elif inp == '4':
        FilterByDate()
    elif inp == '5':
        SummaryReport()
    elif inp == '6':
        print("Good bye!")
        break
    else:
        print("You entered an invalid choice!")