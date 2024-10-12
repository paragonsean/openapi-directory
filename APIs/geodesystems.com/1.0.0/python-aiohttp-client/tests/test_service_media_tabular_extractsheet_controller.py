# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_media_tabular_extractsheet(client):
    """Test case for media_tabular_extractsheet

    API for Extract sheets
    """
    params = [('output', 'media_tabular_extractsheet'),
                    ('entryid', 'entryid_example'),
                    ('arg1', 'arg1_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/entry/show',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

