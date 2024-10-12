# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_media(client):
    """Test case for get_media

    Retrieve media associated with Collections and Cenotaph subjects in Auckland Museum
    """
    params = [('rendering', 'rendering_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/id/media/{path}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

