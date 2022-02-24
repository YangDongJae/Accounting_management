import pymysql
class Accounting():
  def __version__(self):
    self.version = "0.0.1"
    return self.version

  def __init__(self):
    import re
    self.conn = pymysql.connect(host = "localhost", user = "root", password = "0000", charset = 'utf8')
    self.cursor = self.conn.cursor()
    self.expenditure = None
    self.incom = None
    self.date = None
    self.category = ["other"]
    self.medium_category = ["other"]
    self.small_category = ["other"]
    self.note = None

  def get_note(self):
    return self.note

  def get_expenditure(self):
    return self.expenditure
  
  def get_incom(self):
    return self.incom

  def get_date(self):
    return self.date

  def get_category(self):
    return self.category

  def get_medium_category(self):
    return self.medium_category
    
  def get_small_category(self):
    return self.small_category

  def set_note(self,note):
    self.note = note

  def set_expenditure(self,expenditure):
    self.expenditure = expenditure

  def set_incom(self,income):
    self.incom = income

  def set_date(self,date):
    self.date = date

  def add_category(self, item):
    self.category.insert(len(self.get_category())-1, item)

  def add_medium_category(self, item):
    self.medium_category.insert(len(self.get_medium_category())-1, item)

  def add_small_category(self, item):
    self.small_category.insert(len(self.get_small_category())-1, item)        

  def del_category(self,item):
    if item in self.category is True:
        self.category.remove(item)

    else:
      "sometings going wrong"

  def saved_server(self,Table_name,Date_Of, Category, Medium_category, Small_category, Value, Note = ''):
    if Table_name == "EXPENDITURE":
      sql = "INSERT INTO EXPENDITURE values ({Date_Of_Expenditure},{Category},{Medium_category},{Small_category},{Note},{Value}",format(Table_name = Table_name, Date_Of_Expenditure = Date_Of, Category = Category, Medium_category = Medium_category, Small_category = Small_category, Note = Note, Value = Value)
      self.cursor.execute(sql)
      self.conn.commt()
      self.conn.close()
    
    elif Table_name == "INCOME":
      sql = "INSERT INTO INCOME values ({Date_Of_INCOME},{Category}{Note},{Value}",format(Table_name = Table_name, Date_Of_Expenditure = Date_Of, Category = Category, Note = Note, Value = Value)



class Visualization():
  import matplotlib as mpl
  import matplotlib.pyplot as plt
  import numpy as np
