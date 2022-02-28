#Describe Parameters
preTaxIncome = 0
postTaxIncome = 0
incomeTaxOwed = 0
incomeTaxRate = 0
salary = 0
transaction = 0 

def retrievePreTaxIncome():
    global preTaxIncome
    print("Please enter your total pre-tax income: ")
    preTaxIncome = int(input())
    return preTaxIncome

def calculateFederalIncomeTax():
    global incomeTaxOwed
    retrievePreTaxIncome()
    print("Calculating your taxes owed with a $"+str(preTaxIncome)+" income...")

    if preTaxIncome > 0 and preTaxIncome <= 9950:
        incomeTaxOwed = preTaxIncome * .10
    elif preTaxIncome >= 9951 and preTaxIncome <= 40525:
        incomeTaxOwed = 995 + (preTaxIncome - 9950)*.12
    elif preTaxIncome >= 40526 and preTaxIncome <= 86375:
        incomeTaxOwed = 4664 + (preTaxIncome - 40525)*.22
    elif preTaxIncome >= 86376 and preTaxIncome <= 164925:
        incomeTaxOwed = 14751 + (preTaxIncome - 86375)*.24
    elif preTaxIncome >= 164926 and preTaxIncome <= 209425:
        incomeTaxOwed = 33603 + (preTaxIncome - 164925)*.32
    elif preTaxIncome >= 209426 and preTaxIncome <= 523600:
        incomeTaxOwed = 47843 + (preTaxIncome - 209425)*.35
    elif preTaxIncome >= 523601:
        incomeTaxOwed = 157804.25 + (preTaxIncome - 523600)*.37
    else:
        print("Please enter a valid income tax number.")

    print("Your taxable income is: $"+str(round(incomeTaxOwed, 2))) 

def calculateFederalIncomeTaxRate(incomeTaxOwed, preTaxIncome):
    global incomeTaxRate
    incomeTaxRate = (incomeTaxOwed / preTaxIncome)*100
    print("Your federal income tax rate is: "+str(round(incomeTaxRate, 2))+"%") 


calculateFederalIncomeTax()
calculateFederalIncomeTaxRate(incomeTaxOwed, preTaxIncome)