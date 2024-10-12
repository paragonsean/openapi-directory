# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_payor_link_request import CreatePayorLinkRequest
from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404


pytestmark = pytest.mark.asyncio

async def test_create_payor_links(client):
    """Test case for create_payor_links

    Create a Payor Link
    """
    body = {"fromPayorId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","linkType":"PARENT_OF","toPayorId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/payorLinks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

