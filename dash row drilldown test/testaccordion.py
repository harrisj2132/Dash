import dash
from dash import html,dcc,Input,Output,State
from dash.dash_table import DataTable
import dash_bootstrap_components as dbc
import pandas as pd

data = [
	{
		'id': '001',
		'company': 'XYZ pvt ltd',
		'location': 'London',
		'info': {
			'president': 'Rakesh Kapoor',
			'contacts': {
					'email': 'contact@xyz.com',
					'tel': '9876543210'
			}
		}
	},
	{
		'id': '002',
		'company': 'PQR Associates',
		'location': 'Abu Dhabi',
		'info': {
			'president': 'Neelam Subramaniyam',
			'contacts': {
					'email': 'contact@pqr.com',
					'tel': '8876443210'
			}
		}
	}
]

df=pd.DataFrame(data)

app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout=html.Div([
    DataTable(id='table1',data=df.to_dict('records'))
])

if __name__=='__main__':
    app.run_server(debug=True)