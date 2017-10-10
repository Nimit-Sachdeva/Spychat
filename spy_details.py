from datetime import datetime
#Creating class spy
class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

#Creating class chatmessage to read chat history
class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Spyderman', 'Mr.', 20, 5.0)

friend_one = Spy('Spyderwoman', 'Ms.', 27,4.9)
friend_two = Spy('Hitler', 'Mr.', 21,4.7)
friend_three = Spy('Rocker', 'Mr.', 37,4.9)


friends = [friend_one, friend_two, friend_three]