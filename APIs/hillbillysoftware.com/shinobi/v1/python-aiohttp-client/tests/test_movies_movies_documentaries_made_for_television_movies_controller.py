# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.movie_information import MovieInformation


pytestmark = pytest.mark.asyncio

async def test_movie_id_get(client):
    """Test case for movie_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Movie/ByID/{accesstoken}/{imdb_id}'.format(accesstoken='accesstoken_example', imdb_id='imdb_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_movie_search_get_async(client):
    """Test case for movie_search_get_async

    Searches for movies, result set limited to 5 records
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Movie/Search/{access_token}/{query}'.format(access_token='access_token_example', query='query_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

