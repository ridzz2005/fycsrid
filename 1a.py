from datetime import date
name =input("Enter your name")
age =int(input("Enter your age"))
current_date=date.today()
print("current year :",current_date.year)
diff=100-age
final_year=current_date.year+diff
print("Dear",name,",your age will be 100 years old in the year",final_year)


