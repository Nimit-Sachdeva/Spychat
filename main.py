print 'Hey spy '
print 'What\\\'s up'
spy_name = raw_input("Welcome to spy chat, ohh spy spy spy tera naam to btaaa: ")
# spy_name will take name of the user as input of the spy
if len(spy_name)>0:             #the user should give his name input
    spy_age= 0
    spy_rating= 0.0
    spy_online= False
    spy_age= input('Kitne saalo se bojh ho is duniya pe ?')
    if spy_age > 12 and spy_age<50:
        spy_rating = input('What is your rating?')
        print 'Arre bhai tu to ekdm fit hai spy bnne k liye'
    else:
        print 'Budha ho gya hai tu chhod de moh maya aur sanyasi bnja '
    print 'jb ye aega garmi thodi bdh jaegi'
    print 'Welcome ' + spy_name + '. Apse milkr khushi hui.'
    spy_salutation = raw_input("Should I call you Mister or Miss?: ")
    #asking if he is a male or female
    spy_name = spy_salutation + " " + spy_name
    print 'Arre deewano ' + 'Mujhe Pehchano ' + 'Kahan se aayaaaaa ' +'Main hu corn' + ' Main hu' + spy_name
    print 'Alright ' +spy_name + '. Aur bta apne baare me fir  '
else:                       #If spy didnt give any input
    print 'Oh nadaaan parinde naam bata jaa'
if spy_rating >=4.5:
    print 'Tu hi to hai hmara best spy'
elif spy_rating >=3.5 and spy_rating<4.5:
    print 'chl chl ache se kaam kia kr'
elif spy_rating >=2.5 and spy_rating<3.5:
    print 'tujhe bhi denge kuch kaam'
else:
    print 'tu bhai naam dubayega'
spy_online=True
print 'Authentication complete, Aaja mere sher, check krle,\n Naam hai: '+spy_name+ '\n Umar hai : '+str(spy_age) +'\n Rating hai:'+str(spy_rating) +'\n Chl fir aage bdho'



