# playful app that takes in the name of the users and counts how many times the letters of the words True Love occur in the users name to determine what the final score is

# for love scores less than 10 or greater than 90, the message will be: You go together like coke and mentos
# for love scores between 40 and 50, the message should be: you are alright together
# for all other scores, the message will just be the score

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

count_true_name1 = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
count_true_name2 = name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")
count_true = str(count_true_name1 + count_true_name2)

count_love_name1 = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")
count_love_name2 = name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")
count_love = str(count_love_name1 + count_love_name2)

count_final = int(count_true + count_love)

if count_final < 10 or count_final > 90:
    print(f"Your score is {count_final}, you go together like coke and mentos")
elif count_final > 40 and count_final < 50:
    print(f"Your score is {count_final}, you are alright together")
else:
    print(f"Your score is {count_final}")
