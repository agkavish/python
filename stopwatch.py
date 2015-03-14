# template for "Stopwatch: The Game"
import simplegui

# define global variables
ctime = 0
hr = 0
mt = 0
sec = 0
ms = 0
interval = 100
tstops = 0 # total stops counter
wstops = 0 # sucessful stop counter

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global hr, mt, sec, ms
    ms = t % 10
    sec = t / 10
    mt = sec / 60
    hr = mt / 60
    ss = '' # seconds in string
    mms = str(ms)  # millisconds in string
    mts = '' # minutes in string
    hrs = '' # Hours in string
    ts = 0
    tm = 0
    
    ts = sec - (sec/60)*60
    if(ts == 0):
        ss = '00'
    elif(ts < 10):
        ss = '0' + str(ts)
    else :
        ss = str(ts)
    
    tm = mt - (mt/60)*60

    if(tm == 0):
        mts = '0'
    else:
        mts = str(tm)
     
    if (hr < 10):
        hrs = '0' + str(hr)
    else:
        hrs = str(hr)
        
    formatedStr = mts + ':' + ss + '.' + mms
    return formatedStr
    
def count_success(running):
    global tstops, wstops
    if(running == True):
        tstops += 1
        if(ctime % 10 == 0):
            wstops += 1
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_event():
    if(timer.is_running() == False):
        timer.start()
    

    
def stop_event():
    if(timer.is_running()):
        timer.stop()
        count_success(True)
    
    
def reset_event():
    global ctime, tstops, wstops
    timer.stop()
    ctime = 0
    tstops = 0
    wstops = 0
    
    
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global ctime
    # incrementing counter by 1 for each 0.1 sec.
    ctime += 1 
    
# define draw handler
def draw(canvas):
    canvas.draw_text(format(ctime), (80, 110), 24, 'white')
    scorestr = str(wstops) + '/' + str(tstops)
    canvas.draw_text(scorestr, (160, 20), 18, 'Green')
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 200, 200)
button_start = frame.add_button('Start', start_event, 60)
button_stop = frame.add_button('Stop', stop_event, 60)
button_reset = frame.add_button('Reset', reset_event, 60)
timer = simplegui.create_timer(interval, timer_handler)

# register event handlers
frame.set_draw_handler(draw)


# start frame
frame.start()

# Please remember to review the grading rubric
