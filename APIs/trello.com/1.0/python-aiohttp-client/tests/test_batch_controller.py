# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_batch(client):
    """Test case for get_batch

    getBatch()
    """
    params = [('urls', 'urls_example'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/batch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

