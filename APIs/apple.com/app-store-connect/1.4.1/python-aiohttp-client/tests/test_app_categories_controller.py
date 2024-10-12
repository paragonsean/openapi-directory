# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_categories_response import AppCategoriesResponse
from openapi_server.models.app_category_response import AppCategoryResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_app_categories_get_collection(client):
    """Test case for app_categories_get_collection

    
    """
    params = [('filter[platforms]', ['filter_platforms_example']),
                    ('exists[parent]', ['exists_parent_example']),
                    ('fields[appCategories]', ['fields_app_categories_example']),
                    ('limit', 56),
                    ('include', ['include_example']),
                    ('limit[subcategories]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appCategories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_categories_get_instance(client):
    """Test case for app_categories_get_instance

    
    """
    params = [('fields[appCategories]', ['fields_app_categories_example']),
                    ('include', ['include_example']),
                    ('limit[subcategories]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appCategories/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_categories_parent_get_to_one_related(client):
    """Test case for app_categories_parent_get_to_one_related

    
    """
    params = [('fields[appCategories]', ['fields_app_categories_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appCategories/{id}/parent'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_categories_subcategories_get_to_many_related(client):
    """Test case for app_categories_subcategories_get_to_many_related

    
    """
    params = [('fields[appCategories]', ['fields_app_categories_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appCategories/{id}/subcategories'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

