# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.get_recommendation_genres200_response import GetRecommendationGenres200Response


pytestmark = pytest.mark.asyncio

async def test_get_recommendation_genres(client):
    """Test case for get_recommendation_genres

    Get Available Genre Seeds 
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/recommendations/available-genre-seeds',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

