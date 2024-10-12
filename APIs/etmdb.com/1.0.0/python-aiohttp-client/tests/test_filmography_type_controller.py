# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_filmography_type_search_read(client):
    """Test case for filmography_type_search_read

    Return filmography type search result
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/filmography-type/search/{filmography_description}'.format(filmography_description='filmography_description_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

