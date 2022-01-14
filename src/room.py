from src.song import Song
from src.guest import Guest

class Room:
    def __init__(self, room, entry_fee, guests, playlist):
        self.room = room
        self.playlist = playlist
        self.guests = guests
        self.entry_fee = entry_fee
        self.capacity = 2

    def guest_count(self):
        return len(self.guests)
    
    def song_count(self):
        return len(self.playlist)

    def check_in_guest(self, guest):
        self.guests.append(guest)
    
    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        return self.playlist.append(song)

    def is_at_capacity(self):
        return self.guest_count() >= self.capacity

    def pay_entry_fee(self, guest):
        if guest.wallet < self.entry_fee:
            return "Can't afford the entry fee"
        guest.wallet -= self.entry_fee


    

