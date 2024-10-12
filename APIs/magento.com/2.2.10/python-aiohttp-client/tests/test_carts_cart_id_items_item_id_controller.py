# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_cart_item_repository_v1_save_post_request import QuoteCartItemRepositoryV1SavePostRequest
from openapi_server.models.quote_data_cart_item_interface import QuoteDataCartItemInterface


pytestmark = pytest.mark.asyncio

async def test_v1_carts_cart_id_items_item_id_delete(client):
    """Test case for v1_carts_cart_id_items_item_id_delete

    carts/{cartId}/items/{itemId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/carts/{cart_id}/items/{item_id}'.format(cart_id=56, item_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v1_carts_cart_id_items_item_id_put(client):
    """Test case for v1_carts_cart_id_items_item_id_put

    carts/{cartId}/items/{itemId}
    """
    body = openapi_server.QuoteCartItemRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/carts/{cart_id}/items/{item_id}'.format(cart_id='cart_id_example', item_id='item_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

