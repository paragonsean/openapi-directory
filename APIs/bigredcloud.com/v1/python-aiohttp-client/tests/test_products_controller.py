# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_item_product_dto import BatchItemProductDto
from openapi_server.models.page_result_product_dto import PageResultProductDto
from openapi_server.models.product_dto import ProductDto


pytestmark = pytest.mark.asyncio

async def test_products_delete(client):
    """Test case for products_delete

    Removes an existing Product.
    """
    params = [('timestamp', 'timestamp_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/products/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_get(client):
    """Test case for products_get

    Returns a list of company's Products. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \"id\" and \"stockCode\" fields.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/products',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_post(client):
    """Test case for products_post

    Creates a new Product.
    """
    body = {"details":["det1","det2","det3"],"grossUnitPrice":False,"hasDefaultVatRate":False,"id":9,"productTypeId":0,"stockCode":"PRO1","timestamp":"fRreu9RD2wg=","unitPrice":100,"vatAnalysisTypeId":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/products',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_process_batch(client):
    """Test case for products_process_batch

    Processes a batch of Products.
    """
    body = [openapi_server.BatchItemProductDto()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/products/batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_put(client):
    """Test case for products_put

    Updates an existing Product.
    """
    body = {"details":["det1","det2","det3"],"grossUnitPrice":False,"hasDefaultVatRate":False,"id":9,"productTypeId":0,"stockCode":"PRO1","timestamp":"fRreu9RD2wg=","unitPrice":100,"vatAnalysisTypeId":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/products/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_products_id_get(client):
    """Test case for v1_products_id_get

    Returns information about a single Product.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/products/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

