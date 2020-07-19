from chef import Chef


class ChineseChef(Chef):

    @staticmethod
    def make_special_dish():
        print('The chef makes bbq')

    @staticmethod
    def make_fried_rice():
        print('The chef makes fried rice')
