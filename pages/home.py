import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

register_page(__name__,order=0, path="/")

layout=  dbc.Container(
    [])  