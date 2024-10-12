# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_programmes_ato_z_search(client):
    """Test case for get_programmes_ato_z_search

    Programmes by initial title character
    """
    params = [('rights', web),
                    ('page', 56),
                    ('per_page', 56),
                    ('initial_child_count', 4),
                    ('sort', 'sort_example'),
                    ('sort_direction', 'sort_direction_example'),
                    ('availability', available)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/atoz/{letter}/programmes'.format(letter='letter_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

