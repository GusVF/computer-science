class Tv:
    def __init__(self, size):
        self.__volume = 50
        self.__channel = 1
        self.__size = size
        self.__is_on = False

    def raise_volume(self):
        if self.__volume < 99:
            self.__volume += 1

    def lower_volume(self):
        if self.__volume > 0:
            self.__volume -= 1

    def change_channel(self, channel):
        if channel <= 1 or channel >= 99:
            raise ValueError('Channel does not exist!')

        self.__channel == channel

    def tv_on_off(self):
        self.__is_on = not self.__is_on
