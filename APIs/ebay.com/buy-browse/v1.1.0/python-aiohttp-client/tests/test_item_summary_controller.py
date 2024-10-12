# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.search_paged_collection import SearchPagedCollection


pytestmark = pytest.mark.asyncio

async def test_search(client):
    """Test case for search

    
    """
    params = [('aspect_filter', 'aspect_filter_example'),
                    ('auto_correct', 'auto_correct_example'),
                    ('category_ids', 'category_ids_example'),
                    ('charity_ids', 'charity_ids_example'),
                    ('compatibility_filter', 'compatibility_filter_example'),
                    ('epid', 'epid_example'),
                    ('fieldgroups', 'fieldgroups_example'),
                    ('filter', 'filter_example'),
                    ('gtin', 'gtin_example'),
                    ('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('q', 'q_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/buy/browse/v1/item_summary/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

