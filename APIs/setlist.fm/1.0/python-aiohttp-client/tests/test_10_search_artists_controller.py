# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.json_artists import JsonArtists


pytestmark = pytest.mark.asyncio

async def test_resource10_search_artists_get_artists_get(client):
    """Test case for resource10_search_artists_get_artists_get

    Search for artists.
    """
    params = [('artistMbid', 'artist_mbid_example'),
                    ('artistName', 'artist_name_example'),
                    ('artistTmid', 56),
                    ('p', 1),
                    ('sort', 'sortName')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/1.0/search/artists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

