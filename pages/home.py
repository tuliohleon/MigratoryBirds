import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

register_page(__name__,order=0, path="/")

from model import df_birds
from components.maps.mapsCol import MapColombia

#mapa_chia_sectores = mapchia_emergencias('2021 Emergencias totales en Chía por sectores', 'id_figura_mapa_chia',df_emergencias, None)
mapColombia = MapColombia()
layout=  dbc.Container(
    [])  