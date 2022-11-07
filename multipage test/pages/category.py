from msilib.schema import Icon
import dash
from dash import dcc,html,Output,Input
import dash_bootstrap_components as dbc
from data import datasets as ds
import plotly.express as px

dash.register_page(__name__,path='/',icon="fa fa-line-chart")

layout=html.Div([
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id='catdrop',options=ds.df_cat['Category']),
            dcc.Graph(id='catchart',figure=px.line(ds.df_cat,x='Category',y='Sales',line_shape='spline'))
        ],width=12)
    ])
])