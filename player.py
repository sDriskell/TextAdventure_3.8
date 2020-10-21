from dataclasses import dataclass

@dataclass
class Player:
    name: str
    backpack: list

    def navigate_menu(self):
        print("""What would you like to do?
        1. name?""")
        user_input = input(">")
        if user_input == "1":
            print(self.name)
        else:
            print("invalid command")

