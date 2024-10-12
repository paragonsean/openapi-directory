# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_voice_conversion(client):
    """Test case for voice_conversion

    Tell Nexmo if your voice call was successful
    """
    params = [('message-id', '00A0B0C0'),
                    ('delivered', true),
                    ('timestamp', '2020-01-01 12:00:00')]
    headers = { 
        'apiKey': 'special-key',
        'apiSig': 'special-key',
        'apiSecret': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/conversions/voice',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

