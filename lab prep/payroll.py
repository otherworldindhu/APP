user = str
end = "0"
hours = round(40,2)
print("One Stop Shop Payroll Calculator")
hours = (float(input("Please enter hours worked: ", )))
payrate =(float(input("Please enter your payrate: $", )))
if hours < 40:
 print("Employee's name: ", user)
 print("Overtime hours: 0")
 print("Overtime Pay: $0.00")
 regularpay = round(hours * payrate, 2)
 print("Gross Pay: $", regularpay)
elif hours > 40:
 overtimehours = round(hours - 40.00,2)
 print("Overtime hours: ", overtimehours)
 print("Employee's name: ", user)
 regularpay = round(hours * payrate,2)
 overtimerate = round(payrate * 1.5, 2)
 overtimepay = round(overtimehours * overtimerate)
 grosspay = round(regularpay+overtimepay,2)
 print("Regular Pay: $", regularpay)
 print("Overtime Pay: $",overtimepay)
 print("Gross Pay: $", grosspay)
while user != end:
 print()
 user = input("Please enter your name or type '0' to quit: ")
if user == end:
 print("End of Report")