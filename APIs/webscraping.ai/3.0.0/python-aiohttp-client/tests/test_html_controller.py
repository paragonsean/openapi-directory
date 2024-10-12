# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.page_error import PageError


pytestmark = pytest.mark.asyncio

async def test_get_html(client):
    """Test case for get_html

    Page HTML by URL
    """
    params = [('url', 'https://example.com'),
                    ('headers', {'key': '{\"Cookie\":\"session=some_id\"}'}),
                    ('timeout', 10000),
                    ('js', True),
                    ('js_timeout', 2000),
                    ('proxy', datacenter),
                    ('country', us),
                    ('device', desktop),
                    ('error_on_404', False),
                    ('error_on_redirect', False)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/html',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

