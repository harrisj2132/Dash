from distutils.log import debug
import dash
from dash import html,dcc,Input,Output,State
from dash.dash_table import DataTable
import dash_bootstrap_components as dbc
import pandas as pd

app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

def defineDF():
    df = pd.DataFrame({'Country': ['USA', 'China', 'China', 'USA', 'France'],
                   'City': ['New-York', 'Shanghai', 'Beijing', 'Los Angeles', 'Paris'],
                   'Population': [19, 26, 20, 12, 11],
                   'Other': [5, 3, 4, 11, 43]})
    df.sort_values(by=['Country', 'City'], inplace=True)
    return df

def baseDF():
    df = pd.DataFrame({'Country': ['USA', 'China', 'China', 'USA', 'France'],
                   'City': ['New-York', 'Shanghai', 'Beijing', 'Los Angeles', 'Paris'],
                   'Population': [19, 26, 20, 12, 11],
                   'Other': [5, 3, 4, 11, 43]})
    df.sort_values(by=['Country', 'City'], inplace=True)
    f = {'Population': 'sum', 'Other': 'sum'}
    cols = ['Country']
    return df.groupby(cols).agg(f).reset_index()

startDF = baseDF()

app.layout = html.Div([
    html.Div(html.H6("Country/City population"), style={"text-align":"center"}),
    html.Hr(),
    DataTable(
        id='table',
        columns=[{'name': i, 'id': i} for i in startDF.columns],
        data = startDF.to_dict('records'),
        selected_rows=[],
    )
])

@app.callback([
Output('table', 'data'),
Output('table', 'columns')
],
[
    Input('table', 'active_cell')
],
[
    State('table', 'data'),
    State('table', 'columns')
],
)
def updateGrouping(active_cell, power_position, power_position_cols):
    if active_cell is None:
        returndf = baseDF()
    elif active_cell['column'] == 0:
        returndf = defineDF()
    else:
        returndf = baseDF()

    cols = [{'name': i, 'id': i} for i in returndf.columns]

    return [returndf.to_dict('records'), cols]
    

if __name__=='__main__':
    app.run_server(debug=True)