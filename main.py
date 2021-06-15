import time
import random

file1 = open('catflowers.txt', 'r')
content_list1 = file1.readlines()
file2 = open('catmovies.txt', 'r')
content_list2 = file2.readlines()
file3 = open('catsuperheroes.txt', 'r')
content_list3 = file3.readlines()


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global again_play
    global score
    global scoreboard
    global games_won
    global games_lost
    category = input("Choose category: \n F - flowers.txt, \n M - movies.txt, \n S - superheroes.txt, \n X - exit \n")
    secret_word = random.choice(category)
    playGame = True
    continueGame = "Y"
    count = 5
    limit = 5
    if category.upper() == 'F':
        secret_word = random.choice(open("catflowers.txt").readline().split())
        count = 1
    elif category.upper() == 'M':
        secret_word = random.choice(open("catmovies.txt").readline().split())
        count = 1
    elif category.upper() == 'S':
        secret_word = random.choice(open("catsuperheroes.txt").readline().split())
        count = 1
    # game
    length_word = len(secret_word)
    helper = [0] * length_word
    print('_' * length_word)
    popop = input()
    win = False
    while count != 5:
        check_char = input()
        solved = ''
        if check_char in secret_word:
            print("good")
            i = 0
            for x in secret_word:
                if x == check_char:
                    helper[i] = 1
                i = i + 1
        else:
            count = count + 1
            print("wrong")
        i = 0
        for x in secret_word:
            if helper[i] == 1:
                solved += secret_word[i]
            else:
                solved += '_'
            i = i + 1
        print(solved)
        if '_' not in solved:
            win = True
            break
        if count == 1:
            print("Wrong choice. " + str(limit - count) + " guess remaining\n")
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

        elif count == 2:
            print("Wrong choice. " + str(limit - count) + " guess remaining\n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

        elif count == 3:
            print("Wrong choice. \n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif count == 4:
            print("Wrong choice. You have one last chance.\n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |       \n"
                  "__|__\n")
        elif count == 5:
            print("Wrong choice. You are hanged\n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            again_play()
    if win == True:
        print("You won!!!")
        games_won += 1
        again_play()
    else:
        print("You lose :(")
        games_lost += 1
        scoreboard()
        again_play()

def again_play():
    global play_again
    global score
    play_again = input("Do You want to play again? 1 = yes, 2 = no \n")
    while play_again not in ["1", "2"]:
        play_again = input("Do You want to play again? 1 = yes, 2 = no \n")
    if play_again == "1":
        main()
    elif play_again == "2":
        score()
        time.sleep(2)
        exit()

def score():
    print(" ")
    print("  Score")
    print("  -----")
    print("  Won: " + str(games_won) +" Lost: " + str(games_lost))
def scoreboard():
     global games_won
     scoreboard = open('scoreboard.txt', 'a')
     scoreboard.write(name + str(games_won))
     scoreboard.close()

name = input("What is your name?: ")
print("Welcome to hangman " + name + "! Good luck!")
time.sleep(1)
print("You can choose each letter more than once. Good luck!")
time.sleep(2)
print("The game begins now...\n")
time.sleep(2)

main()
