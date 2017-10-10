from datetime import datetime
import time
import csv
from termcolor import colored
from steganography.steganography import Steganography
from spy_details import spy, Spy, ChatMessage, friends
#below are the previous statuses
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']
# chats=[]
#List of special words
SPECIAL_WORDS=['SOS','SAVE ME','NEED HELP']
new_friend = Spy ('', '', 0, 0.0)
# below function add_status is used to add status by spy just like apps like fb has
def add_status(current_status_message):
    if spy.current_status_message != None:
        print "Your current status message is " + current_status_message + "\n"
    else:
        print 'Abhi tk tera status message diya nahi hua koi tune...  \n'
    default = raw_input("Ye status pehle vala hi dena hai kya? (y/n)? ")
    if default.upper() == "N":
        new_status_message = raw_input("Kuch btana chahoge apne dosto ko?")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == "Y":
        item_position = 1
        for message in STATUS_MESSAGES:
            # can also write print item_position + " , " + message
            print '%d. %s' % (item_position, message)
            # error----- item position is not printing more than 1
            item_position = item_position + 1  # incrementing the item_position in order to check other items in list
        message_selection = input(" Bta beta kya btana hai?? Number bol: ")

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
    else:
        print 'You did not update your status message'
    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'Oh nadaan parinde status bta jaaa'

    return updated_status_message


def add_friend():
    # new_friend = Spy ('', '', 0, 0.0)
    new_friend.name = raw_input("Tere jesa yaar kahaaan ?? Vese tera naam to btaaaa:")
    new_friend.salutation = raw_input("Arrre ye bta tu hai kya... Mr. or Ms.?:")

    new_friend.age = input("Kitne saalo ka hai ye friend?")
    new_friend.rating = input("bta bhai teri rating bta")

    if new_friend.age > 12 and new_friend.rating >= 4 and len(new_friend.name) > 0:
        friends.append(new_friend)
        with open('friends.csv', 'a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([new_friend.name,new_friend.salutation, new_friend.age,new_friend.rating, new_friend.is_online])
        print 'Sabhi spyjano ko soochit kiya jata hai k hme ek mitra mila hai !'
    else:
        print 'Tu nahi bn skta dost ....'
    new_friend.name = new_friend.salutation + " " + new_friend.name
    return len(friends)

def load_friends():
    with open('friends.csv', 'rb') as friends_data:
        reader = csv.reader(friends_data)
        for row in reader:
                # spy = Spy(row[1],row[2],row[2], row[4])
                print row
                # friends.append(new_friend)


print 'Hey spy '
print 'What\\\'s up'

question = "Continue as " + spy.salutation + " " + spy.name + "(Y/N)?"  # just to check if it is existing user or another one
existing = raw_input(question)


# below function is used for selecting a particular friend for chat
def select_a_friend():
    friend_item_number = 0
    for friend in friends:
        print '%d %s aged %d having rating %2f is online' % (friend_item_number + 1, friend.name,friend.age,friend.rating)
        friend_item_number = friend_item_number + 1
    friend_choice = input('Choose the number from your friends')
    friend_choice_position = friend_choice - 1
    return friend_choice_position

#This module will enable spy to send the secret encoded message to another spy
#Send message method starts from here
def send_encoded_message():
    friend_choice = select_a_friend()
    original_image = raw_input('Abe bole to apni fotuu ka naam bta ?')
    original_path = 'Manzil.jpg'
    text = raw_input('Kya bhejna hai tujhe gupt rkhkr ..mujhe to btana pdega')
    with open('chats.csv', 'a') as chats_data:
        writer = csv.writer(chats_data)
        writer.writerow([text,datetime.now()])
    Steganography.encode(original_image, original_path, text)
    #below ChatMessage function is imported from spy_details.py
    new_chat = ChatMessage(text, True)
    print "Spyjan kripya dhyan de, apka secret message image ready hai!"

    friends[friend_choice].chats.append(new_chat)

def load_chats():
    with open('friends.csv', 'rb') as chats_data:
        reader = csv.reader(chats_data)
        for row in reader:
                # spy = Spy(row[1],row[2],row[2], row[4])
                print row
#This module will enable spy to read the secret message sent by another spy
#Read Message method starts from here
def read_message():

    sender = select_a_friend()
    output_path = raw_input('Abe chl khajoor fotuu ka naam bta')
    secret_text = Steganography.decode(output_path)
    new_chat = ChatMessage(secret_text,False)
    friends[sender].chats.append(new_chat)
    print "Abe oh kaaliaa ,Tera khana mene kha lia .....aur han Message mere pas hai re!"
    print secret_text

    text_length = len(secret_text) - secret_text.count(" ")
    if text_length > 100:
        del friends[sender]
    if "save me".upper() in secret_text:
        print "Spyjan zara dhyaan de ....apke ek bhai bandhu ko sahayta chahiye !"
    if "alert".upper() in secret_text:
        print "Abe oh ghonchuu , Dhyan rkh "
    if "sos".upper() in secret_text:
        print "Emergency call"
#below function is used to read chat history
def read_chat_history():
    read_for=select_a_friend()
    print '\n'
    for chat in friends[read_for].chats:

        if chat.sent_by_me:
            print colored('[%s]'%(chat.time.strftime('%d %B %Y')),'blue')
            print colored('You said:%s' % chat.message, "grey")
        else:
            print colored('[%s]  ' % (chat.time.strftime('%d %B %Y')), "blue")
            print colored('%s' % (friends[read_for].name), "red")
            print colored('%s' % (chat.message), "grey")

#below is the function that is used for chat mainly
def start_chat(spy):
    current_status_message = None
    spy.name = spy.salutation + " " + spy.name
    if spy.age > 12 and spy.age < 50:
        print 'Authentication complete, Aaja mere sher, check krle,\n Naam hai: ' + spy.name + '\n Umar hai : ' + str(
            spy.age) + '\n Rating hai:' + str(spy.rating) + '\n Chl fir aage bdho'
        print 'Welcome %s. Apse milkr khushi hui.' % spy.name
        # we can also write %s instead of ' '+ variable

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = input(menu_choices)

            # if len(menu_choice) > 0:
            #     menu_choice = int(menu_choice)

            if menu_choice == 1:
                current_status_message = add_status(current_status_message)
            elif menu_choice == 2:
                number_of_friends = add_friend()
                print 'You have %d friends' % (number_of_friends)
            elif menu_choice==3:
                send_encoded_message()
            elif menu_choice==4:
                read_message()
            elif menu_choice == 5:
                read_chat_history()
            else:
                show_menu = False

    else:
        print 'tu chhod de moh maya tumse na ho paega '
        exit()




if existing.upper() == "Y":
    load_friends()
    load_chats()
    start_chat(spy)
elif existing.upper() =="N":
    spy = Spy('', '', 0, 0.0)
    spy.name = raw_input("Welcome to spy chat, ohh spy spy spy tera naam to btaaa: ")
    if len(spy.name) > 0:  # the user should give his name input
        # asking if he is a male or female
        spy.salutation = raw_input("Should I call you Mister or Miss?: ")
        spy.name = spy.salutation + " " + spy.name
        print 'Arre deewano ' + 'Mujhe Pehchano ' + 'Kahan se aayaaaaa ' + 'Main hu corn' + ' Main hu ' + spy.name
        print 'Alright ' + spy.name + '. Aur bta apne baare me fir  '
        spy_age = input('Kitne saalo se bojh ho is duniya pe ?')
        if spy_age > 12 and spy_age < 50:
            spy.rating = input('What is your rating?')
            print 'Arre bhai tu to ekdm fit hai spy bnne k liye'
            if spy.rating >= 4.5:
                print 'Tu hi to hai hmara best spy'
            elif spy.rating >= 3.5 and spy.rating < 4.5:
                print 'Acha hai pr aur ache se kaam kia kr'
            elif spy.rating >= 2.5 and spy.rating < 3.5:
                print 'tujhe bhi denge kuch kaam'
            else:
                print 'tu bhai naam dubayega'
            spy_online = True

            start_chat(spy)

            print 'jb ye aega garmi thodi bdh jaegi'
        else:
            print 'tu chhod de moh maya tumse na ho paega '
            exit()
    else:  # If spy didnt give any input
        print 'Oh nadaaan parinde naam bata jaa'
else:
    print 'Bol spy bol Naam hoga to koi :-)....aur jo bola utna hi enter kro'

