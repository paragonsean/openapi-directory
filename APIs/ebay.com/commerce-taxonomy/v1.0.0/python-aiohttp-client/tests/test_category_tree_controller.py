# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aspect_metadata import AspectMetadata
from openapi_server.models.base_category_tree import BaseCategoryTree
from openapi_server.models.category_subtree import CategorySubtree
from openapi_server.models.category_suggestion_response import CategorySuggestionResponse
from openapi_server.models.category_tree import CategoryTree
from openapi_server.models.get_categories_aspect_response import GetCategoriesAspectResponse
from openapi_server.models.get_compatibility_metadata_response import GetCompatibilityMetadataResponse
from openapi_server.models.get_compatibility_property_values_response import GetCompatibilityPropertyValuesResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_item_aspects(client):
    """Test case for fetch_item_aspects

    Get Aspects for All Leaf Categories in a Marketplace
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects'.format(category_tree_id='category_tree_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_category_subtree(client):
    """Test case for get_category_subtree

    Get a Category Subtree
    """
    params = [('category_id', 'category_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree'.format(category_tree_id='category_tree_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_category_suggestions(client):
    """Test case for get_category_suggestions

    Get Suggested Categories
    """
    params = [('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions'.format(category_tree_id='category_tree_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_category_tree(client):
    """Test case for get_category_tree

    Get a Category Tree
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/commerce/taxonomy/v1/category_tree/{category_tree_id}'.format(category_tree_id='category_tree_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_compatibility_properties(client):
    """Test case for get_compatibility_properties

    Get Compatibility Properties
    """
    params = [('category_id', 'category_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties'.format(category_tree_id='category_tree_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_compatibility_property_values(client):
    """Test case for get_compatibility_property_values

    Get Compatibility Property Values
    """
    params = [('compatibility_property', 'compatibility_property_example'),
                    ('category_id', 'category_id_example'),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values'.format(category_tree_id='category_tree_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_default_category_tree_id(client):
    """Test case for get_default_category_tree_id

    Get a Default Category Tree ID
    """
    params = [('marketplace_id', 'marketplace_id_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/commerce/taxonomy/v1/get_default_category_tree_id',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item_aspects_for_category(client):
    """Test case for get_item_aspects_for_category

    
    """
    params = [('category_id', 'category_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category'.format(category_tree_id='category_tree_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

