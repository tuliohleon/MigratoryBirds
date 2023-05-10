from dash import html , dcc
import plotly.express as px
import pandas as pd

class MapColombia:
    """A clas to represent the maps of Colombia
    """
    def __init__(self,map_title:str, ID:str,df,animation):
        """__init__ _summary_

        Args:
            map_title (str): Titulo del mapa, html H4 element
            ID (str): css id to use with callbacks
            df (_type_): dataframe with info to use in choropleth
            markers (_type_): small point as overlay in map
        """        
        self.map_title = map_title 
        self.id = ID
        self.df = df
        self.animation = animation #None, 'MES', 'MARKERS','USUARIOS',PRON

    #@staticmethod
    def figura(self):
        
        if self.animation == None:
            df=self.df
        
            week_orders=[]
            for i in range(53):
                week_orders.append(i)
            

            fig = px.density_mapbox(
                df,
                lat='decimalLatitude',
                lon='decimalLongitude',
                z='individualCount',
                radius=10,
                center=dict(lat=4.862437, lon=-74.058655),
                zoom=3.8,
                mapbox_style="carto-positron",
                animation_frame="week",
                category_orders={"week": week_orders},
                color_continuous_scale="viridis", 
                labels={'individualCount': 'Count'},            
               )
        
        annotations = [dict(
        showarrow=False,
        align="right",
        text="",
        font=dict(color="#000000"),
        bgcolor="#f9f9f9",
        x=0.95,
        y=0.95,
        )]   


        fig.update_layout(
        geo_scope='south america',
        annotations=annotations,
        height=400,
        width=500,
        margin={"r":0,"t":0,"l":0,"b":0}
        ),
               
        return fig

    def display(self):
           layout = html.Div(
            [
                html.H4([self.map_title]),
                html.Div([
                    dcc.Graph(figure=MapColombia.figura(self), id=self.id)
                ])
                
            ]
        )
           return layout                       
