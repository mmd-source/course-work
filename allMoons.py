import datetime
import ephem

class allMoons:

    def __init__(self, moons, date, end_date,year = 2021):
        self.date = ephem.Date(datetime.date(year - 1, 12, 31))
        self.end_date = ephem.Date(datetime.date(year + 1, 1, 1))
        self.a_moons = []

    def all_moons(year):
        moons = []
        date = ephem.Date(datetime.date(year - 1, 12, 31))
        end_date = ephem.Date(datetime.date(year + 1, 1, 1))

        while date <= end_date:
            date = ephem.next_full_moon(date)
            local_date = ephem.localtime(date)
            if local_date.year == year:
                moons.append(local_date.strftime("%d.%m.%Y"))
        return moons

    moons = all_moons(2021)
