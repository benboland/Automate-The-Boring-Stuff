catNames = []
while True:
    name = input('Enter the name of a cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop): ')
    if name == '':
        break
    catNames = catNames + [name]
print('The cat names are: ')
for name in catNames:
    print(' ' + name)
