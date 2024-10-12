# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_search(client):
    """Test case for get_search

    Perform simple search queries over Auckland Museum Collections and Cenotaph data
    """
    params = [('q', 'q_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/search/{index}/{operation}'.format(index='index_example', operation='operation_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_search(client):
    """Test case for post_search

    Perform complex search queries over Auckland Museum Collections and Cenotaph data
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/search/{index}/{operation}'.format(index='index_example', operation='operation_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

