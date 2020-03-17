This is the source code for my Arduino based Rubik’s cube solving robot.

I based my robot design on <a href="https://www.instructables.com/id/Rubiks-Cube-Solver/">this </a> link.

Look at the pictures folder for a video of my robot working on the Rubik’s cube.

The rubiksRobot.ino file contains the code for the arduino board,the rubiksSolver.py file contains the code for the a tkinter based GUI to enter the state of the cube. 

To solve the cube, I used <a href="https://github.com/muodov/kociemba">this </a> package in order to use Kociemba algorithm to solve the cube in around 20 moves. I used the <a href="https://pythonhosted.org/pyserial/">pyserial</a> package to be able to communicate with the Arduino board from the python app.











