# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server.models.product_uuids import ProductUuids
from openapi_server.models.products import Products


pytestmark = pytest.mark.asyncio

async def test_get_app_catalog_mapped_products(client):
    """Test case for get_app_catalog_mapped_products

    Get the list of mapped products related to a catalog
    """
    params = [('search_after', 'cursor to the first page'),
                    ('limit', 100),
                    ('updated_before', '2013-10-20'),
                    ('updated_after', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/catalogs/{id}/mapped-products'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_app_catalog_product_uuids(client):
    """Test case for get_app_catalog_product_uuids

    Get the list of product uuids
    """
    params = [('search_after', 'cursor to the first page'),
                    ('limit', 100),
                    ('updated_before', '2013-10-20'),
                    ('updated_after', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/catalogs/{id}/product-uuids'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_app_catalog_products(client):
    """Test case for get_app_catalog_products

    Get the list of products related to a catalog
    """
    params = [('search_after', 'cursor to the first page'),
                    ('limit', 100),
                    ('updated_before', '2013-10-20'),
                    ('updated_after', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/catalogs/{id}/products'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_app_catalog_products_uuid(client):
    """Test case for get_app_catalog_products_uuid

    Get a product related to a catalog
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/catalogs/{id}/products/{uuid}'.format(id='id_example', uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

