# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.section_format_get200_response import SectionFormatGet200Response


pytestmark = pytest.mark.asyncio

async def test_section_format_get(client):
    """Test case for section_format_get

    Top Stories
    """
    params = [('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/topstories/v2/{section_format}'.format(section='section_example', format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

