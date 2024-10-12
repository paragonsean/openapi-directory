# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.product_list_default_response import ProductListDefaultResponse
from openapi_server.models.product_subscriptions_list200_response import ProductSubscriptionsList200Response


pytestmark = pytest.mark.asyncio

async def test_product_subscriptions_list(client):
    """Test case for product_subscriptions_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/products/{product_id}/subscriptions'.format(product_id='product_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

