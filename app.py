"""
This top portion allows for the app_tools to be 
imported to all files in the /pages/ dir
"""
from pathlib import Path
import sys

# Get path to this module
script_dir = Path( __file__ ).parent
if not any("cata_tools" in p for p in sys.path):
    utils_path = script_dir.joinpath( '..', 'cata_tools' )
    sys.path.append(str(utils_path))


# from apscheduler.schedulers.background import BackgroundScheduler

from dash import Dash, html, dcc
from dash.dependencies import Output, Input, State, ALL
import dash_bootstrap_components as dbc
import dash




app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.CYBORG, dbc.icons.BOOTSTRAP],
    use_pages=True
)




app.title = 'Queslar Tools'

server=app.server


navbar = dbc.Navbar([
    # dbc.DropdownMenu(
    #         children=[
    #             dbc.DropdownMenuItem("Guardians", href='/playoffs'),
    #             dbc.DropdownMenuItem("Final Standings", href='/standings'),
    #             dbc.DropdownMenuItem("Draft Results", href="/drafts"),
    #             dbc.DropdownMenuItem("Regular Season", href="/matchups"),
    #             dbc.DropdownMenuItem("DMB Podcast", href="/podcasts"),
    #             dbc.DropdownMenuItem("Transactions", href="/transactions"),
    #         ],
    #         nav=True,
    #         in_navbar=True,
    #         label="Menu",
    #     ),
    dbc.NavbarBrand(
        "Queslar Sim Tools",
        href="/#",
        # class_name="ms-2",
    ),
],
    # color="dark",
    dark=True,
)


app.layout = html.Div([
	navbar,
	dash.page_container,
])





# sched = BackgroundScheduler(daemon=True)
# sched.add_job(refresh_API_Calls,'interval',seconds=20)
# sched.start()



if __name__ == '__main__':

    
    app.run_server(debug=True)