import turtle as t

screen = t.Screen()

# set screen title
screen.title('Process Scheduling Simulator (WIP)')

# hide turtle and set speed to zero
t.hideturtle()
#t.speed(0)

# lift the pen
t.up()

# set initial position for writing
t.goto(100,200)

# write processes text with their coressponding colors

t.color('red')
t.write('Process 1 : RED',font=('Arial',8,'bold'))
t.sety(t.pos()[1] - 15)

t.color('green')
t.write('Process 2 : GREEN',font=('Arial',8,'bold'))
t.sety(t.pos()[1] - 15)

t.color('blue')
t.write('Process 3 : BLUE',font=('Arial',8,'bold'))
t.sety(t.pos()[1] - 15)

t.color('black')
t.write('Process 4 : BLACK',font=('Arial',8,'bold'))
t.sety(t.pos()[1] - 15)

t.color('purple')
t.write('Process 5 : PURPLE',font=('Arial',8,'bold'))

screen.mainloop()
