import re

print("Our Magical Calculator")
print("Type 'quit'  to exit\n")
previous = 0
run =True


def performMath():
    global run,previous
    equation=""
    if previous ==0 :
        equation = input ("Enter equation:")
    else:
        equation = input(str(previous))



    if equation=='quit':
        print("Thanks, come again!")
        run=False
    else:
        equation= re.sub('[a-zA-Z,.()" "]','',equation)
        if previous==0:
            previous=eval(equation)
        else:
            previous =eval(str(previous)+equation)



while run:
    performMath()