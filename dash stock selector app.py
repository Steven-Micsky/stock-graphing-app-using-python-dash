import dash
import dash_core_components as dcc
import dash_html_components as html
from iexfinance.stocks import get_historical_data
import datetime
from dateutil.relativedelta import relativedelta
import plotly.graph_objs as go
from dash.dependencies import Input, Output


app = dash.Dash()

app.layout = html.Div(children=[
    html.Div(children="Symbol to graph: "),
    dcc.Input(id='input',value="",type="text"),
    html.Div(id="output-graph"),
])

@app.callback(
    Output(component_id="output-graph",component_property="children"),
    [Input(component_id="input",component_property="value")]
)

def update_value(input_data):
    start = datetime.datetime.today() - relativedelta(years=5)
    end = datetime.datetime.today()
    df = get_historical_data(input_data, start=start, end=end, output_format="pandas")

    return dcc.Graph(
        id="stock-graph",
        figure={
            'data': [
                {'x':df.index,'y':df.close,'type':'line','name':input_data},
                ],
        'layout': {
            'title':input_data
        }

        }
    )


if __name__== "__main__":
    app.run_server(debug=True)