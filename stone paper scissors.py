import random
p1_point=0
p2_point=0

def ask():
    choosen=int(input("choose one of them \n 1) stone \n 2) paper \n 3) scissor \n"))
    return choosen

def calcu(p1,p2):
    global p1_point,p2_point
    if p1 == p2:
        print("its draw")
    elif (p1 == 1 and p2==3) or (p1 == 2 and p2==1) or (p1 == 3 and p2==2):
        p1_point=p1_point+1
        print(f"p1 won, his proint is {p1_point}")
    else:
        p2_point=p2_point+1
        print(f"p2 won, his proint is {p2_point}")
        
    return p1_point,p2_point

def str_dic(dict,key):
    if key in dict:
        return dict[key]
dict={
    1:"stone",
    2:"paper",
    3:"scissors"
}


while(True):
    p1=ask()
    p2=random.randrange(1, 4)
    p1_str=str_dic(dict,p1)
    p2_str=str_dic(dict,p2)
    print(f"you have choosen {p1}:-{p1_str}")
    print(f"computer chooses {p2}:-{p2_str}")
    p1_point,p2_point = calcu(p1, p2)
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        print(f" the score is p1 = {p1_point} and p2={p2_point}")
        break