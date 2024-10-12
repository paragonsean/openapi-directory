# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.location_capabilities import LocationCapabilities


pytestmark = pytest.mark.asyncio

async def test_capabilities_list_by_location(client):
    """Test case for capabilities_list_by_location

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Sql/locations/{location_name}/capabilities'.format(location_name='location_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

