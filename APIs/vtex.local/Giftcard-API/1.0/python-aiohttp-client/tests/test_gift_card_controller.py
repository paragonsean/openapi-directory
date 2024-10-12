# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_gift_card_request import CreateGiftCardRequest
from openapi_server.models.get_gift_cardusing_json_request import GetGiftCardusingJSONRequest
from openapi_server.models.response import Response
from openapi_server.models.response2 import Response2


pytestmark = pytest.mark.asyncio

async def test_create_gift_card(client):
    """Test case for create_gift_card

    Create GiftCard
    """
    body = openapi_server.CreateGiftCardRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/vnd.vtex.giftcard.v1+json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'x_vtex_api_app_key': '{{X-VTEX-API-AppKey}}',
        'x_vtex_api_app_token': '{{X-VTEX-API-AppToken}}',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/giftcards',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gift_cardby_id(client):
    """Test case for get_gift_cardby_id

    Get GiftCard by ID
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/giftcards/{gift_card_id}'.format(gift_card_id='2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gift_cardusing_json(client):
    """Test case for get_gift_cardusing_json

    Get GiftCard using JSON
    """
    body = {"cart":{"discounts":0,"grandTotal":123.1,"items":[{"id":"1","name":"Product Name","price":100,"productId":"1","quantity":1,"refId":"12"}],"itemsTotal":100,"redemptionCode":null,"relationName":null,"shipping":0,"taxes":12},"client":{"document":"21301923110","email":"email@damoain.com","id":"019a0cc1-409a-4c16-859b-eefdb81f825e"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'rest_range': 'giftcard=0-49',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/giftcards/_search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

