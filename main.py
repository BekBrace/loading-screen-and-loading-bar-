# 1) Loading Bar
# 2) Loading Screen
import os
import time


def loading_bar(seconds):
    for loading in range(0, seconds+1):
        percent = (loading * 100) // seconds
        print("\n")
        print("Loading...")
        print("<" + ("-" * loading) + ("" * (seconds + loading)) +
              ">" + str(percent) + "%")
        print("\n")
        time.sleep(1)
        os.system('cls' if os.name == "nt" else "clear")


def loading_screen(seconds):
    print("Loading Screen...")
    with open('imperial.txt', 'r') as screen:
        for lines in screen:
            print(lines, end='')
            time.sleep(seconds)


loading_bar(10)
os.system('cls' if os.name == "nt" else "clear")
loading_screen(.5)
