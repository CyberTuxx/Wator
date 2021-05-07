from tkinter import *

class Fenetre():
    
    def __init__(self, size_x, size_y):
        size_x = size_x + 1
        size_y = size_y + 1
        self.size_case = 24
        self.fen = Tk()
        self.fen.title("WaTor")
        self.window_h = size_x*self.size_case
        self.window_w = size_y*self.size_case
        self.can = Canvas(self.fen, width = self.window_w + self.size_case, height = self.window_h + self.size_case, bg = 'white')
        self.can.pack(side = TOP, padx = 5, pady = 5)
        self.display_line()
        #self.fen.mainloop()

    def display_line(self):
        y = 0
        while y <= self.window_h:
            self.can.create_line(y,self.size_case,y,self.window_h,width=1,fill='black')
            y+=self.size_case
        
        x = 0
        while x <= self.window_w:
            self.can.create_line(self.size_case,x,self.window_w,x,width=1,fill='black')
            x+=self.size_case
    
    def display_grille(self, grille, is_empty, is_requin):
        self.can.delete(ALL)
        self.display_line()
        for x in range(0, len(grille)):
            for y in range(0, len(grille[x])):
                if not (is_empty(grille, x, y)):
                    if is_requin(grille, x, y):
                        self.can.create_rectangle(x*self.size_case + self.size_case, y*self.size_case + self.size_case, x*self.size_case + (2*self.size_case), y*self.size_case + (2*self.size_case), fill='red')
                    else:
                        self.can.create_rectangle(x*self.size_case + self.size_case, y*self.size_case + self.size_case, x*self.size_case + (2*self.size_case), y*self.size_case + (2*self.size_case), fill='blue')

    def next(self, time, func, *args):
        self.fen.after(time, func, *args)
