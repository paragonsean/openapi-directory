# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.image_type import ImageType
from openapi_server.models.item_fields import ItemFields
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_get_episodes(client):
    """Test case for get_episodes

    Gets episodes for a tv season.
    """
    params = [('userId', 'user_id_example'),
                    ('fields', [openapi_server.ItemFields()]),
                    ('season', 56),
                    ('seasonId', 'season_id_example'),
                    ('isMissing', True),
                    ('adjacentTo', 'adjacent_to_example'),
                    ('startItemId', 'start_item_id_example'),
                    ('startIndex', 56),
                    ('limit', 56),
                    ('enableImages', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()]),
                    ('enableUserData', True),
                    ('sortBy', 'sort_by_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Shows/{series_id}/Episodes'.format(series_id='series_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_next_up(client):
    """Test case for get_next_up

    Gets a list of next up episodes.
    """
    params = [('userId', 'user_id_example'),
                    ('startIndex', 56),
                    ('limit', 56),
                    ('fields', [openapi_server.ItemFields()]),
                    ('seriesId', 'series_id_example'),
                    ('parentId', 'parent_id_example'),
                    ('enableImges', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()]),
                    ('enableUserData', True),
                    ('enableTotalRecordCount', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Shows/NextUp',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_seasons(client):
    """Test case for get_seasons

    Gets seasons for a tv series.
    """
    params = [('userId', 'user_id_example'),
                    ('fields', [openapi_server.ItemFields()]),
                    ('isSpecialSeason', True),
                    ('isMissing', True),
                    ('adjacentTo', 'adjacent_to_example'),
                    ('enableImages', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()]),
                    ('enableUserData', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Shows/{series_id}/Seasons'.format(series_id='series_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_upcoming_episodes(client):
    """Test case for get_upcoming_episodes

    Gets a list of upcoming episodes.
    """
    params = [('userId', 'user_id_example'),
                    ('startIndex', 56),
                    ('limit', 56),
                    ('fields', [openapi_server.ItemFields()]),
                    ('parentId', 'parent_id_example'),
                    ('enableImges', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()]),
                    ('enableUserData', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Shows/Upcoming',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

