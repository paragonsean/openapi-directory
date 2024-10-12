# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_news_search_read(client):
    """Test case for news_search_read

    Return news or article search result
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/news/search/{title}'.format(title='title_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

