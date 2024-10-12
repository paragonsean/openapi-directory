# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.branded_food_object import BrandedFoodObject
from openapi_server.models.ingredient_object import IngredientObject


pytestmark = pytest.mark.asyncio

async def test_food_branded_barcode_php_get(client):
    """Test case for food_branded_barcode_php_get

    Get a branded food item using a barcode
    """
    params = [('code', 'code_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/food/branded/barcode.php',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_food_branded_name_php_get(client):
    """Test case for food_branded_name_php_get

    Get a branded food item by name
    """
    params = [('name', 'name_example'),
                    ('limit', 56),
                    ('page', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/food/branded/name.php',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_food_branded_search_php_get(client):
    """Test case for food_branded_search_php_get

    Get data for branded food items using various search parameters
    """
    params = [('allergen', 'allergen_example'),
                    ('brand', 'brand_example'),
                    ('category', 'category_example'),
                    ('country', 'country_example'),
                    ('diet', 'diet_example'),
                    ('ingredient', 'ingredient_example'),
                    ('keyword', 'keyword_example'),
                    ('mineral', 'mineral_example'),
                    ('nutrient', 'nutrient_example'),
                    ('palm_oil', 'palm_oil_example'),
                    ('trace', 'trace_example'),
                    ('vitamin', 'vitamin_example'),
                    ('limit', 56),
                    ('page', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/food/branded/search.php',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_food_ingredient_search_php_get(client):
    """Test case for food_ingredient_search_php_get

    Get raw/generic food ingredient item(s)
    """
    params = [('find', 'find_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/food/ingredient/search.php',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

