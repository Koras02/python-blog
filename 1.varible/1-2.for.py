sports = ['football', 'baseball', 'cricket'];

for w in sports:
     print(w, len(w))

''' football 8
baseball 8
cricket 7
'''

# Create a users collection
users = {'Koke': 'active', 'Rike': 'inactive', 'Ko':'active'}

# Strategy: Iterate over a copy
for user, status in users.copy().items():
      if status == 'inactive':
           del users[user]

# Strategy: Create a new collection
active_users = {}
for user, status in users.items():
     if status == 'active':
         active_users[user] = status