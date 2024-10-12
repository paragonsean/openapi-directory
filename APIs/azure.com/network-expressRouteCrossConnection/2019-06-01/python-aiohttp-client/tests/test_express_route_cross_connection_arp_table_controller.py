# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.express_route_cross_connections_list_arp_table200_response import ExpressRouteCrossConnectionsListArpTable200Response


pytestmark = pytest.mark.asyncio

async def test_express_route_cross_connections_list_arp_table(client):
    """Test case for express_route_cross_connections_list_arp_table

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCrossConnections/{cross_connection_name}/peerings/{peering_name}/arpTables/{device_path}'.format(resource_group_name='resource_group_name_example', cross_connection_name='cross_connection_name_example', peering_name='peering_name_example', device_path='device_path_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

