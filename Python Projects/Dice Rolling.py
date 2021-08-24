import random

# Define infinite loop
while True:

    # Generate a random number between 1 and 6
    dice = random.randint(1, 6)

    # Define the funnction that prints the outcome of the dice throw
    def roll_the_dice(dice):
        switcher = {
            1: "[     ]\n|  0  |\n[     ]",
            2: "[0    ]\n|     |\n[    0]",
            3: "[0    ]\n|  0  |\n[    0]",
            4: "[0   0]\n|     |\n[0   0]",
            5: "[0   0]\n|  0  |\n[0   0]",
            6: "[ 0 0 ]\n| 0 0 |\n[ 0 0 ]"
        } 
        return switcher.get(dice)

    # Call the function
    print(roll_the_dice(dice))
    # Ask the user to roll the dice again
    answer = input("Do you want to roll the dice one more time(Y/N)? : ")
    # Terminate the loop if the user declines
    if answer != 'Y':
        exit(0)
