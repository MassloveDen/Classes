class Purse:
    def __init__(self, valuta, name = 'Unknown'):
        if valuta not in ('USD', 'Eur'):
            raise ValueError
        self.__money = 0.00
        self.valuta = valuta
        self.name = name

    def up_balance(self, howmany):
        self.__money = self.__money + howmany
        return howmany

    def down_balance(self, howmany):
        if self.__money - howmany < 0:
            print('No money')
            raise ValueError ('No sredstv')
        self.__money = self.__money - howmany
        return howmany

    def info(self):
        print(self.__money)

    def __del__(self):
        print('Deleted')


x = Purse('USD')
y = Purse('USD')
y.up_balance(10)
y.info()
x.up_balance(y.down_balance(7))


x.info()
y.info()
# x.down_balance(200)


