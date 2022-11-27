
import random

       # r > s, s > p, p > r

def define_winner(player, opponent):
    
    if (player == 'r' and opponent == 's') \
    or (player == 's' and opponent == 'p') \
    or (player == 'p' and opponent == 'r'):
        return True
   
def play():
    user = input(f"What's your choice? : 'r' for rock, 'p' for paper or 's' for scissors\n")
    computer= random.choice(['r', 'p', 's'])
                
    if user == computer:
        return" It's a tie"
    if define_winner (user, computer):
        return'You won!'
    
    return'You lost!'
    
       
print(play())
