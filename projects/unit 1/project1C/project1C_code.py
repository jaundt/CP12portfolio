# TODO: make an inventory with at least one item and an append. later, copy code into new file and plant 3 bugs


inv = {'rat':0 , 'ipad':0 , 'hope':0 , 'grok':0 , }


name = input('what is your character name?')
fingers = 3
height = input('what is your character height in feet with decimals?')
lives = input ('is this character alive?(Y/N) ')

#funcions:___________________________________________________________________

def storyProgression():
    
    leave = input ('would you like to end the game?')
    if leave == ('yes', 'y', 'Y', 'YES'):
        exit
    elif leave != ('yes', 'y', 'Y', 'YES'):
        print('staying in program')   
#________________________________________________________________________
def add_itemRAT():
    
    inv['rat'] = inv['rat'] + 1
#________________________________________________________________________
def add_itemIPAD():
    
    inv['ipad'] = inv['ipad'] + 1
#________________________________________________________________________
def add_itemHOPE():
    
    inv['hope'] = inv['hope'] + 1
#________________________________________________________________________
def add_itemGROK():
    
    inv['grok'] = inv['grok'] + 1
#________________________________________________________________________

if lives == ('yes', 'y', 'Y', 'YES') :
    lives = True
else: lives = True

if lives == True and float(height) < 5.0 :
    print ( 'your character is alive and short' )
elif lives == True and float(height) > 5.0 :
    print ( 'your character is alive and tall' )
else: print ('uhh it doesnt look like your character is alive!')

#introduce character 
if lives == True :
    print ( 'welcome, ' + name + '!' )

storyProgression()
add_itemRAT()
