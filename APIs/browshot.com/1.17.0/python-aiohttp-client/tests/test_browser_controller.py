# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.browser import Browser
from openapi_server.models.browser_error import BrowserError
from openapi_server.models.browser_list import BrowserList


pytestmark = pytest.mark.asyncio

async def test_get_browser_info(client):
    """Test case for get_browser_info

    Get information about a browser
    """
    params = [('id', 56)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/browser/info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_browsers_info(client):
    """Test case for get_browsers_info

    Get all browsers
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/browser/list',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

