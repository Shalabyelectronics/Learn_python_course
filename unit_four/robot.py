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


class Robotv(Robot):
    os = "ROS 10"
    voice_commands_data = {
            "A":"Arabic",
            "E":"English",
            "B":"Arabic & English"
            }
    def __init__(self,name,color,lang_support=None):
        super().__init__(name,color)
        if lang_support:
            self.lang_support = lang_support
        else:
            self.lang_support = "Not support Voice commands"
    def voice_commands_info(self):
        if self.lang_support in Robotv.voice_commands_data.keys():
            return f"{self.name} Robot can support voice commands in {Robotv.voice_commands_data[self.lang_support]}."
        return self.lang_support


