# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.trailer import Trailer
from openapi_server.models.trailer_count import TrailerCount


pytestmark = pytest.mark.asyncio

async def test_trailer_count_by_id_get(client):
    """Test case for trailer_count_by_id_get

    Get trailer count for passed ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Trailers/CountByID/{access_token}/{imdb_id}'.format(access_token='access_token_example', imdb_id='imdb_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_trailer_count_by_name_get(client):
    """Test case for trailer_count_by_name_get

    Get trailer count for passed name (Movie title or TVShow name)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Trailers/CountByName/{access_token}/{name}'.format(access_token='access_token_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_trailer_search_get(client):
    """Test case for trailer_search_get

    Gets trailers by search phrase (limited to 10 records)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Trailers/Search/{access_token}/{phrase}'.format(access_token='access_token_example', phrase='phrase_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_trailersby_id_get(client):
    """Test case for trailersby_id_get

    Get Trailers for passed imdbID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Trailers/ByID/{access_token}/{imdb_id}'.format(access_token='access_token_example', imdb_id='imdb_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

