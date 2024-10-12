# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.gift_card_account_data_gift_card_account_interface import GiftCardAccountDataGiftCardAccountInterface


pytestmark = pytest.mark.asyncio

async def test_gift_card_account_gift_card_account_management_v1_get_list_by_quote_id_get(client):
    """Test case for gift_card_account_gift_card_account_management_v1_get_list_by_quote_id_get

    carts/{quoteId}/giftCards
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/carts/{quote_id}/giftCards'.format(quote_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

