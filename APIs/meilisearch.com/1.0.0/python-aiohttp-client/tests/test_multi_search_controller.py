# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.search_one_or_more_indexes_request import SearchOneOrMoreIndexesRequest


pytestmark = pytest.mark.asyncio

async def test_search_one_or_more_indexes(client):
    """Test case for search_one_or_more_indexes

    Search one or more indexes
    """
    body = {"queries":[{"indexUid":"books","q":"Pride and Prejudice"},{"attributesToHighlight":["title"],"indexUid":"books","q":"Alice In Wonderland"}]}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/multi-search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

