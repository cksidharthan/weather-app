from django.shortcuts import render, redirect
from .forms import SearchByLocationForm, DashboardSearchForm
from weather_functions import api_functions, visualizations
from datetime import datetime


def home_search(request, *args, **kwargs):
    if request.method == 'POST':
        form = SearchByLocationForm(request.POST or None)
        if form.is_valid():
            search_location = form.cleaned_data.get('search_location')
            form.save()
            request.session['search_location'] = search_location
            return redirect(to='dashboard')
    else:
        form = SearchByLocationForm(request.POST or None)
    context = {
        'search_form': form,
    }
    return render(request, 'home.html', context)


def dashboard(request, *args, **kwargs):
    form = DashboardSearchForm(request.POST or None)
    search_location = request.session.get('search_location')
    location_weater_data = api_functions.cityWeather(search_location)
    city_id = api_functions.get_city_data(search_location)
    forecast_data = api_functions.getForecastData(location_weater_data)
    current_day_stats = visualizations.get_current_day_stats(forecast_data)
    temp_vs_date_graph = visualizations.get_temp_vs_day(forecast_data)
    hum_wind_graph = visualizations.get_hum_wind_graph(forecast_data)
    context = {
        'city_id': city_id,
        'search_form': form,
        'search_location': search_location,
        'current_time': datetime.now(),
        'current_day_stats': current_day_stats,
        'temp_vs_date_graph': temp_vs_date_graph,
        'hum_wind_graph': hum_wind_graph
    }
    return render(request, 'dashboard.html', context)
