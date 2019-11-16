import random #Imports the random function

def game(y): #setup the game function
    win = False #yit makes "win" and sets it to false 
    while(win==False): #while loop 
        print("Guess a number (1-10)") #says guess a number from 1-10
        z = input() #takes the input from the user
        if int(z) == y: #if z is the number...
            print("you won") #say you have won
            win = True #this means u have won
        else: #otherwise say...
            print("u succ lol") #you suck lol

game(random.randint(1,11)) #chooses a random number fromo 1 - 10



 
