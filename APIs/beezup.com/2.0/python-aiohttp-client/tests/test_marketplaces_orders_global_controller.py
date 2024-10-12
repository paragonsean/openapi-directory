# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_synchronization_list import AccountSynchronizationList
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.order_index import OrderIndex


pytestmark = pytest.mark.asyncio

async def test_get_marketplace_accounts_synchronization(client):
    """Test case for get_marketplace_accounts_synchronization

    [DEPRECATED] Get current synchronization status between your marketplaces and BeezUP accounts
    """
    params = [('storeId', '04730364-9826-4ff3-92e4-51fccd02bf10')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/marketplaces/orders/status',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_order_index(client):
    """Test case for get_order_index

    [DEPRECATED] Get all actions you can do on the order API
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/marketplaces/orders/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_harvest_all(client):
    """Test case for harvest_all

    [DEPRECATED] Send harvest request to all your marketplaces
    """
    params = [('storeId', '04730364-9826-4ff3-92e4-51fccd02bf10')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/orders/harvest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

