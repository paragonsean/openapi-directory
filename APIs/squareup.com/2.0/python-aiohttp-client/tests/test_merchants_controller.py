# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_merchants_response import ListMerchantsResponse
from openapi_server.models.retrieve_merchant_response import RetrieveMerchantResponse


pytestmark = pytest.mark.asyncio

async def test_list_merchants(client):
    """Test case for list_merchants

    ListMerchants
    """
    params = [('cursor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/merchants',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_merchant(client):
    """Test case for retrieve_merchant

    RetrieveMerchant
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/merchants/{merchant_id}'.format(merchant_id='merchant_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

