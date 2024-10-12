# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.font import Font


pytestmark = pytest.mark.asyncio

async def test_fonts_list(client):
    """Test case for fonts_list

    Lists Handwryting styles available for use
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/fonts/list',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

