"Script for forward motion and steering via R2 and left stick."
from pyPS4Controller.controller import Controller


"""
min R2 value: -32252 ~ -33000
max R2 value: 32767 ~ 33000

min L3 value: -32767 ~ -33000
max L3 value: 32767 ~ 33000
"""


class MyController(Controller):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # In __init__ or after MyController definition
        for attr in dir(MyController):
            if attr.startswith("on_") and callable(getattr(MyController, attr)):
                if attr not in ["on_R2_press", "on_R2_release", "on_L3_left", "on_L3_right"]:
                    setattr(MyController, attr, lambda *args, **kwargs: None)
        #
        #self.min_r2 = 0
        #self.max_r2 = 0

    def on_R2_press(self, value):
        #if value > self.max_r2:
        #    self.max_r2 = value
        #if value < self.min_r2:
        #    self.min_r2 = value
        print("speed:", ((value+33000)/66000)**2) # [0,1]

    def on_R2_release(self):
        #print("Goodbye world", self.min_r2, self.max_r2)
        print("speed: 0")

    def on_L3_left(self, value):
        print("steer:", value/33000) #[-1,0]
    def on_L3_right(self, value):
        print("steer:", value/33000) #[0,1]

    #def on_R3_left(self, value): pass
    #def on_R3_right(self, value): pass
    #def on_R3_up(self, value): pass
    #def on_R3_down(self, value): pass
    #def on_R3_x_at_rest(self): pass
    #def on_R3_y_at_rest(self): pass
    #def on_L3_left(self, value): pass
    #def on_L3_right(self, value): pass
    #def on_L3_up(self, value): pass
    #def on_L3_down(self, value): pass
    #def on_L3_x_at_rest(self): pass
    #def on_L3_y_at_rest(self): pass


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
#controller.listen(timeout=60)
controller.listen()
