# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.search_hint_result import SearchHintResult


pytestmark = pytest.mark.asyncio

async def test_get(client):
    """Test case for get

    Gets the search hint result.
    """
    params = [('startIndex', 56),
                    ('limit', 56),
                    ('userId', 'user_id_example'),
                    ('searchTerm', 'search_term_example'),
                    ('includeItemTypes', ['include_item_types_example']),
                    ('excludeItemTypes', ['exclude_item_types_example']),
                    ('mediaTypes', ['media_types_example']),
                    ('parentId', 'parent_id_example'),
                    ('isMovie', True),
                    ('isSeries', True),
                    ('isNews', True),
                    ('isKids', True),
                    ('isSports', True),
                    ('includePeople', True),
                    ('includeMedia', True),
                    ('includeGenres', True),
                    ('includeStudios', True),
                    ('includeArtists', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Search/Hints',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

