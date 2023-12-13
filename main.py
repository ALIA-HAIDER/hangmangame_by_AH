#hangman game by<ah>
import random
hangman=(
'''-------
   |
   |
   |
   |
   |
   |______
   ''',
   '''
   --------
   |     |
   |     0 
   |     
   |  
   |________
   ''',
   '''
   --------
   |     |
   |     0 
   |   /-+-/  
   |  
   |________
   ''',
   '''
   --------
   |     |
   |     0 
   |   /-+-/  
   |     |
   |
   |______
   ''',
   '''
   --------
   |     |
   |     0 
   |   /-+-/  
   |     |
   |     |
   |
   |_______
   ''',
   '''
   --------
   |     |
   |     0 
   |   /-+-/  
   |     |
   |     |
   |   |
   |   |
   |_______
   ''',
   '''
   --------
   |     |
   |     0 
   |   /-+-/  
   |     |
   |     |
   |   |   |
   |   |   |
   |_______
   '''
   )
wrong=0
print("Wlcome to hangman game <a/h>")
print("In this we will give you incomplete words you have to complete them by guessing the missing alphabets ")
print("so! let's start")
print("ANI_A_")
b=input("write your guessed word:")
# q1
if b=="ANIMAL":
    print("bravo you guessed right")
else:
    wrong=wrong+1
    print("opps! you guessed wrong")
    print(hangman[wrong]) 
print("now,it's time of next word" )
# q2
print("W_NT_R")
c=input("write your guessed word:")
if c=="WINTER":
    print("bravo you guessed right")
else:
    wrong=wrong+1
    print("opps! you guessed wrong")
    print(hangman[wrong]) 
print("now,it's time of next word" )
# q3
print("P_TH_N")
d=input("write your guessed word:")
if d=="PYTHON":
    print("bravo you guessed right")
else:
    wrong=wrong+1
    print("opps! you guessed wrong")
    print(hangman[wrong]) 
print("now,it's time of next word" )
# q4
print("LE__E")
e=input("write your guessed word:")
if e=="LEAVE":
    print("bravo you guessed right")
else:
    wrong=wrong+1
    print("opps! you guessed wrong")
    print(hangman[wrong]) 
print("now,it's time of next word" )
# q5
print("ME__I_G")
f=input("write your guessed word:")
if f=="MEETING":
    print("bravo you guessed right")
else:
    wrong=wrong+1
    print("opps! you guessed wrong")
    print(hangman[wrong]) 
print("now,it's time of next word" )
# q6
print("N_T_R__")
g=input("write your guessed word:")
if g=="NATURAL":
    print("bravo you guessed right")
else:
    wrong=wrong+1
    print("opps! ygvyou guessed wrong")
    print(hangman[wrong]) 
if wrong!=6:
    print("now, it's time of new word")
    # q7
    print("P_O_IN_")
    H=input("Write your gussed word")
    if H=="PROTIEN":
        print("Bravo you guessed it")
    else:
        wrong=wrong+1
        print("opps! you guessed wrong")
        print(hangman[wrong])
if wrong!=6:
    print("now, it's time of new word")
    # q8
    print("E_O_GH")
    
    K=input("Write your gussed word")
    if K=="PROTIEN":
        print("Bravo you guessed it")
    else:
        wrong=wrong+1
        print("opps! you guessed wrong")
        print(hangman[wrong])
if wrong==6:
    print( "alas!, your man died ")
    print("the end , may god bless his soule")
    







    

    

          
    

         