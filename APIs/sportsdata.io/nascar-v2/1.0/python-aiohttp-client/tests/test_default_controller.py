# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.driver import Driver
from openapi_server.models.driver_race_projection import DriverRaceProjection
from openapi_server.models.race import Race
from openapi_server.models.race_result import RaceResult
from openapi_server.models.series import Series


pytestmark = pytest.mark.asyncio

async def test_driver_details(client):
    """Test case for driver_details

    Driver Details
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/nascar/v2/{format}/driver/{driverid}'.format(format=xml, driverid='driverid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_driver_race_projections_entry_list(client):
    """Test case for driver_race_projections_entry_list

    Driver Race Projections (Entry List)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/nascar/v2/{format}/DriverRaceProjections/{raceid}'.format(format=xml, raceid='raceid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drivers(client):
    """Test case for drivers

    Drivers
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/nascar/v2/{format}/drivers'.format(format=xml),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_race_results(client):
    """Test case for race_results

    Race Results
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/nascar/v2/{format}/raceresult/{raceid}'.format(format=xml, raceid='raceid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_races_schedule(client):
    """Test case for races_schedule

    Races / Schedule
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/nascar/v2/{format}/races/{season}'.format(format=xml, season='season_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_series(client):
    """Test case for series

    Series
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/nascar/v2/{format}/series'.format(format=xml),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

