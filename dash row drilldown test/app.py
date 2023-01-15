from distutils.log import debug
import dash
from dash import html,dcc,Input,Output,State
from dash.dash_table import DataTable
import dash_bootstrap_components as dbc
import pandas as pd
from scipy.fftpack import diff

df=pd.read_csv(r'C:\Users\venkat\Downloads\Book1.csv')
df_grp=df.groupby('Category',as_index=False)['Sales'].sum()
test_df=df_grp.append(df,sort=True,ignore_index=True).sort_values('Category')[['Category','Sub Category','Sales']]
# print(df)
# print(df_grp)

app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

modal = html.Div(
    [
        dbc.Button("Open modal", id="open", n_clicks=0),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Header")),
                dbc.ModalBody(DataTable(id='table2',data=df.to_dict('records'),columns=[{'name':col,'id':col,'selectable':True} for col in df.columns])),
                dbc.ModalFooter(
                    dbc.Button(
                        "Close", id="close", className="ms-auto", n_clicks=0
                    )
                ),
            ],
            id="modal",
            is_open=False,
        ),
    ]
)


app.layout=html.Div([
        DataTable(id='table1',data=test_df.to_dict('records')),
        # DataTable(id='table2',data=df.to_dict('records')),
        modal
])


@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

# @app.callback(Output('table1','data'),Input('table1','active_cell'))
# def update_table(selected):
#     if selected is None:
#         return df_grp.to_dict('records')
#     else:
#         selected_value=df_grp.at[selected['row'],selected['column_id']]
#         dff=df[df['Category']==selected_value]
#         print(dff)
#         return dff.to_dict('records')



if __name__=='__main__':
    app.run_server(debug=True)







# collapse = html.Div(
#     [
#         dbc.Button(
#             "expand all rows",
#             id="collapse-button",
#             className="mb-3",
#             color="primary",
#             n_clicks=0,
#         ),
#         # dbc.Collapse(
#         #     DataTable(id='table2',data=df.to_dict('records'),columns=[{'name':col,'id':col,'selectable':True} for col in df.columns]),
#         #     id="collapse",
#         #     is_open=False,
#         # ),
#     ]
# )
# modal = html.Div(
#     [
#         dbc.Button("Open modal", id="open", n_clicks=0),
#         dbc.Modal(
#             [
#                 dbc.ModalHeader(dbc.ModalTitle("Header")),
#                 dbc.ModalBody(DataTable(id='table2',data=df.to_dict('records'),columns=[{'name':col,'id':col,'selectable':True} for col in df.columns])),
#                 dbc.ModalFooter(
#                     dbc.Button(
#                         "Close", id="close", className="ms-auto", n_clicks=0
#                     )
#                 ),
#             ],
#             id="modal",
#             is_open=False,
#         ),
#     ]
# )




# @app.callback(
#     Output("modal", "is_open"),
#     [Input("open", "n_clicks"), Input("close", "n_clicks")],
#     [State("modal", "is_open")],
# )
# def toggle_modal(n1, n2, is_open):
#     if n1 or n2:
#         return not is_open
#     return is_open

# @app.callback(
#     Output("collapse", "is_open"),
#     [Input("collapse-button", "n_clicks")],
#     [State("collapse", "is_open")],
# )
# def toggle_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open