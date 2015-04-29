# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
paddle1_pos = [[0, 0 ], [0 + PAD_WIDTH,0], [0 + PAD_WIDTH,PAD_HEIGHT ], [0, PAD_HEIGHT] ]
paddle2_pos = [[WIDTH - PAD_WIDTH, 0 ], [WIDTH,0],  [WIDTH-1, PAD_HEIGHT],[WIDTH - PAD_WIDTH,PAD_HEIGHT ] ]
#paddle1_pos = [[1, 1], [1, PAD_HEIGHT]]
#paddle2_pos = [[WIDTH - 1, 0 ], [WIDTH - 1,PAD_HEIGHT ] ]
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos[0] = WIDTH/2
    ball_pos[1] = HEIGHT/2


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
    if ball_pos[0] >= WIDTH - 1 - PAD_WIDTH - BALL_RADIUS :
        ball_vel[0] = - ball_vel[0]
    if ball_pos[1] <= BALL_RADIUS :
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= HEIGHT - 1 - BALL_RADIUS :
        ball_vel[1] = - ball_vel[1]
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]       
    
    
        
    # draw ball
    canvas.draw_circle([ball_pos[0], ball_pos[1]], BALL_RADIUS, 4, "Green","Blue")
    
    # update paddle's vertical position, keep paddle on the screen
  
    pd1_t0 = paddle1_pos[0]
    pd1_t1 = paddle1_pos[1]
    pd1_t2 = paddle1_pos[2]
    pd1_t3 = paddle1_pos[3]

    if pd1_t0[1] > 0  and pd1_t0 [1] < HEIGHT -1:   
        #or (pd1_t0[1] <= (HEIGHT - PAD_HEIGHT)
        pd1_t0[1] = paddle1_vel[1]
    
        paddle1_pos[0] = pd1_t0
    
        pd1_t1[1] = paddle1_vel[1]
    
        paddle1_pos[1] = pd1_t1
    
        pd1_t2[1] = PAD_HEIGHT + paddle1_vel[1]
    
        paddle1_pos[2] = pd1_t2
    
        pd1_t3[1] = PAD_HEIGHT + paddle1_vel[1]
    
        paddle1_pos[3] = pd1_t3
    
    #print 'paddle1_vel ', paddle1_vel
    #print 'paddle1_pos ', paddle1_pos
    
    
    # draw paddles

    canvas.draw_polygon(paddle1_pos, 1, 'Yellow', 'Orange')
    canvas.draw_polygon(paddle2_pos, 1, 'Yellow', 'Orange')
    
    #canvas.draw_line(paddle1_pos[0],paddle1_pos[1], PAD_WIDTH, "Orange")
    #canvas.draw_line(paddle2_pos[0],paddle2_pos[1], PAD_WIDTH, "Orange")

    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    acc = 1

    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["down"]:
        paddle1_vel[1] += 10
    elif key==simplegui.KEY_MAP["up"]:
        paddle1_vel[1] -= 10
    elif key==simplegui.KEY_MAP["w"]:
        paddle2_vel[1] += 10
    elif key==simplegui.KEY_MAP["s"]:
        paddle2_vel[1] -= 10    
    elif key==simplegui.KEY_MAP["left"]:
        ball_vel[0] -= acc
        ball_vel[1] -= acc
    elif key==simplegui.KEY_MAP["right"]:
        ball_vel[0] += acc 
        ball_vel[1] += acc

 
def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
