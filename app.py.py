
import pandas as pd 
import dash 
import dash_html_components as html
import webbrowser
from dash.dependencies import Input, State, Output
import plotly.graph_objects as go

import dash_core_components as dcc

app = dash.Dash()

def load_data():
      df = pd.read_csv('C:\\Users\\Sahaj\\Desktop\\forks\\global_terror.csv')   
      print(df.sample(5))
def open_webbrowser():
    webbrowser.open_new('http://127.0.0.1:8050/')

def create_app_ui():
    main_layout = html.Div( 
    [  
    html.H1(id='Main_title', children='Terrorism Analysis with Insights'),    
    html.Button(id='button_close',children='close', n_clicks=0),
    html.Hr(),
    dcc.Dropdown(id='dropdown-1',
        options = [{'label':'Bar', 'value':'Bar'},{'label':'Line', 'value':'Line'}],
        value ='Line'
    ),
    dcc.Graph(id='graph-object')
    
    ]
    )
    
    
    return  main_layout

@app.callback(
     dash.dependencies.Output('button_close','children'),
     [
      dash.dependencies.Input('button_close','n_clicks')
    ]
    )

def update_app_ui(n_clicks):
    print("value passed is=", str(n_clicks))

    if (n_clicks > 0):
        return"i clicked = " + str(n_clicks)
    else:
        return"Click To Text"

@app.callback(
    dash.dependencies.Output('graph-object','figure'),
    [ 
    dash.dependencies.Input('dropdown-1','value')
    ]
    )
def update_app_ui(dd_value):
    print("Data type of dd_value =",str(type(dd_value)))
    print("value of dd_value =",str(dd_value))

    figure = go.Figure()
    return figure 

    if(dd_value =='Bar'):
        print("A bar graph")
    elif(dd_value =='Line'):
        print("A line Graph")
    else:
        print("nothing is selected")

def main():
    print("welcome to project")
    
    load_data()
    open_webbrowser()
    
    global app
    app.layout = create_app_ui()
    app.title = "Terrorism Analysis with Insights"
    app.run_server()
    
    print("Thanks for using my project")
if __name__ == '__main__':
    main()