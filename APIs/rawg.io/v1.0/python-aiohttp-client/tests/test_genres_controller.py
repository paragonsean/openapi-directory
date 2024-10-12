# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.genre_single import GenreSingle
from openapi_server.models.genres_list200_response import GenresList200Response


pytestmark = pytest.mark.asyncio

async def test_genres_list(client):
    """Test case for genres_list

    Get a list of video game genres.
    """
    params = [('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/genres',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_genres_read(client):
    """Test case for genres_read

    Get details of the genre.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/genres/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

