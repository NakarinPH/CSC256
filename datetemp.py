# ----------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------

import datetime


# ----------------------------------------------------------------------
# DateTemp Class
# ----------------------------------------------------------------------

class DateTemp:

    def __init__(self, date, temperature):
        self._date = date
        self._temperature = temperature

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, datetime.date):
            raise ValueError(f"Value {value} is not a datetime.date")
        self._date = value

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        # If value cannot be parsed, 'float' will raise a ValueError
        self._temperature = float(value)

    def set_date_from_ints(self, year, month, day):
        # If arguments cannot be parsed, 'int' will raise a ValueError
        # If arguments do not represent a valid date, 'datetime.date' will raise a ValueError
        self._date = datetime.date(int(year), int(month), int(day))

    def __str__(self):
        return f'The temperature on {self.date} was {self.temperature} F'

    def __repr__(self):
        return self.__str__()


# ----------------------------------------------------------------------
# Sorting Functions
# As a precondition, assume 'items' is a list of DateTemp objects
# ----------------------------------------------------------------------

def sorted_by_date(items):
    return sorted(items, key=lambda x: x.date)


def sorted_by_temp(items):
    return sorted(items, key=lambda x: x.temperature)
