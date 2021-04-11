import os

os.system('cls')
regHours = 40
multiplier = 1.5
overTimeHours = 0
hours = float(0)
payRate = float(0)
taxRate = .28
tax = 0


def totalPay(Hours, payRte):
    pay = float(0)
    if float(Hours) > float(regHours):
        overTmeHours = float(hours) - float(regHours)
        print('Over Time Hours', overTmeHours)
        overTimePay = ((overTmeHours * payRte) * multiplier)
        print("Overtime pay is:", overTimePay)
        print('Regular pay is: $', regHours * payRte)
        pay = ((float(regHours) * float(payRate)) + float(overTimePay))
        tax = (float(pay) * float(taxRate))
        print('Tax is:$', round(tax, 2))
        pay = float(pay) - float(tax)

        return pay
    else:
        pay = (float(hours) * float(payRte))
        tax = (float(pay) * float(taxRate))
        print('Tax is:$', round(tax, 2))
        pay = (float(pay) - float(round(tax, 2)))
        return pay


hours = input('Enter the hours you worked this week:')
payRate = input('Enter your hourly pay rate:')
print('pay Rate :$', float(payRate), 'Hours is:', float(hours))
total = totalPay(float(hours), float(payRate))
print('Your pay today is $', '{:,.2f}' .format(total))
