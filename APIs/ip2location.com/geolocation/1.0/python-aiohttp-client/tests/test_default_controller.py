# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_root_get(client):
    """Test case for root_get

    
    """
    params = [('package', 'package_example'),
                    ('addon', ['continent,country']),
                    ('ip', '8.8.8.8'),
                    ('format', 'format_example'),
                    ('lang', 'lang_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v2/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

