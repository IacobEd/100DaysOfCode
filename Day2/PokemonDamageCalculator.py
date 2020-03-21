# It's a Pokemon battle! Your task is to calculate the damage that a particular move would do using the following formula (not the actual one from the game):
# damage = 50 * (attack / defense) * effectiveness
# Where:
# attack = your attack power
# defense = the opponent's defense
# effectiveness = the effectiveness of the attack based on the matchup (see explanation below)
# Effectiveness:
# Attacks can be super effective, neutral, or not very effective depending on the matchup. For example, water would be super effective against fire, but not very effective against grass.
# Super effective: 2x damage
# Neutral: 1x damage
# Not very effective: 0.5x damage
# To prevent this kata from being tedious, you'll only be dealing with four types: fire, water, grass, and electric. Here is the effectiveness of each matchup:
# fire > grass
# fire < water
# fire = electric
# water < grass
# water < electric
# grass = electric
def calculate_damage(your_type, opponent_type, attack, defense):
    effectiveness = 0
    if(your_type == "grass" and opponent_type == "fire"): effectiveness = 0.5
    elif(your_type == "grass" and opponent_type == "water"): effectiveness = 2
    elif(your_type == "grass" and opponent_type == "electric"): effectiveness = 1
    elif (your_type == "fire" and opponent_type == "grass"): effectiveness = 2
    elif (your_type == "fire" and opponent_type == "water"): effectiveness = 0.5
    elif (your_type == "fire" and opponent_type == "electric"): effectiveness = 1
    elif (your_type == "water" and opponent_type == "fire"): effectiveness = 2
    elif (your_type == "water" and opponent_type == "grass"): effectiveness = 0.5
    elif (your_type == "water" and opponent_type == "electric"): effectiveness = 0.5
    elif (your_type == "electric" and opponent_type == "fire"): effectiveness = 1
    elif (your_type == "electric" and opponent_type == "water"): effectiveness = 2
    elif (your_type == "electric" and opponent_type == "grass"): effectiveness = 1

    damage = 50 * (attack / defense) * effectiveness
    return int(damage)

print(calculate_damage("grass", "water", 40, 40))
