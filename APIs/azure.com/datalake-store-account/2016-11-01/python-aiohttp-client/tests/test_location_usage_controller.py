# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.usage_list_result import UsageListResult


pytestmark = pytest.mark.asyncio

async def test_locations_get_usage(client):
    """Test case for locations_get_usage

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DataLakeStore/locations/{location}/usages'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

