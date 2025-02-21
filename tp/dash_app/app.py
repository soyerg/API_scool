import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import requests
import pandas as pd
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Retry mechanism to wait for the FastAPI service
max_retries = 5
retry_delay = 5
for attempt in range(max_retries):
    try:
        # Fetch data from the FastAPI
        response = requests.get('http://api:5000/schools/')
        response.raise_for_status()
        data = response.json()

        # Convert the data to a pandas DataFrame
        df = pd.DataFrame(data)
        logger.info(f"Fetched data: {df.head()}")
        break
    except Exception as e:
        logger.error(f"Error fetching data from API: {e}")
        if attempt < max_retries - 1:
            time.sleep(retry_delay)
        else:
            df = pd.DataFrame()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(children=[
    html.H1(children='Distribution of IPS Values'),

    dcc.Graph(
        id='ips-histogram',
        figure={
            'data': [
                {'x': df.get('ips', []), 'type': 'histogram', 'name': 'IPS'},
            ],
            'layout': {
                'title': 'Distribution of IPS Values'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
