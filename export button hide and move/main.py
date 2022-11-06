from distutils.log import debug
import os
import pandas as pd
import dash_table
import dash
import dash_html_components as html
from dash.dependencies import Input, Output


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/solar.csv"
)
app = dash.Dash(__name__)
app.layout = html.Div([
    # html.Button("Custom export", id="export_table"),
    dash_table.DataTable(
        id="table_to_export",
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        export_format="xlsx",
        export_headers="display",
        ),
    ])

# app.clientside_callback(
#     """
#     function(n_clicks) {
#         if (n_clicks > 0)
#             document.querySelector("#table_to_export button.export").click()
#         return ""
#     }
#     """,
#     Output("export_table", "data-dummy"),
#     [Input("export_table", "n_clicks")]
# )

if __name__ == "__main__":
    app.run_server(debug=True)
