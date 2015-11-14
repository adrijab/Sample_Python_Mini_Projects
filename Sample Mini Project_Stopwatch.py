#Mini-project description - "Stopwatch: The Game" 

#Our mini-project will focus on combining text drawing in the canvas with timers to build a simple digital stopwatch that keeps track of the time in tenths of a second. The stopwatch should contain "Start", "Stop" and "Reset" buttons. 



import simplegui

count = 0
A = 0
B = 0
C = 0
D = 0
clock = ""
x = 0
y = 0
result = str(x) + '/' + str(y)	

def counter():
    global count
    count += 1
    
def format(t):
    global A,B,C,D,clock
    A = t // 600
    B = (t // 100) % 6
    C = (t // 10) % 10
    D = t % 10
    clock = str(A) + ':' + str(B) + str(C) + '.' + str(D)
    return clock

def start():
    timer.start()
    
def stop():
    global x,y,result
    
    if (timer.is_running() == True):	
        if ( D == 0 ):
            x += 1
        y += 1
    result = str(x) + '/' + str(y)
    timer.stop()
    
    
def reset():
    global count,x,y,result
    
    count = 0
    format(count)
    x = 0
    y = 0
    result = str(x) + '/' + str(y)
    timer.stop()
    
timer = simplegui.create_timer(100, counter)

def draw(canvas):
    canvas.draw_text(format(count), [125, 125], 25, "White")
    canvas.draw_text(result, [225,50], 25, "Red")
    
frame = simplegui.create_frame("StopWatch", 300, 200)

frame.set_draw_handler(draw)	
frame.add_button("Start", start, 75)	
frame.add_button("Stop", stop, 75)
frame.add_button("Reset", reset, 75)

frame.start()