# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_arrivals_and_departures_by_crs(client):
    """Test case for get_arrivals_and_departures_by_crs

    getArrivalsAndDeparturesByCRS is used to get a list of services arriving to and departing from a UK train station by the CRS (Computer Reservation System) code. This will typically return a list of train services, but will also return any replacement bus or ferry services that are in place.
    """
    params = [('apiKey', 'api_key_example'),
                    ('numServices', 10),
                    ('timeOffset', 0),
                    ('timeWindow', 120),
                    ('serviceDetails', True),
                    ('filterStation', 'filter_station_example'),
                    ('filterType', 'filter_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v2.0/getArrivalsAndDeparturesByCRS/{crs}'.format(crs='crs_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_arrivals_by_crs(client):
    """Test case for get_arrivals_by_crs

    getArrivalsByCRS is used to get a list of services arriving to a UK train station by the CRS (Computer Reservation System) code. This will typically return a list of train services, but will also return any replacement bus or ferry services that are in place.
    """
    params = [('apiKey', 'api_key_example'),
                    ('numServices', 10),
                    ('timeOffset', 0),
                    ('timeWindow', 120),
                    ('serviceDetails', True),
                    ('filterStation', 'filter_station_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v2.0/getArrivalsByCRS/{crs}'.format(crs='crs_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_departures_by_crs(client):
    """Test case for get_departures_by_crs

    getDeparturesByCRS is used to get a list of services departing from a UK train station by the CRS (Computer Reservation System) code. This will typically return a list of train services, but will also return any replacement bus or ferry services that are in place.
    """
    params = [('apiKey', 'api_key_example'),
                    ('numServices', 10),
                    ('timeOffset', 0),
                    ('timeWindow', 120),
                    ('serviceDetails', True),
                    ('filterStation', 'filter_station_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v2.0/getDeparturesByCRS/{crs}'.format(crs='crs_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

