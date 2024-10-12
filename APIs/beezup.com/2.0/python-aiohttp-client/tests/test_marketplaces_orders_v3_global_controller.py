# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_synchronization_list import AccountSynchronizationList
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.error_response_message import ErrorResponseMessage
from openapi_server.models.list_of_value_item import ListOfValueItem


pytestmark = pytest.mark.asyncio

async def test_get_marketplace_accounts_synchronization_v3(client):
    """Test case for get_marketplace_accounts_synchronization_v3

    
    """
    params = [('storeIds', ['store_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/orders/v3/status',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_order_management_ready_marketplace_business_code(client):
    """Test case for get_order_management_ready_marketplace_business_code

    
    """
    params = [('storeIds', ['store_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': ['accept_language_example'],
    }
    response = await client.request(
        method='GET',
        path='/orders/v3/lov/orderManagementReadyMarketplaceBusinessCode',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_harvest_all_v3(client):
    """Test case for harvest_all_v3

    Send harvest request to all your marketplaces
    """
    params = [('storeId', '04730364-9826-4ff3-92e4-51fccd02bf10')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/orders/v3/harvest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

