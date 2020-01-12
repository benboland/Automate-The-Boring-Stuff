myPets = ['Zophie', 'Pooka', 'Fat-tail']
name = input('Enter a pet name: ')
if name.capitalize() not in myPets:
    print('I do not have a pet named ' + name.capitalize())
else:
    print(name.capitalize() + ' is my pet.')
