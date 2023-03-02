# Print a welcome message
print('Welcome to the Love Calculator')

# Ask the user for the two names to be used in the love calculation
name1 = input('What is your name?\n')
name2 = input('What is their name?')

# Concatenate the two names and convert the resulting string to lowercase
comname = name1 + name2
lowername = comname.lower()

# Calculate the number of occurrences of each letter in the string and add up the counts for 'true'
t = lowername.count("t")
r = lowername.count("r")
u = lowername.count('u')
e = lowername.count('e')
true = t + r + u + e

# Calculate the number of occurrences of each letter in the string and add up the counts for 'love'
l = lowername.count("l")
o = lowername.count("o")
v = lowername.count('v')
e = lowername.count('e')
love = l + o + v + e

# Combine the 'true' and 'love' scores to get a love score as a string
lovescore1 = str(true) + str(love)

# Convert the love score string to an integer
lovescore = int(lovescore1)

# Print a message to the user based on their love score
if (lovescore < 10) or (lovescore > 90):
    print(f"Your Love score is {lovescore}, you go together like coke and mentos.")
elif lovescore >= 40 and lovescore <= 50:
    print(f"Your score is {lovescore}, you are allright with each other.")
else:
    print(f'Your score is {lovescore}.')
