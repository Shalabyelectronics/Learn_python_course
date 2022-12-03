class Robot:
    os = "ROS 1"
    robots = 0
    def __init__(self,name,color):
        self.name = name
        self.color = color
        Robot.robots += 1
        self.__ip = None
        self.__port = None
        self.is_internet_connection = False
    @property
    def ip_port_info(self):
        if self.__ip and self.__port:
            self.is_internet_connection = True
            return f"Ip : {self.__ip}\nPort : {self.__port}."
        return "There is no internet connection."
    @ip_port_info.setter
    def ip_port_info(self,data):
        self.__ip, self.__port = data
    @ip_port_info.deleter
    def ip_port_info(self):
        print("IP and Port Was Deleted!!!")
        self.__ip = None
        self.__port = None
        self.is_internet_connection = False
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
    robot_length = 100
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
        self.my_ro_commands = {}
    def voice_commands_info(self):
        if self.lang_support in Robotv.voice_commands_data.keys():
            return f"{self.name} Robot can support voice commands in {Robotv.voice_commands_data[self.lang_support]}."
        return self.lang_support
    def __str__(self):
        return f"Robot name : {self.name}\nRobot color: {self.color}\nRobot Language Support :{self.voice_commands_info()}"
    def __repr__(self):
        return f"Robotv(name={self.name},color={self.color},lang_support={self.lang_support})"
    def __len__(self):
        return Robotv.robot_length
    def __setitem__(self,command,replay):
        if command not in self.my_ro_commands.keys():
            self.my_ro_commands[command] = replay
        else:
            return f"This {command} command is already added"
    def __getitem__(self,command):
        if command in self.my_ro_commands.keys():
            return self.my_ro_commands[command]
        else:
            return f"Sorry We can't find this {command} command."
    def __delitem__(self,command):
        if command in self.my_ro_commands.keys():
            del self.my_ro_commands[command]
            return f"Deleted {command} command is Done."
        return f"We can't find {command} command to delete it?"





