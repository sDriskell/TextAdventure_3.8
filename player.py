from dataclasses import dataclass


@dataclass
class Player:
    name: str
    backpack: list

    def navigate_menu(self):
        print("""What would you like to do?
        1. name
        2. check backpack
        """)

        user_input = input(">")
        if user_input == "1":
            print(self.name)
        elif user_input == "2":
            Player.check_backpack(self)
        else:
            print("invalid command")

    def add_to_backpack(self, current_room):
        if current_room.item_found is False:
            self.backpack.append(current_room.item)
            current_room.item_found = True
        else:
            print("Nothing to pick-up")

    def check_backpack(self):
        for item in self.backpack:
            print(item.name, ": ", item.description)
