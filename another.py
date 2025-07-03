import json
from datetime import date

#declearing lists and dictionaries for latter use
diction = {}
records = []
expns = {}
cats = ["Amount", "Cathagory", "Date"]

def addExpense():
    for det in cats:
        if det == "Date":
            diction[det] = str(date.today())
        elif det == "Amount":
            diction[det] = int(input("Enter your " + det + " of expense: "))
        else:
            diction[det] = input("Enter your " + det + " of expense: ")
    try:
        with open("Expenses.json", "x") as file:
            records.append(diction)
            expns["Expenses"] = records
            json.dump(expns, file, indent=2)
    except FileExistsError:
        with open("Expenses.json") as file:
            expns = json.load(file)
            records = list(expns["Expenses"])
            records.append(diction)
            expns["Expenses"] = records
        with open("Expenses.json", "w") as file:
            json.dump(expns, file, indent=2)
def viewExpenses():
    with open("Expenses.json") as file:
        view = json.load(file)
        print(44 * "_")
        print("| %-8s| %-14s| %-14s |" % ("Amount", "Cathagory", "Date"))
        for i in view["Expenses"]:
            print("| %-8s| %-14s| %-14s |" % (i["Amount"], i["Cathagory"], i["Date"]))
        print("|" + 42 * "_" + "|")

def fileLoader():
    with open("Expenses.json") as file:
        filt = json.load(file)
        lists = filt["Expenses"]
    return lists

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

def FilterByCathagory():
    print(44 * "_")
    for i in CathagoryFilterer("Cathagory"):
        print("|_______________ " + i + "__________")
        for a in fileLoader():
            if a["Cathagory"] == i:
                print("| %-8s| %-14s| %-14s |" % (a["Amount"], a["Cathagory"], a["Date"]))
    print("|" + 42 * "_" + "|")

def FilterByDate():
    print(44 * "_")
    for i in CathagoryFilterer("Date"):
        print("|_______________ " + i + "__________")
        for a in fileLoader():
            if a["Date"] == i:
                print("| %-8s| %-14s| %-14s |" % (a["Amount"], a["Cathagory"], a["Date"]))
    print("|" + 42 * "_" + "|")
    
def SummaryReport():
    print("Summary report from " + fileLoader()[0]["Date"] + " to " + fileLoader()[len(fileLoader()) - 1]["Date"])
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
    print("|======Welcome to Expense Tracker!=======")
    print("|        Main menu")
    print("| 1. Add Expense")
    print("| 2. View Expenses")
    print("| 3. Filter by Category")
    print("| 4. Filter by Date")
    print("| 5. Summary Report")
    print("| 6. Save and Exit")
    inp = int(input("Enter your choice: "))
    if inp == 1:
        addExpense()
    elif inp == 2:
        viewExpenses()
    elif inp == 3:
        FilterByCathagory()
    elif inp == 4:
        FilterByDate()
    elif inp == 5:
        SummaryReport()
    elif inp == 6:
        print("Good bye!")
        break
    else:
        print("You entered an invalid choice!")