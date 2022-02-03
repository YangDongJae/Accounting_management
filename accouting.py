from unicodedata import category


class Accounting():
  def __version__(self):
    self.version = "0.0.1"
    return self.version

  def __init__(self):
    self.expenditure = None
    self.incom = None
    self.date = None
    self.category = ["other"]

  def get_expenditure(self):
    return self.expenditure
  
  def get_incom(self):
    return self.incom

  def get_date(self):
    return self.date

  def get_category(self):
    return self.category

  def set_expenditure(self,expenditure):
    self.expenditure = expenditure

  def set_incom(self,income):
    self.incom = income

  def set_date(self,date):
    self.date = date

  def add_category(self, item):
    self.category.insert(len(self.get_category())-1, item)

  def del_category(self,item):
    if item in self.category is True:
        self.category.remove(item)

    else:
      "sometings going wrong"

class Visualization():
  import matplotlib as mpl
  import matplotlib.pyplot as plt
  import numpy as np
