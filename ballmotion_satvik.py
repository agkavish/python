
import simplegui

# Initialize globals
WIDTH = 200
HEIGHT = 200
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-40.0 / 60.0,  5.0 / 60.0]
stop_ball_flag = False

# define event handlers
def draw(canvas):
    if (stop_ball_flag == False):
        # Update ball position
        ball_pos[0] += vel[0]
        ball_pos[1] += vel[1]
    
        # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS:
        vel[0] = - vel[0]
    if ball_pos[0] >= WIDTH - 1 - BALL_RADIUS :
           vel[0] = - vel[0]
    if ball_pos[1] <= BALL_RADIUS :
            vel[1] = - vel[1]
    if ball_pos[1] >= HEIGHT - 1 - BALL_RADIUS :
            vel[1] = - vel[1]    
    
    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

def button_stop_handler():
    frame.stop()
    
def button_stop_ball():
    global stop_ball_flag
    if(stop_ball_flag):
        stop_ball_flag = False
    else:
        stop_ball_flag = True
        
def button_move_forward():
    ball_pos[0] += 10

    
# create frame
frame = simplegui.create_frame("Ball physics", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
button1 = frame.add_button('Stop Frame', button_stop_handler)
button2 = frame.add_button('Ball Toggele' , button_stop_ball)
button3 = frame.add_button('move forward',button_move_forward)
# start frame
frame.start()


# stop frame
#frame.stop()


