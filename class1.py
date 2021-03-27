from tkinter import Tk, Button
from class3 import Verification

class V2(Verification):

    def __init__(self, login, password, age):
        super().__init__(login, password)
        self.__save()
        self.age = age

    def __save(self):
        with open('users') as r:
            for i in r:
                if f'{self.login, self.password}' + '\n' == i:
                    raise ValueError ('Parol syshestvyet')
        super().save()

    def show(self):
        return self.login, self.password


#x = V2('Dennis2', '1234567', 27)

# class My_app(Tk):
#
#     def __init__(self):
#         Tk.__init__(self)
#         self.geometry('400x400')
#         self.setUI()
#     def setUI(self):
#         Button(self, text = 'Ok').pack()
# root = My_app()
# root.mainloop()

x = V2('bob', '181920', 39)