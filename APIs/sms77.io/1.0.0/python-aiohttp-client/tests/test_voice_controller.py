# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_voice(client):
    """Test case for voice

    
    """
    params = [('to', 'to_example'),
                    ('text', 'text_example'),
                    ('xml', 3.4),
                    ('from', '_from_example')]
    headers = { 
        'Accept': 'text/plain',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/voice',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

