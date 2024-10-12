# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.endpoint_services_list_result import EndpointServicesListResult


pytestmark = pytest.mark.asyncio

async def test_available_endpoint_services_list(client):
    """Test case for available_endpoint_services_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/locations/{location}/virtualNetworkAvailableEndpointServices'.format(location='location_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

