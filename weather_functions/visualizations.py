def get_current_day_stats(forecast_data):
    current_day_stats_dict = {'current_temp': forecast_data['Temp'][0],
                              'max_temp': forecast_data['Temp_max'][0],
                              'min_temp': forecast_data['Temp_min'][0],
                              'humidity': forecast_data['humidity'][0],
                              'wind_speed': forecast_data['wind_speed'][0],
                              'sunrise': forecast_data['sunrise'][0].split(" ")[3],
                              'sunset': forecast_data['sunset'][0].split(" ")[3]}
    return current_day_stats_dict
