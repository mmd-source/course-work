import importlib,math, decimal, datetime
from position import *

dec = decimal.Decimal

class phase:

   def a_phase(pos):
      index = (pos * dec(8)) + dec("0.5")
      index = math.floor(index)
      return {
         0: "Новолуние",
         1: "Изгряващ полумесец",
         2: "Първа четвърт",
         3: "растяща луна (наближаваща пълнолуние, млада луна)",
         4: "Пълнолуние",
         5: "Намаляваща луна (преминала пълнолуние, стара луна)",
         6: "Трета (последна) четвърт",
         7: "Залязващ полумесец"
      }[int(index) & 7]

   def __init__(self,phase):
      self.phase = phase.a_phase()
