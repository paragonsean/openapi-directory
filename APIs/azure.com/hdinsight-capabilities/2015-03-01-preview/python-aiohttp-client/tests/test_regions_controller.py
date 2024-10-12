# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.capabilities_result import CapabilitiesResult


pytestmark = pytest.mark.asyncio

async def test_location_get_capabilities(client):
    """Test case for location_get_capabilities

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.HDInsight/locations/{location}/capabilities'.format(location='location_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

