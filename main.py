from spy_details import spy_name, spy_salutation, spy_age, spy_rating

print 'Hey spy '
print 'What\\\'s up'

question = "Continue as " + spy_salutation + " " + spy_name + "(Y/N)?"
existing = raw_input(question)


def start_chat(spy_name, spy_age, spy_rating):
    current_status_message = None
    spy_name = spy_salutation + " " + spy_name
    if spy_age > 12 and spy_age < 50:
        print 'Authentication complete, Aaja mere sher, check krle,\n Naam hai: ' + spy_name + '\n Umar hai : ' + str(
            spy_age) + '\n Rating hai:' + str(spy_rating) + '\n Chl fir aage bdho'
        # show_menu = True

        # while show_menu:
    # Create on your own
    else:
        print 'tu chhod de moh maya tumse na ho paega '

    print 'Welcome %s. Apse milkr khushi hui.' % spy_name
    # we can also write %s instead of ' '+ variable


if existing == "Y":
    start_chat(spy_name, spy_age, spy_rating)
else:
    spy_name = ''
    spy_salutation = ''
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    spy_name = raw_input("Welcome to spy chat, ohh spy spy spy tera naam to btaaa: ")
    if len(spy_name) > 0:  # the user should give his name input
        # asking if he is a male or female
        spy_salutation = raw_input("Should I call you Mister or Miss?: ")

        print 'Arre deewano ' + 'Mujhe Pehchano ' + 'Kahan se aayaaaaa ' + 'Main hu corn' + ' Main hu ' + spy_name
        print 'Alright ' + spy_name + '. Aur bta apne baare me fir  '
        spy_age = input('Kitne saalo se bojh ho is duniya pe ?')
        # if spy_age > 12 and spy_age < 50:
        spy_rating = input('What is your rating?')
        print 'Arre bhai tu to ekdm fit hai spy bnne k liye'
        if spy_rating >= 4.5:
            print 'Tu hi to hai hmara best spy'
        elif spy_rating >= 3.5 and spy_rating < 4.5:
            print 'Acha hai pr aur ache se kaam kia kr'
        elif spy_rating >= 2.5 and spy_rating < 3.5:
            print 'tujhe bhi denge kuch kaam'
        else:
            print 'tu bhai naam dubayega'
        spy_online = True

        start_chat(spy_name, spy_age, spy_rating)

        print 'jb ye aega garmi thodi bdh jaegi'
    else:  # If spy didnt give any input
        print 'Oh nadaaan parinde naam bata jaa'
