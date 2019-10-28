"""
Опишите несколько классов: TownCar, SportCar, WorkCar, PoliceCar. У каждого класса
должны быть следующие атрибуты: speed, color, name, is_police ( булево). А также несколько
методов: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда).
"""


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.name = name
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f"машина {self.name} поехала")

    def stop(self):
        print(f"машина {self.name} остановилась")

    def turn(self, direction):
            print(f"машина {self.name} повернула({direction})")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


car1 = SportCar(100, "red", "car1")
car2 = PoliceCar(120, "white", "car2")

car1.go()
car1.turn("left")

car2.go()
car2.stop()
