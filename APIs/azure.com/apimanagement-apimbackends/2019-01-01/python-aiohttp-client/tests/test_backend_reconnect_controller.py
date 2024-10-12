# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backend_list_by_service_default_response import BackendListByServiceDefaultResponse
from openapi_server.models.backend_reconnect_request import BackendReconnectRequest


pytestmark = pytest.mark.asyncio

async def test_backend_reconnect(client):
    """Test case for backend_reconnect

    
    """
    parameters = openapi_server.BackendReconnectRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/backends/{backend_id}/reconnect'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', backend_id='backend_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

