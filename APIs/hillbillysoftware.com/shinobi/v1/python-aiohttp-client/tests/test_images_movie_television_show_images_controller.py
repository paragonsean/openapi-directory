# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.imdb_images import ImdbImages


pytestmark = pytest.mark.asyncio

async def test_image_search_get(client):
    """Test case for image_search_get

    Get images available for movie/tv show with passed query
    """
    params = [('Strictmatch', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Images/Search/{accesstoken}/{query}'.format(accesstoken='accesstoken_example', query='query_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_images_get(client):
    """Test case for images_get

    Get images available for movie/tv show with passed imdbID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Images/ByID/{access_token}/{imdb_id}'.format(access_token='access_token_example', imdb_id='imdb_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

