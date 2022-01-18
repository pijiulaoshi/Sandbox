import turtle
from turtle import Turtle
from trees import *

class SpaceTurtle(Turtle):

    def __init__(self):
        super().__init__(shape='turtle')
        self.speed(0)
        self.st_size = 10
        self.angle = 90
        self.penup()
        self.left(180)
        self.forward(0)
        self.right(90)
        self.pendown()
        self.pos_list = []

    def update_actions(self):
        self.actions = {
            "F": {"func": self._forward, "pars":[self.st_size, True]},
            "G": {"func": self._forward, "pars":[self.st_size, True]},
            "f": {"func": self._forward, "pars":[self.st_size, False]},
            "|": {"func": self._turn, "pars":["L", 180]},
            "+": {"func": self._turn, "pars":["L", self.angle]},
            "-": {"func": self._turn, "pars":["R", self.angle]},
            "[": {"func": self.save_state, "pars":[None]},
            "]": {"func": self.restore_state, "pars":[None]},
            "X": {"func": self.do_nothing, "pars":[None]},
            # FIXME:
            ">": {"func": self.do_nothing, "pars":[None]},  #Multiply the line length by the line length scale factor
            "<": {"func": self.do_nothing, "pars":[None]},  #Divide the line length by the line length scale factor
        } 
        
    def create_string(self, ax, dpth, rules):
        """Hier moet info"""
        a_string = ax
        for i in range(dpth):
            n_string = ""
            for ch in a_string:
                n_string += rules.get(ch, ch)
            a_string = n_string
        return(a_string)

    def _forward(self, *args):
        ags = args[0]
        if ags[1] == False:
            self.penup()
        self.forward(int(ags[0]))
        self.pendown()
    
    def _turn(self, *args):
        ags = args[0]
        if ags[0] == "L":
            self.left(self.angle)
        elif ags[0] == "R":
            self.right(self.angle)
    
    def save_state(self, *args):
        st_x, st_y = self.pos()
        st_head = self.heading()
        self.pos_list.append([st_x, st_y, st_head])
    
    def restore_state(self, *args):
        self.penup()
        st = self.pos_list.pop(-1)
        self.setpos(st[0], st[1])
        self.seth(st[2])
        self.pendown()
    
    def do_nothing(self, *args):
        return

    
    def draw_fractal(self, axiom="F", depth=5, rules=None, step_size=4, angle=90):
        '''Draw fractal
        axiom := str
        depth := int
        rules := dict
        '''
        # prep
        self.st_size = step_size
        self.angle = angle
        self.update_actions()
        path = self.create_string(axiom, depth, rules)
        print(path)

        # work
        for ch in path:
            if ch in self.actions:
                pars = self.actions[ch]["pars"]
                self.actions[ch]["func"](pars)
        # finish
        turtle.done()
        return


    
if __name__ == "__main__":
    st = SpaceTurtle()
   
    stt = XMAS
    st.draw_fractal(stt["A"], stt["D"], stt["R"], stt["S"], stt["AN"])
