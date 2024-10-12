# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.resource_skus_result import ResourceSkusResult


pytestmark = pytest.mark.asyncio

async def test_resource_skus_list_0(client):
    """Test case for resource_skus_list_0

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute/skus'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

