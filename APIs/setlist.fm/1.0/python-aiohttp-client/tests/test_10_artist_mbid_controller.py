# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.json_artist import JsonArtist


pytestmark = pytest.mark.asyncio

async def test_resource10_artist_mbid_get_artist_get(client):
    """Test case for resource10_artist_mbid_get_artist_get

    .
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/1.0/artist/{mbid}'.format(mbid='mbid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

