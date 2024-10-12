# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_cart_repository_v1_save_put_request import QuoteCartRepositoryV1SavePutRequest
from openapi_server.models.quote_data_cart_interface import QuoteDataCartInterface


pytestmark = pytest.mark.asyncio

async def test_quote_cart_management_v1_create_empty_cart_for_customer_post(client):
    """Test case for quote_cart_management_v1_create_empty_cart_for_customer_post

    carts/mine
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/carts/mine',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_cart_management_v1_get_cart_for_customer_get(client):
    """Test case for quote_cart_management_v1_get_cart_for_customer_get

    carts/mine
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/carts/mine',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_quote_cart_repository_v1_save_put(client):
    """Test case for quote_cart_repository_v1_save_put

    carts/mine
    """
    body = openapi_server.QuoteCartRepositoryV1SavePutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/carts/mine',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

