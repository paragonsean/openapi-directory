# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.available_operations_list_response import AvailableOperationsListResponse
from openapi_server.models.csrp_error import CSRPError
from openapi_server.models.operation_resource import OperationResource


pytestmark = pytest.mark.asyncio

async def test_operations_get(client):
    """Test case for operations_get

    Implements get of async operation
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'referer': 'referer_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.VMwareCloudSimple/locations/{region_id}/operationResults/{operation_id}'.format(subscription_id='subscription_id_example', region_id='region_id_example', operation_id='operation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operations_list(client):
    """Test case for operations_list

    Implements list of available operations
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.VMwareCloudSimple/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

