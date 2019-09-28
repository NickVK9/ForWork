'''
Выполнения тестового задания для ПАО Быстробанк
'''

class Man():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return "Hello, my name is {}".format(self.name)

class Car():
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def sit_into(self, driver): #водителем должен быть объект класса Man
        return 'Я {}, в меня сел {}'.format(self.model, driver.name)

    def start_engine(self):
        return 'Я {}, я запускаю двигатель'.format(self.model)

    def drive(self):
        return 'Я {}, я еду'.format(self.model)

    def breaks(self):
        return 'Я {}, я торможу БЫСТРО'.format(self.model)

    def get_out(self, driver):
        return 'Я {}, из меня вышел {}'.format(self.model, driver.name)

class Truck():
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def sit_into(self, driver): #водителем должен быть объект класса Man
        return 'Я {}, в меня сел {}'.format(self.model, driver.name)

    def start_engine(self):
        return 'Я {}, я запускаю двигатель'.format(self.model)

    def drive(self):
        return 'Я {}, я еду'.format(self.model)

    def breaks(self):
        return 'Я {}, я торможу МЕДЛЕННО'.format(self.model)

    def get_out(self, driver):
        return 'Я {}, из меня вышел {}'.format(self.model, driver.name)


'''Тесты'''

if __name__ == "__main__":
    p1 = Man("Петр", 36)
    print(p1.greet())

    c1 = Car("lada granta", "зеленый")

    print(c1.sit_into(p1))
    print(c1.drive())
    print(c1.breaks())
    print(c1.get_out(p1))

    t1 = Truck("Газель", "серый")

    print(t1.sit_into(p1))
    print(t1.drive())
    print(t1.breaks())
    print(t1.get_out(p1))