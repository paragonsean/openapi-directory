# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.movie import Movie


pytestmark = pytest.mark.asyncio

async def test_get_movies(client):
    """Test case for get_movies

    Get the status of your movies
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/movies',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_new_movie(client):
    """Test case for new_movie

    Create a new movie
    """
    body = openapi_server.Movie()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/movies',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

