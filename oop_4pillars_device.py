    def get_screen_size(self):
        return self.screen_size

    def set_screen_size(self, s_size):       #encapsulation
        if s_size > 30:
            self.screen_size = s_size
        else:
            print("Screen size is very large")

    def not_portable(self):                  #abstraction
        self.portable = False
        print("This device is not portable")
        return self.portable

class Laptop(Devices):                       #inheritance

    def __init__(self, o_system, processor, ram, network, p_origin, s_size, charge):
        super().__init__(o_system, processor, ram, network, p_origin, s_size)

        self.charge = charge

    def get_charge(self):
        charge = input("What is the type of charger? ")
        self.charge = charge
        return self.charge


class Computer(Devices):

    def __init__(self, o_system, processor, ram, network, p_origin, s_size,  cd_drive, speakers):
        super().__init__(o_system, processor, ram, network, p_origin, s_size)

        self.cd_drive = cd_drive
        self.speakers = speakers

    def get_cd_drive(self):
        return self.cd_drive

    def speakers(self):
        return self.speakers


class Tablet(Devices):

    def __init__(self,o_system, processor, ram, network, p_origin, s_size, charge):
        super().__init__(o_system, processor, ram, network, p_origin, s_size)

        self.charge = charge

    def get_charge(self):                       ##polymorphism
        charge = input("What is the type of charger? ")
        self.charge = charge
        return self.charge