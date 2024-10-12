# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sku_enumeration_for_new_resource_result import SkuEnumerationForNewResourceResult


pytestmark = pytest.mark.asyncio

async def test_capacities_list_skus(client):
    """Test case for capacities_list_skus

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.PowerBIDedicated/skus'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

