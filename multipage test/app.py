from distutils.log import debug
import dash
from dash import dcc,html,Output,Input,State
import dash_bootstrap_components as dbc

app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],use_pages=True)

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

# sidebar=dbc.Nav([

#     dbc.NavLink([
#         html.Div(page['name'],className='ms-2')
#     ],href=page['path'],active='exact') for page in dash.page_registry.values()

# ],vertical=True,pills=True)

navbar=dbc.Navbar([

    dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Navbar", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),

    dbc.DropdownMenu([

        dbc.DropdownMenuItem([
            page['name']
        ],href=page['path'],active='exact') for page in dash.page_registry.values()

    ],label='Pages')
],color='primary',dark=True)#,brand='Multipage app w/ dash',brand_href='#',color='primary',dark=True)

# html.Div(
#         [
#             html.Div(
#                 dcc.Link(
#                     f"{page['name']} - {page['path']}", href=page["relative_path"]
#                 )
#             )
#             for page in dash.page_registry.values()
#         ]
#     )

# offcanvas = html.Div([
#         dbc.Button("Open Offcanvas", id="open-offcanvas", n_clicks=0),
#         dbc.Offcanvas([
#             dbc.NavLink([
#         html.Div(page['name'],className='ms-2')
#     ],href=page['path'],active='exact') for page in dash.page_registry.values(),
#             id="offcanvas",
#             title="Title",
#             is_open=False,
#         ])
# ])

app.layout=dbc.Container([
    dbc.Row([
        navbar
    ]),
    dbc.Row([
        dbc.Col([
            dash.page_container
        ],xs=8,sm=8,md=10,xl=10,xxl=10)
    ])
],fluid=True)

# @app.callback(
#     Output("offcanvas", "is_open"),
#     Input("open-offcanvas", "n_clicks"),
#     [State("offcanvas", "is_open")],
# )
# def toggle_offcanvas(n1, is_open):
#     if n1:
#         return not is_open
#     return is_open

if __name__=='__main__':
    app.run_server(debug=True)