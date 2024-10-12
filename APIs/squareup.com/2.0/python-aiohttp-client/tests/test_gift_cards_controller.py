# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_gift_card_request import CreateGiftCardRequest
from openapi_server.models.create_gift_card_response import CreateGiftCardResponse
from openapi_server.models.link_customer_to_gift_card_request import LinkCustomerToGiftCardRequest
from openapi_server.models.link_customer_to_gift_card_response import LinkCustomerToGiftCardResponse
from openapi_server.models.list_gift_cards_response import ListGiftCardsResponse
from openapi_server.models.retrieve_gift_card_from_gan_request import RetrieveGiftCardFromGANRequest
from openapi_server.models.retrieve_gift_card_from_gan_response import RetrieveGiftCardFromGANResponse
from openapi_server.models.retrieve_gift_card_from_nonce_request import RetrieveGiftCardFromNonceRequest
from openapi_server.models.retrieve_gift_card_from_nonce_response import RetrieveGiftCardFromNonceResponse
from openapi_server.models.retrieve_gift_card_response import RetrieveGiftCardResponse
from openapi_server.models.unlink_customer_from_gift_card_request import UnlinkCustomerFromGiftCardRequest
from openapi_server.models.unlink_customer_from_gift_card_response import UnlinkCustomerFromGiftCardResponse


pytestmark = pytest.mark.asyncio

async def test_create_gift_card(client):
    """Test case for create_gift_card

    CreateGiftCard
    """
    body = {"request_body":{"gift_card":{"type":"DIGITAL"},"idempotency_key":"NC9Tm69EjbjtConu","location_id":"81FN9BNFZTKS4"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/gift-cards',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_link_customer_to_gift_card(client):
    """Test case for link_customer_to_gift_card

    LinkCustomerToGiftCard
    """
    body = {"request_body":{"customer_id":"GKY0FZ3V717AH8Q2D821PNT2ZW"},"request_params":"?gift_card_id=gftc:71ea002277a34f8a945e284b04822edb"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/gift-cards/{gift_card_id}/link-customer'.format(gift_card_id='gift_card_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_gift_cards(client):
    """Test case for list_gift_cards

    ListGiftCards
    """
    params = [('type', 'type_example'),
                    ('state', 'state_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example'),
                    ('customer_id', 'customer_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/gift-cards',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_gift_card(client):
    """Test case for retrieve_gift_card

    RetrieveGiftCard
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/gift-cards/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_gift_card_from_gan(client):
    """Test case for retrieve_gift_card_from_gan

    RetrieveGiftCardFromGAN
    """
    body = {"request_body":{"gan":"7783320001001635"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/gift-cards/from-gan',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_gift_card_from_nonce(client):
    """Test case for retrieve_gift_card_from_nonce

    RetrieveGiftCardFromNonce
    """
    body = {"request_body":{"nonce":"cnon:7783322135245171"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/gift-cards/from-nonce',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unlink_customer_from_gift_card(client):
    """Test case for unlink_customer_from_gift_card

    UnlinkCustomerFromGiftCard
    """
    body = {"request_body":{"customer_id":"GKY0FZ3V717AH8Q2D821PNT2ZW"},"request_params":"?gift_card_id=gftc:71ea002277a34f8a945e284b04822edb"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/gift-cards/{gift_card_id}/unlink-customer'.format(gift_card_id='gift_card_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

