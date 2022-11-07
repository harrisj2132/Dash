from distutils.log import debug
import dash
from dash import dcc,html,Output,Input,State
import dash_bootstrap_components as dbc

app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

offcanvas = html.Div(
    [
        dbc.Button("Open Offcanvas", id="open-offcanvas", n_clicks=0),
        dbc.Offcanvas(
            html.P(
                "This is the content of the Offcanvas. "
            ),
            id="offcanvas",
            title="Title",
            is_open=False,
        ),
    ]
)

app.layout=html.Div([
    
        offcanvas
    
])

@app.callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas", "n_clicks"),
    [State("offcanvas", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open

if __name__=='__main__':
    app.run_server(debug=True)