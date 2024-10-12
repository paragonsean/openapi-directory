# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.negotiable_quote_data_attachment_content_interface import NegotiableQuoteDataAttachmentContentInterface


pytestmark = pytest.mark.asyncio

async def test_negotiable_quote_attachment_content_management_v1_get_get(client):
    """Test case for negotiable_quote_attachment_content_management_v1_get_get

    negotiableQuote/attachmentContent
    """
    params = [('attachmentIds', [56])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/negotiableQuote/attachmentContent',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

