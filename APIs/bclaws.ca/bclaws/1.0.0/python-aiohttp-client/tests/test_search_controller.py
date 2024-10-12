# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_aspect_id_fullsearch_get(client):
    """Test case for search_aspect_id_fullsearch_get

    A listing of metadata available for the specified aspect and search term from the BCLaws legislative repository
    """
    params = [('q', 'water'),
                    ('s', '0'),
                    ('e', 20),
                    ('nFrag', 5),
                    ('lFrag', 100)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/civix/search/{aspect_id}/fullsearch'.format(aspect_id=complete),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

