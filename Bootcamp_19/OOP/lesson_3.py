# class Computer:
#     def __init__(self, cpu, memory):
#         self.__cpu = cpu
#         self.__memory = memory
#
#     # Геттеры
#     def get_cpu(self):
#         return self.__cpu
#
#     def get_memory(self):
#         return self.__memory
#
#     # Сеттеры
#     def set_cpu(self, cpu):
#         self.__cpu = cpu
#
#     def set_memory(self, memory):
#         self.__memory = memory
#
#     def make_computations(self):
#         result = self.__cpu + self.__memory
#         print(f"Computations result: {result}")
#
#     def __str__(self):
#         return f"Computer(cpu={self.__cpu}, memory={self.__memory})"
#
#     def __eq__(self, other):
#         return self.__memory == other.get_memory()
#
#
# class Phone:
#     def __init__(self):
#         self.__sim_cards_list = []
#
#     # Геттер
#     def get_sim_cards_list(self):
#         return self.__sim_cards_list
#
#     # Сеттер
#     def set_sim_cards_list(self, sim_cards_list):
#         self.__sim_cards_list = sim_cards_list
#
#     def call(self, sim_card_number, call_to_number):
#         print(f"Calling {call_to_number} from sim card-{sim_card_number}")
#
#     def __str__(self):
#         return f"Phone(sim_cards_list={self.__sim_cards_list})"
#
#
# class SmartPhone(Computer, Phone):
#     def __init__(self, cpu, memory):
#         Computer.__init__(self, cpu, memory)
#         Phone.__init__(self)
#
#     def use_gps(self, location):
#         print(f"Routing to location: {location}")
#
#     def __str__(self):
#         return f"SmartPhone(cpu={self.get_cpu()}, memory={self.get_memory()}, sim_cards_list={self.get_sim_cards_list()})"
#
#
# # Создаем объекты
# computer = Computer(cpu="Intel i5", memory=8)
# phone = Phone()
# smartphone1 = SmartPhone(cpu="Snapdragon", memory=4)
# smartphone2 = SmartPhone(cpu="Exynos", memory=6)
#
# # Распечатываем информацию о созданных объектах
# print("Computer:", computer)
# print("Phone:", phone)
# print("SmartPhone 1:", smartphone1)
# print("SmartPhone 2:", smartphone2)
#
# # Опробовываем методы
# computer.make_computations()
# phone.call(sim_card_number=1, call_to_number="+996 777 99 88 11")
# smartphone1.use_gps(location="Destination A")
# smartphone2.use_gps(location="Destination B")
#
# # Переопределяем магические методы сравнения в классе Computer
# print("Memory of Computer and Smartphone 1 are equal:", computer == smartphone1)
# print("Memory of Smartphone 1 and Smartphone 2 are equal:", smartphone1 == smartphone2)
#



# class Phone:
#     def __init__(self, num, nomer):
#         self.num = num
#         self.nomer = nomer
#
#     def call(self):
#         if self.num == 1:
#             return f"beeline dan {self.nomer} ushuga calling"
#         elif self.num == 2:
#             return f"megacom dan {self.nomer} ushuga calling"
#         else:
#             return 'bag'
#
#
# f = Phone(4, +996779202060)
# print(f.call())
