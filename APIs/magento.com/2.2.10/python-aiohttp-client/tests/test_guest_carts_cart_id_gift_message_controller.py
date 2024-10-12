# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.gift_message_cart_repository_v1_save_post_request import GiftMessageCartRepositoryV1SavePostRequest
from openapi_server.models.gift_message_data_message_interface import GiftMessageDataMessageInterface


pytestmark = pytest.mark.asyncio

async def test_gift_message_guest_cart_repository_v1_get_get(client):
    """Test case for gift_message_guest_cart_repository_v1_get_get

    guest-carts/{cartId}/gift-message
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/guest-carts/{cart_id}/gift-message'.format(cart_id='cart_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_gift_message_guest_cart_repository_v1_save_post(client):
    """Test case for gift_message_guest_cart_repository_v1_save_post

    guest-carts/{cartId}/gift-message
    """
    body = openapi_server.GiftMessageCartRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/guest-carts/{cart_id}/gift-message'.format(cart_id='cart_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

