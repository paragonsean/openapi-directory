# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_zebra_get(client):
    """Test case for zebra_get

    Generate bar codes and QR codes with ZXING.
    """
    params = [('format', 'format_example'),
                    ('value', 'value_example'),
                    ('showlabel', True),
                    ('height', 56),
                    ('width', 56)]
    headers = { 
        'Accept': 'image/png',
        'QueryApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/zebra',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

