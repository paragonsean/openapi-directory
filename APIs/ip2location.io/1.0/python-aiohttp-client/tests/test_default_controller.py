# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_root_get(client):
    """Test case for root_get

    
    """
    params = [('key', 'key_example'),
                    ('ip', '8.8.8.8'),
                    ('format', 'format_example'),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

