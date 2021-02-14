from phase import *
from position import *
from allMoons import *
import datetime

def main():

    date = datetime.datetime.now()
    pos = position.current_possition(date)
    phasename = phase.a_phase(pos)

    print(date.strftime("%d.%m.%Y -"), phasename)
    print("Всички дати на пълнолуния в текущата година:\n", allMoons.all_moons)

    if __name__ == "__main__":
        main()

'''
Информация за пресмятане местополужението на луната:
http://gmmentalgym.blogspot.com/2013/01/moon-phase-for-any-date.html#mpbasics
https: // en.wikipedia.org / wiki / Lunar_phase

Нужна е PyEphem astronomy library за някой от пресмятанията в програмата.
'''
