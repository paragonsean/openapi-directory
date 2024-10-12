# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_chromecast_icon(client):
    """Test case for chromecast_icon

    Chromecast Icon
    """
    headers = { 
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/icon.png',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_legal_notice(client):
    """Test case for legal_notice

    Legal Notice
    """
    headers = { 
        'Accept': 'text/plain',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/NOTICE.html.gz',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

