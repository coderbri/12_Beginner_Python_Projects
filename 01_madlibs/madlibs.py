persons_name = input("Person's name: ")
age = input("Age: ")
noun = input("Noun: ")
number = input("Number: ")
verb = input("Verb: ")
verb2 = input("Verb: ")
adj = input("Adjective: ")
place = input("Place: ")
place2 = input("Place: ")
place3 = input("Place: ")
adj2 = input("Adjective: ")
food = input("Food: ")
adj3 = input("Adjective: ")
food2 = input("Food: ")
drink = input("Drink: ")
adj4 = input("Adjective: ")
adj5 = input("Adjective: ")

madlib_title = "\n=== VISITING CHINA ====\n"
madlib = f'When {persons_name} was {age}, her parents told her \
they were going on a trip to China. They told her to pack her {noun}. \
The plane ride was {number} hours long! She {verb} and {verb2}. \
When they got to China, she was very {adj}. On their trip, they \
visited {place}, {place2}, and {place3}. They ate a lot of interesting \
things including {adj2} {food}, {adj3} {food2}, and {drink}. Everyone \
had a/an {adj4} time. When it was time to go home, she was very {adj5}. \
"!" she said. "Can\'t we stay longer?"'

print(madlib_title)
print(madlib)
