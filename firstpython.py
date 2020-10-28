#first test of adding code
import time

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

door = 0
button = 0
window = 0

required = ("\nUse only A, B, or C\n")

def intro():
    print('You are in a room with a door, sitting on a chair. Do you want to leave or stay?')
    time.sleep(1)
    print("a. leave, b. stay")
    choice = input('Whats your move: ')
    if choice in answer_A:
        option_door()
    elif choice in answer_B:
        option_chair()    
    else:
        print(required)
        intro()    

def option_door():
    print('You have entered a room with a panel with a button on it, and a window. Will you: ')
    time.sleep(1)
    print("a. press the button, b. open the window?")
    choice = input("Whats your move: ") 
    if choice in answer_A:
        print("You have pressed the button and activated the self destruct. Good bye!")
    elif choice in answer_B:
        print("With the window open, you decide to end it all. Good bye!")
    else:
        print(required)
        option_door()        

def option_chair():
    print('Staying sat down, you realise that your life is pointless and youll end it now.')
    time.sleep(1)
    print('Do you a. hold your breath, b. beat yourself to death?')
    choice = input('Whats you move: ')
    if choice in answer_A:
        print('You hold your breath and pass out. After waking, you realise that you are very stupid and resgin yourself to an eternity in this room.')
    elif choice in answer_B:
        print('A painful choice. You pound your skull against the chair, eventually breaking it. Laying on the floor, bleeding, you realise that its a good thing that you have done.')
    else:
        print(required) 
        option_chair()                      

intro()        
