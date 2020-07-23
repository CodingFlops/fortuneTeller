import random
def fortune_teller():
    Ass = "Yes"
    while(Ass == "Yes"):
        Q = input("Enter your future ")
        number = random.randint(1, 2)
        if number == 1:
            print(Q, "?")
        elif number == 2:
            print(Q, "!")
        Ass = input("Do you want continue?  Yes or No? ") 
fortune_teller()