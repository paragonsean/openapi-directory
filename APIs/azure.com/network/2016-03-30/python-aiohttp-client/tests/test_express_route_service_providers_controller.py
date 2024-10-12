# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.express_route_service_provider_list_result import ExpressRouteServiceProviderListResult


pytestmark = pytest.mark.asyncio

async def test_express_route_service_providers_list(client):
    """Test case for express_route_service_providers_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/expressRouteServiceProviders'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

