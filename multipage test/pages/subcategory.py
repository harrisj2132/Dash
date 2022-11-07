import dash
from dash import dcc,html,Output,Input
import dash_bootstrap_components as dbc
from data import datasets as ds
import plotly.express as px

dash.register_page(__name__)

layout=html.Div([
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id='subcatdrop',options=ds.df_subcat['Sub-Category']),
            dcc.Graph(id='subcatchart',figure=px.line(ds.df_subcat,x='Sub-Category',y='Sales',line_shape='spline'))
        ],width=12)
    ])
])