import requests
import json



def get_cata_player(key):

    r = requests.get(
        f"https://queslar.com/api/player/full/{key}"
    )

    data = r.json()

    player = {
        'village-blacksmith': 0,

        'character-health': 0,
        'character-damage': 0,
        'character-hit': 0,
        'character-dodge': 0,
        'character-crit_damage': 0,
        'character-crit_chance': 0,
        'character-water_damage': 0,
        'character-thunder_damage': 0,
        'character-fire_damage': 0,

        'banner-mob_multiplier': 0,
        'banner-character_multiplier': 0,
        'banner-water_resistance': 0,
        'banner-thunder_resistance': 0,
        'banner-fire_resistance': 0,
        'banner-melee_resistance': 0,
        'banner-ranged_resistance': 0,
        'banner-elemental_conversion': 0,

        'tomes-mob_multiplier': 0,
        'tomes-character_multiplier': 0,
        'tomes-water_resistance': 0,
        'tomes-thunder_resistance': 0,
        'tomes-fire_resistance': 0,
        'tomes-melee_resistance': 0,
        'tomes-ranged_resistance': 0,
        'tomes-elemental_conversion': 0,
        'tomes-lifesteal': 0,

        'relic-catacombs_health': 0,
        'relic-catacombs_damage': 0,
        'relic-catacombs_hit': 0,
        'relic-catacombs_dodge': 0,
        'relic-catacombs_elemental': 0,

        'guardian-health_upgrades': 0,
        'guardian-damage_upgrades': 0,
        'guardian-hit_upgrades': 0,
        'guardian-dodge_upgrades': 0,
        'guardian-crit_damage_upgrades': 0,
        'guardian-crit_chance_upgrades': 0,
    }




    # village boosts
    player['village-blacksmith'] = data['village']['boosts']['blacksmith']


    # character levels
    player['character-health'] = data['catacombCharacter']['health']
    player['character-damage'] = data['catacombCharacter']['damage']
    player['character-hit'] = data['catacombCharacter']['hit']
    player['character-dodge'] = data['catacombCharacter']['dodge']
    player['character-crit_damage'] = data['catacombCharacter']['crit_damage']
    player['character-crit_chance'] = data['catacombCharacter']['crit_chance']
    player['character-water_damage'] = data['catacombCharacter']['water_damage']
    player['character-thunder_damage'] = data['catacombCharacter']['thunder_damage']
    player['character-fire_damage'] = data['catacombCharacter']['fire_damage']

    

    player['banner-mob_multiplier'] = data['catacombBanner']['mob_multiplier']
    player['banner-character_multiplier'] = data['catacombBanner']['character_multiplier']
    player['banner-water_resistance'] = data['catacombBanner']['water_resistance']
    player['banner-thunder_resistance'] = data['catacombBanner']['thunder_resistance']
    player['banner-fire_resistance'] = data['catacombBanner']['fire_resistance']
    player['banner-melee_resistance'] = data['catacombBanner']['melee_resistance']
    player['banner-ranged_resistance'] = data['catacombBanner']['ranged_resistance']
    player['banner-elemental_conversion'] = data['catacombBanner']['elemental_conversion']

    


    for tome in data['catacombTomeInventory']:

        if tome['equipped'] == 1:

            player['tomes-mob_multiplier'] += tome['mob_multiplier']
            player['tomes-character_multiplier'] += tome['character_multiplier']
            player['tomes-water_resistance'] += tome['water_resistance']
            player['tomes-thunder_resistance'] += tome['thunder_resistance']
            player['tomes-fire_resistance'] += tome['fire_resistance']
            player['tomes-melee_resistance'] += tome['melee_resistance']
            player['tomes-ranged_resistance'] += tome['ranged_resistance']
            player['tomes-elemental_conversion'] += tome['elemental_conversion']
            player['tomes-lifesteal'] += tome['lifesteal']



    player['relic-catacombs_health'] = data['boosts']['catacombs_health']
    player['relic-catacombs_damage'] = data['boosts']['catacombs_damage']
    player['relic-catacombs_hit'] = data['boosts']['catacombs_hit']
    player['relic-catacombs_dodge'] = data['boosts']['catacombs_dodge']
    player['relic-catacombs_elemental'] = data['boosts']['catacombs_elemental']


    base_guardian_boosts = [

        {
            'health_upgrades': 0,
            'damage_upgrades': 0,
            'hit_upgrades': 0,
            'dodge_upgrades': 0,
            'crit_damage_upgrades': 0,
            'crit_chance_upgrades': 0
        },
        {
            'health_upgrades': 50,
            'damage_upgrades': 0,
            'hit_upgrades': 0,
            'dodge_upgrades': 0,
            'crit_damage_upgrades': 0,
            'crit_chance_upgrades': 0
        },
        {
            'health_upgrades': 100,
            'damage_upgrades': 50,
            'hit_upgrades': 0,
            'dodge_upgrades': 0,
            'crit_damage_upgrades': 0,
            'crit_chance_upgrades': 0
        },
        {
            'health_upgrades': 150,
            'damage_upgrades': 100,
            'hit_upgrades': 50,
            'dodge_upgrades': 50,
            'crit_damage_upgrades': 0,
            'crit_chance_upgrades': 0
        },
        {
            'health_upgrades': 200,
            'damage_upgrades': 150,
            'hit_upgrades': 100,
            'dodge_upgrades': 100,
            'crit_damage_upgrades': 50,
            'crit_chance_upgrades': 0
        },
        {
            'health_upgrades': 300,
            'damage_upgrades': 200,
            'hit_upgrades': 150,
            'dodge_upgrades': 150,
            'crit_damage_upgrades': 100,
            'crit_chance_upgrades': 50
        },

    ]



    guardian = base_guardian_boosts[
        len(data['catacombGuardian'])
    ]

    if len(data['catacombGuardian']) > 0:
        guardian['health_upgrades'] += data['catacombGuardian'][-1]['health_upgrades']
        guardian['damage_upgrades'] += data['catacombGuardian'][-1]['damage_upgrades']
        guardian['hit_upgrades'] += data['catacombGuardian'][-1]['hit_upgrades']
        guardian['dodge_upgrades'] += data['catacombGuardian'][-1]['dodge_upgrades']
        guardian['crit_damage_upgrades'] += data['catacombGuardian'][-1]['crit_damage_upgrades']
        guardian['crit_chance_upgrades'] += data['catacombGuardian'][-1]['crit_chance_upgrades']


        player['guardian-health_upgrades'] = guardian['health_upgrades']
        player['guardian-damage_upgrades'] = guardian['damage_upgrades']
        player['guardian-hit_upgrades'] = guardian['hit_upgrades']
        player['guardian-dodge_upgrades'] = guardian['dodge_upgrades']
        player['guardian-crit_damage_upgrades'] = guardian['crit_damage_upgrades']
        player['guardian-crit_chance_upgrades'] = guardian['crit_chance_upgrades']



    return player    






def get_cata_player_old(key):

    r = requests.get(
        f"https://queslar.com/api/player/full/{key}"
    )

    data = r.json()


    player = {
        'levels': {
            'village-blacksmith': 0,

            'character-health': 0,
            'character-damage': 0,
            'character-hit': 0,
            'character-dodge': 0,
            'character-crit_damage': 0,
            'character-crit_chance': 0,
            'character-water_damage': 0,
            'character-thunder_damage': 0,
            'character-fire_damage': 0,

            'banner-mob_multiplier': 0,
            'banner-character_multiplier': 0,
            'banner-water_resistance': 0,
            'banner-thunder_resistance': 0,
            'banner-fire_resistance': 0,
            'banner-melee_resistance': 0,
            'banner-ranged_resistance': 0,
            'banner-elemental_conversion': 0,

            'tomes-mob_multiplier': 0,
            'tomes-character_multiplier': 0,
            'tomes-water_resistance': 0,
            'tomes-thunder_resistance': 0,
            'tomes-fire_resistance': 0,
            'tomes-melee_resistance': 0,
            'tomes-ranged_resistance': 0,
            'tomes-elemental_conversion': 0,
            'tomes-lifesteal': 0,

            'relic-catacombs_health': 0,
            'relic-catacombs_damage': 0,
            'relic-catacombs_hit': 0,
            'relic-catacombs_dodge': 0,
            'relic-catacombs_elemental': 0,

            'guardian-health_upgrades': 0,
            'guardian-damage_upgrades': 0,
            'guardian-hit_upgrades': 0,
            'guardian-dodge_upgrades': 0,
            'guardian-crit_damage_upgrades': 0,
            'guardian-crit_chance_upgrades': 0,

        },
        'values': {
            'village-blacksmith': 0,

            'character-health': 0,
            'character-damage': 0,
            'character-hit': 0,
            'character-dodge': 0,
            'character-crit_damage': 0,
            'character-crit_chance': 0,
            'character-water_damage': 0,
            'character-thunder_damage': 0,
            'character-fire_damage': 0,

            'banner-mob_multiplier': 0,
            'banner-character_multiplier': 0,
            'banner-water_resistance': 0,
            'banner-thunder_resistance': 0,
            'banner-fire_resistance': 0,
            'banner-melee_resistance': 0,
            'banner-ranged_resistance': 0,
            'banner-elemental_conversion': 0,

            'tomes-mob_multiplier': 0,
            'tomes-character_multiplier': 0,
            'tomes-water_resistance': 0,
            'tomes-thunder_resistance': 0,
            'tomes-fire_resistance': 0,
            'tomes-melee_resistance': 0,
            'tomes-ranged_resistance': 0,
            'tomes-elemental_conversion': 0,
            'tomes-lifesteal': 0,

            'relic-catacombs_health': 0,
            'relic-catacombs_damage': 0,
            'relic-catacombs_hit': 0,
            'relic-catacombs_dodge': 0,
            'relic-catacombs_elemental': 0,

            'guardian-health_upgrades': 0,
            'guardian-damage_upgrades': 0,
            'guardian-hit_upgrades': 0,
            'guardian-dodge_upgrades': 0,
            'guardian-crit_damage_upgrades': 0,
            'guardian-crit_chance_upgrades': 0,
        }
        
    }






    # with open('data.json', 'r') as f:
    #     data = json.loads(f.read())




    # village boosts
    player['levels']['village-blacksmith'] = data['village']['boosts']['blacksmith']
    player['values']['village-blacksmith'] = sum(
        [.01 + .01*(x // 20) for x in range(player['levels']['village-blacksmith'])]
    )

    # character levels
    player['levels']['character-health'] = data['catacombCharacter']['health']
    player['levels']['character-damage'] = data['catacombCharacter']['damage']
    player['levels']['character-hit'] = data['catacombCharacter']['hit']
    player['levels']['character-dodge'] = data['catacombCharacter']['dodge']
    player['levels']['character-crit_damage'] = data['catacombCharacter']['crit_damage']
    player['levels']['character-crit_chance'] = data['catacombCharacter']['crit_chance']
    player['levels']['character-water_damage'] = data['catacombCharacter']['water_damage']
    player['levels']['character-thunder_damage'] = data['catacombCharacter']['thunder_damage']
    player['levels']['character-fire_damage'] = data['catacombCharacter']['fire_damage']

    player['values']['character-health'] = data['catacombCharacter']['health']*300 + 1000
    player['values']['character-damage'] = data['catacombCharacter']['damage']*20 + 40
    player['values']['character-hit'] = data['catacombCharacter']['hit']*50 + 100
    player['values']['character-dodge'] = data['catacombCharacter']['dodge']*50 + 100
    player['values']['character-crit_damage'] = data['catacombCharacter']['crit_damage']*.0025
    player['values']['character-crit_chance'] = data['catacombCharacter']['crit_chance']*.0025
    player['values']['character-water_damage'] = data['catacombCharacter']['water_damage']*20
    player['values']['character-thunder_damage'] = data['catacombCharacter']['thunder_damage']*20
    player['values']['character-fire_damage'] = data['catacombCharacter']['fire_damage']*20


    player['levels']['banner-mob_multiplier'] = data['catacombBanner']['mob_multiplier']
    player['levels']['banner-character_multiplier'] = data['catacombBanner']['character_multiplier']
    player['levels']['banner-water_resistance'] = data['catacombBanner']['water_resistance']
    player['levels']['banner-thunder_resistance'] = data['catacombBanner']['thunder_resistance']
    player['levels']['banner-fire_resistance'] = data['catacombBanner']['fire_resistance']
    player['levels']['banner-melee_resistance'] = data['catacombBanner']['melee_resistance']
    player['levels']['banner-ranged_resistance'] = data['catacombBanner']['ranged_resistance']
    player['levels']['banner-elemental_conversion'] = data['catacombBanner']['elemental_conversion']

    player['values']['banner-mob_multiplier'] = data['catacombBanner']['mob_multiplier']*.00325
    player['values']['banner-character_multiplier'] = data['catacombBanner']['character_multiplier']*.00535
    player['values']['banner-water_resistance'] = data['catacombBanner']['water_resistance']*.0011
    player['values']['banner-thunder_resistance'] = data['catacombBanner']['thunder_resistance']*.0011
    player['values']['banner-fire_resistance'] = data['catacombBanner']['fire_resistance']*.0011
    player['values']['banner-melee_resistance'] = data['catacombBanner']['melee_resistance']*.0011
    player['values']['banner-ranged_resistance'] = data['catacombBanner']['ranged_resistance']*.0011
    player['values']['banner-elemental_conversion'] = data['catacombBanner']['elemental_conversion']*.0011


    for tome in data['catacombTomeInventory']:

        if tome['equipped'] == 1:

            player['levels']['tomes-mob_multiplier'] += tome['mob_multiplier']
            player['levels']['tomes-character_multiplier'] += tome['character_multiplier']
            player['levels']['tomes-water_resistance'] += tome['water_resistance']
            player['levels']['tomes-thunder_resistance'] += tome['thunder_resistance']
            player['levels']['tomes-fire_resistance'] += tome['fire_resistance']
            player['levels']['tomes-melee_resistance'] += tome['melee_resistance']
            player['levels']['tomes-ranged_resistance'] += tome['ranged_resistance']
            player['levels']['tomes-elemental_conversion'] += tome['elemental_conversion']
            player['levels']['tomes-lifesteal'] += tome['lifesteal']


    player['values']['tomes-mob_multiplier'] = player['levels']['tomes-mob_multiplier']/10000
    player['values']['tomes-character_multiplier'] = player['levels']['tomes-character_multiplier']/10000
    player['values']['tomes-water_resistance'] = player['levels']['tomes-water_resistance']/10000
    player['values']['tomes-thunder_resistance'] = player['levels']['tomes-thunder_resistance']/10000
    player['values']['tomes-fire_resistance'] = player['levels']['tomes-fire_resistance']/10000
    player['values']['tomes-melee_resistance'] = player['levels']['tomes-melee_resistance']/10000
    player['values']['tomes-ranged_resistance'] = player['levels']['tomes-ranged_resistance']/10000
    player['values']['tomes-elemental_conversion'] = player['levels']['tomes-elemental_conversion']/10000
    player['values']['tomes-lifesteal'] = player['levels']['tomes-lifesteal']/10000


    player['levels']['relic-catacombs_health'] = data['boosts']['catacombs_health']
    player['levels']['relic-catacombs_damage'] = data['boosts']['catacombs_damage']
    player['levels']['relic-catacombs_hit'] = data['boosts']['catacombs_hit']
    player['levels']['relic-catacombs_dodge'] = data['boosts']['catacombs_dodge']
    player['levels']['relic-catacombs_elemental'] = data['boosts']['catacombs_elemental']

    player['values']['relic-catacombs_health'] = data['boosts']['catacombs_health'] / 10000
    player['values']['relic-catacombs_damage'] = data['boosts']['catacombs_damage'] / 10000
    player['values']['relic-catacombs_hit'] = data['boosts']['catacombs_hit'] / 10000
    player['values']['relic-catacombs_dodge'] = data['boosts']['catacombs_dodge'] / 10000
    player['values']['relic-catacombs_elemental'] = data['boosts']['catacombs_elemental'] / 10000



    base_guardian_boosts = [

        {
            'health_upgrades': 0,
            'damage_upgrades': 0,
            'hit_upgrades': 0,
            'dodge_upgrades': 0,
            'crit_damage_upgrades': 0,
            'crit_chance_upgrades': 0
        },
        {
            'health_upgrades': 50,
            'damage_upgrades': 0,
            'hit_upgrades': 0,
            'dodge_upgrades': 0,
            'crit_damage_upgrades': 0,
            'crit_chance_upgrades': 0
        },
        {
            'health_upgrades': 100,
            'damage_upgrades': 50,
            'hit_upgrades': 0,
            'dodge_upgrades': 0,
            'crit_damage_upgrades': 0,
            'crit_chance_upgrades': 0
        },
        {
            'health_upgrades': 150,
            'damage_upgrades': 100,
            'hit_upgrades': 50,
            'dodge_upgrades': 50,
            'crit_damage_upgrades': 0,
            'crit_chance_upgrades': 0
        },
        {
            'health_upgrades': 200,
            'damage_upgrades': 150,
            'hit_upgrades': 100,
            'dodge_upgrades': 100,
            'crit_damage_upgrades': 50,
            'crit_chance_upgrades': 0
        },
        {
            'health_upgrades': 300,
            'damage_upgrades': 200,
            'hit_upgrades': 150,
            'dodge_upgrades': 150,
            'crit_damage_upgrades': 100,
            'crit_chance_upgrades': 50
        },

    ]



    guardian = base_guardian_boosts[
        len(data['catacombGuardian'])
    ]

    if len(data['catacombGuardian']) > 0:
        guardian['health_upgrades'] += data['catacombGuardian'][-1]['health_upgrades']
        guardian['damage_upgrades'] += data['catacombGuardian'][-1]['damage_upgrades']
        guardian['hit_upgrades'] += data['catacombGuardian'][-1]['hit_upgrades']
        guardian['dodge_upgrades'] += data['catacombGuardian'][-1]['dodge_upgrades']
        guardian['crit_damage_upgrades'] += data['catacombGuardian'][-1]['crit_damage_upgrades']
        guardian['crit_chance_upgrades'] += data['catacombGuardian'][-1]['crit_chance_upgrades']


        player['levels']['guardian-health_upgrades'] = guardian['health_upgrades']
        player['levels']['guardian-damage_upgrades'] = guardian['damage_upgrades']
        player['levels']['guardian-hit_upgrades'] = guardian['hit_upgrades']
        player['levels']['guardian-dodge_upgrades'] = guardian['dodge_upgrades']
        player['levels']['guardian-crit_damage_upgrades'] = guardian['crit_damage_upgrades']
        player['levels']['guardian-crit_chance_upgrades'] = guardian['crit_chance_upgrades']

        player['values']['guardian-health_upgrades'] = guardian['health_upgrades'] / 100
        player['values']['guardian-damage_upgrades'] = guardian['damage_upgrades'] / 100
        player['values']['guardian-hit_upgrades'] = guardian['hit_upgrades'] / 100
        player['values']['guardian-dodge_upgrades'] = guardian['dodge_upgrades'] / 100
        player['values']['guardian-crit_damage_upgrades'] = guardian['crit_damage_upgrades'] / 100
        player['values']['guardian-crit_chance_upgrades'] = guardian['crit_chance_upgrades'] / 100


    for key in player['values']:

        player['values'][key] = round(
            player['values'][key], 5
        )


    return player



def get_guardian_stats(l):

    levels = [
        50,
        200,
        500,
        1000,
        1500
    ]

    return [
        300*levels[l] + 300*(levels[l]**1.65),
        20*levels[l] + 20*(levels[l]**1.65),
        20*levels[l] + 20*(levels[l]**1.65),
        20*levels[l] + 20*(levels[l]**1.65),
        .001*levels[l] + .001*(levels[l]**1.65),
        .001*levels[l] + .001*(levels[l]**1.65),
    ]


