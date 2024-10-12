# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.create_store_request import CreateStoreRequest
from openapi_server.models.error_response_message_payment_required import ErrorResponseMessagePaymentRequired
from openapi_server.models.links_get_store_link import LinksGetStoreLink
from openapi_server.models.store import Store
from openapi_server.models.store_list import StoreList
from openapi_server.models.update_store_request import UpdateStoreRequest


pytestmark = pytest.mark.asyncio

async def test_create_store(client):
    """Test case for create_store

    Create a new store
    """
    body = openapi_server.CreateStoreRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/customer/stores',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_store(client):
    """Test case for delete_store

    Delete a store
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/user/customer/stores/{store_id}'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_store(client):
    """Test case for get_store

    Get store's information
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/customer/stores/{store_id}'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_stores(client):
    """Test case for get_stores

    Get store list
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/customer/stores',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_store(client):
    """Test case for update_store

    Update some store's information.
    """
    body = openapi_server.UpdateStoreRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/user/customer/stores/{store_id}'.format(store_id='store_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

