from dataclasses import dataclass


@dataclass
class Player:
    name: str
    backpack: list
    max_hp: int
    current_hp: int
    attack: int
    defense: int

    def navigate_menu(self):
        """Provides information on character"""
        print("""What would you like to do?
        1. character
        2. check backpack
        """)

        user_input = input(">")
        if user_input == "1":
            Player.character_status(self)
        elif user_input == "2":
            Player.check_backpack(self)
        else:
            print("invalid command")

    def add_to_backpack(self, current_room):
        """Checks boolean value to determine if item can be moved"""
        if current_room.item_found is False:
            self.backpack.append(current_room.item)
            current_room.item_found = True
        else:
            print("Nothing to pick-up")

    def check_backpack(self):
        """Inspect backpack list"""
        for item in self.backpack:
            print(item.name, ": ", item.description)

    def character_status(self):
        """Player status"""
        print("""
        Name: {}
        HP: {} / {}
        Attack: {}
        Defense: {}
        """.format(self.name, self.current_hp, self.max_hp, self.attack, self.defense))

    def take_damage(self, damage):
        """Remove damage done to player"""
        pass

    def check_if_dead(self):
        """Checks if player has 0 or less currentHP"""
        pass