# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server.models.payor_links_response import PayorLinksResponse


pytestmark = pytest.mark.asyncio

async def test_payor_links_v1(client):
    """Test case for payor_links_v1

    List Payor Links
    """
    params = [('descendantsOfPayor', 'descendants_of_payor_example'),
                    ('parentOfPayor', 'parent_of_payor_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/payorLinks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

