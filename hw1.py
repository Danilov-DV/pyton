"""
Создать класс TrafficLight ( светофор) и определить у него один атрибут color (цвет) и метод
running ( запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Время перехода между
режимами должно составлять 7 и 2 секунды. Проверить работу примера, создав экземпляр и
вызвав описанный метод.
"""


import time


class TrafficLight:
    color = "зеленый"

    def running(self):
        while True:
            if self.color == "зеленый":
                print("желтый")
                time.sleep(1)
                print("красный")
                time.sleep(2)
                self.color = "красный"

            if self.color == "красный":
                print("желтый")
                time.sleep(1)
                print("зеленый")
                time.sleep(7)
                self.color = "зеленый"


my_TrafficLight = TrafficLight()
my_TrafficLight.running()
