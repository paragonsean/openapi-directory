# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_cart_repository_v1_save_put_request import QuoteCartRepositoryV1SavePutRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_negotiable_quote_negotiable_cart_repository_v1_save_put(client):
    """Test case for negotiable_quote_negotiable_cart_repository_v1_save_put

    negotiableQuote/{quoteId}
    """
    body = openapi_server.QuoteCartRepositoryV1SavePutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/negotiableQuote/{quote_id}'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

