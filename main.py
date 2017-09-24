print 'Hey spy '
print 'What\\\'s up'
spy_name = raw_input("Welcome to spy chat, ohh spy spy spy tera naam to btaaa: ")
# spy_name will take name of the user as input of the spy
if len(spy_name)>0:             #the user should give his name input
    print 'jb ye aega garmi thodi bdh jaegi'
    print 'Welcome ' + spy_name + '. Apse milkr khushi hui.'
    spy_salutation = raw_input("Should I call you Mister or Miss?: ") #asking if he is a male or female
    spy_name = spy_salutation + " " + spy_name
    print 'Arre deewano ' + 'Mujhe Pehchano ' + 'Kahan se aayaaaaa ' +'Main hu corn' + 'Main hu' + spy_name
    print 'Alright ' +spy_name + '. Aur bta apne baare me fir  '
else:
    print 'Oh nadaaan parinde naam bata jaa'
    

