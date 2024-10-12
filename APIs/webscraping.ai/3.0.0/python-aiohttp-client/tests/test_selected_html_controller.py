# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.page_error import PageError


pytestmark = pytest.mark.asyncio

async def test_get_selected(client):
    """Test case for get_selected

    HTML of a selected page area by URL and CSS selector
    """
    params = [('selector', 'h1'),
                    ('url', 'https://example.com'),
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
        path='/selected',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_selected_multiple(client):
    """Test case for get_selected_multiple

    HTML of multiple page areas by URL and CSS selectors
    """
    params = [('selectors', ['[\"h1\"]']),
                    ('url', 'https://example.com'),
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
        path='/selected-multiple',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

