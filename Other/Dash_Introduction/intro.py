import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)





app = Dash(__name__)

# -- Import and clean data (importing csv into pandas)
# df = pd.read_csv("intro_bees.csv")
df = pd.read_csv("intro_bees.csv")

df = df.groupby(['State', 'ANSI', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)
#print(df[:5])

# ------------------------------------------------------------------------------
# App layout
    #dash components go in here, as well as any html
        #to see where he got this from, go to dash plotly website, search dropdown examples and reference
            #https://dash.plotly.com
app.layout = html.Div([

    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}), #title of webpage

    # dcc.Dropdown(id="slct_year",
    #              options=[
    #                  {"label": "2015", "value": 2015}, #user actually sees the label, value is what the code uses
    #                  {"label": "2016", "value": 2016},
    #                  {"label": "2017", "value": 2017},
    #                  {"label": "2018", "value": 2018}],
    #              multi=False, #for other dropdowns, there would be different parameters
    #              value=2015,
    #              style={'width': "40%"}
    #              ),

    dcc.Dropdown(id="slct_disease",
                 options=[
                     {"label": "Disease", "value": 'Disease'}, 
                     {"label": "Pesticides", "value": 'Pesticides'},
                     {"label": "Pests (except Varroa Mites)", "value": 'Pests_excl_Varroa'},
                     {"label": "Unknown", "value": 'Unknown'},
                     {"label": "Varroa Mites", "value": 'Varroa_mites'},
                     {"label": "Other", "value": 'Other'}],
                 multi=False, 
                 value='Varroa_mites',
                 style={'width': "40%"}
                 ),

     dcc.Dropdown(id="slct_state",
                 options=[
                    {'label' : 'Alabama', 'value' : 'Alabama'},
                    {'label' : 'Arizona', 'value' : 'Arizona'},
                    {'label' : 'Arkansas', 'value' : 'Arkansas'},
                    {'label' : 'California', 'value' : 'California'},
                    {'label' : 'Colorado', 'value' : 'Colorado'},
                    {'label' : 'Connecticut', 'value' : 'Connecticut'},
                    {'label' : 'Florida', 'value' : 'Florida'},
                    {'label' : 'Georgia', 'value' : 'Georgia'},
                    {'label' : 'Hawaii', 'value' : 'Hawaii'},
                    {'label' : 'Idaho', 'value' : 'Idaho'},
                    {'label' : 'Illinois', 'value' : 'Illinois'},
                    {'label' : 'Indiana', 'value' : 'Indiana'},
                    {'label' : 'Iowa', 'value' : 'Iowa'},
                    {'label' : 'Kansas', 'value' : 'Kansas'},
                    {'label' : 'Kentucky', 'value' : 'Kentucky'},
                    {'label' : 'Louisiana', 'value' : 'Louisiana'},
                    {'label' : 'Maine', 'value' : 'Maine'},
                    {'label' : 'Maryland', 'value' : 'Maryland'},
                    {'label' : 'Massachusetts', 'value' : 'Massachusetts'},
                    {'label' : 'Michigan', 'value' : 'Michigan'},
                    {'label' : 'Minnesota', 'value' : 'Minnesota'},
                    {'label' : 'Mississippi', 'value' : 'Mississippi'},
                    {'label' : 'Missouri', 'value' : 'Missouri'},
                    {'label' : 'Montana', 'value' : 'Montana'},
                    {'label' : 'Nebraska', 'value' : 'Nebraska'},
                    {'label' : 'New Jersey', 'value' : 'New Jersey'},
                    {'label' : 'New Mexico', 'value' : 'New Mexico'},
                    {'label' : 'New York', 'value' : 'New York'},
                    {'label' : 'North Carolina', 'value' : 'North Carolina'},
                    {'label' : 'North Dakota', 'value' : 'North Dakota'},
                    {'label' : 'Ohio', 'value' : 'Ohio'},
                    {'label' : 'Oklahoma', 'value' : 'Oklahoma'},
                    {'label' : 'Oregon', 'value' : 'Oregon'},
                    {'label' : 'Pennsylvania', 'value' : 'Pennsylvania'},
                    {'label' : 'South Carolina', 'value' : 'South Carolina'},
                    {'label' : 'South Dakota', 'value' : 'South Dakota'},
                    {'label' : 'Tennessee', 'value' : 'Tennessee'},
                    {'label' : 'Texas', 'value' : 'Texas'},
                    {'label' : 'Utah', 'value' : 'Utah'},
                    {'label' : 'Vermont', 'value' : 'Vermont'},
                    {'label' : 'Virginia', 'value' : 'Virginia'},
                    {'label' : 'Washington', 'value' : 'Washington'},
                    {'label' : 'West Virginia', 'value' : 'West Virginia'},
                    {'label' : 'Wisconsin', 'value' : 'Wisconsin'},
                    {'label' : 'Wyoming', 'value' : 'Wyoming'}],
                 multi=True, 
                 value=['Texas', 'California', 'Hawaii'],
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]), #nothing is in the children spot yet
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={}) #later, we will put figure code in the figure spot. Has an id tho 

])

#if we commented out what is inbetween these two lines -----, then we would still have an interactive webpage, but no data in the plot

# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback( #connect compenents with graph
    [Output(component_id='output_container', component_property='children'), #two outputs, one the children out the output container, and also the figure of the compenent id my_bee_map
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_disease', component_property='value'),
    Input(component_id='slct_state', component_property='value')]
)
#under each callback, you need a function that updates something
    #for every input, you need an argument

def update_graph(option_slctd, option_slctd_b): #this argument refers to the component_property value in the callback inpput
    print(option_slctd)
    print(type(option_slctd))

    container = "The disease chosen by user was: {}".format(option_slctd)

    # dff = df.copy()
    # dff = dff[dff["Year"] == option_slctd]
    # dff = dff[dff["Affected by"] == "Varroa_mites"]

    #Challenge A: Bar Chart
    # fig = px.bar(
    #     data_frame=dff,
    #     x = 'State',
    #     y='Pct of Colonies Impacted',
    #     template = 'plotly_dark'
    # )

    #Challenge B: Line Chart

    dff = df.copy()
    dff = dff[dff["Affected by"] == option_slctd]
    dff = dff[dff['State'].isin(option_slctd_b)]
    # options1 = ['Texas', 'California', 'Hawaii']
    # dff = dff[dff.State.isin(options1)]

    fig = px.line(
        data_frame=dff,
        x = 'Year',
        y = 'Pct of Colonies Impacted',
        color = 'State',
        title = "Bee Colonies Impacted by Disease and State",
        template = 'plotly_dark'    
    )

    # Plotly Express
    # fig = px.choropleth(
    #     data_frame=dff,
    #     locationmode='USA-states',
    #     locations='state_code',
    #     scope="usa",
    #     color='Pct of Colonies Impacted',
    #     hover_data=['State', 'Pct of Colonies Impacted'],
    #     color_continuous_scale=px.colors.sequential.YlOrRd,
    #     labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
    #     template='plotly_dark'
    # )

    # Plotly Graph Objects (GO)
    # fig = go.Figure(
    #     data=[go.Choropleth(
    #         locationmode='USA-states',
    #         locations=dff['state_code'],
    #         z=dff["Pct of Colonies Impacted"].astype(float),
    #         colorscale='Reds',
    #     )]
    # )
    #
    # fig.update_layout(
    #     title_text="Bees Affected by Mites in the USA",
    #     title_xanchor="center",
    #     title_font=dict(size=24),
    #     title_x=0.5,
    #     geo=dict(scope='usa'),
    # )

    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)


# @app.callback( #connect compenents with graph
#     [Output(component_id='output_container', component_property='children'), #two outputs, one the children out the output container, and also the figure of the compenent id my_bee_map
#      Output(component_id='my_bee_map', component_property='figure')],
#     [Input(component_id='slct_state', component_property='value')]
# ) 

# def update_graph(option_slctd_b): #this argument refers to the component_property value in the callback inpput
#     print(option_slctd_b)
#     print(type(option_slctd_b))

#     container = "The state(s) chosen by user was: {}".format(option_slctd_b)



#     #Challenge B: Line Chart

#     dff2 = df.copy()
#     dff2 = dff2[dff2["Affected by"] == 'Varroa_mites']
#     dff2 = dff2[dff2['State'].isin(option_slctd_b)]

#     fig = px.line(
#         data_frame=dff2,
#         x = 'Year',
#         y = 'Pct of Colonies Impacted',
#         color = 'State',
#         title = "Bee Colonies Impacted by Disease in Texas, California, and Hawaii",
#         template = 'plotly_dark'    
#     )

#     return container, fig


# # ------------------------------------------------------------------------------
# if __name__ == '__main__':
#     app.run_server(debug=True)
