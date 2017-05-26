import random
import pyautogui
import sys
import time
import win32api, win32com

SpamText = ['Nerd', 'I Hate You', 'The Revenge is Sweet', 'Die in a Fire', 'Is this annoying yet?', 'Hi', 'TicTacs', 'I Like Turtles', 'Jesus is pretty Good', 'Supercalifragilisticexpialidocious', 'NERF THIS', 'HEROES NEVER DIE', 'RYUU GA WAGA TEKI WO KURAU', 'Deleted', 'Scrub', 'ITS HIGH NOON', 'OH LETS BREAK IT DOWN','FREEZE! DONT MOVE.', 'JUSTICE RAINS FROM ABOVE', 'LOL', 'You seem nice. Its a shame that I have to kill you.', 'NRF DIS', 'Mada Mada'
                  , 'DIE, DIE, DIE', "HAMMER DOWN!", "I'VE GOT YOU IN MY SIGHTS", "FIRE IN THE HOLE", 'CEASE YOUR RESISTANCE', 'APAGANDO LAS LUCES', 'EAT THIS', 'TELEPORTER ONLINE. I HAVE OPENED THE PATH.', 'TIMES UP', 'MOLTEN CORE', 'NO ONE CAN HIDE FROM MY SIGHTS', 'FIRE AT WILL', 'PASS INTO THE IRIS', 'CATCH PHRASE!', 'Cheers Love, the Cavalrys here!', 'Love, D.Va.', 'Its in the refrigerator.', 'Youre welcome', 'Hey Daddy-O', 'Boop', 'NERF THIS', 'NERF THIS', 'D.Va Online', 'Meka Activated!'
                  , 'Hey', 'I need healing.'] #spam phrases, these can be changed based on the user
mposx = 0
mposy = 0
#print(mposx)
#print(mposy)

def spam(): #random spam function
    endcount = eval(input('Enter the amount of messages you would like to spam: '))#user inputs amount of times for spamming
    print("Click when you are ready to begin.")
    state_left = win32api.GetKeyState(0x01) #Determine State Left Mouse is in
    mousePressed = False #Declare Variable for if Mouse is Pressed
    while mousePressed == False:
        a = win32api.GetKeyState(0x01) #Variable for Determining if there is a difference between previous and current state
        if a != state_left: #Compare Previous and Current States
            mousePressed = True
            mposx, mposy = pyautogui.position() #grab mouse position
        time.sleep(.01) #Limit amount of times while loop runs
    count = 1
    while count <= endcount:
        state_esc = win32api.GetKeyState(0x1B) #Determines if Esc Is Pressed
        if state_esc > 0: #Breaks if Esc Is Pressed
            break
        pyautogui.click(mposx, mposy)#get position of chatbox
        pyautogui.typewrite(random.choice(SpamText), interval=0.01)#type random string, set interval time for typing each character
        pyautogui.hotkey('enter')#pressing of enter button
        count += 1  

def singleSpam(userPhrase):#single phrase spam function
    endcount = eval(input('Enter the amount of messages you would like to spam: '))#user inputs amount of times for spamming
    print("Click when you are ready to begin.")
    state_left = win32api.GetKeyState(0x01) #Determine State Left Mouse is in
    mousePressed = False #Declare Variable for if Mouse is Pressed
    while mousePressed == False:
        a = win32api.GetKeyState(0x01) #Variable for Determining if there is a difference between previous and current state
        if a != state_left: #Compare Previous and Current States
            mousePressed = True
            mposx, mposy = pyautogui.position() #grab mouse position
        time.sleep(.01) #Limit amount of times while loop runs
    count = 1
    while count <= endcount:
        state_esc = win32api.GetKeyState(0x1B) #Determines if Esc Is Pressed
        if state_esc > 0: #Breaks if Esc Is Pressed
            break
        pyautogui.click(mposx, mposy)#get position of chatbox
        pyautogui.typewrite(userPhrase, interval=0.01)#type user selected string, set interval time for typing each character
        pyautogui.hotkey('enter')#pressing of enter button
        count += 1
        
def gather(): #main function
    sPhrase = eval(input('Enter 1 for a Single Phrase, or 2 for a random set of phrases: '))#determines if user wants to spam a single phrase or a prebuilt set of random phrases
    if sPhrase == 1:
        userPhrase = input('Please Enter the Phrase you would like to spam: ')#changes SpamText to user designated phrase
        singleSpam(userPhrase)
        print('User Phrase Spamming')#console output to verify which sPhrase choice is running
    elif sPhrase == 2: #runs preselected spam phrases
        spam()
        print('Pre-Selected Phrases Spamming')#console output to verify which sPhrase choice is running
    else:
        print('Slection invalid. Please try again.')
        gather()

#spam()
gather()
