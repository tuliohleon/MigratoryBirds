from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

register_page(__name__,order=0, path="/")

from components.sampledf.model import df_birds
from components.maps.mapsCol import MapColombia
from components.markdown.markformat import markformat


file1 = open('./data/md/story1.md')

texto1  = markformat('Citizenship', file1.read())

mapColombia = MapColombia('Ocurrence 2021' , 'id_figure_map_colombia', df_birds, None)
layout=  dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                html.H2("Mapa de Usuarios Registrados", className='title ml-2'),
        ])
    ]),


        dbc.Row([
            dbc.Col([
                mapColombia.display()
        ]),
        #dbc.Col(["hola"], lg=4),
        dbc.Col([texto1], lg=4),
    ]),

    ])  