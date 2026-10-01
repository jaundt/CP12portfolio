# TODO: define your character's variables — one str, one int, one float, one bool

name = input('what is your character name?')
fingers = 3
height = input('what is your character height with decimals?')
lives = input ('is this character alive?')

if lives == 'yes' :
    lives = True
else: lives = False

if lives == True and float(height) < 5.0 :
    print ( 'your character is alive and short' )
elif lives == True and float(height) > 5.0 :
    print ( 'your character is alive and tall' )
else: print ('uhh it doesnt look like your character is alive!')

#introduce character 
if lives == True :
    print ( 'welcome, ' + name + '!' )
