from spy_details import spy_name, spy_salutation, spy_age, spy_rating

STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']
friends_name = []
friends_age = []
friends_rating = []
friends_is_online = []


# below function add_status is used to add status by spy just like apps like fb has
def add_status(current_status_message):
    if current_status_message != None:
        print "Your current status message is " + current_status_message + "\n"
    else:
        print 'Abhi tk tera status message diya nahi hua koi tune...  \n'
    default = input("Ye status pehle vala hi dena hai kya? (y/n)? ")
    if default.upper() == "N":
        new_status_message = input("Kuch btana chahoge apne dosto ko?")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)
    elif default.upper() == "Y":
        item_position = 1
        for message in STATUS_MESSAGES:
            print item_position + " , " + message
            # can also use print '%d. %s' % (item_position, message)

            item_position = item_position + 1  # incrementing the item_position in order to check other items in list
            message_selection = input(" Bta beta kya btana hai?? Number bol: ")
            if len(STATUS_MESSAGES) >= message_selection:
                updated_status_message = STATUS_MESSAGES[message_selection - 1]
            else:
                print 'You did not update your status message'
            return updated_status_message


def add_friend():
    friend_name = raw_input("Tere jesa yaar kahaaan ?? Vese tera naam to btaaaa:")
    friend_salutation = raw_input("Arrre ye bta tu hai kya... Mr. or Ms.?:")
    friend_name = friend_salutation + " " + friend_name
    friend_age = input("Kitne saalo ka hai ye friend?")
    friend_rating = input("bta bhai teri rating bta")

    if friend_age > 12 and friend_rating >= spy_rating and len(friend_name) > 0:
        friends_name.append(friend_name)
        friends_age.append(friend_age)
        friends_rating.append(friend_rating)
        friends_is_online.append(True)
        print 'Sabhi spyjano ko soochit kiya jata hai k hme ek mitra mila hai !'
    else:
        print 'Tu nahi bn skta dost ....'
    return len(friends_name)


print 'Hey spy '
print 'What\\\'s up'

question = "Continue as " + spy_salutation + " " + spy_name + "(Y/N)?"  # just to check if it is existing user or another one
existing = raw_input(question)


def start_chat(spy_name, spy_age, spy_rating):
    current_status_message = None
    spy_name = spy_salutation + " " + spy_name
    if spy_age > 12 and spy_age < 50:
        print 'Authentication complete, Aaja mere sher, check krle,\n Naam hai: ' + spy_name + '\n Umar hai : ' + str(
            spy_age) + '\n Rating hai:' + str(spy_rating) + '\n Chl fir aage bdho'
        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)
                if menu_choice == 1:
                    current_status_message = add_status(current_status_message)
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                else:
                    show_menu = False

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
