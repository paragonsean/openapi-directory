# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.autocomplete_menu_item_search200_response import AutocompleteMenuItemSearch200Response
from openapi_server.models.get_menu_item_information200_response import GetMenuItemInformation200Response
from openapi_server.models.search_menu_items200_response import SearchMenuItems200Response


pytestmark = pytest.mark.asyncio

async def test_autocomplete_menu_item_search(client):
    """Test case for autocomplete_menu_item_search

    Autocomplete Menu Item Search
    """
    params = [('query', 'chicke'),
                    ('number', 10)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/menuItems/suggest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_menu_item_information(client):
    """Test case for get_menu_item_information

    Get Menu Item Information
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/menuItems/{id}'.format(id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_menu_item_nutrition_by_id_image(client):
    """Test case for menu_item_nutrition_by_id_image

    Menu Item Nutrition by ID Image
    """
    headers = { 
        'Accept': 'image/png',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/menuItems/{id}/nutritionWidget.png'.format(id=424571),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_menu_item_nutrition_label_image(client):
    """Test case for menu_item_nutrition_label_image

    Menu Item Nutrition Label Image
    """
    params = [('showOptionalNutrients', false),
                    ('showZeroValues', false),
                    ('showIngredients', false)]
    headers = { 
        'Accept': 'image/png',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/menuItems/{id}/nutritionLabel.png'.format(id=342313),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_menu_item_nutrition_label_widget(client):
    """Test case for menu_item_nutrition_label_widget

    Menu Item Nutrition Label Widget
    """
    params = [('defaultCss', True),
                    ('showOptionalNutrients', false),
                    ('showZeroValues', false),
                    ('showIngredients', false)]
    headers = { 
        'Accept': 'text/html',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/menuItems/{id}/nutritionLabel'.format(id=342313),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_menu_items(client):
    """Test case for search_menu_items

    Search Menu Items
    """
    params = [('query', 'burger'),
                    ('minCalories', 50),
                    ('maxCalories', 800),
                    ('minCarbs', 10),
                    ('maxCarbs', 100),
                    ('minProtein', 10),
                    ('maxProtein', 100),
                    ('minFat', 1),
                    ('maxFat', 100),
                    ('addMenuItemInformation', true),
                    ('offset', 56),
                    ('number', 10)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/menuItems/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_visualize_menu_item_nutrition_by_id(client):
    """Test case for visualize_menu_item_nutrition_by_id

    Menu Item Nutrition by ID Widget
    """
    params = [('defaultCss', True)]
    headers = { 
        'Accept': 'text/html',
        'accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/menuItems/{id}/nutritionWidget'.format(id=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

