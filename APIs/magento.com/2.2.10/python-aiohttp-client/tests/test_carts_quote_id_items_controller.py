# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_cart_item_repository_v1_save_post_request import QuoteCartItemRepositoryV1SavePostRequest
from openapi_server.models.quote_data_cart_item_interface import QuoteDataCartItemInterface


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v1_carts_quote_id_items_post(client):
    """Test case for v1_carts_quote_id_items_post

    carts/{quoteId}/items
    """
    body = openapi_server.QuoteCartItemRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/carts/{quote_id}/items'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

