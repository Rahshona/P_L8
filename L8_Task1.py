class Data():
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Ok'
                else:
                    return f'It is wrong'
            else:
                return f'It is wrong'
        else:
            return f'It is wrong'

    def __str__(self):
        return f'Today {Data.extract(self.day_month_year)}'

d_day = Data('9 - 8 - 1999')
print(d_day)
print(Data.valid(18, 10, 2023))
print(d_day.valid(8, 20, 2012))
print(Data.extract('12 - 10 - 2009'))
print(d_day.extract('6 - 7 - 2013'))
print(Data.valid(29, 12, 1991))