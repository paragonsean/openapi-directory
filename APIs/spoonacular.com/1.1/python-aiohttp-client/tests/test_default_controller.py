# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analyze_recipe_request import AnalyzeRecipeRequest
from openapi_server.models.analyze_recipe_request1 import AnalyzeRecipeRequest1
from openapi_server.models.search_restaurants200_response import SearchRestaurants200Response


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analyze_recipe(client):
    """Test case for analyze_recipe

    Analyze Recipe
    """
    body = openapi_server.AnalyzeRecipeRequest()
    params = [('language', 'en'),
                    ('includeNutrition', false),
                    ('includeTaste', false)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': '',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/recipes/analyze',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_recipe_card_get(client):
    """Test case for create_recipe_card_get

    Create Recipe Card
    """
    params = [('mask', 'ellipseMask'),
                    ('backgroundImage', 'background1'),
                    ('backgroundColor', 'ffffff'),
                    ('fontColor', '333333')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/card'.format(id=4632),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_restaurants(client):
    """Test case for search_restaurants

    Search Restaurants
    """
    params = [('query', 'beach cafe'),
                    ('lat', 37.7786357),
                    ('lng', -122.3918135),
                    ('distance', 2),
                    ('budget', 20),
                    ('cuisine', 'italian'),
                    ('min-rating', 4.4),
                    ('is-open', true),
                    ('sort', 'distance'),
                    ('page', 0)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/restaurants/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

