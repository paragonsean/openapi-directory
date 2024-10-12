# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.base_item_dto import BaseItemDto
from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.image_type import ImageType
from openapi_server.models.item_fields import ItemFields


pytestmark = pytest.mark.asyncio

async def test_get_music_genre(client):
    """Test case for get_music_genre

    Gets a music genre, by name.
    """
    params = [('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/MusicGenres/{genre_name}'.format(genre_name='genre_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_music_genres(client):
    """Test case for get_music_genres

    Gets all music genres from a given item, folder, or the entire library.
    """
    params = [('startIndex', 56),
                    ('limit', 56),
                    ('searchTerm', 'search_term_example'),
                    ('parentId', 'parent_id_example'),
                    ('fields', [openapi_server.ItemFields()]),
                    ('excludeItemTypes', ['exclude_item_types_example']),
                    ('includeItemTypes', ['include_item_types_example']),
                    ('isFavorite', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()]),
                    ('userId', 'user_id_example'),
                    ('nameStartsWithOrGreater', 'name_starts_with_or_greater_example'),
                    ('nameStartsWith', 'name_starts_with_example'),
                    ('nameLessThan', 'name_less_than_example'),
                    ('enableImages', True),
                    ('enableTotalRecordCount', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/MusicGenres',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

