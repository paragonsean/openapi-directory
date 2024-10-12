# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.base_item_dto import BaseItemDto
from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.image_type import ImageType
from openapi_server.models.item_fields import ItemFields
from openapi_server.models.item_filter import ItemFilter


pytestmark = pytest.mark.asyncio

async def test_get_album_artists(client):
    """Test case for get_album_artists

    Gets all album artists from a given item, folder, or the entire library.
    """
    params = [('minCommunityRating', 3.4),
                    ('startIndex', 56),
                    ('limit', 56),
                    ('searchTerm', 'search_term_example'),
                    ('parentId', 'parent_id_example'),
                    ('fields', [openapi_server.ItemFields()]),
                    ('excludeItemTypes', ['exclude_item_types_example']),
                    ('includeItemTypes', ['include_item_types_example']),
                    ('filters', [openapi_server.ItemFilter()]),
                    ('isFavorite', True),
                    ('mediaTypes', ['media_types_example']),
                    ('genres', ['genres_example']),
                    ('genreIds', ['genre_ids_example']),
                    ('officialRatings', ['official_ratings_example']),
                    ('tags', ['tags_example']),
                    ('years', [56]),
                    ('enableUserData', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()]),
                    ('person', 'person_example'),
                    ('personIds', ['person_ids_example']),
                    ('personTypes', ['person_types_example']),
                    ('studios', ['studios_example']),
                    ('studioIds', ['studio_ids_example']),
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
        path='/Artists/AlbumArtists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_artist_by_name(client):
    """Test case for get_artist_by_name

    Gets an artist by name.
    """
    params = [('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Artists/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_artists(client):
    """Test case for get_artists

    Gets all artists from a given item, folder, or the entire library.
    """
    params = [('minCommunityRating', 3.4),
                    ('startIndex', 56),
                    ('limit', 56),
                    ('searchTerm', 'search_term_example'),
                    ('parentId', 'parent_id_example'),
                    ('fields', [openapi_server.ItemFields()]),
                    ('excludeItemTypes', ['exclude_item_types_example']),
                    ('includeItemTypes', ['include_item_types_example']),
                    ('filters', [openapi_server.ItemFilter()]),
                    ('isFavorite', True),
                    ('mediaTypes', ['media_types_example']),
                    ('genres', ['genres_example']),
                    ('genreIds', ['genre_ids_example']),
                    ('officialRatings', ['official_ratings_example']),
                    ('tags', ['tags_example']),
                    ('years', [56]),
                    ('enableUserData', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()]),
                    ('person', 'person_example'),
                    ('personIds', ['person_ids_example']),
                    ('personTypes', ['person_types_example']),
                    ('studios', ['studios_example']),
                    ('studioIds', ['studio_ids_example']),
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
        path='/Artists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

