import random
import pyautogui
import sys
import time
import win32api, win32com

SpamText = ['Nerd', 'I Hate You', 'The Revenge is Sweet', 'Die in a Fire', 'Is this annoying yet?', 'Hi', 'TicTacs', 'I Like Turtles', 'Jesus is pretty Good', 'Supercalifragilisticexpialidocious', 'NERF THIS', 'HEROES NEVER DIE', 'RYUU GA WAGA TEKI WO KURAU', 'Deleted', 'Scrub', 'ITS HIGH NOON', 'OH LETS BREAK IT DOWN','FREEZE! DONT MOVE.', 'JUSTICE RAINS FROM ABOVE', 'LOL', 'You seem nice. Its a shame that I have to kill you.', 'NRF DIS', 'Mada Mada'
                  , 'DIE, DIE, DIE', "HAMMER DOWN!", "I'VE GOT YOU IN MY SIGHTS", "FIRE IN THE HOLE", 'CEASE YOUR RESISTANCE', 'APAGANDO LAS LUCES', 'EAT THIS', 'TELEPORTER ONLINE. I HAVE OPENED THE PATH.', 'TIMES UP', 'MOLTEN CORE', 'NO ONE CAN HIDE FROM MY SIGHTS', 'FIRE AT WILL', 'PASS INTO THE IRIS', 'CATCH PHRASE!', 'Cheers Love, the Cavalrys here!', 'Love, D.Va.', 'Its in the refrigerator.', 'Youre welcome', 'Hey Daddy-O', 'Boop', 'NERF THIS', 'NERF THIS', 'D.Va Online', 'Meka Activated!'
                  , 'Hey', 'I need healing.']

mposx, mposy = pyautogui.position()
#print(mpos)
#print(mposx)
#print(mposy)

def spam():
    endcount = eval(input('Enter the amount of messages you would like to spam: '))
    print("Click when you are ready to begin.")
    state_left = win32api.GetKeyState(0x01) #Determine State Left Mouse is in
    mousePressed = False #Declare Variable for if Mouse is Pressed
    while mousePressed == False:
        a = win32api.GetKeyState(0x01) #Variable for Determining if there is a difference between previous and current state
        if a != state_left: #Compare Previous and Current States
            mousePressed=True 
        time.sleep(.01) #Limit amount of times while loop runs
    count = 1
    while count <= endcount:
        state_esc = win32api.GetKeyState(0x1B) #Determines if Esc Is Pressed
        if state_esc > 0: #Breaks if Esc Is Pressed
            break
        pyautogui.click(mposx, mposy)#position of chatbox
        pyautogui.typewrite(random.choice(SpamText), interval=0.01)
        pyautogui.hotkey('enter')#position of enter button
        count += 1  

spam()
