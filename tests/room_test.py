import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room("Part-A", 5, [], [])

    def test_room_has_name(self):
        self.assertEqual("Part-A", self.room.room)

    def test_guests_can_check_in(self):
        guest = Guest("Donkey", 10)
        self.room.check_in_guest(guest)
        self.assertEqual(1, self.room.guest_count())

    def test_guests_can_check_out(self):
        guest = Guest("Fiona", 5)
        self.room.check_in_guest(guest)
        self.room.check_out_guest(guest)
        self.assertEqual(0, self.room.guest_count())

    def test_can_add_song(self):
        song = Song("Smash Mouth", "All-Star")
        self.room.add_song(song)
        self.assertEqual(1, self.room.song_count())

    def test_room_is_full(self):
        result = self.room.is_at_capacity()
        self.assertFalse(result)

    def test_pay_entry_fee(self):
        # Test can't afford
        guest2 = Guest("Farquad", 4)
        result = self.room.pay_entry_fee(guest2)
        self.assertEqual("Can't afford the entry fee", result)
        # Test can afford
        guest = Guest("Donkey", 10)
        result = self.room.pay_entry_fee(guest)
        self.assertEqual(guest.wallet, 5)

