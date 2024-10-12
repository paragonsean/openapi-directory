# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.search_by_image_request import SearchByImageRequest
from openapi_server.models.search_paged_collection import SearchPagedCollection


pytestmark = pytest.mark.asyncio

async def test_search_by_image(client):
    """Test case for search_by_image

    
    """
    body = {"image":"image"}
    params = [('aspect_filter', 'aspect_filter_example'),
                    ('category_ids', 'category_ids_example'),
                    ('charity_ids', 'charity_ids_example'),
                    ('fieldgroups', 'fieldgroups_example'),
                    ('filter', 'filter_example'),
                    ('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/buy/browse/v1/item_summary/search_by_image',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

