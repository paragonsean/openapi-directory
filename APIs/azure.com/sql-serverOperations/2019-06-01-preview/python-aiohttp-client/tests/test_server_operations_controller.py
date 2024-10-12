# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.server_operation_list_result import ServerOperationListResult


pytestmark = pytest.mark.asyncio

async def test_server_operations_list_by_server(client):
    """Test case for server_operations_list_by_server

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/operations'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

