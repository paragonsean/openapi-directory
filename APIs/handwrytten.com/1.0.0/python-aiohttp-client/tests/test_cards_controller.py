# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.card import Card
from openapi_server.models.card_details import CardDetails
from openapi_server.models.filterable_card_details_request import FilterableCardDetailsRequest
from openapi_server.models.list_cards_request import ListCardsRequest


pytestmark = pytest.mark.asyncio

async def test_filterable_card_details(client):
    """Test case for filterable_card_details

    Provides full information on a specific card
    """
    body = openapi_server.FilterableCardDetailsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/cards/view',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_cards(client):
    """Test case for list_cards

    Lists information on cards
    """
    body = openapi_server.ListCardsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/cards/list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_simple_list_cards(client):
    """Test case for simple_list_cards

    Lists information on cards
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/cards/list',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

