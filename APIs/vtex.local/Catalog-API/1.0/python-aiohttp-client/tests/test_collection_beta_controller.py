# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.request_body import RequestBody


pytestmark = pytest.mark.asyncio

async def test_g_et_all_collections(client):
    """Test case for g_et_all_collections

    Get All Collections
    """
    params = [('page', 2),
                    ('pageSize', 15),
                    ('orderByAsc', true)]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pvt/collection/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_all_inactive_collections(client):
    """Test case for g_et_all_inactive_collections

    Get All Inactive Collections
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog/pvt/collection/inactive',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_collectionsbyseachterms(client):
    """Test case for g_et_collectionsbyseachterms

    Get Collections by search terms
    """
    params = [('page', 2),
                    ('pageSize', 15),
                    ('orderByAsc', true)]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pvt/collection/search/{search_terms}'.format(search_terms='costume'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_importfileexample(client):
    """Test case for g_et_importfileexample

    Import Collection file example
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog/pvt/collection/stockkeepingunit/importfileexample',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_productsfromacollection(client):
    """Test case for g_et_productsfromacollection

    Get products from a collection
    """
    params = [('page', 2),
                    ('pageSize', 15),
                    ('Filter', 'Pre launch'),
                    ('Active', true),
                    ('Visible', true),
                    ('CategoryId', 12),
                    ('BrandId', 3),
                    ('SupplierId', 1),
                    ('SalesChannelId', 1),
                    ('ReleaseFrom', '2069-11-26T15:23:00'),
                    ('ReleaseTo', '2069-11-26T15:23:00'),
                    ('SpecificationProduct', 'M'),
                    ('SpecificationFieldId', 40)]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog/pvt/collection/{collection_id}/products'.format(collection_id=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_p_ost_addproductsbyimportfile(client):
    """Test case for p_ost_addproductsbyimportfile

    Add products to Collection by imported file
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
        'content_type': 'multipart/form-data',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    data = FormData()
    data.add_field('file', None)
    response = await client.request(
        method='POST',
        path='/api/catalog/pvt/collection/{collection_id}/stockkeepingunit/importinsert'.format(collection_id=1),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p_ost_create_collection(client):
    """Test case for p_ost_create_collection

    Create Collection
    """
    body = openapi_server.RequestBody()
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/catalog/pvt/collection/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_p_ost_removeproductsbyimportfile(client):
    """Test case for p_ost_removeproductsbyimportfile

    Remove products from Collection by imported file
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
        'content_type': 'multipart/form-data',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    data = FormData()
    data.add_field('file', None)
    response = await client.request(
        method='POST',
        path='/api/catalog/pvt/collection/{collection_id}/stockkeepingunit/importexclude'.format(collection_id=1),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

