# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.card_transactionsv1 import CardTransactionsv1
from openapi_server.models.cards import Cards
from openapi_server.models.new_card import NewCard
from openapi_server.models.new_card_response import NewCardResponse


pytestmark = pytest.mark.asyncio

async def test_block_card(client):
    """Test case for block_card

    Block a card
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/business/v1/cards/{card_id}/block'.format(card_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_new_card(client):
    """Test case for create_new_card

    Create a new debit card.
    """
    body = openapi_server.NewCard()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/business/v1/cards',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_listof_card_transactions(client):
    """Test case for get_listof_card_transactions

    List Card Transactions.
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v1/cards/{card_id}/transactions'.format(card_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_listof_cards(client):
    """Test case for get_listof_cards

    View List of Cards.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v1/cards',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unblock_card(client):
    """Test case for unblock_card

    Unblock a card
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/business/v1/cards/{card_id}/unblock'.format(card_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

