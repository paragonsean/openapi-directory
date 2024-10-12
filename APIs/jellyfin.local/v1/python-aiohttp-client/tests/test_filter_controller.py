# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.query_filters import QueryFilters
from openapi_server.models.query_filters_legacy import QueryFiltersLegacy


pytestmark = pytest.mark.asyncio

async def test_get_query_filters(client):
    """Test case for get_query_filters

    Gets query filters.
    """
    params = [('userId', 'user_id_example'),
                    ('parentId', 'parent_id_example'),
                    ('includeItemTypes', ['include_item_types_example']),
                    ('isAiring', True),
                    ('isMovie', True),
                    ('isSports', True),
                    ('isKids', True),
                    ('isNews', True),
                    ('isSeries', True),
                    ('recursive', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Items/Filters2',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_query_filters_legacy(client):
    """Test case for get_query_filters_legacy

    Gets legacy query filters.
    """
    params = [('userId', 'user_id_example'),
                    ('parentId', 'parent_id_example'),
                    ('includeItemTypes', ['include_item_types_example']),
                    ('mediaTypes', ['media_types_example'])]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Items/Filters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

