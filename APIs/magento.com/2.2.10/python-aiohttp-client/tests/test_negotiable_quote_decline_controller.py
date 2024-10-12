# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.negotiable_quote_negotiable_quote_management_v1_decline_post_request import NegotiableQuoteNegotiableQuoteManagementV1DeclinePostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_negotiable_quote_negotiable_quote_management_v1_decline_post(client):
    """Test case for negotiable_quote_negotiable_quote_management_v1_decline_post

    negotiableQuote/decline
    """
    body = openapi_server.NegotiableQuoteNegotiableQuoteManagementV1DeclinePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/negotiableQuote/decline',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

