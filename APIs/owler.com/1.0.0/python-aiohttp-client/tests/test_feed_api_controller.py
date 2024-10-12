# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.results import Results


pytestmark = pytest.mark.asyncio

async def test_v1_feed_get(client):
    """Test case for v1_feed_get

    Get Feeds for given Company Ids
    """
    params = [('format', json),
                    ('company_id', ['company_id_example']),
                    ('limit', '10'),
                    ('pagination_id', '*'),
                    ('category', ['category_example'])]
    headers = { 
        'Accept': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/feed',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_feed_url_get(client):
    """Test case for v1_feed_url_get

    Get Feeds for given Company Websites
    """
    params = [('format', json),
                    ('domain', ['domain_example']),
                    ('limit', '10'),
                    ('pagination_id', '*'),
                    ('category', ['category_example'])]
    headers = { 
        'Accept': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/feed/url',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

