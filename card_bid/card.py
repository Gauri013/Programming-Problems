import random
diamond = ['2','3','4','5','6','7','8','9','10','jack','queen','king','ace']
spade = ['2','3','4','5','6','7','8','9','10','jack','queen','king','ace']
heart = ['2','3','4','5','6','7','8','9','10','jack','queen','king','ace']
value = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'jack':11 , 'queen':12, 'king':13 , 'ace':14}
score_player1 = 0.0
score_computer = 0.0

def banker(value_one , display_diamond , score):
    value_two = random.choice(heart)
    print("computer :" , value_two,"of heart")
    spade.remove(value_one)
    heart.remove(value_two)
    lst = calculate_score(value_one , value_two , display_diamond ,score[0] , score[1]) 
    return (lst)

def calculate_score(value_one , value_two , diamond_val,score_player1 , score_computer):
    score_one = value.get(value_one)
    score_two = value.get(value_two)
    if(score_one > score_two):
        score_player1 += value.get(diamond_val)
    elif (score_one == score_two):
        score_player1 += (value.get(diamond_val))/2
        score_computer += (value.get(diamond_val))/2
    else:
        score_computer += value.get(diamond_val)
    score =[score_player1 , score_computer]
    return (score)

def winner(player_score , comp_score):
    if (player_score > comp_score):
        return ("winner is player one")
    elif (player_score == comp_score):
        return ("tie")
    else:
        return ("winner is comp")
 
score = [0.0 , 0.0]
while (len(diamond) != 0):
    display_diamond = random.choice(diamond)
    diamond.remove(display_diamond)
    print("diamond",display_diamond)
    print ("enter your card of spade")
    player_one = input()
    score = banker(player_one , display_diamond ,score)
    print("Player one score =",score[0])
    print("Score of comp =", score[1])
print(winner(score[0] , score[1]))
