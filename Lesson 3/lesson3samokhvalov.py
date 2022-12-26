import random
# 1 задача
x =(random.randint(0,59))

if x < 15:
    print (x,"число в первой части" )

elif x < 30:
    print (x,"число во второй части" )

elif x < 45:
    print (x,"число в третей части" )

elif x < 59:
    print (x,"число в четвертой части" )

# Задача 2
birth_month = int(input(" Запишіть номер місяця вашого народження " ))
a = birth_month

if a > 2 and a < 6:
    print("Весна - Все довкола розцвітало.")
elif a >5 and a < 9:
    print("Літо - Діти насолоджувались літніми канікулами")
elif a > 8 and a < 12 :
    print("Осінь - Все довкола загоралось яскравими фарбами.")
elif  a > 11 and a <13:
    print("Зима - За вікном падав сніг.")
elif  a < 3 :
    print("Зима - За вікном падав сніг.")
else:
    print("Невірно введений місяць! ")
    #задача 3
import random  # підключення моду
x = (random.randint(0 ,200))
print(x)
if x %6==0 and x %3==0:
    print("Число х ділиться на 6")
else:
    print("Число х не ділиться на 6”")
#задача 4
print('Введіть координати точки:')
x = float(input("x = "))
y = float(input("y = "))

if x > 0 and y > 0:
  print('Точка в I четверті')
elif x < 0 and y > 0:
  print('Точка в II четверті')
elif x < 0 and y < 0:
  print('Точка в III четверті')
elif x > 0 and y < 0:
  print('Точка в IV четверті')
elif x == 0 and y == 0:
  print('Точка в початку координат')
elif x == 0:
  print('Точка на осі Y')
elif y == 0:
  print('Точка на осі X')
