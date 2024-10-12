# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult


pytestmark = pytest.mark.asyncio

async def test_get_suggestions(client):
    """Test case for get_suggestions

    Gets suggestions.
    """
    params = [('mediaType', ['media_type_example']),
                    ('type', ['type_example']),
                    ('startIndex', 56),
                    ('limit', 56),
                    ('enableTotalRecordCount', False)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Users/{user_id}/Suggestions'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

