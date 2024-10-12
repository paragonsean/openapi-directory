# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_people_search_read(client):
    """Test case for people_search_read

    Return cast search result
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/people/search/{user}'.format(user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

