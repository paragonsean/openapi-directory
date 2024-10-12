# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_success_response import CreateSuccessResponse
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.offers_get200_response import OffersGet200Response
from openapi_server.models.offers_offer_id_get200_response import OffersOfferIdGet200Response
from openapi_server.models.offers_post_request import OffersPostRequest


pytestmark = pytest.mark.asyncio

async def test_offers_get(client):
    """Test case for offers_get

    View list of offers
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/offers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offers_offer_id_delete(client):
    """Test case for offers_offer_id_delete

    Delete an offer
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/offers/{offer_id}'.format(offer_id='offer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offers_offer_id_get(client):
    """Test case for offers_offer_id_get

    View offer
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/offers/{offer_id}'.format(offer_id='offer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_offers_offer_id_put(client):
    """Test case for offers_offer_id_put

    Edit an offer
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    data = {
        'status': draft
        }
    response = await client.request(
        method='PUT',
        path='/api/v1/offers/{offer_id}'.format(offer_id='offer_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offers_post(client):
    """Test case for offers_post

    Add new offer
    """
    body = openapi_server.OffersPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/offers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

