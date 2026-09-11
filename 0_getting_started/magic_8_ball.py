import random


ans1 = ('maybe')
ans2 = ('it is unlikely')
ans3 = ('it is decidedly so')
ans4 = ('definitely')
ans5 = ('it is undecided')
ans6 = ('as I see it, yes')
ans7 = ('not at all')
ans8 = ('reply hazy, try again')

answers = [ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8]  # List of possible answers and refers to the variables above (I did this to comprehed the code)


# loops the program until the user types "quit" to end the program  v
while True:
    usrA = input("Ask the magic 8 ball a question: ")
    print(random.choice(answers))

    
    #breaks the loop if the user types "quit" or leaves the answer blank
    if input('type "quit" to end the program or leave your answer blank to ask another question: ') == 'quit':
        break