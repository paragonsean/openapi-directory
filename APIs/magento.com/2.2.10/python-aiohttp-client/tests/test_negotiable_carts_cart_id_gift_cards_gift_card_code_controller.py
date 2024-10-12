# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_negotiable_quote_gift_card_account_management_v1_delete_by_quote_id_delete(client):
    """Test case for negotiable_quote_gift_card_account_management_v1_delete_by_quote_id_delete

    negotiable-carts/{cartId}/giftCards/{giftCardCode}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/negotiable-carts/{cart_id}/giftCards/{gift_card_code}'.format(cart_id=56, gift_card_code='gift_card_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

