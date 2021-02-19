import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# Choose a random person from the input list to pay for all others "Mashareeb el ahwa 3ala 7sab meen?"
person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today!")
