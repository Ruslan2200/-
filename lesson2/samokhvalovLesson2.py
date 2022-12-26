#завдання 1
first_name = input (" Введите свое имя ! ")
last_name = input(" Введите вашу фамилию !  ")
age = input("Сколько вам лет ")
full_name = first_name + ' ' + last_name + ' ' + age
print('Hello'" " +full_name.title())

print("\nRuslan")

print("Ruslan\tSamokhvalov")
double_name = first_name*5

print(double_name)

name = "Гарний день сьогодні!        "
print(name.strip())

name = "     Сніг не падав, він летів"
print(name.lstrip())
#print("Ruslan")
#print("\tRuslan")
#print("Samokhvalov")
#print("\nSamokhvalov")

#задання 2
import math
r = float(input("Довжини кола та площі круга R " ))
d = 3.14 * r
print(f"Рузультат {d}")


#завдання 3
print("Сейчас курс: 1 доллар = 36,92 uah")

q1 = int(input('Введите сумму UAH :'))
q2 = float(0.027)


r = q1 * q2
float = r

d = (round(float,2 ))
print(f"Поточний курс складає {d}" )




