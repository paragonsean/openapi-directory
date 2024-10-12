# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.autocomplete_ingredient_search200_response_inner import AutocompleteIngredientSearch200ResponseInner
from openapi_server.models.compute_ingredient_amount200_response import ComputeIngredientAmount200Response
from openapi_server.models.get_ingredient_information200_response import GetIngredientInformation200Response
from openapi_server.models.get_ingredient_substitutes200_response import GetIngredientSubstitutes200Response
from openapi_server.models.ingredient_search200_response import IngredientSearch200Response
from openapi_server.models.map_ingredients_to_grocery_products200_response_inner import MapIngredientsToGroceryProducts200ResponseInner
from openapi_server.models.map_ingredients_to_grocery_products_request import MapIngredientsToGroceryProductsRequest


pytestmark = pytest.mark.asyncio

async def test_autocomplete_ingredient_search(client):
    """Test case for autocomplete_ingredient_search

    Autocomplete Ingredient Search
    """
    params = [('query', 'burger'),
                    ('number', 10),
                    ('metaInformation', false),
                    ('intolerances', 'egg'),
                    ('language', 'en')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/ingredients/autocomplete',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_compute_ingredient_amount(client):
    """Test case for compute_ingredient_amount

    Compute Ingredient Amount
    """
    params = [('nutrient', 'protein'),
                    ('target', 2),
                    ('unit', 'oz')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/ingredients/{id}/amount'.format(id=9266),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ingredient_information(client):
    """Test case for get_ingredient_information

    Get Ingredient Information
    """
    params = [('amount', 150),
                    ('unit', 'grams')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/ingredients/{id}/information'.format(id=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ingredient_substitutes(client):
    """Test case for get_ingredient_substitutes

    Get Ingredient Substitutes
    """
    params = [('ingredientName', 'butter')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/ingredients/substitutes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ingredient_substitutes_by_id(client):
    """Test case for get_ingredient_substitutes_by_id

    Get Ingredient Substitutes by ID
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/ingredients/{id}/substitutes'.format(id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ingredient_search(client):
    """Test case for ingredient_search

    Ingredient Search
    """
    params = [('query', 'burger'),
                    ('addChildren', true),
                    ('minProteinPercent', 10),
                    ('maxProteinPercent', 90),
                    ('minFatPercent', 10),
                    ('maxFatPercent', 90),
                    ('minCarbsPercent', 10),
                    ('maxCarbsPercent', 90),
                    ('metaInformation', false),
                    ('intolerances', 'egg'),
                    ('sort', 'calories'),
                    ('sortDirection', 'asc'),
                    ('offset', 56),
                    ('number', 10),
                    ('language', 'en')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/ingredients/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ingredients_by_id_image(client):
    """Test case for ingredients_by_id_image

    Ingredients by ID Image
    """
    params = [('measure', 'metric')]
    headers = { 
        'Accept': 'image/png',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/ingredientWidget.png'.format(id=1082038),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_map_ingredients_to_grocery_products(client):
    """Test case for map_ingredients_to_grocery_products

    Map Ingredients to Grocery Products
    """
    body = {"ingredients":["eggs","bacon"],"servings":2}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/food/ingredients/map',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_visualize_ingredients(client):
    """Test case for visualize_ingredients

    Ingredients Widget
    """
    params = [('language', 'en')]
    headers = { 
        'Accept': 'text/html',
        'Content-Type': 'application/x-www-form-urlencoded',
        'content_type': 'application/json',
        'accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/recipes/visualizeIngredients',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

