import plotly.graph_objects as go
from plotly.offline import plot
from plotly.subplots import make_subplots

config = {
    'displaylogo': False,
    'modeBarButtonsToAdd': ['drawline', 'drawrect', 'eraseshape'],
}

def get_hum_wind_graph(dataframe):
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    # Add traces
    fig.add_trace(go.Scatter(x=dataframe.index, y=dataframe.wind_speed, name="Wind Speed",
                             line=dict(color='firebrick', width=4)), secondary_y=False, )
    fig.add_trace(go.Scatter(x=dataframe.index, y=dataframe.humidity, name="Humidity",
                             line=dict(color='royalblue', width=4, dash='dash')), secondary_y=True)
    # Add figure title
    fig.update_layout(title_text="<b>Humidity & Windspeed Dual Axis Forecast</b>")
    # Set x-axis title
    fig.update_xaxes(title_text="<b>Date</b>")
    # Set y-axes titles
    fig.update_yaxes(title_text="<b>Wind Speed</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>Humidity</b>", secondary_y=True)
    plot_div = plot(fig, output_type='div', config=config)
    return plot_div





def get_temp_vs_day(dataframe):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataframe.index, y=dataframe.Temp_max, fill='toself', fillcolor='rgba(0,100,80,0.2)',
                             line_color='rgba(255,255,255,0)', showlegend=False, name='Max Temperature'))
    fig.add_trace(go.Scatter(x=dataframe.index, y=dataframe.Temp_min, fill='toself', fillcolor='rgba(0,176,246,0.2)',
                             line_color='rgba(255,255,255,0)', name='Min Temmperature', showlegend=False))
    fig.add_trace(
        go.Scatter(x=dataframe.index, y=dataframe.Temp_max, line_color='rgb(0,100,80)', name='Max Temperature'))
    fig.add_trace(
        go.Scatter(x=dataframe.index, y=dataframe.Temp_min, line_color='rgb(0,176,246)', name='Min Temperature'))
    fig.update_traces(mode='lines')
    # Add figure title
    fig.update_layout(title_text="<b>Max & Min Temperature Forecast</b>")
    # Set x-axis title
    fig.update_xaxes(title_text="<b>Date</b>")
    # Set y-axes titles
    fig.update_yaxes(title_text="<b>Temperature</b>")
    plot_div = plot(fig, output_type='div', config=config)
    return plot_div


def get_current_day_stats(forecast_data):
    current_day_stats_dict = {'current_temp': forecast_data['Temp'][0],
                              'max_temp': forecast_data['Temp_max'][0],
                              'min_temp': forecast_data['Temp_min'][0],
                              'humidity': forecast_data['humidity'][0],
                              'wind_speed': forecast_data['wind_speed'][0],
                              'sunrise': forecast_data['sunrise'][0].split(" ")[3],
                              'sunset': forecast_data['sunset'][0].split(" ")[3]}
    return current_day_stats_dict
