# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.operation_result import OperationResult


pytestmark = pytest.mark.asyncio

async def test_operations_get(client):
    """Test case for operations_get

    
    """
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DevTestLab/locations/{location_name}/operations/{name}'.format(subscription_id='subscription_id_example', location_name='location_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

