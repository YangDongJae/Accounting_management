import pandas as pd
import numpy as np
from accouting import * 


acc = Accounting()


def check_category(item_list, num, category = "category"):
  if len(item_list) == num:
    acc.add_category(input("what kind of it?"))
    for i in range (len(item_list)):
      print("{num}.{item}".format(num = i + 1, item = item_list[i]))
    num = int(input())

    if category == "category":
      check_category(acc.get_category(), num)
    elif category == "medium":
      check_category(acc.get_medium_category(), num)
    elif category == "small":
      check_category(acc.get_small_category(), num)

  


while True:
  mode = input("Did you make Income or Expenditure?")

  if mode in ["Expenditure","expenditure","Income","income"]:
    break  

  else:
    print("please enter correct value ")


while True:
  if mode == "Income" or "income":
    income = acc.set_incom(input("how much?"))
    date = acc.set_date(input("when? \n"))

    for i in range (0,len(acc.get_category())):
      remote_category = "category"
      print("choose the category")
      print("{num}.{item}".format(num = i + 1, item = acc.get_category()[i]))
    category = int(input())

    check_category(acc.get_category(), category, remote_category)

    for j in range (0, len(acc.get_medium_category())):
      remote_category = "medium"
      print("choose the medium category")
      print("{num}.{item}".format(num = i + 1, item = acc.get_medium_category()[i]))
    medium_category = int(input())
    
    check_category(acc.get_medium_category(), medium_category, remote_category)

    for k in range (0, len(acc.get_small_category())):
      remote_category = "small"
      print("Choose the small category")
      print("{num}.{item}".format(num = i + 1, item = acc.get_small_category()[i]))
    small_category = int(input())                                                     # we have to consider about input value is intiger but database datatype is VARCHART so we have to handle it on the main or class with impelment method 

    check_category(acc.get_small_category(), small_category, remote_category)

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

    
