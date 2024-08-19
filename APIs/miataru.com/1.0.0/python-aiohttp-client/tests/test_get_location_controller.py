# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.miataru_get_location_geo_json_response import MiataruGetLocationGeoJSONResponse
from openapi_server.models.miataru_get_location_history_request import MiataruGetLocationHistoryRequest
from openapi_server.models.miataru_get_location_history_response import MiataruGetLocationHistoryResponse
from openapi_server.models.miataru_get_location_request import MiataruGetLocationRequest
from openapi_server.models.miataru_get_location_response import MiataruGetLocationResponse


pytestmark = pytest.mark.asyncio

async def test_get_location(client):
    """Test case for get_location

    
    """
    body = {"MiataruConfig":{"RequestMiataruDeviceID":"6140c3c0-4a7d-40d2-99ab-39414cac3509"},"MiataruGetLocation":[{"Device":"7b8e6e0ee5296db345162dc2ef652c1350761823"},{"Device":"7b8e6e0ee5296db345162dc2ef652c1350761823"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/GetLocation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_location_geo_json(client):
    """Test case for get_location_geo_json

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/GetLocationGeoJSON/{device_id}'.format(device_id='7b8e6e0ee5296db345162dc2ef652c1350761823'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_location_history(client):
    """Test case for get_location_history

    
    """
    body = {"MiataruConfig":{"RequestMiataruDeviceID":"6140c3c0-4a7d-40d2-99ab-39414cac3509"},"MiataruGetLocationHistory":{"Device":"7b8e6e0ee5296db345162dc2ef652c1350761823","Amount":"10"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/GetLocationHistory',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

