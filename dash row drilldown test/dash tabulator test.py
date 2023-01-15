import dash_tabulator
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import plotly_express as px
import dash_core_components as dcc
import pandas as pd


external_scripts = ["https://oss.sheetjs.com/sheetjs/xlsx.full.min.js"]
external_stylesheets = [
    "https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
]
app = dash.Dash(
    __name__,
    external_scripts=external_scripts,
    external_stylesheets=external_stylesheets,
)

styles = {"pre": {"border": "thin lightgrey solid", "overflowX": "scroll"}}

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv"
)

# This adds an "id" column
df = df.reset_index().rename(columns={"index": "id"})

data = df.to_dict("records")

columns = [
    {"title": "Year", "field": "year", "hozAlign": "left", "headerFilter": True},
    {"title": "Continent", "field": "continent", "hozAlign": "left", "headerFilter": True,},
    {"title": "Country", "field": "country", "hozAlign": "left", "headerFilter": True},
    {
        "title": "Population",
        "field": "pop",
        "formatter": "money",
        "formatterParams": {"precision": 0},
        "topCalc": "avg",
        "topCalcParams": {"precision": 0},
        "topCalcFormatter": "money",
        "topCalcFormatterParams": {"precision": 0},
        "hozAlign": "right",
    },
    {
        "title": "Life Expectancy",
        "field": "lifeExp",
        "hozAlign": "right",
        "formatter": "money",
        "formatterParams": {"precision": 1},
        "topCalc": "avg",
        "topCalcParams": {"precision": 1},
    },
    {
        "title": "GDP Per Capita",
        "field": "gdpPercap",
        "hozAlign": "right",
        "formatter": "money",
        "formatterParams": {"precision": 2},
        "topCalc": "avg",
        "topCalcParams": {"precision": 2},
        "topCalcFormatter": "money",
        "topCalcFormatterParams": {"precision": 2},
    },
]

# Note:  With  large datasets, it's necessary to set the maxHeight for the table otherwise the app will be slow.
#        See more info here:  http://tabulator.info/docs/4.8/virtual-dom
options = {"groupBy": "country", "selectable": 1, "maxHeight": "500px"}
downloadButtonType = {"css": "btn btn-primary", "text": "Export", "type": "xlsx"}
clearFilterButtonType = {"css": "btn btn-outline-dark", "text": "Clear Filters"}

app.layout = html.Div(
    [
        dash_tabulator.DashTabulator(
            id="table",
            columns=columns,
            data=data,
            options=options,
            downloadButtonType=downloadButtonType,
            clearFilterButtonType=clearFilterButtonType,
        ),

    ], 
)





if __name__ == "__main__":
    app.run_server(debug=True)