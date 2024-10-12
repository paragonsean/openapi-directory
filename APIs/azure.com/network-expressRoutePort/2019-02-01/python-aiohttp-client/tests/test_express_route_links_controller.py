# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.express_route_link import ExpressRouteLink
from openapi_server.models.express_route_link_list_result import ExpressRouteLinkListResult


pytestmark = pytest.mark.asyncio

async def test_express_route_links_get(client):
    """Test case for express_route_links_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/ExpressRoutePorts/{express_route_port_name}/links/{link_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', express_route_port_name='express_route_port_name_example', link_name='link_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_links_list(client):
    """Test case for express_route_links_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/ExpressRoutePorts/{express_route_port_name}/links'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', express_route_port_name='express_route_port_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

