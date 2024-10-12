# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.gift_message_cart_repository_v1_save_post_request import GiftMessageCartRepositoryV1SavePostRequest
from openapi_server.models.gift_message_data_message_interface import GiftMessageDataMessageInterface


pytestmark = pytest.mark.asyncio

async def test_v1_carts_cart_id_gift_message_item_id_get(client):
    """Test case for v1_carts_cart_id_gift_message_item_id_get

    carts/{cartId}/gift-message/{itemId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/carts/{cart_id}/gift-message/{item_id}'.format(cart_id=56, item_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v1_carts_cart_id_gift_message_item_id_post(client):
    """Test case for v1_carts_cart_id_gift_message_item_id_post

    carts/{cartId}/gift-message/{itemId}
    """
    body = openapi_server.GiftMessageCartRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/carts/{cart_id}/gift-message/{item_id}'.format(cart_id=56, item_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

