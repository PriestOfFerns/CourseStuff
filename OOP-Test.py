

class Car: # Класс Машина
    def __init__(self,  speed, wheels, size, brand): # инициализация
        self.wheels = wheels # Количество колес
        self.speed = speed   # скорость
        self.size = size # Размер
        self.brand = brand # Брэнд
    def changeSpeed(self, Newspeed): # Метод изменить скорость
        self.speed = Newspeed
        print("vroom vroom")

class SUV(Car): # Класс Внедорожник

    def __init__(self, speed, brand):  # инициализация
        super().__init__(speed,4,"medium",brand)
    def driveOffroad(self): #метод "езда по бездорожью"
        print("Am now driving offroad ")


class Ford(SUV): # Класс форд
    def __init__(self, speed):  # инициализация
        super().__init__(speed,"Ford")

FordF150 = Ford(0)
