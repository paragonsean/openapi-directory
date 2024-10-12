# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_card_request import CreateCardRequest
from openapi_server.models.create_card_response import CreateCardResponse
from openapi_server.models.disable_card_response import DisableCardResponse
from openapi_server.models.list_cards_response import ListCardsResponse
from openapi_server.models.retrieve_card_response import RetrieveCardResponse


pytestmark = pytest.mark.asyncio

async def test_create_card(client):
    """Test case for create_card

    CreateCard
    """
    body = {"request_body":{"card":{"billing_address":{"address_line_1":"500 Electric Ave","address_line_2":"Suite 600","administrative_district_level_1":"NY","country":"US","locality":"New York","postal_code":"10003"},"cardholder_name":"Amelia Earhart","customer_id":"VDKXEEKPJN48QDG3BGGFAK05P8","reference_id":"user-id-1"},"idempotency_key":"4935a656-a929-4792-b97c-8848be85c27c","source_id":"cnon:uIbfJXhXETSP197M3GB"},"request_url":"/v2/cards"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/cards',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_card(client):
    """Test case for disable_card

    DisableCard
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/cards/{card_id}/disable'.format(card_id='card_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_cards(client):
    """Test case for list_cards

    ListCards
    """
    params = [('cursor', 'cursor_example'),
                    ('customer_id', 'customer_id_example'),
                    ('include_disabled', True),
                    ('reference_id', 'reference_id_example'),
                    ('sort_order', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/cards',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_card(client):
    """Test case for retrieve_card

    RetrieveCard
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/cards/{card_id}'.format(card_id='card_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

