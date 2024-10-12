# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.facility import Facility
from openapi_server.models.station import Station


pytestmark = pytest.mark.asyncio

async def test_find_facilities(client):
    """Test case for find_facilities

    
    """
    params = [('type', ["ESCALATOR","ELEVATOR"]),
                    ('state', ["ACTIVE","INACTIVE","UNKNOWN"]),
                    ('equipmentnumbers', [56]),
                    ('stationnumber', 56),
                    ('area', ['area_example'])]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/fasta/v2/facilities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_station_by_station_number(client):
    """Test case for find_station_by_station_number

    
    """
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/fasta/v2/stations/{stationnumber}'.format(stationnumber=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_facility_by_equipment_number(client):
    """Test case for get_facility_by_equipment_number

    
    """
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/fasta/v2/facilities/{equipmentnumber}'.format(equipmentnumber=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

