from tkinter import *

#Create tkinter instance
root = Tk()
root.title('US Federal Income Tax Calculator - Single Filer - 2021')
root.geometry("500x400")

#Create label frame
label_frame = LabelFrame(root, text="Income Tax Calculator")
label_frame.pack(pady=30)

#Create frame
frame = Frame(label_frame)
frame.pack(pady=20)

#Labels and Data Entry
preTaxIncome_label = Label(frame, text="Pre-Tax Income")
preTaxIncome_entry = Entry(frame, font=("Helvetica", 18))
incomeTax_label = Label(frame, text="Amount you owe in taxes")
taxRate_label = Label(frame, text="Tax Rate")

#Calculate Button Function
def calculateFederalIncomeTax():
    if preTaxIncome_entry.get():
        preTaxIncome = int(preTaxIncome_entry.get())

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

        incomeTaxOwed = round(incomeTaxOwed, 2)

        #Calculate Tax Rate
        incomeTaxRate = round(((incomeTaxOwed / preTaxIncome)*100),2)

        incomeTax_label.config(text=f"Income Tax: ${incomeTaxOwed}")
        taxRate_label.config(text=f"Income Tax Rate: {incomeTaxRate}%")

    else:
        incomeTax_label.config(text="Please enter an income value.")
        taxRate_label.config(text="Please enter an income value.")

#Add labels and data entries to screen
preTaxIncome_label.grid(row=0, column=0)
preTaxIncome_entry.grid(row=0, column=1)
incomeTax_label.grid(row=2, column=0)
taxRate_label.grid(row=3, column=0)

#Create Calculate Button
calculateTax_button = Button(label_frame, text="Calculate Income Tax", command=calculateFederalIncomeTax)
calculateTax_button.pack(pady=20)

#Execute GUI
root.mainloop()
