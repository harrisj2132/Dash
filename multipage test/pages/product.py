import dash
from dash import dcc,html,Output,Input
import dash_bootstrap_components as dbc
from data import datasets as ds
import plotly.express as px

dash.register_page(__name__)

layout=html.Div([
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id='proddrop',options=ds.df_prod['Product Name']),
            dcc.Graph(id='prodchart',figure=px.line(ds.df_prod,x='Product Name',y='Sales',line_shape='hvh'))
        ],width=12)
    ])
])