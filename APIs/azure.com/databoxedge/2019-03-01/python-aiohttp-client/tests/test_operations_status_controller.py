# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.job import Job


pytestmark = pytest.mark.asyncio

async def test_operations_status_get(client):
    """Test case for operations_status_get

    Gets the details of a specified job on a data box edge/gateway device.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/operationsStatus/{name}'.format(device_name='device_name_example', name='name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

