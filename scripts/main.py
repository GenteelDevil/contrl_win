import time
import random

class main_win():
    def __init__(self):
        self.frame = "###################################################################################\n" + \
                     "# Command:                                                                        #\n" + \
                     "#                                                                                 #\n" + \
                     "###################################################################################\n" + \
                     "#          Catagories            #                        Info                    #\n" + \
                     "# ----------                     #                                                 \n" + \
                     "# Anti1 (10000/10000)            #"
    

    def show(self):
        print(self.frame)



if __name__ == "__main__":
    win = main_win()
    win.show()