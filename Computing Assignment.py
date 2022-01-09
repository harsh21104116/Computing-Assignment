#QUESTION1
print('To find avgreges of three numbers')
num1=int(input("Enter num1 :"))
num2=int(input("Enter num2 :"))
num3=int(input("Enter num3 :"))
avg=(num1+num2+num3)/3
print("Average:",avg)




#QUESTION2
print('To compute persson income tax')
print("Tax Rate=20%")
print("Standard Deduction=$10000")
print("Dependent Deduction=$3000")
gross=int(input("Enter Gross Income :"))
dependents=int(input("Enter number of dependents :"))
Taxableincome=gross - 10000 - 3000 * dependents
print("Taxable Income:",Taxableincome)
tax=Taxableincome*20/100
print("Tax:",tax)




#QUESTION3
print('Different data type values into a list')
Student1= [21104116, "Harsh", "M", "B.Tech", 8.5]
Student2= [21104568, "Kartikay", "M", "B,Tech", 8.3]
Student3= [25640025, "Sarika", "F", "BSc", 7.9]
Student4= [15689423, "Diksha", "F", "B.A", 8.2]
print(Student1)
print(Student2)
print(Student3)
print(Student4)




#QUESTION4
print('Marks of 5 students into a list and display them in sorted manner')
print('Marks of students in computing')
marks=[100,58,79,15,62]
print(marks)
marks.sort()
print("Ascending Order:",marks)
marks.sort(reverse=True)
print("Descending Order:",marks)




#QUESTION5(a)
print('To remove an item from list')
Color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("List before removing:",Color)
item= 'Black'
Color.remove(item)
print("List after removing:",Color)



#QUESTUION(b)
print("To Remove Black and Pink from the list and replace them with Purple")
color=['Red','Green','White','Black','Pink','Yellow',]
color[3]='Purple';color[4]='Purple'
print("Replaced List:", color)
