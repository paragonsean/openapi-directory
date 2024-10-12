# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_gift_card_account_guest_gift_card_account_management_v1_check_gift_card_get(client):
    """Test case for gift_card_account_guest_gift_card_account_management_v1_check_gift_card_get

    carts/guest-carts/{cartId}/checkGiftCard/{giftCardCode}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/carts/guest-carts/{cart_id}/checkGiftCard/{gift_card_code}'.format(cart_id='cart_id_example', gift_card_code='gift_card_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

