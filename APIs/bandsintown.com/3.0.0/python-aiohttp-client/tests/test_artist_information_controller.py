# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.artist_data import ArtistData


pytestmark = pytest.mark.asyncio

async def test_artist(client):
    """Test case for artist

    Get artist information
    """
    params = [('app_id', 'app_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/artists/{artistname}'.format(artistname='artistname_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

