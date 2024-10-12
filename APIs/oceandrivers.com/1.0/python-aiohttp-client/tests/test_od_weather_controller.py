# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_compare_station(client):
    """Test case for compare_station

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1.0/compareStation/{station_name}'.format(station_name='cnarenal'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_aemet_station(client):
    """Test case for get_aemet_station

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1.0/getAemetStation/{station_name}/{period}'.format(station_name='aeropuertopalma', period='lastdata'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_easywind(client):
    """Test case for get_easywind

    
    """
    params = [('period', 'latestdata')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1.0/getEasyWind/{easywind_id}'.format(easywind_id='EW013'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_stations(client):
    """Test case for get_event_stations

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1.0/getEventStations/{event_id}'.format(event_id='trofeoprincesasofia'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_forecast_points(client):
    """Test case for get_forecast_points

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1.0/getForecastPoints/{yatchclubid}/language/{language}'.format(yatchclubid='cnarenal', language='language_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_forecast_time_series(client):
    """Test case for get_forecast_time_series

    
    """
    params = [('inittime', 'inittime_example'),
                    ('endtime', 'endtime_example'),
                    ('days', 56),
                    ('hours', 56),
                    ('weather', 'weather_example'),
                    ('wave', 'wave_example'),
                    ('entryid', 'entryid_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1.0/getForecastTimeSeries/{latitude}/{longitude}'.format(latitude=39.49, longitude=2.74),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_forecast_time_series_wrf(client):
    """Test case for get_forecast_time_series_wrf

    
    """
    params = [('inittime', 'inittime_example'),
                    ('endtime', 'endtime_example'),
                    ('days', 56),
                    ('hours', 56),
                    ('weather', 'weather_example'),
                    ('wave', 'wave_example'),
                    ('entryid', 'entryid_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1.0/getForecastTimeSeriesWrf/{latitude}/{longitude}'.format(latitude=39.49, longitude=2.74),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_socib_weather_station(client):
    """Test case for get_socib_weather_station

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1.0/getSocibWeatherStation/{station_name}/{period}'.format(station_name='boyaenderrocat', period='lastdata'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_weather_display(client):
    """Test case for get_weather_display

    
    """
    params = [('period', 'latestdata')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1.0/getWeatherDisplay/{station_name}'.format(station_name='cnarenal'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_web_cams(client):
    """Test case for get_web_cams

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1.0/getWebCams/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

