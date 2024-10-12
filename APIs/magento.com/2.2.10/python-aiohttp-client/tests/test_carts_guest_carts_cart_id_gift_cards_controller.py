# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.gift_card_account_guest_gift_card_account_management_v1_add_gift_card_post_request import GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_gift_card_account_guest_gift_card_account_management_v1_add_gift_card_post(client):
    """Test case for gift_card_account_guest_gift_card_account_management_v1_add_gift_card_post

    carts/guest-carts/{cartId}/giftCards
    """
    body = openapi_server.GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/carts/guest-carts/{cart_id}/giftCards'.format(cart_id='cart_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

