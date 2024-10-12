# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_product200_response import GetProduct200Response
from openapi_server.models.get_product_description200_response import GetProductDescription200Response
from openapi_server.models.get_product_query200_response import GetProductQuery200Response
from openapi_server.models.post_product200_response import PostProduct200Response
from openapi_server.models.post_product_request import PostProductRequest
from openapi_server.models.put_product_description_request import PutProductDescriptionRequest
from openapi_server.models.put_product_request import PutProductRequest


pytestmark = pytest.mark.asyncio

async def test_get_product(client):
    """Test case for get_product

    Get Product by ID
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
        path='/api/catalog-seller-portal/products/{product_id}'.format(product_id='189371'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_product_description(client):
    """Test case for get_product_description

    Get Product Description by Product ID
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
        path='/api/catalog-seller-portal/products/{product_id}/description'.format(product_id='189371'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_product_query(client):
    """Test case for get_product_query

    Get Product by external ID,  SKU ID, SKU external ID or slug
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
        path='/api/catalog-seller-portal/products/{param}'.format(param='external-id=189371'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_product(client):
    """Test case for post_product

    Create Product
    """
    body = {"attributes":[{"name":"Fabric","value":"Cotton"},{"name":"Gender","value":"Feminine"}],"brandId":"1","categoryIds":["732"],"description":"Shirt number 10 by VTEX.","images":[{"alt":"VTEX","id":"vtex_logo.jpg","url":"https://vtxleo7778.vtexassets.com/assets/vtex.catalog-images/products/vtex_logo.jpg"}],"name":"VTEX 10 Shirt","origin":"vtxleo7778","skus":[{"dimensions":{"height":2.1,"length":1.6,"width":1.5},"externalId":"1909621862","images":["vtex_logo.jpg"],"isActive":true,"manufacturerCode":"1234567","name":"VTEX Shirt Black Size S","specs":[{"name":"Color","value":"Black"},{"name":"Size","value":"S"}],"weight":300},{"dimensions":{"height":2.1,"length":1.6,"width":1.5},"externalId":"1909621862","images":["vtex_logo.jpg"],"isActive":true,"manufacturerCode":"1234568","name":"VTEX Shirt White Size L","specs":[{"name":"Color","value":"White"},{"name":"Size","value":"L"}],"weight":300}],"slug":"/vtex-shirt","specs":[{"name":"Color","values":["Black","White"]},{"name":"Size","values":["S","M","L"]}],"status":"active","taxCode":"234","transportModal":"110"}
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
        path='/api/catalog-seller-portal/products',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_product(client):
    """Test case for put_product

    Update Product
    """
    body = {"attributes":[{"name":"Fabric","value":"Cotton"},{"name":"Gender","value":"Feminine"}],"brandId":"1","categoryIds":["732"],"id":"189371","images":[{"alt":"VTEX","id":"vtex_logo.jpg","url":"https://vtxleo7778.vtexassets.com/assets/vtex.catalog-images/products/vtex_logo.jpg"}],"name":"VTEX 10 Shirt","origin":"vtxleo7778","skus":[{"dimensions":{"height":2.1,"length":1.6,"width":1.5},"externalId":"1909621862","id":"182907","images":["vtex_logo.jpg"],"isActive":true,"manufacturerCode":"1234567","name":"VTEX Shirt Black Size S","specs":[{"name":"Color","value":"Black"},{"name":"Size","value":"S"}],"weight":300},{"dimensions":{"height":2.1,"length":1.6,"width":1.5},"externalId":"1909621862","id":"182908","images":["vtex_logo.jpg"],"isActive":true,"manufacturerCode":"1234568","name":"VTEX Shirt White Size L","specs":[{"name":"Color","value":"White"},{"name":"Size","value":"L"}],"weight":300}],"slug":"/vtex-shirt","specs":[{"name":"Color","values":["Black","White"]},{"name":"Size","values":["S","M","L"]}],"status":"active","taxCode":null,"transportModal":null}
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/catalog-seller-portal/products/{product_id}'.format(product_id='189371'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_product_description(client):
    """Test case for put_product_description

    Update Product Description by Product ID
    """
    body = {"description":"White shirt.","productId":"71"}
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/catalog-seller-portal/products/{product_id}/description'.format(product_id='71'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

