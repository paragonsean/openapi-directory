# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_category_request import CreateCategoryRequest
from openapi_server.models.get_category_tree200_response import GetCategoryTree200Response
from openapi_server.models.getbyid200_response import Getbyid200Response
from openapi_server.models.roots_inner import RootsInner
from openapi_server.models.update_category_tree_request import UpdateCategoryTreeRequest


pytestmark = pytest.mark.asyncio

async def test_create_category(client):
    """Test case for create_category

    Create Category
    """
    body = {"Name":"Beauty","parentId":"567"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/catalog-seller-portal/category-tree/categories',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_category_tree(client):
    """Test case for get_category_tree

    Get Category Tree
    """
    params = [('depth', 1)]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog-seller-portal/category-tree',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getbyid(client):
    """Test case for getbyid

    Get Category by ID
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog-seller-portal/category-tree/categories/{category_id}'.format(category_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_category_tree(client):
    """Test case for update_category_tree

    Update Category Tree
    """
    body = {"roots":[{"children":[{"children":[{"children":[],"value":{"id":"4","isActive":false,"name":"Artesanato de Barro Vermelho"}}],"value":{"id":"3","isActive":false,"name":"Artesanato de Barro"}}],"value":{"id":"2","isActive":true,"name":"Departamento Artesanato"}},{"children":[{"children":[],"value":{"id":"6","isActive":false,"name":"Perfume Feminino"}},{"children":[],"value":{"id":"7","isActive":false,"name":"Perfume Masculino"}}],"value":{"id":"5","isActive":false,"name":"Perfumes"}}]}
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/catalog-seller-portal/category-tree',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

