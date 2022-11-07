from distutils.log import debug
import dash
from dash import dcc,html,Output,Input
import dash_bootstrap_components as dbc
import plotly.express as px

app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar=dbc.NavbarSimple([
    dbc.NavItem(dbc.NavLink('Page1',href='/Page1',active='exact')),
    dbc.NavItem(dbc.NavLink('Page2',href='/Page2',active='exact')),
    dbc.NavItem(dbc.NavLink('Page3',href='/Page3',active='exact')),
    dbc.DropdownMenu([
        dbc.DropdownMenuItem('Page4',href='/Page4'),
        dbc.DropdownMenuItem('Page5',href='/Page5'),
        dbc.DropdownMenuItem('Page6',href='/Page6')
    ],label='More Pages',nav=True,in_navbar=True)
],brand='NavbarSimple',brand_href='/',color='primary',dark=True)

app.layout=dbc.Container([
    dbc.Row([
        navbar
    ])
])

if __name__=='__main__':
    app.run_server(debug=True)