"""Rhythm Game Quiz by Gregory Bateham"""
__author__ = "Gregory Bateham"
# This is a quiz that will determine whether or not you
# are a dedicated rhythm gamer, or if you
# are not worthy to this program's very convoluted and biased opinions.
import sys


def rhythm_potential(grind_time, device, artist, soul):
    """Calculator for Rhythm Gaming Potential"""
    product = grind_time * 10
    # multiplies by 10
    quotient = device / 10
    # divides by 10
    exponent = artist ** 2
    # exponentially increase variable artist by 2
    no_remainder = soul // 4
    # divides soul by 4 and gives a quotient without a remainder
    modulus = float(product) % quotient
    # exerts a modulus
    difference = exponent - no_remainder
    # subtracts the variables
    total_sum = int(modulus) + difference
    # adds the variables
    return str(total_sum)


def main():
    """Main Function/Variables Used to Compute Percentage"""
    print("Interesting, onto the real important questions.")

    # Question 3

    print("How often would you say you play rhythm games? ")
    print("Choose one of the following corresponding numbers:")
    print("1- Never 2- Very rarely 3- Rarely 4- Once a week ")
    print("5- Few times a week 6- Once a day 7- 1 hour a day ")
    print("8- The grind never stops")
    grind = input()
    if grind.isdigit():
        if 1 <= int(grind) <= 8:
            print("Storing data...")
        else:
            print("1 through 8! Trolling will not be tolerated.")
            sys.exit()
    else:
        print("I asked for a number!! Goodbye Troll!")
        sys.exit()
    print("What is your favorite type of rhythm gaming device to use?")
    print("Select one of the following options:")
    print("1- Console (SDVX controller, Guitar Hero/ Rock Band controller,")
    print(" Taiko Drum, etc.) 2-PC 3- Phone/Tablet")
    rhythm_device = input()
    if rhythm_device.isdigit():
        if 1 <= int(rhythm_device) <= 3:
            integer_rhythm = int(rhythm_device)
            if rhythm_device == 1:
                print("What is your favorite type of console to use?")
                favorite_device = str(input())
            else:
                print("Classic.")
                favorite_device = "PC/Phone/Tablet"
        else:
            print("1 through 3! Trolling will not be tolerated.")
            sys.exit()
    else:
        print("I asked for a number!! Goodbye Troll!")
        sys.exit()

    # Question 4

    print("Do you know any of these artists? ")
    print("If you know more than one, pick the one with the highest number.")
    print("10 - Frums 9 - Sta 8 - M2U 7 - Ice 6.5 - KIVA ")
    print("6 - Imperial Circus Dead Decadence 5 -t+pazolite 4.5 - Yamajet")
    print(" 4 - Camellia 3 - xi 2.5 - COSIO 2 - NOMA 1.5 - Paul Bazooka ")
    print("1 - I don't know any of these")
    music_artist = input()
    favorite_song = 0
    if music_artist.isdigit():
        if 1 <= float(music_artist) <= 10:
            float_music = float(music_artist)
            if float_music > 1:
                print("What is your favorite rhythm game song?")
                favorite_song = str(input())
            elif float_music == 1:
                print("What is your favorite song then?")
                favorite_song = str(input())
        else:
            print("1 through 10!! How hard is that to comprehend... Goodbye troll!")
            sys.exit()
    else:
        print("I asked for a number.... Please spare me. Goodbye!")
        sys.exit()

    # Question 5

    print("Is Soulless 4 harder than Soulless 5?")
    print(" 1-Yes 2-No 3-I will never fall for such lame tactics ")
    print("of a simple human-generated code. I refuse to answer ")
    print("this question. 4- What")
    soul_test = input()
    if soul_test.isdigit():
        if 1 <= int(soul_test) <= 4:
            integer_soul = int(soul_test)
            print("Calculating Results...")
        else:
            print("1 through 4. Goodbye troll!")
            sys.exit()
    else:
        print("Asked for a number... Goodbye Troll!")
        sys.exit()

    # Results

    print("Your results are...")
    print("Favorite rhythm game is", your_choice, sep=': ')
    if soul_test == 4 or grind == 1:
        print("bruh why did you take this test." * 1)
    while integer_rhythm == 1 and float_music >= 1:
        print("Favorite rhythm game console: " + favorite_device)
        # adds the strings to form a single string
        print("Favorite song: " + favorite_song)
        integer_rhythm += 1
        float_music -= 10
        integer_soul = int(soul_test)
    print("Your percentage of rhythm gaming aura:")
    print(rhythm_potential(grind, integer_rhythm, float_music, integer_soul), " %")
    print("Bonus: Type a number to get a pog spam!")
    pog_spam = input()
    print("Generating ", pog_spam, " Pogs...")
    for pog_spam in range(1, 100):
        pog_spam -= 1
        print("pog")
    print(end="Thanks for taking my quiz!")


start_message = "Hello! Welcome to the Rhythm Gaming Quiz!"
start_message2 = "(Definitely not biased in any way)! How much of "
start_message3 = "a rhythm gamer are you?"
print(start_message + start_message2 + start_message3)
print("Type anything to continue, or cancel to exit the program: ")
human_test = input()
if human_test == "cancel":
    print(end="Exiting the program...")
    sys.exit('Goodbye!')
if human_test == "hi!":
    print("Hello! :))")
if human_test == "anything":
    print("Funny. Very funny.")
intro = "There are a total of 7 questions that you will be "
intro2 = "asked during this quiz, please be sure to answer to "
intro3 = "your most musical self!~"

# Question 1

q1 = "What is your favorite rhythm game?"
q1a = "Please enter one of the corresponding numbers: "
q1b = "1- Piano Tiles 2- Cytus 3-Cytus 2 4- Geometry Dash "
q1c = "5-Deemo 6-Dancing Line 7-Arcaea 8-Osu! 9-Smule Piano 10-Other"
print(intro + intro2 + intro3)
print(q1)
print(q1a)
print(q1b + q1c)
fav_game = input()
if fav_game.isdigit():
    if int(fav_game) == 1:
        print("Piano Tiles is not a rhythm game.")
        your_choice = "not real"
    elif int(fav_game) == 2:
        cytus_answer = "Dude, there is a second Cytus now."
        cytus_answer2 = "It's been out for about 3 years, idk why you"
        cytus_answer3 = "are still living in 2012. Freedom Dive is no excuse either."
        print(cytus_answer)
        print(cytus_answer2 + cytus_answer3)
        your_choice = "outdated"
    elif int(fav_game) == 3:
        cytus2_answer = "You are my type of friend and lifelong partner."
        cytus2_answer2 = "If you are a neko stan though, I "
        cytus2_answer3 = "seriously do not know what to tell you."
        print(cytus2_answer)
        print(cytus2_answer2 + cytus2_answer3)
        your_choice = "Cytus 2"
    elif int(fav_game) == 4:
        print("Please never talk to me, contact me, or look at me ever again.")
        your_choice = "Geometry Dash"
    elif int(fav_game) == 5:
        print("Classic, piano is truly one of my favorites. Please contact me.")
        your_choice = "Deemo"
    elif int(fav_game) == 6:
        print("You are being watched. Do not get up, do not look around.")
        your_choice = "[REDACTED]"
    elif int(fav_game) == 7:
        arcaea_answer = "Marry me!! Just kidding."
        arcaea_answer2 = "But you have incredible taste and don't need to finish"
        arcaea_answer3 = "this test unless you just want to be teased."
        print(arcaea_answer)
        print(arcaea_answer2 + arcaea_answer3)
        your_choice = "Arcaea"
    elif int(fav_game) == 8:
        print("You are either super chill or a complete weirdo. Regardless...")
        print("Let's be friends. My tag is gdubs, add me.")
        your_choice = "Osu!"
    elif int(fav_game) == 9:
        print("I seriously do not understand how people like you exist.")
        your_choice = "horrible awful mediocre piano game"
    elif int(fav_game) == 10:
        print("Oh! What game did you have in mind then?")
        your_choice = input()
        print("Noted.")
    else:
        print(end="That is not a number I asked for. Goodbye troll!")
        sys.exit()
else:
    print("I asked for a number between 1 and 10. Goodbye troll!")
    sys.exit()

# Question 2

print("Is osu!lazer better than osu!", "?")
print("Answer yes or no.")
osu_test = str(input())
if osu_test == "yes":
    print("yes" not in osu_test)
elif osu_test == "no":
    print("yes" not in osu_test)
else:
    print("I asked for yes or no! Goodbye troll!")
    sys.exit()
main()
# Call to Main
