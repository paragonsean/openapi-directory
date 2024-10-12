# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_genre_type_search_read(client):
    """Test case for genre_type_search_read

    Return genre type search result
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/genre-type/search/{genre_description}'.format(genre_description='genre_description_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

