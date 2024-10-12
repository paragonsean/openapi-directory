# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.call_sentiment import CallSentiment


pytestmark = pytest.mark.asyncio

async def test_v2_call_sentiments_json_get(client):
    """Test case for v2_call_sentiments_json_get

    List call sentiments
    """
    params = [('name', 'name_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_direction', 'sort_direction_example'),
                    ('per_page', 56),
                    ('page', 56),
                    ('include_paging_counts', True),
                    ('limit_paging_counts', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/call_sentiments.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

