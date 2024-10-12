# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.resource_type_sku_collection import ResourceTypeSkuCollection


pytestmark = pytest.mark.asyncio

async def test_skus_list(client):
    """Test case for skus_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Blockchain/skus'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

