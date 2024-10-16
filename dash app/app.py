from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output
import plotly.express as px
from mpg import *

app = Dash()  # Initial the app

# Build the layout
app.layout = [
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.origin.unique(), 'USA', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]

# Callbacks
@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.origin==value]
    fig = px.scatter(dff, x = "horsepower", y = "mpg", color="origin",
           title= "Correlation between MPG Horsepower",
                   labels={"cylinders" : "Cylinders", "mpg" : "MPG"}, 
                   template="simple_white")
    return fig

if __name__ == '__main__':
    app.run(debug=True)
