# Rhythm Game Quiz by Gregory Bateham
# This is a quiz that will determine whether or not you are a dedicated rhythm gamer, or if you are not worthy to this program's very convoluted and biased opinions.
def rhythmgamingness(d,e,f,g):
    h = d * 10
    # multiplies by 10
    i = e / 10
    # divides by 10
    j = f ** 2
    # exponentializes variable f by 2
    k = g // 4
    # divides g by 4 and gives a quotient without a remainder
    m = h % i
    # exerts a modulus
    n = j - k
    # subtracts the variables
    o = m + n
    #adds the variables
    return o

def main():
    print("Interesting, onto the real important questions.")
    print("How often would you say you play rhythm games? Choose one of the following corresponding numbers:")
    print("1- Never 2- Very rarely 3-Rarely 4- Once a week 5- Few times a week 6-Once a day 7-1 hour a day 8- The grind never stops")
    d = int(input())
    print("What is your favorite type of rhythm gaming device to use?")
    print("Select one of the following options:")
    print("1- Console (SDVX controller, Guitar Hero/ Rock Band controller, Taiko Drum, etc.) 2- PC 3- Phone/Tablet")
    e = int(input())
    if e == 1:
        print("What is your favorite type of console to use?")
        p = str(input())
    else:
        print("Classic.")
    print("Do you know any of these artists? If you know more than one, pick the one with the highest number.")
    print("10 - Frums 9 - Sta 8 - M2U 7 - Ice 6.5 - KIVA 6 - Imperial Circus Dead Decadence 5 - t+pazolite 4.5 - Yamajet 4 - Camellia 3 - xi 2.5 - COSIO 2 - NOMA 1.5 - Paul Bazooka 1 - I don't know any of these")
    f = int(input())
    if f > 1:
        print("What is your favorite rhythm game song?")
        q = str(input())
    elif f == 1:
        print("What is your favorite song then?")
        q = str(input())
    print("Is Soulless 4 harder than Soulless 5?")
    print(" 1-Yes 2-No 3-I will never fall for such lame tactics of a simple human-generated code. I refuse to answer this quesiton. 4- What")
    g = int(input())
    print("Calculating Results...")
    print("Your results are...")
    print("Favorite rhythm game is:", c, sep=' ')
    if g == 4 or d == 1:
        print("bruh why did you take this test." * 1)
        # determines the amount of times the string is printed
    while e == 1 and f >= 1:
        print("Favorite rhythm game console: " + p)
        #adds the strings to form a single string
        print("Favorite song: " + q)
        e += 1
        f -= 10
    print("Your percentage of rhythm gaming aura:", rhythmgamingness(d,e,f,g), "%", sep=' ')
    print(end="Thanks for taking my quiz!")   

print("Hello! Welcome to the Rhythm Gaming Quiz (Definitely not biased in any way)! How much of a rhythm gamer are you?")
print("Type anything to continue, or cancel to exit the program: ")
a = input()
if a == "cancel":
    print(end= "Exiting the program...")
if a != "cancel":
    print("There are a total of 7 questions that you will be asked during this quiz, please be sure to answer to your most musical self!~")
    print("What is your favorite game? Please enter one of the corresponding numbers: ")
    print("1- Piano Tiles 2- Cytus 3-Cytus 2 4- Geometry Dash 5-Deemo 6-Dancing Line 7-Arcaea 8-Osu! 9-Smule Piano 10-Other")
b = int(input())
for c in range(0 < b < 11):
    if b == 1:
        print("Piano Tiles is not a rhythm game.")
        c = "Not real"
    elif b == 2:
        print("Dude, there is a second Cytus now. It's been out for about 3 years, idk why you are still living in 2012. Freedom Dive is no excuse either.")
        c = "Outdated"
    elif b == 3:
        print("You are my type of friend and lifelong partner. If you are a neko stan though, I seriouly do not know what to tell you.")
        c = "Cytus 2"
    elif b == 4:
        print("Please never talk to me, contact me, or look at me ever again.")
        c = "Geometry Dash"
    elif b == 5:
        print("Classic, piano is truly one of my favorites. Please contact me.")
        c = "Deemo"
    elif b == 6:
        print("You are being watched. Do not get up, do not look around.")
        c = "[REDACTED]"
    elif b == 7:
        print("Marry me!! Just kidding. But you have incredible taste and don't need to finish this test unless you just want to be teased.")
        c = "Arcaea"
    elif b == 8:
        print("You are either super chill or a complete weirdo. Regardless... let's be friends. My tag is gdubs, add me.")
        c = "Osu!"
    elif b == 9:
        print("I seriously do not understand how people like you exist.")
        c = "Horrible awful mediocre piano game"
    else:
        print("Oh! What game did you have in mind then?")
        c = input()
    print("Is osu!lazer better than osu!", "?")
    print("Answer yes or no.")
    r = str(input())
    print("yes" not in r)
    main()

