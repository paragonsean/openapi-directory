# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.item_fields import ItemFields
from openapi_server.models.recommendation_dto import RecommendationDto


pytestmark = pytest.mark.asyncio

async def test_get_movie_recommendations(client):
    """Test case for get_movie_recommendations

    Gets movie recommendations.
    """
    params = [('userId', 'user_id_example'),
                    ('parentId', 'parent_id_example'),
                    ('fields', [openapi_server.ItemFields()]),
                    ('categoryLimit', 5),
                    ('itemLimit', 8)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Movies/Recommendations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

