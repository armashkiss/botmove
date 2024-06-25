import pyautogui as pg 
import time
KEY_RUN = "numlock"
KEY_JUMP = "space"
KEY_FORWARD = "w"
KEY_BACKWARD = "s"
KEY_LEFT ="a"
KEY_RIGHT = "d"
KEY_STRAFE_LEFT = "q"
KEY_STRAFE_RIGHT = "e"
KEY_SHEATHE = "Z"
KEY_SIT = "x"

def forward_start():
    pg.keyDown(KEY_FORWARD)
def forward_stop():
    pg.keyUp(KEY_FORWARD)
    
def backward_start():
    pg.keyDown(KEY_BACKWARD)
def backward_stop():
    pg.keyUp(KEY_BACKWARD)
    
def right_start():
    pg.keyDown(KEY_RIGHT)
def right_stop():
    pg.keyUp(KEY_RIGHT)
    
def left_start():
    pg.keyDown(KEY_LEFT)
def left_stop():
    pg.keyUp(KEY_LEFT)
    
def left_strafe_start():
    pg.keyDown(KEY_STRAFE_RIGHT)
def left_strafe_stop():
    pg.keyUp(KEY_STRAFE_LEFT)
def right_strafe_start():
    pg.keyDown(KEY_STRAFE_RIGHT)
def right_strafe_stop():
    pg.keyUp(KEY_STRAFE_RIGHT)
def jump():
    pg.press(KEY_JUMP)
def bump_forward():
    pg.keyDown(KEY_FORWARD)
    time.sleep(0.05)
    pg.keyUp(KEY_FORWARD)
def bump_backward():
    pg.keyDown(KEY_BACKWARD)
    time.sleep(0.05)
    pg.keyUp(KEY_BACKWARD)
    
def bump_right():
    pg.keyDown(KEY_RIGHT)
    time.sleep(0.05)
    pg.keyUp(KEY_RIGHT)
def bump_left():
    pg.keyDown(KEY_LEFT)
    time.sleep(0.05)
    pg.keyUp(KEY_LEFT)
def bump_strafe_right():
    pg.keyDown(KEY_STRAFE_RIGHT)
    time.sleep(0.05)
    pg.keyUp(KEY_STRAFE_RIGHT)
def bump_strafe_left():
    pg.keyDown(KEY_STRAFE_LEFT)
    time.sleep(0.05)
    pg.keyUp(KEY_STRAFE_LEFT)
def sheathe_toggle():
    pg.press(KEY_SHEATHE)
def sit ():
    pg.press(KEY_SIT)

if __name__ == "__name__":
    time.sleep(10)
    while True:
        jump()
        forward_start()
        time.sleep(2)
        left_strafe_start()
        time.sleep(0.05)
        left_strafe_stop()
        time.sleep(2)
        forward_stop()
        
        backward_start()
        time.sleep(1)
        backward_stop()
        
        sheathe_toggle()
        time.sleep(2)
        sit()
        time.sleep(1)
        jump()
        time.sleep(2)
        
        bump_backward()
        bump_forward()
        bump_left()
        bump_right()
        bump_strafe_left()
        bump_strafe_right()
        
        
        
