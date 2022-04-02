#Love Calculator
print('Welcome to the Love Calculator')
name1=input('What is your name?\n')
name2=input('What is their name?')

comname=name1+name2
lowername=comname.lower()
t=lowername.count("t")
r=lowername.count("r")
u=lowername.count('u')
e=lowername.count('e')
 
true=t+r+u+e

l=lowername.count("l")
o=lowername.count("o")
v=lowername.count('v')
e=lowername.count('e')

love=l+o+v+e
lovescore1=str(true)+str(love)
lovescore=int(lovescore1)
if (lovescore<10) or (lovescore>90):
    print(f"Your Love score is {lovescore},you go together like coke and mentos .")
elif lovescore>=40 and lovescore<=50:
    print(f"Your score is {lovescore},  you are allright with each other")
else:
    print(f'Your score is {lovescore}')