# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.card import Card
from openapi_server.models.card_resume import CardResume


pytestmark = pytest.mark.asyncio

async def test_cards(client):
    """Test case for cards

    fetch the list of cards
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/en/cards',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_pets_by_tags(client):
    """Test case for find_pets_by_tags

    Finds Card by Global ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/en/cards/{card_id}'.format(card_id='card_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sets_set_card_local_id_get(client):
    """Test case for sets_set_card_local_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/en/sets/{set}/{card_local_id}'.format(set='set_example', card_local_id='card_local_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

