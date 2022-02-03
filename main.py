import pandas as pd
import numpy as np
from accouting import * 
acc = Accounting()


def check_category(item_list, num):
  if len(item_list) == num:
    acc.add_category(input("what kind of it?"))
    for i in range (len(item_list)):
      print("{num}.{item}".format(num = i + 1, item = item_list[i]))
    num = int(input())

    check_category(acc.get_category(), num)

  


while True:
  mode = input("Did you make Income or Expenditure?")

  if mode in ["Expenditure","expenditure","Income","income"]:
    break  

  else:
    print("please enter correct value ")


while True:
  if mode == "Income" or "income":
    income = acc.set_incom(input("how much?"))
    date = acc.set_date(input("when?"))

    for i in range (0,len(acc.get_category())):
      print("{num}.{item}".format(num = i + 1, item = acc.get_category()[i]))
    category = int(input())

    check_category(acc.get_category(), category)

    # if category == len(category_list):
    #   acc.add_category(input("what kind of it?"))
    #   for j in range (len(category_list)):
    #     print("{num}.{item}".format(num = j + 1, item = category_list[j]))
    #   category = int(input())


  elif mode == "expenditure" or "Expenditure":
    expenditure = acc.set_expenditure("how many use for it?")
    date = acc.set_data("when?")

  else:
    print("please check your answer")

  break
    
