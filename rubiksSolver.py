import kociemba
import serial
import tkinter as tk
from tkinter import messagebox
from time import sleep

def colorMap(color):
    color = color.lower()
    if color == 'white': return 'U'
    elif color == 'blue': return 'F'
    elif color == 'red': return 'L'
    elif color == 'orange': return 'R'
    elif color == 'green': return 'B'
    elif color == 'yellow': return 'D'
    else: raise Exception


def formatCubeString(s):

    l = s.split()
    for i in range(len(l)):
        if len(l[i]) == 1: l[i] += 'o'

    s = ''.join(l)
    s = s.replace("'", "p")
    s = s.replace("2", "t")

    return s


class Cube:
    def __init__(self):
        self.U = ''
        self.F = ''
        self.L = ''
        self.R = ''
        self.B = ''
        self.D = ''
    
    def __str__(self):
        return self.U + self.R + self.F +self.D + self.L + self.B

    def solve(self):
        solution = None
        try:
            solution = kociemba.solve(str(self))
        except:
            pass
        return solution

class app(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        self.windowOpen = False
        self.cube = Cube()

        self.start()
        
        
    def start(self):
        self.parent.geometry('300x300')
        self.parent.title('Rubik')

        tk.Button(self, bg="blue", fg="orange", height = 4, width = 20, text= 'Enter combination', command = self.ingresarCombinacion).grid(column=1, row=0)
        tk.Button(self, bg="Green", fg="orange", height = 4, width = 20, text= 'Solve', command=self.solveRubiksCube).grid(column=1, row=3)


    def ingresarCombinacion(self):
        if self.windowOpen: return
        self.windowOpen = True
        self.curFace = 'white'
        self.cube.D = '' #makes sure it returns an error until all cupe positions are marked

        self.window = tk.Toplevel(self)
        self.window.geometry('300x300')
        self.window.protocol("WM_DELETE_WINDOW", self.closeCombinaitionWindow)


        self.buttons = [None]*9
        btn = tk.Button(self.window, bg="gray", height = 3, width = 6, command = lambda: self.colorChange(0))
        btn.grid(column=2, row=2)
        self.buttons[0] = btn 
        
        btn = tk.Button(self.window, bg="gray", height = 3, width = 6, command = lambda: self.colorChange(3))
        btn.grid(column=2, row=3)
        self.buttons[3] = btn

        btn = tk.Button(self.window, bg="gray", height = 3, width = 6, command = lambda: self.colorChange(6))
        btn.grid(column=2, row=4)
        self.buttons[6] = btn

        btn = tk.Button(self.window, bg="gray", height = 3, width = 6, command = lambda: self.colorChange(1))
        btn.grid(column=3, row=2)
        self.buttons[1] = btn

        btn = tk.Button(self.window, bg="white",height = 3, width = 6)
        btn.grid(column=3, row=3)
        self.buttons[4] = btn

        btn = tk.Button(self.window, bg="gray",height = 3, width = 6, command = lambda: self.colorChange(7))
        btn.grid(column=3, row=4)
        self.buttons[7] = btn


        btn  = tk.Button(self.window, bg="gray",height = 3, width = 6, command = lambda: self.colorChange(2))
        btn.grid(column=4, row=2)
        self.buttons[2] = btn

        btn = tk.Button(self.window, bg="gray",height = 3, width = 6, command = lambda: self.colorChange(5))
        btn.grid(column=4, row=3)
        self.buttons[5] = btn
        
        btn = tk.Button(self.window, bg="gray", height = 3, width = 6, command = lambda: self.colorChange(8))
        btn.grid(column=4, row=4)
        self.buttons[8] = btn

        self.upSquare = tk.Button(self.window, bg="green", height = 1, width = 2)
        self.upSquare.grid(column=3, row=1)

        self.downSquare = tk.Button(self.window, bg="blue", height = 1, width = 2)
        self.downSquare.grid(column=3, row=5)

        self.rightSquare = tk.Button(self.window, bg="orange", height = 1, width = 2)
        self.rightSquare.grid(column=5, row=3)

        self.leftSquare = tk.Button(self.window, bg="red", height = 1, width = 2)
        self.leftSquare.grid(column=1, row=3)

        self.nextButton = self.btn9 = tk.Button(self.window, bg="brown", height = 1, width = 6, text='Next', command=self.nextButtonAction)
        self.nextButton.grid(column=3, row=7)


    def closeCombinaitionWindow(self):
        self.windowOpen = False
        self.window.destroy()

    def colorChange(self, name):
        colors = ['white', 'yellow', 'green', 'blue', 'orange', 'red']
        color = self.buttons[name].cget('bg')

        nextColor = ''
        if color.lower() == 'gray': nextColor = 'white'
        else: nextColor = colors[(colors.index(color) + 1 ) % len(colors)]
        self.buttons[name].configure(bg=nextColor)
        
    def nextButtonAction(self):

        s = ''
        for button in self.buttons:
            color = button.cget('bg')
            if color == 'gray': return
            s += colorMap(color)
        
        for index, button in enumerate(self.buttons):
            if index == 4: continue
            button.configure(bg='gray')



        if self.curFace == 'white':
            self.cube.U = s
            self.curFace = 'blue'
            self.buttons[4].configure(bg='blue')
            self.upSquare.configure(bg='white')
            self.downSquare.configure(bg='yellow')
            self.rightSquare.configure(bg='orange')
            self.leftSquare.configure(bg='red')
        elif self.curFace == 'blue':
            self.cube.F = s
            self.curFace = 'red'
            self.buttons[4].configure(bg='red')
            self.upSquare.configure(bg='white')
            self.downSquare.configure(bg='yellow')
            self.rightSquare.configure(bg='blue')
            self.leftSquare.configure(bg='green')
        elif self.curFace == 'red':
            self.cube.L = s
            self.curFace = 'orange'
            self.buttons[4].configure(bg='orange')
            self.upSquare.configure(bg='white')
            self.downSquare.configure(bg='yellow')
            self.rightSquare.configure(bg='green')
            self.leftSquare.configure(bg='blue')
        elif self.curFace == 'orange':
            self.cube.R = s
            self.curFace = 'green'
            self.buttons[4].configure(bg='green')
            self.upSquare.configure(bg='white')
            self.downSquare.configure(bg='yellow')
            self.rightSquare.configure(bg='red')
            self.leftSquare.configure(bg='orange')
        elif self.curFace == 'green':
            self.cube.B = s
            self.curFace = 'yellow'
            self.buttons[4].configure(bg='yellow')
            self.upSquare.configure(bg='blue')
            self.downSquare.configure(bg='green')
            self.rightSquare.configure(bg='orange')
            self.leftSquare.configure(bg='red')
            self.nextButton.configure(text='Ready')
        elif self.curFace == 'yellow':
            self.cube.D = s
            self.windowOpen = False
            self.window.destroy()

    def solveRubiksCube(self):
        solution = self.cube.solve()
        if solution == None:
            messagebox.showerror("Error", "Invalid combination")
            return
        
        print(solution)
        #communicate solution to robot
        solution = formatCubeString(solution)
        try:
            ser = serial.Serial('COM9', 9600) 
            sleep(2)
            ser.write(solution.encode())
            sleep(1)
            
        except:
            messagebox.showerror("Error", "Cant connect to robot")

if __name__ == "__main__":
    root = tk.Tk()
    app(root).pack(side="top", fill="both", expand = True)
    root.mainloop()
