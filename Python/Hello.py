"""
 def squared():
  a = input("Введите число: ")
  a = int(a)
  print(a * a)

squared(7)

def string():
  a = input("Введите строку: ")
  print(a)


string()

def fuck(a, b, c, f=3, d=4):
print(a + b + c + f + d)


fuck(1, 3, 4,)


x = 100

def a(x):
  global z
  z = x / 2

  print(z)ou


a(x)


def b(z):
    y = z * 4
    print(y)


b(z)
"""


def string():
    """
    Возвращает a из str в float
    """
    try:
         a = input("введите число: ")
         a = float(a)
         print(a)

    except(ValueError):
         print("Error Syntax")


string()

