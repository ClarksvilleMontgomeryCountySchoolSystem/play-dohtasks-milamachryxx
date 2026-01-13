def main():
    color1 = "gray"
    color2 = "pink"
    print(f"1) Roll a ball using {color1}")
    choice1 = input("long body or round body? ")
    # CAUTION: You must include the word "body" when checking!
    if choice1 == "long body":
        print("2) Roll the ball into an egg shape.\n")
    else:
        print("2) Keep it as a ball.\n")
    print(f'3) Roll a smaller ball using {color1} for the head.\n')
    print('4) Attach the head to one end of the body.\n')

    choice2 = input('long tail or short tail? ')
    if choice2 == "long tail":
        print(f'5) Roll a thin rope using {color2} and attach to the back.\n')
    else:
        print(f"5) Add a small bump using {color2} to the back.")
    print(f'6) Add four small legs to the bottom using {color1}.\n')
    print('7) Add two dots for eyes and a tiny nose.\n')
    print('8) Name this creation: "Mouse"\n')


if __name__ == "__main__":
    main()
