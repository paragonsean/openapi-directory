# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operation_status import OperationStatus


pytestmark = pytest.mark.asyncio

async def test_compute_fabric_operations_get(client):
    """Test case for compute_fabric_operations_get

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/System.{location}/providers/{provider}/fabricLocations/{location}/computeOperationResults/{compute_operation_result}'.format(subscription_id='subscription_id_example', location='location_example', provider='provider_example', compute_operation_result='compute_operation_result_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

