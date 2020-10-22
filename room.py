import item
from dataclasses import dataclass

@dataclass()
class Room:
    name: str
    description: str
    item: item

    n_room = None
    s_room = None
    e_room = None
    w_room = None

    item_found = False

    def connect_rooms(self, n, s, e, w):
        """Points to neighboring rooms by direction."""
        self.n_room = n
        self.s_room = s
        self.e_room = e
        self.w_room = w

    def move_rooms(self, user_input):
        """ Room navigation."""
        if user_input in ['n', 'N']:
            return self.n_room
        elif user_input in ['s', 'S']:
            return self.s_room
        elif user_input in ['e', 'E']:
            return self.e_room
        elif user_input in ['w', 'W']:
            return self.w_room
        else:
            return

    def inspect_room(self):
        if self.item_found is False:
            print("Found item {}. {}".format(self.item.name, self.item.description))
        else:
            print("Nothing in this room is noteworthy.")