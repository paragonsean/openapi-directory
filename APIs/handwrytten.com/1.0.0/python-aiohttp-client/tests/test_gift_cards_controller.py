# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.gift_card import GiftCard


pytestmark = pytest.mark.asyncio

async def test_get_gift_card_details(client):
    """Test case for get_gift_card_details

    Lists information on gift cards
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/giftCards/view',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gift_card_details(client):
    """Test case for gift_card_details

    Lists information on gift cards
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/giftCards/view',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

