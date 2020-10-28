"""
Shane Driskell
Text Adventure in Python 3.8
TODO:
*Create an OOP text adventure
*Have object rooms, items, player, enemies
*Implement an inventory system
*Create a combat system
*
"""
import room
import player
import item


def game():
    """Game Loop and Setup"""
    # Item
    test_item1 = item.Item("candle", "It lights the way.")
    test_item2 = item.Item("rope", "It is long and sturdy.")
    test_item3 = item.Item("chalice", "It is a dull copper.")

    # Create room object
    t_room1 = room.Room("R1", "D1", test_item1)
    t_room2 = room.Room("R2", "D2", test_item2)
    t_room3 = room.Room("R3", "D3", test_item3)

    # Room adds go as:    North  South  East  West
    t_room1.connect_rooms(t_room2, None, None, None)
    t_room2.connect_rooms(None, t_room1, None, t_room3)
    t_room3.connect_rooms(None, None, t_room2, None)

    """
    Map:
    3 - 2
        |
        1
    """

    current_room = t_room1
    game_loop = True
    character = player.Player(input("Your name? "), [], 10, 10, 5, 5)

    print("Start the game, {}!".format(character.name))
    while game_loop:
        user_input = input(">").lower()

        if user_input in ["end", "stop", "quit", "bye", "exit"]:
            game_loop = False
        elif user_input == "test":
            print(current_room)
        elif user_input == "menu":
            character.navigate_menu()
        elif user_input == "inspect":
            current_room.inspect_room()
        elif user_input == "get":
            character.add_to_backpack(current_room)
        elif user_input == "move":
            temp_room = current_room.move_rooms(input("N, S, E, W? ")[0])
            if temp_room is None:
                print("There is no room there!")
            else:
                current_room = temp_room
        else:
            print("Invalid input.")

    print("Game over.")


if __name__ == "__main__":
    game()
