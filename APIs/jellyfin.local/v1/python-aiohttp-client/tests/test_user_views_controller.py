# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.special_view_option_dto import SpecialViewOptionDto


pytestmark = pytest.mark.asyncio

async def test_get_grouping_options(client):
    """Test case for get_grouping_options

    Get user view grouping options.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Users/{user_id}/GroupingOptions'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_views(client):
    """Test case for get_user_views

    Get user views.
    """
    params = [('includeExternalContent', True),
                    ('presetViews', ['preset_views_example']),
                    ('includeHidden', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Users/{user_id}/Views'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

