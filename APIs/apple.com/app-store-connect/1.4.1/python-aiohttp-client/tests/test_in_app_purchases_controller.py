# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.in_app_purchase_response import InAppPurchaseResponse


pytestmark = pytest.mark.asyncio

async def test_in_app_purchases_get_instance(client):
    """Test case for in_app_purchases_get_instance

    
    """
    params = [('fields[inAppPurchases]', ['fields_in_app_purchases_example']),
                    ('include', ['include_example']),
                    ('limit[apps]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/inAppPurchases/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

