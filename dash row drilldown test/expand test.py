from distutils.log import debug
import dash
from dash import html,dcc,Input,Output,State
from dash.dash_table import DataTable
import dash_bootstrap_components as dbc
import pandas as pd

app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

df=pd.read_csv(r'C:\Users\venkat\Downloads\Book1.csv')
df.sort_values(by=['Category','Sub Category'],inplace=True)
df_grp=df.groupby('Category',as_index=False)['Sales'].sum()

print(df_grp)

app.layout=html.Div([
    html.Div(html.H6('Expandable collapse test',style={'text-align':'center'})),
    html.Hr(),
    DataTable()
])