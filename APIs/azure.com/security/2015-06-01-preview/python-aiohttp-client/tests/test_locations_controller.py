# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.asc_location import AscLocation
from openapi_server.models.asc_location_list import AscLocationList
from openapi_server.models.cloud_error import CloudError


pytestmark = pytest.mark.asyncio

async def test_locations_get(client):
    """Test case for locations_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/locations/{asc_location}'.format(subscription_id='subscription_id_example', asc_location='asc_location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locations_list(client):
    """Test case for locations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/locations'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

