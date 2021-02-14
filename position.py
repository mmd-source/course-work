import importlib
import math, decimal, datetime
dec = decimal.Decimal

class position:

   def current_possition(now=None):
      if now is None:
         now = datetime.datetime.now()
   
      diff = now - datetime.datetime(2000, 1, 1)
      days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
      luns = dec("0.20439731") + (days * dec("0.03386319269"))
   
      return luns % dec(1)

   def __init__(self,curPos):
      self.curPos = position.current_possition()