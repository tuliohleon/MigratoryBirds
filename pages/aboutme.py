from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page
from dash import dcc
register_page(__name__,order=0, path="/aboutme")

layout=  dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                html.Img(src='assets/Tulio.png'),
                dcc.Markdown('''**Tulio Hernán León Daza**, Ingeniero Físico, [linkedIn](http://www.linkedin.com/in/tulio-hernán-leon-daza-30511548)'''),
            ])
        ])

    ],style={'textAlign': 'center'},
    fluid=True,)