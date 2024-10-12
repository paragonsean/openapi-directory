# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operation_result import OperationResult


pytestmark = pytest.mark.asyncio

async def test_blockchain_member_operation_results_get(client):
    """Test case for blockchain_member_operation_results_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Blockchain/locations/{location_name}/blockchainMemberOperationResults/{operation_id}'.format(location_name='location_name_example', operation_id='operation_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

