# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.card_create_request import CardCreateRequest
from openapi_server.models.card_list_response import CardListResponse
from openapi_server.models.card_patch_request import CardPatchRequest
from openapi_server.models.card_response import CardResponse
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_delete_crm_v3_extensions_cards_app_id_card_id(client):
    """Test case for delete_crm_v3_extensions_cards_app_id_card_id

    Delete a card
    """
    headers = { 
        'Accept': '*/*',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/crm/v3/extensions/cards/{app_id}/{card_id}'.format(app_id=56, card_id='card_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_crm_v3_extensions_cards_app_id(client):
    """Test case for get_crm_v3_extensions_cards_app_id

    Get all cards
    """
    headers = { 
        'Accept': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/crm/v3/extensions/cards/{app_id}'.format(app_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_crm_v3_extensions_cards_app_id_card_id(client):
    """Test case for get_crm_v3_extensions_cards_app_id_card_id

    Get a card.
    """
    headers = { 
        'Accept': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/crm/v3/extensions/cards/{app_id}/{card_id}'.format(app_id=56, card_id='card_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_crm_v3_extensions_cards_app_id_card_id(client):
    """Test case for patch_crm_v3_extensions_cards_app_id_card_id

    Update a card
    """
    body = {"actions":{"baseUrls":["https://www.example.com/hubspot"]},"display":{"properties":{"dataType":"STRING","label":"Pets Name","name":"pet_name"}},"fetch":{"objectTypes":[{"name":"contacts","propertiesToSend":["email","firstname"]}],"targetUrl":"https://www.example.com/hubspot/target"},"title":"PetSpot"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/crm/v3/extensions/cards/{app_id}/{card_id}'.format(app_id=56, card_id='card_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_crm_v3_extensions_cards_app_id(client):
    """Test case for post_crm_v3_extensions_cards_app_id

    Create a new card
    """
    body = {"actions":{"baseUrls":["https://www.example.com/hubspot"]},"display":{"properties":{"dataType":"STRING","label":"Pets Name","name":"pet_name"}},"fetch":{"objectTypes":[{"name":"contacts","propertiesToSend":["email","firstname"]}],"targetUrl":"https://www.example.com/hubspot/target"},"title":"PetSpot"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/crm/v3/extensions/cards/{app_id}'.format(app_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

