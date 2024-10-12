# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.express_route_ports_location import ExpressRoutePortsLocation
from openapi_server.models.express_route_ports_location_list_result import ExpressRoutePortsLocationListResult


pytestmark = pytest.mark.asyncio

async def test_express_route_ports_locations_get(client):
    """Test case for express_route_ports_locations_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/ExpressRoutePortsLocations/{location_name}'.format(subscription_id='subscription_id_example', location_name='location_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_ports_locations_list(client):
    """Test case for express_route_ports_locations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/ExpressRoutePortsLocations'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

