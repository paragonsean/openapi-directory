# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_brand200_response import GetBrand200Response
from openapi_server.models.list_brand200_response import ListBrand200Response
from openapi_server.models.post_brand200_response import PostBrand200Response
from openapi_server.models.post_brand_request import PostBrandRequest
from openapi_server.models.put_brand_request import PutBrandRequest


pytestmark = pytest.mark.asyncio

async def test_get_brand(client):
    """Test case for get_brand

    Get Brand by ID
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
        path='/api/catalog-seller-portal/brands/{brand_id}'.format(brand_id='863'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_brand(client):
    """Test case for list_brand

    Get List of Brands
    """
    params = [('q', 'tshirt'),
                    ('from', '1'),
                    ('to', '50'),
                    ('orderBy', 'status,asc;name,asc'),
                    ('name', 'Zwilling')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog-seller-portal/brands',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_brand(client):
    """Test case for post_brand

    Create Brand
    """
    body = {"isActive":true,"name":"Zwilling"}
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
        path='/api/catalog-seller-portal/brands',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_brand(client):
    """Test case for put_brand

    Update Brand
    """
    body = {"id":"20","isActive":true,"name":"Zwilling"}
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/catalog-seller-portal/brands/{brand_id}'.format(brand_id='20'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

