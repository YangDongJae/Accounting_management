from re import M
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

def check_medium_category(item_list, num):
   if len(item_list) == num:
     acc.add_medium_category(input("what's the new category for Medium Category?"))
     for i in range (len(item_list)):
       print("{num}.{item}".format(num = i + 1, item = item_list[i]))
     num = int(input())

     check_medium_category(acc.get_medium_category(), num)

def check_small_category(item_list, num):
   if len(item_list) == num:
     acc.add_small_category(input("what's the new small category?"))
     for i in range (len(item_list)):
       print("{num}.{item}".format(num = i + 1, item = item_list[i]))
     num = int(input())

     check_small_category(acc.get_small_category(), num)

def check_date(date):
  import re
  date_pattern = r'\d{4}-\d{2}-\d{2}'
  check_date_pattern = re.match(date_pattern, date)
    
  if check_date_pattern:
    date = list(map(int,date.split("-")))
    long_day = [1,3,5,7,8,10,12]
    short_day = [4,6,9,11]
    extr_day = [2]
    
    if date[1] in long_day and date[2] <= 31:
      return True

    elif date[1] in short_day and date[2] <= 30:
      return True

    elif date[1] in extr_day and date[2] <= 28:
      return True

def income_mode():

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

        # Income-Coast
  while True:
    coast_value = int(input("How much is it?"))
    remote = input("You can't change this coast after this pages. is coast {coast} correct? \n 1.Yes \t 2.No \n".format(coast = coast_value))

    if remote == "1" or remote == "Yes" or remote == "yes":
      acc.set_incom(coast_value)
      break

    elif remote == "2" or remote == "No" or remote == "no":
      print("back to the coast page")      

        # Note
  while True:
    remote = input("Do you wanna note for this Incom? \n 1.Yes \t 2.No \n")

    if remote == "1" or remote == "Yes" or remote == "yes":
      note = input("please note \n")
      if len(note) > 50:
        print("is it too much please write under the 50 characters")
      else:
        acc.set_note(note)
        break
    elif remote == "2" or remote == "no!" or remote == "No!":
      break
    
  print('''
    Category is {category} \n
    Medium Category is {M} \n
    Small Category is {S} \n
    Date is {D} \n
    Coast is {C} \n
    Note {N}
  '''.format(category = acc.get_category(), M = acc.get_medium_category() , S = acc.get_small_category() , D = acc.get_date(), C = acc.get_incom(), N = acc.get_note()))
          



def expenditure_mode():
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
    date = input("When you get the money?")
    if check_date(date):
      acc.set_date(date)
      break
    else:
      print("Your date is wrong please check your date!!")

        # Income
  while True:
    coast_value = int(input("How much is it?"))
    remote = input("You can't change this coast. this coast is {coast} correct? \n 1.Yes \t 2.No \n".format(coast = coast_value))

    if remote == "1" or remote == "Yes" or remote == "yes":
      acc.set_expenditure(coast_value)
      break

    elif remote == "2" or remote == "No" or remote == "no":
      print("back to the coast page")

        # Note
  while True:
    remote = input("Do you wanna note for this income? \n 1.Yes \t 2.No \n")

    if remote == "1" or remote == "Yes" or remote == "yes":
      note = input("please note \n")
      if len(note) > 50:
        print("is it too much please write under the 50 characters")
      else:
        acc.set_note(note)
        break
    elif remote == "2" or remote == "no!" or remote == "No!":
      break

  print('''
    Category is {category} \n
    Medium Category is {M} \n
    Small Category is {S} \n
    Date is {D} \n
    Coast is {C} \n
    Note {N}
  '''.format(category = acc.get_category(), M = acc.get_medium_category() , S = acc.get_small_category() , D = acc.get_date(), C = acc.get_expenditure(), N = acc.get_note()))


  
while True:
  mode = input("Did you make Income or Expenditure?")

  if mode == "income" or mode == "Income":
    income_mode()


  elif mode == "expenditure" or mode == "Expenditure":
    expenditure_mode()
  
  else:
    print("try again")

    

    



    
