import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import cata_tools


dash.register_page(__name__, path='/')




layout = dbc.Container([

    dcc.Store(id='player_cata_data'),
    dbc.Card(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Input(
                            placeholder='Paste API Key',
                            id='api_key',
                            type='text',
                        ),
                        width=10
                    ),
                    dbc.Col(
                        dbc.Button(
                            'Refresh',
                            id='call_api',
                            n_clicks=0
                        ),
                        width=2
                    )
                ],
            ),

            dbc.Row(
                [
                    dbc.Col(
                        dbc.Button(
                            'Show/Hide Character Stats',
                            id='collapse_button-character',
                            color='info'
                        ),
                        width=4
                    ),
                ],
                style={
                    'margin-top': '10px',
                    'margin-bottom': '10px',
                }
            ),
            dbc.Collapse(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                'Stat',
                                width=2,
                                style={
                                    'font-weight': 'bold',
                                    'color': 'blue'
                                }
                            ),
                            dbc.Col(
                                'Points',
                                width=3,
                                style={
                                    'font-weight': 'bold',
                                    'color': 'blue'
                                }
                            ),
                            dbc.Col(
                                'Value',
                                width=3,
                                style={
                                    'font-weight': 'bold',
                                    'color': 'blue'
                                }
                            ),
                            dbc.Col(
                                'Relic Cost',
                                width=3,
                                style={
                                    'font-weight': 'bold',
                                    'color': 'blue'
                                }
                            ),
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                'Health',
                                width=2
                            ),
                            dbc.Col(
                                dbc.Input(
                                    id='health-input',
                                    type='number',
                                    min=0,
                                    max=999990,
                                    debounce=True
                                ),
                                width=3
                            ),
                            dbc.Col(
                                id='health-value',
                                width=3
                            ),
                            dbc.Col(
                                id='health-cost',
                                width=3
                            ),
                        ],
                        align="center",
                        className="h-50",
                        style={
                            'margin-top': '2px',
                            'margin-bottom': '2px',
                        }
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                'Damage',
                                width=2
                            ),
                            dbc.Col(
                                dbc.Input(
                                    id='damage-input',
                                    type='number',
                                    min=0,
                                    max=999990,
                                    debounce=True
                                ),
                                width=3
                            ),
                            dbc.Col(
                                id='damage-value',
                                width=3
                            ),
                            dbc.Col(
                                id='damage-cost',
                                width=3
                            ),
                        ],
                        align="center",
                        className="h-50",
                        style={
                            'margin-top': '2px',
                            'margin-bottom': '2px',
                        }
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                'Hit',
                                width=2
                            ),
                            dbc.Col(
                                dbc.Input(
                                    id='hit-input',
                                    type='number',
                                    min=0,
                                    max=999990,
                                    debounce=True
                                ),
                                width=3
                            ),
                            dbc.Col(
                                id='hit-value',
                                width=3
                            ),
                            dbc.Col(
                                id='hit-cost',
                                width=3
                            ),
                        ],
                        align="center",
                        className="h-50",
                        style={
                            'margin-top': '2px',
                            'margin-bottom': '2px',
                        }
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                'Dodge',
                                width=2
                            ),
                            dbc.Col(
                                dbc.Input(
                                    id='dodge-input',
                                    type='number',
                                    min=0,
                                    max=999990,
                                    debounce=True
                                ),
                                width=3
                            ),
                            dbc.Col(
                                id='dodge-value',
                                width=3
                            ),
                            dbc.Col(
                                id='dodge-cost',
                                width=3
                            ),
                        ],
                        align="center",
                        className="h-50",
                        style={
                            'margin-top': '2px',
                            'margin-bottom': '2px',
                        }
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                'Crit Damage',
                                width=2
                            ),
                            dbc.Col(
                                dbc.Input(
                                    id='crit_damage-input',
                                    type='number',
                                    min=0,
                                    max=999990,
                                    debounce=True
                                ),
                                width=3
                            ),
                            dbc.Col(
                                id='crit_damage-value',
                                width=3
                            ),
                            dbc.Col(
                                id='crit_damage-cost',
                                width=3
                            ),
                        ],
                        align="center",
                        className="h-50",
                        style={
                            'margin-top': '2px',
                            'margin-bottom': '2px',
                        }
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                'Crit Chance',
                                width=2
                            ),
                            dbc.Col(
                                dbc.Input(
                                    id='crit_chance-input',
                                    type='number',
                                    min=0,
                                    max=999990,
                                    debounce=True
                                ),
                                width=3
                            ),
                            dbc.Col(
                                id='crit_chance-value',
                                width=3
                            ),
                            dbc.Col(
                                id='crit_chance-cost',
                                width=3
                            ),
                        ],
                        align="center",
                        className="h-50",
                        style={
                            'margin-top': '2px',
                            'margin-bottom': '2px',
                        }
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                'Water',
                                width=2
                            ),
                            dbc.Col(
                                dbc.Input(
                                    id='water-input',
                                    type='number',
                                    min=0,
                                    max=999990,
                                    debounce=True
                                ),
                                width=3
                            ),
                            dbc.Col(
                                id='water-value',
                                width=3
                            ),
                            dbc.Col(
                                id='water-cost',
                                width=3
                            ),
                        ],
                        align="center",
                        className="h-50",
                        style={
                            'margin-top': '2px',
                            'margin-bottom': '2px',
                        }
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                'Thunder',
                                width=2
                            ),
                            dbc.Col(
                                dbc.Input(
                                    id='thunder-input',
                                    type='number',
                                    min=0,
                                    max=999990,
                                    debounce=True
                                ),
                                width=3
                            ),
                            dbc.Col(
                                id='thunder-value',
                                width=3
                            ),
                            dbc.Col(
                                id='thunder-cost',
                                width=3
                            ),
                        ],
                        align="center",
                        className="h-50",
                        style={
                            'margin-top': '2px',
                            'margin-bottom': '2px',
                        }
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                'Fire',
                                width=2
                            ),
                            dbc.Col(
                                dbc.Input(
                                    id='fire-input',
                                    type='number',
                                    min=0,
                                    max=999990,
                                    debounce=True
                                ),
                                width=3
                            ),
                            dbc.Col(
                                id='fire-value',
                                width=3
                            ),
                            dbc.Col(
                                id='fire-cost',
                                width=3
                            ),
                        ],
                        align="center",
                        className="h-50",
                        style={
                            'margin-top': '2px',
                            'margin-bottom': '2px',
                        }
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                width=2
                            ),
                            dbc.Col(
                                width=3
                            ),
                            dbc.Col(
                                width=3
                            ),
                            dbc.Col(
                                id='total-cost',
                                style={
                                    'font-weight': 'bold'
                                },
                                width=3
                            ),
                        ],
                        align="center",
                        className="h-50",
                        style={
                            'margin-top': '2px',
                            'margin-bottom': '2px',
                        }
                    )
                ],
                id='collapse-character',
                is_open=True
            ),
        ],
        
        style={
            'max-width': '800px',
            'min-height': '200px',
            'margin-top':'5px',
            'padding': '4px'
        } 
    ),
    dbc.Row(style={'margin-top': '10px'}),
    dbc.Card(
        [
            dbc.Row(
                dbc.Label(
                    'Guardian Success Rates',
                    style={
                        'font-weight': 'bold',
                        'font-size': '20px'
                    }
                )
            ),
            dbc.Row(
                dbc.Label(
                    'Your Damage: 0',
                    id='player_net_damage',
                    style={
                        'color': 'purple'
                    }
                ),
                style={
                    'margin-top': '10px',
                    'margin-bottom': '10px',
                }
            ),
            dbc.Row(
                [
                    dbc.Col(width=2),
                    dbc.Col(
                        'Guardian HP',
                        style={
                            'font-weight': 'bold',
                            'color': 'green'
                        },
                        width=3
                    ),
                    # dbc.Col(
                    #     'Your Damage',
                    #     style={
                    #         'font-weight': 'bold',
                    #         'color': 'green'
                    #     },
                    #     width=2
                    # ),
                    dbc.Col(
                        'Required Hits',
                        style={
                            'font-weight': 'bold',
                            'color': 'green'
                        },
                        width=3
                    ),
                    dbc.Col(
                        'Odds of Success',
                        style={
                            'font-weight': 'bold',
                            'color': 'green'
                        },
                        width=3
                    ),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        'Guardian 1',
                        width=2
                    ),
                    dbc.Col(
                        id='guardian_hp-1',
                        width=3
                    ),
                    dbc.Col(
                        id='guardian_hits-1',
                        width=3
                    ),
                    dbc.Col(
                        id='guardian_odds-1',
                        width=3
                    ),
                ],  
            ),
            dbc.Row(
                [
                    dbc.Col(
                        'Guardian 2',
                        width=2
                    ),
                    dbc.Col(
                        id='guardian_hp-2',
                        width=3
                    ),
                    dbc.Col(
                        id='guardian_hits-2',
                        width=3
                    ),
                    dbc.Col(
                        id='guardian_odds-2',
                        width=3
                    ),
                ],  
            ),
            dbc.Row(
                [
                    dbc.Col(
                        'Guardian 3',
                        width=2
                    ),
                    dbc.Col(
                        id='guardian_hp-3',
                        width=3
                    ),
                    dbc.Col(
                        id='guardian_hits-3',
                        width=3
                    ),
                    dbc.Col(
                        id='guardian_odds-3',
                        width=3
                    ),
                ],  
            ),
            dbc.Row(
                [
                    dbc.Col(
                        'Guardian 4',
                        width=2
                    ),
                    dbc.Col(
                        id='guardian_hp-4',
                        width=3
                    ),
                    dbc.Col(
                        id='guardian_hits-4',
                        width=3
                    ),
                    dbc.Col(
                        id='guardian_odds-4',
                        width=3
                    ),
                ],  
            ),
            dbc.Row(
                [
                    dbc.Col(
                        'Guardian 5',
                        width=2
                    ),
                    dbc.Col(
                        id='guardian_hp-5',
                        width=3
                    ),
                    dbc.Col(
                        id='guardian_hits-5',
                        width=3
                    ),
                    dbc.Col(
                        id='guardian_odds-5',
                        width=3
                    ),
                ],  
            ),

        ],
        style={
            'max-width': '800px',
            'min-height': '200px',
            'margin-top':'5px',
            'padding': '5px'
        } 
    )

    


])





@callback(
    Output("collapse-character", "is_open"),
    [Input("collapse_button-character", "n_clicks")],
    [State("collapse-character", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open




stat_names = [
    'health', 'damage', 'hit', 'dodge',
    'crit_damage', 'crit_chance',
    'water', 'thunder', 'fire'
]

@callback(
    [[
        Output(f'{stat}-input', 'value') for stat in stat_names
    ]],
    Output('player_cata_data', 'data'),
    Input('call_api', 'n_clicks'),
    State('api_key', 'value')

)
def get_api_data(n, api_key):

    if n > 0:

        player = cata_tools.get_cata_player(api_key)

        out = []
        out.append(player['character-health'])
        out.append(player['character-damage'])
        out.append(player['character-hit'])
        out.append(player['character-dodge'])
        out.append(player['character-crit_damage'])
        out.append(player['character-crit_chance'])
        out.append(player['character-water_damage'])
        out.append(player['character-thunder_damage'])
        out.append(player['character-fire_damage'])

        return out, player
    


@callback(
    [
        [
            Output('health-value', 'children'),
            Output('damage-value', 'children'),
            Output('hit-value', 'children'),
            Output('dodge-value', 'children'),
            Output('crit_damage-value', 'children'),
            Output('crit_chance-value', 'children'),
            Output('water-value', 'children'),
            Output('thunder-value', 'children'),
            Output('fire-value', 'children'),

            Output('health-cost', 'children'),
            Output('damage-cost', 'children'),
            Output('hit-cost', 'children'),
            Output('dodge-cost', 'children'),
            Output('crit_damage-cost', 'children'),
            Output('crit_chance-cost', 'children'),
            Output('water-cost', 'children'),
            Output('thunder-cost', 'children'),
            Output('fire-cost', 'children'),
            Output('total-cost', 'children'),
        ],

        Output('player_net_damage', 'children'),
        Output('guardian_hp-1', 'children'),
        Output('guardian_hp-2', 'children'),
        Output('guardian_hp-3', 'children'),
        Output('guardian_hp-4', 'children'),
        Output('guardian_hp-5', 'children'),

        Output('guardian_hits-1', 'children'),
        Output('guardian_hits-2', 'children'),
        Output('guardian_hits-3', 'children'),
        Output('guardian_hits-4', 'children'),
        Output('guardian_hits-5', 'children'),

        Output('guardian_odds-1', 'children'),
        Output('guardian_odds-2', 'children'),
        Output('guardian_odds-3', 'children'),
        Output('guardian_odds-4', 'children'),
        Output('guardian_odds-5', 'children'),
    ],

    [
        Input('health-input', 'value'),
        Input('damage-input', 'value'),
        Input('hit-input', 'value'),
        Input('dodge-input', 'value'),
        Input('crit_damage-input', 'value'),
        Input('crit_chance-input', 'value'),
        Input('water-input', 'value'),
        Input('thunder-input', 'value'),
        Input('fire-input', 'value'),
        State('player_cata_data', 'data'),
    ],

)
def display_stats(
        player_health,
        player_damage,
        player_hit,
        player_dodge,
        player_crit_damage,
        player_crit_chance,
        player_water_damage,
        player_thunder_damage,
        player_fire_damage,
        player
    ):

    village_boost = sum(
        [.01 + .01*(x // 20) for x in range(player['village-blacksmith'])]
    )

    player_costs = []

    player_costs.append(
        sum([10000 * i for i in range(1, player_health+1)])
    )
    player_costs.append(
        sum([10000 * i for i in range(1, player_damage+1)])
    )
    player_costs.append(
        sum([10000 * i for i in range(1, player_hit+1)])
    )
    player_costs.append(
        sum([10000 * i for i in range(1, player_dodge+1)])
    )
    player_costs.append(
        sum([10000 * i for i in range(1, player_crit_damage+1)])
    )
    player_costs.append(
        sum([10000 * i for i in range(1, player_crit_chance+1)])
    )
    player_costs.append(
        sum([10000 * i for i in range(1, player_water_damage+1)])
    )
    player_costs.append(
        sum([10000 * i for i in range(1, player_thunder_damage+1)])
    )
    player_costs.append(
        sum([10000 * i for i in range(1, player_fire_damage+1)])
    )
    player_costs.append(sum(player_costs))



    player_health = player_health*300 + 1000
    player_damage = player_damage*20 + 40
    player_hit = player_hit*50 + 100
    player_dodge= player_dodge*50 + 100
    player_crit_damage = player_crit_damage*.0025
    player_crit_chance = player_crit_chance*.0025
    player_water_damage = player_water_damage*20
    player_thunder_damage = player_thunder_damage*20
    player_fire_damage = player_fire_damage*20

    out = []

    out.append(
        
        player_health * ( 
            1 + village_boost \
            + (player['banner-character_multiplier'] * .00535 ) \
            + (player['tomes-character_multiplier'] / 10000 ) \
            + (player['relic-catacombs_health'] / 10000 )
        ) * (
            1 + (player['guardian-health_upgrades'] / 100 )
        )
    )

    out.append(
        player_damage * ( 
            1 + village_boost \
            + (player['banner-character_multiplier'] * .00535 ) \
            + (player['tomes-character_multiplier'] / 10000 ) \
            + (player['relic-catacombs_damage'] / 10000 )
        ) * (
            1 + (player['guardian-damage_upgrades'] / 100 )
        )
    )

    out.append(
        player_hit * ( 
            1 + village_boost \
            + (player['banner-character_multiplier'] * .00535 ) \
            + (player['tomes-character_multiplier'] / 10000 ) \
            + (player['relic-catacombs_hit'] / 10000 )
        ) * (
            1 + (player['guardian-hit_upgrades'] / 100 )
        )
    )

    out.append(
        player_dodge * ( 
            1 + village_boost \
            + (player['banner-character_multiplier'] * .00535 ) \
            + (player['tomes-character_multiplier'] / 10000 ) \
            + (player['relic-catacombs_dodge'] / 10000 )
        ) * (
            1 + (player['guardian-dodge_upgrades'] / 100 )
        )
    )

    out.append(
        player_crit_damage * ( 
            1 + village_boost \
            + (player['banner-character_multiplier'] * .00535 ) \
            + (player['tomes-character_multiplier'] / 10000 ) \
        ) * (
            1 + (player['guardian-crit_damage_upgrades'] / 100 )
        )
    )

    out.append(
        player_crit_chance * ( 
            1 + village_boost \
            + (player['banner-character_multiplier'] * .00535 ) \
            + (player['tomes-character_multiplier'] / 10000 ) \
        ) * (
            1 + (player['guardian-crit_chance_upgrades'] / 100 )
        )
    )

    out.append(
        player_water_damage * ( 
            1 + village_boost \
            + (player['banner-character_multiplier'] * .00535 ) \
            + (player['tomes-character_multiplier'] / 10000 ) \
            + (player['relic-catacombs_elemental'] / 10000 )
        ) 
    )

    out.append(
        player_thunder_damage * ( 
            1 + village_boost \
            + (player['banner-character_multiplier'] * .00535 ) \
            + (player['tomes-character_multiplier'] / 10000 ) \
            + (player['relic-catacombs_elemental'] / 10000 )
        ) 
    )

    out.append(
        player_fire_damage * ( 
            1 + village_boost \
            + (player['banner-character_multiplier'] * .00535 ) \
            + (player['tomes-character_multiplier'] / 10000 ) \
            + (player['relic-catacombs_elemental'] / 10000 )
        ) 
    )

    player_net_values = [f"{x:,.2f}" for x in out]
    
    player_cost_labels = [f"{x:,}" for x in player_costs]

    player_net_damage = out[1] + out[6] + out[7] + out[8]
    player_net_damage*=out[4]
    player_net_damage*=int(out[5])
    player_net_damage+= (out[1] + out[6] + out[7] + out[8])


    player_mob_debuff = (player['banner-mob_multiplier'] * .00325 ) \
            + (player['tomes-mob_multiplier'] / 10000 ) \

    guardian_levels = [
        50,
        200,
        500,
        1000,
        1500
    ]

    guardian_hps = []
    required_hits = []
    success_odds = []


    for level in guardian_levels:

        guardian_hp = (300*level + 300*(level**1.65))/(1+player_mob_debuff)
        guardian_dodge = (20*level + 20*(level**1.65))/(1+player_mob_debuff)
        guardian_crit = (.001*level + .001*(level**1.65))/(1+player_mob_debuff)
        # print(guardian_dodge)
        # print(player_hit)

        guardian_hps.append(
            f"{guardian_hp:,.0f}"
        )

        required_hits.append(
            guardian_hp//player_net_damage+1
        )

        dodge_chance = 1-guardian_dodge/(guardian_dodge+out[3])
        hit_chance = (out[2]/(guardian_dodge+out[2]))


        success_odds.append(
            (dodge_chance*hit_chance)**(guardian_hp//player_net_damage+1)
        )

    
    

    return player_net_values + player_cost_labels, \
        f"Your Damage: {player_net_damage:,.2f}", \
        \
        guardian_hps[0], \
        guardian_hps[1], \
        guardian_hps[2], \
        guardian_hps[3], \
        guardian_hps[4], \
        \
        required_hits[0], \
        required_hits[1], \
        required_hits[2], \
        required_hits[3], \
        required_hits[4], \
        \
        f"{success_odds[0]*100:,.6f}%", \
        f"{success_odds[1]*100:,.6f}%", \
        f"{success_odds[2]*100:,.6f}%", \
        f"{success_odds[3]*100:,.6f}%", \
        f"{success_odds[4]*100:,.6f}%", \

        
        


        
    