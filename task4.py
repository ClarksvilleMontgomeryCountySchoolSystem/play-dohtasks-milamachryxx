def main():
    color1 = "periwinkle purple"
    color2 = "baby pink"
    print(f"1) Roll a ball using {color1} for the body.")
    choice1 = input("hot dog or round like a ball? ")
    if choice1 == "hot dog":
        print("2) Stretch it out.\n")
    else:
        print("2) Keep it round.\n")
    print(f"3) Roll a smaller ball using {color1} for the head.\n")
    print("4) Attach the head to the body.\n")
    choice2 = input("standing up or flopped down? ")
    if choice2 == "standing up":
        print(f"5) Attach two pointed pieces using {color2} upright.\n")
    else:
        print(f"5) Attach two pieces using {color2} hanging downward.\n")
    print(f"6) Add four legs using {color1}, a small tail using {color2}, two eyes, and a nose.\n")
    print('7) Name this creation: "Dog"')


if __name__ == "__main__":
    main()
