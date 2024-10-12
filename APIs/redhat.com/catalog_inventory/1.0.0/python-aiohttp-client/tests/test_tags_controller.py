# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tags_collection import TagsCollection


pytestmark = pytest.mark.asyncio

async def test_list_tags(client):
    """Test case for list_tags

    List Tags
    """
    params = [('limit', 100),
                    ('offset', 0),
                    ('filter', None),
                    ('sort_by', None)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='//api/catalog-inventory/v1.0/tags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

