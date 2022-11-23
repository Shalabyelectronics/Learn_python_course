class Robot:
    os = "ROS 1"
    robots = 0
    def __init__(self,name,color):
        self.name = name
        self.color = color
        Robot.robots += 1
    def move(self):
        steps = input("How many steps do you want me to move?")
        return f"{self.name} moved {steps} step(s)."
    def os_v(self):
        return f"{self.name} - {self.os} OS."
        
    @classmethod
    def update(cls, os_sys):
        print(f"OS updated from {cls.os} OS to {os_sys} OS.")
        cls.os = os_sys

    @classmethod
    def from_file(cls,filename):
        ro_list = []
        with open(filename) as file:
            d = file.readlines()
        for r in d:
            name,color = r[:-1].split("-")
            ro_list.append(cls(name,color))
        return ro_list

    @staticmethod
    def add(*args):
        return sum(args)



