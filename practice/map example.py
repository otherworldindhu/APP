'''squares = map(lambda x: x * x, [0, 1, 2, 3, 4])
print(squares)'''


import random
names = ['Seth', 'Ann', 'Morganna']
team_names = map(lambda x: random.choice(['A Team','B Team']),names)
print(team_names)
##['A Team', 'B Team', 'B Team']


##cant understad both