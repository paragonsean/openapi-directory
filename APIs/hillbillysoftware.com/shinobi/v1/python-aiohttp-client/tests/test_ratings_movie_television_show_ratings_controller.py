# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rating_item import RatingItem


pytestmark = pytest.mark.asyncio

async def test_rating_by_name_get(client):
    """Test case for rating_by_name_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Rating/ByName/{access_token}/{name}'.format(access_token='access_token_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rating_get(client):
    """Test case for rating_get

    Returns ratings from various resources(IMDB,Rotten Tomatoes, metaCritics, TVMaze etc) of passed IMDBid
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Rating/ByID/{access_token}/{imdb_id}'.format(access_token='access_token_example', imdb_id='imdb_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

