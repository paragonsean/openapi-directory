# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.channel import Channel
from openapi_server.models.legacy_error import LegacyError


pytestmark = pytest.mark.asyncio

async def test_get_category_channels(client):
    """Test case for get_category_channels

    Get all the channels in a category
    """
    params = [('direction', 'asc'),
                    ('page', 1),
                    ('per_page', 10),
                    ('query', 'Stop motion'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.channel+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/categories/{category}/channels'.format(category='animation'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

