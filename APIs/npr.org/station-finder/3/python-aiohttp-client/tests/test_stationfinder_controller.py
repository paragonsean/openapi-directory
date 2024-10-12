# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_document import ErrorDocument
from openapi_server.models.station_document import StationDocument
from openapi_server.models.station_list_document import StationListDocument


pytestmark = pytest.mark.asyncio

async def test_get_station_by_id(client):
    """Test case for get_station_by_id

    Retrieve metadata for the station with the given numeric ID
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/v3/stations/{station_id}'.format(station_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_stations(client):
    """Test case for search_stations

    List stations close to you or filter by search criteria
    """
    params = [('q', 'q_example'),
                    ('city', 'city_example'),
                    ('state', 'state_example'),
                    ('lat', 3.4),
                    ('lon', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/v3/stations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

