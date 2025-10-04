import random

WINNING_POSITION = 100
PLAYERS = 2

player_positions = [0] * PLAYERS
current_player = 0

SNAKES = {
    17: 7,
    54: 34,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    99: 78
}

LADDERS = {
    4: 14,
    9: 31,
    20: 38,
    28: 84,
    40: 59,
    51: 67,
    63: 81,
    71: 91
}

print("--- Welcome to Snake and Ladder! ---")
print(f"First player to reach square {WINNING_POSITION} wins.")

while True:
    player_number = current_player + 1
    current_position = player_positions[current_player]
    input(f"\nPlayer {player_number}, you are at square {current_position}. Press Enter to roll...")

    # dice_roll = random.randint(1, 6)
    # player_positions[current_player] += dice_roll
    
    # print(f"Player {player_number} rolled a {dice_roll} and moved to square {player_positions[current_player]}!")
    dice_roll = random.randint(1, 6)
    print(f"Player {player_number} rolled a {dice_roll}!")

    # ✅ Only move if it doesn’t cross 100
    if player_positions[current_player] + dice_roll <= WINNING_POSITION:
        player_positions[current_player] += dice_roll
        print(f"Player {player_number} moved to square {player_positions[current_player]}!")
    else:
        print(f"⚠️ Can't move, need exact number to reach {WINNING_POSITION}. Roll again next turn!")
    
    current_pos = player_positions[current_player]

    if current_pos in SNAKES:
        new_pos = SNAKES[current_pos]
        print(f"-> Oh no, a snake! Player {player_number} slides down to {new_pos}!")
        player_positions[current_player] = new_pos
    
    elif current_pos in LADDERS:
        new_pos = LADDERS[current_pos]
        print(f"-> Yay, a ladder! Player {player_number} climbs up to {new_pos}!")
        player_positions[current_player] = new_pos

    if player_positions[current_player] == WINNING_POSITION:
        print(f"\n*********************************")
        print(f"🎉 Congratulations Player {player_number}, you won! 🎉")
        print(f"*********************************")
        break

    current_player = (current_player + 1) % PLAYERS
