# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operations_discovery_collection import OperationsDiscoveryCollection


pytestmark = pytest.mark.asyncio

async def test_operations_list(client):
    """Test case for operations_list

    Returns the list of available operations.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/operations'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

