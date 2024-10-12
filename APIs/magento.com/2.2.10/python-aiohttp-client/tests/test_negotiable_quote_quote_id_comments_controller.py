# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.negotiable_quote_data_comment_interface import NegotiableQuoteDataCommentInterface


pytestmark = pytest.mark.asyncio

async def test_negotiable_quote_comment_locator_v1_get_list_for_quote_get(client):
    """Test case for negotiable_quote_comment_locator_v1_get_list_for_quote_get

    negotiableQuote/{quoteId}/comments
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/negotiableQuote/{quote_id}/comments'.format(quote_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

