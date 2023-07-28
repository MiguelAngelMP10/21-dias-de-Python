class User:

    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._friends = []
        self._messages = []

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

    def addFriend(self, friend):
        self._friends.append(friend)

    def getFriends(self):
        return self._friends

    def sendMessage(self, message, friend):
        self._messages.append(message)
        friend._messages.append(message)

    def showMessages(self):
        return self._messages
