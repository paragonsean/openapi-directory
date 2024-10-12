# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_cinema_search_read(client):
    """Test case for cinema_search_read

    Return cinema search result
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cinema/search/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

