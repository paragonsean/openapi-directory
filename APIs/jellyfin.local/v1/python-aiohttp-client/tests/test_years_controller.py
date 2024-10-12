# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.base_item_dto import BaseItemDto
from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.image_type import ImageType
from openapi_server.models.item_fields import ItemFields
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_get_year(client):
    """Test case for get_year

    Gets a year.
    """
    params = [('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Years/{year}'.format(year=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_years(client):
    """Test case for get_years

    Get years.
    """
    params = [('startIndex', 56),
                    ('limit', 56),
                    ('sortOrder', 'sort_order_example'),
                    ('parentId', 'parent_id_example'),
                    ('fields', [openapi_server.ItemFields()]),
                    ('excludeItemTypes', ['exclude_item_types_example']),
                    ('includeItemTypes', ['include_item_types_example']),
                    ('mediaTypes', ['media_types_example']),
                    ('sortBy', 'sort_by_example'),
                    ('enableUserData', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()]),
                    ('userId', 'user_id_example'),
                    ('recursive', True),
                    ('enableImages', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Years',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

