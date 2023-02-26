import requests
import json
import cata_tools



mine = '580fa93745120134266d8e050ae7d187c5047629ace6cce69ce3a9888d381273'
other = '90273aebf8d5b4c30e3b3629e301f0b5ccb02c3ab51c5d39492a63244f573327'




player = cata_tools.get_cata_player(mine)


health = (
    player['values']['character-health'] * ( 
        1 \
        + player['values']['village-blacksmith'] \
        + player['values']['banner-character_multiplier'] \
        + player['values']['tomes-character_multiplier'] \
        + player['values']['relic-catacombs_health']
    ) * (
        1 + player['values']['guardian-health_upgrades']
    )
)

phys_damage = (
    player['values']['character-damage'] * ( 
        1 \
        + player['values']['village-blacksmith'] \
        + player['values']['banner-character_multiplier'] \
        + player['values']['tomes-character_multiplier'] \
        + player['values']['relic-catacombs_damage']
    ) * (
        1 + player['values']['guardian-damage_upgrades']
    )
)

hit = (
    player['values']['character-hit'] * ( 
        1 \
        + player['values']['village-blacksmith'] \
        + player['values']['banner-character_multiplier'] \
        + player['values']['tomes-character_multiplier'] \
        + player['values']['relic-catacombs_hit']
    ) * (
        1 + player['values']['guardian-hit_upgrades']
    )
)

dodge = (
    player['values']['character-dodge'] * ( 
        1 \
        + player['values']['village-blacksmith'] \
        + player['values']['banner-character_multiplier'] \
        + player['values']['tomes-character_multiplier'] \
        + player['values']['relic-catacombs_dodge']
    ) * (
        1 + player['values']['guardian-dodge_upgrades']
    )
)



print(
    player['values']['character-hit'], hit
)
print(
    player['values']['character-dodge'], dodge
)