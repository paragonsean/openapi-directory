# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.browser_bot_response import BrowserBotResponse
from openapi_server.models.url_info_response import URLInfoResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_browser_bot(client):
    """Test case for browser_bot

    Browser Bot
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    data = {
        'delay': 3,
        '_exec': ['_exec_example'],
        'ignore_certificate_errors': False,
        'selector': 'selector_example',
        'timeout': 30,
        'url': 'url_example',
        'user_agent': 'user_agent_example'
        }
    response = await client.request(
        method='POST',
        path='/browser-bot',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_h_tml_clean(client):
    """Test case for h_tml_clean

    HTML Clean
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    data = {
        'content': 'content_example',
        'output_type': 'output_type_example'
        }
    response = await client.request(
        method='POST',
        path='/html-clean',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_u_rl_info(client):
    """Test case for u_rl_info

    URL Info
    """
    params = [('url', 'url_example'),
                    ('fetch-content', False),
                    ('ignore-certificate-errors', False),
                    ('timeout', 60),
                    ('retry', 0)]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/url-info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

