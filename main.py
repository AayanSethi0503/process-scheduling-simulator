import turtle as t

# hello

def draw_rectangle(top_left_corner,width,height,clr):

    old_pos = t.pos() # store old position

    SCALE = 10
    t.up()
    t.setheading(0) # set the turtle direction
    t.goto(top_left_corner) # set initial position
    t.begin_fill()
    t.color(clr)
    t.forward(width * SCALE)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width * SCALE)
    t.right(90)
    t.end_fill()
    t.setheading(0) # reset angle
    t.goto(old_pos)
    return

def simulate_FCFS(process): # list of tuples

    top_pointer = top_left_corner
    total_time = 0

    while process:
        curr_proc_burst_time = process[-1][1]
        curr_proc_color = process[-1][2]

        t.write(total_time)
        t.forward(curr_proc_burst_time * 10)
        total_time += curr_proc_burst_time
        draw_rectangle(top_pointer,curr_proc_burst_time,50,curr_proc_color)
        top_pointer = (top_pointer[0] + curr_proc_burst_time * 10,0) # update top_pointer
        process.pop()
    
    t.write(total_time)

    return


screen = t.Screen()

# set screen title
screen.title('Process Scheduling Simulator (WIP)')

# hide turtle and set speed to zero
t.hideturtle()
t.speed(0)

# lift the pen
t.up()

# set initial position for writing
t.goto(100,200)

# write processes text

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


# draw gantt chart template [top-left = (-300,0),top-right = (300,0),bottom-right = (300,50),bottom-left = (-300,50)]
top_left_corner = (-300,0)
top_right_corner = (600,0)
bottom_left_corner = (-300,-50)
bottom_right_corner = (600,-50)

#  top_pointer = top_left_corner # points to current top process recently done

t.color('black')

t.goto(-300,0)
t.down() # ready for writing
t.write('(-300,0)')
t.forward(600)
t.write('(300,0)')
t.right(90)
t.forward(50)
t.write('(300,50)')
t.right(90)
t.forward(600)
t.write('(-300,50)')
t.right(90)
t.forward(50)

t.up()
t.goto(-300,-70)
t.setheading(0)


p1 = (0,5,'red')
p2 = (0,10,'green')
p3 = (0,15,'blue')

processes = [p3,p2,p1]

simulate_FCFS(process=processes)
# time = 0    # total time
# # ---------------
# t.write(0)
# t.down()
# t.right(90)
# t.forward(p1[1] * 10) # scale value = 10 (process have small burst time so we scale them on our window)
# time += p1[1]
# # ---------------
# # draw block and return pointer
# draw_rectangle(top_left_corner,p1[1],50,'red')
# top_pointer = (top_pointer[0] + p1[1] * 10,0)
# # ---------------
# t.write(time)
# t.forward(p2[1] * 10) 
# time += p2[1]
# # ---------------
# # draw block and return pointer
# draw_rectangle(top_pointer,p2[1],50,'green')
# top_pointer = (top_pointer[0] + p2[1] * 10,0) # update top_pointer
# t.write(time)
# t.forward(p3[1] * 10)
# time += p3[1]
# draw_rectangle(top_pointer,p3[1],50,'blue')
# top_pointer = (top_pointer[0] + p2[1] * 10,0) # update top_pointer
# t.write(time)



screen.mainloop()
