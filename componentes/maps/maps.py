from dash import html , dcc
#import plotly.graph_objects as go
import plotly.express as px
#import geopandas
import pandas as pd

class Maps_colombia:
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