def spam():
    global eggs
    print(eggs) # Error!
    eggs = 'spam local'

eggs = 'global taco'
spam()
