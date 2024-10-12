# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.premium_messaging_regions_list_result import PremiumMessagingRegionsListResult


pytestmark = pytest.mark.asyncio

async def test_regions_list_by_sku(client):
    """Test case for regions_list_by_sku

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ServiceBus/sku/{sku}/regions'.format(subscription_id='subscription_id_example', sku='sku_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

