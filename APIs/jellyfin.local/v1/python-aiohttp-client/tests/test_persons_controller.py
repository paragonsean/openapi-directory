# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.base_item_dto import BaseItemDto
from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.image_type import ImageType
from openapi_server.models.item_fields import ItemFields
from openapi_server.models.item_filter import ItemFilter
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_get_person(client):
    """Test case for get_person

    Get person by name.
    """
    params = [('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Persons/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_persons(client):
    """Test case for get_persons

    Gets all persons.
    """
    params = [('limit', 56),
                    ('searchTerm', 'search_term_example'),
                    ('fields', [openapi_server.ItemFields()]),
                    ('filters', [openapi_server.ItemFilter()]),
                    ('isFavorite', True),
                    ('enableUserData', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()]),
                    ('excludePersonTypes', ['exclude_person_types_example']),
                    ('personTypes', ['person_types_example']),
                    ('appearsInItemId', 'appears_in_item_id_example'),
                    ('userId', 'user_id_example'),
                    ('enableImages', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Persons',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

