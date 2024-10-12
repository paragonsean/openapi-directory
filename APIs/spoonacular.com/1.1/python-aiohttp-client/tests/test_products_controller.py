# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.autocomplete_product_search200_response import AutocompleteProductSearch200Response
from openapi_server.models.classify_grocery_product200_response import ClassifyGroceryProduct200Response
from openapi_server.models.classify_grocery_product_bulk200_response_inner import ClassifyGroceryProductBulk200ResponseInner
from openapi_server.models.classify_grocery_product_bulk_request_inner import ClassifyGroceryProductBulkRequestInner
from openapi_server.models.classify_grocery_product_request import ClassifyGroceryProductRequest
from openapi_server.models.get_comparable_products200_response import GetComparableProducts200Response
from openapi_server.models.get_product_information200_response import GetProductInformation200Response
from openapi_server.models.search_grocery_products200_response import SearchGroceryProducts200Response
from openapi_server.models.search_grocery_products_by_upc200_response import SearchGroceryProductsByUPC200Response


pytestmark = pytest.mark.asyncio

async def test_autocomplete_product_search(client):
    """Test case for autocomplete_product_search

    Autocomplete Product Search
    """
    params = [('query', 'chicke'),
                    ('number', 10)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/products/suggest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classify_grocery_product(client):
    """Test case for classify_grocery_product

    Classify Grocery Product
    """
    body = {"plu_code":"","title":"Kroger Vitamin A & D Reduced Fat 2% Milk","upc":""}
    params = [('locale', 'en_US')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/food/products/classify',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classify_grocery_product_bulk(client):
    """Test case for classify_grocery_product_bulk

    Classify Grocery Product Bulk
    """
    body = [{"plu_code":"","title":"Kroger Vitamin A & D Reduced Fat 2% Milk","upc":""}]
    params = [('locale', 'en_US')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/food/products/classifyBatch',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_comparable_products(client):
    """Test case for get_comparable_products

    Get Comparable Products
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/products/upc/{upc}/comparable'.format(upc=33698816271),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_product_information(client):
    """Test case for get_product_information

    Get Product Information
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/products/{id}'.format(id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_nutrition_by_id_image(client):
    """Test case for product_nutrition_by_id_image

    Product Nutrition by ID Image
    """
    headers = { 
        'Accept': 'image/png',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/products/{id}/nutritionWidget.png'.format(id=7657),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_nutrition_label_image(client):
    """Test case for product_nutrition_label_image

    Product Nutrition Label Image
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
        path='/food/products/{id}/nutritionLabel.png'.format(id=22347),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_nutrition_label_widget(client):
    """Test case for product_nutrition_label_widget

    Product Nutrition Label Widget
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
        path='/food/products/{id}/nutritionLabel'.format(id=22347),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_grocery_products(client):
    """Test case for search_grocery_products

    Search Grocery Products
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
                    ('addProductInformation', true),
                    ('offset', 56),
                    ('number', 10)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/products/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_grocery_products_by_upc(client):
    """Test case for search_grocery_products_by_upc

    Search Grocery Products by UPC
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/products/upc/{upc}'.format(upc=41631000564),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_visualize_product_nutrition_by_id(client):
    """Test case for visualize_product_nutrition_by_id

    Product Nutrition by ID Widget
    """
    params = [('defaultCss', True)]
    headers = { 
        'Accept': 'text/html',
        'accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/products/{id}/nutritionWidget'.format(id=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

