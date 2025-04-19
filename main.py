import turtle as t
from tkinter import *
from tkinter import Button
from collections import deque

SCALE = 20

def draw_gantt_chart_outline():
    t.color('black')
    t.goto(-300,0)
    t.down()
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

    return

def draw_text_info():
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
    return


def draw_rectangle(top_left_corner,width,height,clr):

    old_pos = t.pos() # store old position
    t.up()
    t.setheading(0) # set the turtle direction
    t.goto(top_left_corner[0],top_left_corner[1]) # set initial position
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

# input = queue
# return = none
def simulate_FCFS(processes):
    
    # it is to be noted that top_pointer always keeps track of
    # starting top_left position for next rectangle to draw
    top_pointer = [top_left_corner[0],top_left_corner[1]]

    # total time passed by as we move
    total_time = 0 

    # while queue is not empty
    while processes: 
        curr_proc_arrival_time = processes[0][0]
        curr_proc_burst_time = processes[0][1]
        curr_proc_color = processes[0][2]

        # label each milestone
        t.write(total_time)

        # check if atleast one process is terminated
        # and check if current process time is greater than 
        # time currently passed by, if yes it means
        # CPU had to wait = waiting_time 
        # because the queue is sorted based on arrival time
        # which means current process is the most closest process
        # but it will take 'waiting_time' for it to come in ready queue
        if total_time > 0 and curr_proc_arrival_time > total_time:
            waiting_time = curr_proc_arrival_time - total_time
            print(curr_proc_arrival_time)
            draw_rectangle(top_pointer,waiting_time,50,'pink')
            total_time += waiting_time
            t.forward(waiting_time * 10)
            t.write(total_time) # label milestone
            top_pointer[0] += waiting_time * 10
            
        t.forward(curr_proc_burst_time * 10)
        total_time += curr_proc_burst_time

        # remove the process from the queue
        processes.popleft()
        # draw its portion
        draw_rectangle(top_pointer,curr_proc_burst_time,50,curr_proc_color)
        # update top pointer
        top_pointer[0] += curr_proc_burst_time * 10
    
    # label milestone
    t.write(total_time)

    return

def simulate_RR(processes,quantum):

    top_pointer = [top_left_corner[0],top_left_corner[1]]
    total_time = 0

    # write initial value 
    t.write(0)
    
    while processes:
        print(total_time)
        print(processes)
        
        curr_proc_arrival_time = processes[0][0]
        curr_proc_burst_time = processes[0][1]
        curr_proc_color = processes[0][2]

        if len(q) > 1:
            next_proc_arrival_time = processes[1][0]


        if curr_proc_arrival_time > total_time and total_time < next_proc_arrival_time:
            # we have to wait (next_proc_arrival_time - total_time)
            waiting_time = curr_proc_arrival_time - total_time
            draw_rectangle(top_pointer,waiting_time,50,'pink')
            total_time += waiting_time
            t.forward(waiting_time * 10)
            t.write(total_time) # label milestone
            top_pointer[0] += waiting_time * 10
        elif curr_proc_burst_time == 0 and total_time < next_proc_arrival_time:
            
            waiting_time = next_proc_arrival_time - total_time
            draw_rectangle(top_pointer,waiting_time,50,'pink')
            total_time += waiting_time
            t.forward(waiting_time * 10)
            t.write(total_time) # label milestone
            top_pointer[0] += waiting_time * 10


        elif quantum >= curr_proc_burst_time:
            processes.popleft()
            total_time += curr_proc_burst_time
            t.forward(curr_proc_burst_time * SCALE)
            draw_rectangle(top_pointer,curr_proc_burst_time,50,curr_proc_color)
            top_pointer[0] += curr_proc_burst_time * SCALE
            
        else:        
            # use cpu time
            processes[0][1] -= quantum
            total_time += quantum
            t.forward(quantum * SCALE)
            draw_rectangle(top_pointer,quantum,50,curr_proc_color)
            top_pointer[0] += quantum * SCALE
            # we usually switch process after time slice
            # but if there is no other process in the ready queue
            # then we have no choice but to run this one again
            if total_time < next_proc_arrival_time:
                dummy = 0
            else:
                q.append(q[0])
                q.popleft()

        # update milestone
        t.write(total_time)


        
    return

# def merge(left,right):
#     merged = []
#     i=j=0
    
#     while i <len(left) and j<len(right):
#         if left[i][0] <= right[j][0]:
#             merged.append(left[i])
#             i += 1
#         else:
#             merged.append(right[j])
#             j += 1
            
#         merged.extend(left[i:])
#         merged.extend(right[j:])
#         return merged

# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr
    
#     mid = len(arr) // 2
#     left_half = merge_sort(arr[:mid])
#     right_half = merge_sort(arr[mid:])
#     return merge(left_half, right_half)


def simulate_SJF_non_premptive(processes):
# it is to be noted that top_pointer always keeps track of
    # starting top_left position for next rectangle to draw
    top_pointer = [top_left_corner[0],top_left_corner[1]]

    # total time passed by as we move
    total_time = 0
    
    process_list = list(processes)
    process_list.sort(key=lambda proc: proc[1]) 
    processes = deque(process_list)
    # while queue is not empty
    while processes: 
        curr_proc_arrival_time = processes[0][0]
        curr_proc_burst_time = processes[0][1]
        curr_proc_color = processes[0][2]

        # label each milestone
        t.write(total_time)

        # check if atleast one process is terminated
        # and check if current process time is greater than 
        # time currently passed by, if yes it means
        # CPU had to wait = waiting_time 
        # because the queue is sorted based on arrival time
        # which means current process is the most closest process
        # but it will take 'waiting_time' for it to come in ready queue
            
        t.forward(curr_proc_burst_time * 10)
        total_time += curr_proc_burst_time

        # remove the process from the queue
        processes.popleft()
        # draw its portion
        draw_rectangle(top_pointer,curr_proc_burst_time,50,curr_proc_color)
        # update top pointer
        top_pointer[0] += curr_proc_burst_time * 10
    
    # label milestone
    t.write(total_time)

    
    
    return

def simulate_SJF_premptive(processes):
# it is to be noted that top_pointer always keeps track of
    # starting top_left position for next rectangle to draw
    top_pointer = [top_left_corner[0],top_left_corner[1]]

    # total time passed by as we move
    total_time = 0
    
    process_list = list(processes)
    process_list.sort(key=lambda proc: proc[1]) 
    processes = deque(process_list)
    # while queue is not empty
    while processes: 
        curr_proc_arrival_time = processes[0][0]
        curr_proc_burst_time = processes[0][1]
        curr_proc_color = processes[0][2]

        # label each milestone
        t.write(total_time)

        # check if atleast one process is terminated
        # and check if current process time is greater than 
        # time currently passed by, if yes it means
        # CPU had to wait = waiting_time 
        # because the queue is sorted based on arrival time
        # which means current process is the most closest process
        # but it will take 'waiting_time' for it to come in ready queue
            
        t.forward(curr_proc_burst_time * 10)
        total_time += curr_proc_burst_time

        # remove the process from the queue
        processes.popleft()
        # draw its portion
        draw_rectangle(top_pointer,curr_proc_burst_time,50,curr_proc_color)
        # update top pointer
        top_pointer[0] += curr_proc_burst_time * 10
    
    # label milestone
    t.write(total_time)

    
    
    return



# create a screen object
screen = t.Screen()

# set screen title
screen.title('Process Scheduling Simulator (WIP)')

# hide turtle and set speed to zero
t.hideturtle()
t.speed(0)


# draw and write text information on screen
draw_text_info()

# draw gantt chart template 
# [top-left = (-300,0),
# top-right = (300,0),
# bottom-right = (300,50),
# bottom-left = (-300,50)]

top_left_corner = (-300,0)
top_right_corner = (600,0)
bottom_left_corner = (-300,-50)
bottom_right_corner = (600,-50)

#  top_pointer = top_left_corner # points to current top process recently done

# create gantt chart outline
draw_gantt_chart_outline()

# create a queue for scheduling
q = deque() 

# hard coded processes
p1 = [1,5,'red']
p2 = [13,5,'green']
p3 = [15,6,'blue']
p4 = [12,3,'black']
p5 = [8,5,'purple']
# put all processes in a list
process_list = [p1,p2,p3,p4,p5]

# sort the list with key = arrival time
process_list = sorted(process_list)

# add them to queue
for item in process_list:
    q.append(item)


# simulate_FCFS(processes=q)
simulate_RR(processes=q,quantum=2)

screen.mainloop()
