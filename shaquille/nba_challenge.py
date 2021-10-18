# print("Challenge 2.1:")
jamal_murray_3pts_made = 46
# TODO: Create variable here for number of 3 pt shots made by Fred VanVleet
# TODO: Create variable here for number of 3 pt shots made by James Harden
Fred_VanVleet_3pts_made=43
James_Harden_3pts_made=37
# print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
# TODO: Create print statement here for Fred VanVleet
# TODO: Create print statement here for James Harden
print(f"In the 2020 NBA playoffs, Fred Vanvleet made {Fred_VanVleet_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden made {James_Harden_3pts_made} 3 point shots")
# print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
# TODO: Create variable here for number of 3 pt shot attempts by Jamal Murray
# TODO: Create variable here for number of 3 pt shot attempts by Fred VanVleet
# TODO: Create variable here for number of 3 pt shot attempts by James Harden
jamal_murray_3pts_attempts= 93
Fred_VanVleet_3pts_attempts=110
James_Harden_3pts_attempts= 109

# print("Challenge 2.4: Build on your print statement")
# TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
# the number of three point shots for each player. E.g., output should be similar to
# "In the 2020 NBA playoffs, player X made Y 3 point shots and Z 3 point shot attempts."
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots and {jamal_murray_3pts_attempts} shot attempts")
print(f"In the 2020 NBA playoffs, Fred Vanvleet made {Fred_VanVleet_3pts_made} 3 point shots and {Fred_VanVleet_3pts_attempts} shot attempts")
print(f"In the 2020 NBA playoffs, James Harden made {James_Harden_3pts_made} 3 point shots and {James_Harden_3pts_attempts} shot attempts")

# print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
# TODO: Calculate and print the 3 point percentage for Jamal Murray
Jamal_Murray_3pts_percentage= (jamal_murray_3pts_made/jamal_murray_3pts_attempts)
print (f"In the 2020 NBA playoffs, Jamal Murrays 3 pts percentage was {Jamal_Murray_3pts_percentage}.")
# TODO: Calculate and print the 3 point percentage for Fred VanVleet
Fred_VanVleet_3pts_percentage= (Fred_VanVleet_3pts_made/Fred_VanVleet_3pts_attempts)
print (f"In the 2020 NBA playoffs, Fred VanVleets 3 pts percentage was {Fred_VanVleet_3pts_percentage}.")
# TODO: Calculate and print the 3 point percentage for James Harden
James_Harden_3pts_percentage= (James_Harden_3pts_made/James_Harden_3pts_attempts)
print(f"In the 2020 NBA playoffs, James Hardens 3 pts percentage was {James_Harden_3pts_percentage}.")

# print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
# TODO: Print the giant chunk of text out using escape characters so each sentence comes out on a new line
print("In the 2020 NBA playoffs, Jamal Murray made 46 3 point shots\nIn the 2020 NBA playoffs, Fred Vanvleet made 43 3 point shots\nIn the 2020 NBA playoffs, James Harden made 37 3 point shots\nIn the 2020 NBA playoffs, Jamal Murray made 46 3 point shots and 93 shot attempts\nIn the 2020 NBA playoffs, Fred Vanvleet made 43 3 point shots and 110 shot attempts\nIn the 2020 NBA playoffs, James Harden made 37 3 point shots and 109 shot attempts\nIn the 2020 NBA playoffs, Jamal Murrays 3 pts percentage was 0.4946236559139785.\nIn the 2020 NBA playoffs, Fred VanVleets 3 pts percentage was 0.39090909090909093.\nIn the 2020 NBA playoffs, James Hardens 3 pts percentage was 0.3394495412844037.")
# print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
# TODO: As above, orint out the paragraph with only 1 sentence per line, and all in upper case
print(('In the 2020 NBA playoffs, Jamal Murray made 46 3 point shots\nIn the 2020 NBA playoffs, Fred Vanvleet made 43 3 point shots\nIn the 2020 NBA playoffs, James Harden made 37 3 point shots\nIn the 2020 NBA playoffs, Jamal Murray made 46 3 point shots and 93 shot attempts\nIn the 2020 NBA playoffs, Fred Vanvleet made 43 3 point shots and 110 shot attempts\nIn the 2020 NBA playoffs, James Harden made 37 3 point shots and 109 shot attempts\nIn the 2020 NBA playoffs, Jamal Murrays 3 pts percentage was 0.4946236559139785.\nIn the 2020 NBA playoffs, Fred VanVleets 3 pts percentage was 0.39090909090909093.\nIn the 2020 NBA playoffs, James Hardens 3 pts percentage was 0.3394495412844037.').upper())
# print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# TODO: make a variable called `lakers_are_best` to indicate this
lakers_are_best=True
# TODO: print out the variable in an f-string to convey your opinion on the lakers
print(f"I believe that the lakers are the best NBA Team. {lakers_are_best}")
# print('Challenge 3.4: Type Conversion')
# TODO: Convert your `lakers_are_best` variable to an integer, and print it out.
# print(int(lakers_are_best) 
# TODO: Convert your `lakers_are best` variable to a float, and print it out
print(float(lakers_are_best))
# print('Challenge 3.5: Type Conversion Part 2')
# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.
print(str (Jamal_Murray_3pts_percentage))
print (str (Fred_VanVleet_3pts_percentage))
print(str(James_Harden_3pts_percentage))
# TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
print(int(Jamal_Murray_3pts_percentage))
print(int(Fred_VanVleet_3pts_percentage))
print(int(James_Harden_3pts_percentage))


