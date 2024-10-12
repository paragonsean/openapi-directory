# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.category_response import CategoryResponse
from openapi_server.models.create_categories_request import CreateCategoriesRequest
from openapi_server.models.rename_category_request import RenameCategoryRequest


pytestmark = pytest.mark.asyncio

async def test_create_categories(client):
    """Test case for create_categories

    Create a new category
    """
    body = {"categories":[{"name":"name","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},{"name":"name","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}]}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/organizations/{organization_uuid}/categories/v2'.format(organization_uuid='organization_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_category(client):
    """Test case for delete_category

    Delete a category
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/organizations/{organization_uuid}/categories/v2/{category_uuid}'.format(organization_uuid='organization_uuid_example', category_uuid='category_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_product_types(client):
    """Test case for get_product_types

    Retrieve all categories
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/organizations/{organization_uuid}/categories/v2'.format(organization_uuid='organization_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rename_category(client):
    """Test case for rename_category

    Rename a category
    """
    body = {"name":"name"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/organizations/{organization_uuid}/categories/v2/{category_uuid}'.format(organization_uuid='organization_uuid_example', category_uuid='category_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

