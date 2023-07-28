from NodeStack import NodeStack


class Playlist:
    def __init__(self):
        # Tu código aquí 👇
        self.top = None
        self.bottom = None
        self.length = 0

    def addSong(self, song):
        # Tu código aquí 👇
        newSong = NodeStack(song)
        if self.length == 0:
            self.top = newSong
            self.bottom = newSong
        else:
            newSong.next = self.top
            self.top = newSong
        self.length += 1

    def playSong(self):
        # Tu código aquí 👇
        if self.top is None:
            raise Exception("No hay canciones en la lista")
        if self.top == self.bottom:
            self.bottom = None
        play = self.top
        self.top = play.next
        self.length -= 1
        return play.value

    def getPlaylist(self):
        # Tu código aquí 👇
        list = []
        if self.top is None:
            return list
        current = self.top
        while current:
            list.append(current.value)
            current = current.next
        return list
