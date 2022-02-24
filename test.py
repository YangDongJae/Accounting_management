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

    
while True:
  mode = input("Did you make Income or Expenditure?")

  if mode == "Income" or "income":
    while True:
      test = True
      print("!")
      mode = None
      break

  elif mode == "Expenditure" or "expenditure":
    while True:     
        # Category     
      print("choose the category")
      for i in range (0,len(acc.get_category())):
        print("{num}.{item}".format(num = i + 1, item = acc.get_category()[i]))
      category = int(input())
      check_category(acc.get_category(), category)  
      print("choose the medium category")
      for j in range (0, len(acc.get_medium_category())):
        print("{num}.{item}".format(num = j + 1, item = acc.get_medium_category()[j]))
      medium_category = int(input())  
      check_medium_category(acc.get_medium_category(), medium_category) 
      print("Choose the small category")
      for k in range (0, len(acc.get_small_category())):
        print("{num}.{item}".format(num = k + 1, item = acc.get_small_category()[k]))
      small_category = int(input())                                                     
      check_small_category(acc.get_small_category(), small_category)

        # Date
      while True:  
        date = input("When you spend the money?")
        if check_date(date):
          acc.set_date(date)
          break
        else:
          print("Your date is wrong please check your date!!")

        # Expenditure_Coast
      while True:
        coast_value = int(input("How much is it?"))
        remote = input("You can't change this coast. this coast is {coast} correct? \n 1.Yes \t 2.No \n".format(coast = coast_value))

        if remote is "1" or "Yes" or "yes":
          acc.set_expenditure(coast_value)
          break

        elif remote is "2" or "No" or "no":
          print("back to the coast page")

        # Note
      while True:
        remote = input("Do you wanna note for this expenditure? \n 1.Yes \t 2.No \n")

        if remote is "1" or "Yes" or "yes":
          note = input("please note \n")
          if len(note) > 50:
            print("is it too much please write under the 50 characters")
          else:
            acc.set_note(note)
            break
        elif remote is "no!" or "No!":
          break

        print('''
          Category is {category} \n
          Medium Category is {M} \n
          Small Category is {S} \n
          Date is {D} \n
          Coast is {C} \n
          Note {N}
        '''.format(category = acc.get_category(), M = acc.get_medium_category() , S = acc.get_small_category() , D = acc.get_date(), C = acc.get_expenditure(), N = acc.get_note))

  else:
    print("please enter correct value ")